#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2023-05-10 23:59
# describe：
import json
import uuid

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from requests import Response

from utils.notionai.enums import PromptTypeEnum, ToneEnum, TopicEnum, TranslateLanguageEnum

MODEL = "openai-4"
API_URL = "https://www.notion.so"

proxies = {
    "http": None,
    "https": None
}

request_verify = False

timeout = 240


class NotionAIBase(object):
    stream = False

    def __init__(
        self,
        token: str,
        space_id: str,
        model: str = MODEL,
        api_url: str = API_URL,
    ) -> None:
        """Init NotionAI
        Args:
            token (str): Notion token_v2
            space_id (str): Notion workspace id
            model (str, optional): AI model. Default to openai-1.1
            api_url (str, optional): Notion api base url
            stream (bool, optional): use stream result. Defaults to False.
            pageTitle (str, optional): Title for your content. Defaults to PAGE_TITLE.
        """
        self.token = token
        self.space_id = space_id
        self.model = model or MODEL
        self.api_url = api_url or API_URL
        self.is_space_permission = False
        self.url = f"{self.api_url}/api/v3/getCompletion"

    def _request(self, content: dict) -> Response:
        blockId = self._get_id()
        payload = {
            "id": self._get_id(),
            "model": self.model,
            "spaceId": self.space_id,
            "isSpacePermission": self.is_space_permission,
            "context": content,
            "aiSessionId": self._get_id(),
            "metadata": {
                "blockId": blockId
            },
            "attributionForLogging": {
                "blockId": blockId
            },
        }

        headers = self._build_headers(self.token)
        return requests.post(
            self.url, json=payload, headers=headers, stream=self.stream, verify=request_verify, proxies=proxies, timeout=timeout
        )

    @classmethod
    def _build_headers(cls, token: str):
        cookies = [
            "token_v2=" + token,
        ]

        return {
            "accept": "application/json",
            "Cookie": "; ".join(cookies),
            "Content-Type": "application/json",
            # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        }

    def _post(self, content: dict) -> str:
        r = self._request(content)
        if r.status_code != 200:
            # '{"errorId":"3fe5f108-dbbc-442b-8f29-5ec8158e71ed","name":"ValidationError","debugMessage":"Invalid input.","message":"Something went wrong. (400)"}'
            return r.text
        data = r.text.split("\n")
        res = [self._parse_resp_line(d) for d in data]
        return "".join(res).strip("\n")

    def _parse_resp_line(self, line):
        if line:
            try:
                data = json.loads(line)
                if data["type"] == "success":
                    return data["completion"]
            except Exception as e:
                print(f"data: {line}, error: {e}")
                if self.is_un_authorized_error(str(line)) or self.is_429_error(str(line)):
                    return str(line)
        return ""

    def _get_id(self) -> str:
        return str(uuid.uuid4())

    def is_bad_request(self, value) -> bool:
        """
        是否请求错误
        '{"errorId":"3fe5f108-dbbc-442b-8f29-5ec8158e71ed","name":"ValidationError","debugMessage":"Invalid input.","message":"Something went wrong. (400)"}'
        :param value:
        :return:
        """
        value = value or ''
        return 'errorId' in value

    def is_un_authorized_error(self, value) -> bool:
        """
        是否认证失败错误
        :param value:
        :return:
        """
        value = value or ''
        return 'UnauthorizedError' in value

    def is_429_error(self, value) -> bool:
        """
        是否429请求限制
        :param value:
        :return:
        """
        value = value or ''
        return 'code 429' in value


class NotionAI(NotionAIBase):
    @classmethod
    def get_spaces(cls, token: str, api_url: str = API_URL) -> list[dict]:
        """Get all spaces
        Params:
            token (str): Notion token_v2
            api_url (str): Notion api base url

        Returns:
            list[dict]: list of spaces with id and name

        Example: [
            {"id": "space_id_1", "name": "space_name"},
            {"id": "space_id_2", "name": "space_name"}
        ]
        """
        api_url = api_url or API_URL
        url = f"{api_url}/api/v3/getSpaces"
        r = requests.post(url, headers=cls._build_headers(token), verify=request_verify, proxies=proxies, timeout=timeout)
        if r.status_code != 200:
            raise ValueError("Cannot get spaces")
        res = r.json()
        spaces = []
        for _, val in res.items():
            space = val.get("space")
            if space:
                for k, v in space.items():
                    space_id = k
                    space_name = v["value"]["name"]
                    spaces.append({"id": space_id, "name": space_name})
        return spaces

    def writing_with_topic(self, topic: TopicEnum, prompt: str) -> str:
        """Writing for special topic

        Args:
            topic (TopicEnum): the special topic
            prompt (str): prompt for writing

        Returns:
            str: Response from NotionAI
        """
        content = {"type": topic.value, "topic": prompt}
        return self._post(content)

    def writing_with_prompt(
        self,
        prompt_type: PromptTypeEnum,
        context: str,
        page_title: str = "",
    ) -> str:
        """Writing with special prompt, like summarize, explain_this, improve_writing

        Args:
            prompt_type (PromptTypeEnum): special prompt
            context (str): the context for your writing
            page_title (str, optional): I am not sure about this. Defaults to ""

        Returns:
            str: Response from NotionAI
        """
        if prompt_type == PromptTypeEnum.continue_writing:
            return self.continue_write(context, page_title)

        if prompt_type in {
            PromptTypeEnum.help_me_write,
            PromptTypeEnum.help_me_edit,
            PromptTypeEnum.translate,
            PromptTypeEnum.change_tone,
        }:
            raise ValueError("Please use the specific method for this prompt type")
        content = {
            "type": prompt_type.value,
            "pageTitle": page_title,
            "selectedText": context,
            "pageContent": context,
        }
        return self._post(content)

    def help_me_write(
        self, prompt: str, context: str, page_title: str = "", rest_content: str = ""
    ) -> str:
        """Help me write, ask AI to write for you

        Args:
            prompt (str): your prompt, could be anything
            context (str): context for your writing
            page_title (str, optional): not sure. Defaults to "".
            rest_content (str, optional): more context. Defaults to "".

        Returns:
            str: Response from NotionAI
        """
        content = {
            "type": PromptTypeEnum.help_me_write.value,
            "prompt": prompt,
            "pageTitle": page_title,
            "previousContent": context,
            "restContent": rest_content,
        }
        return self._post(content)

    def continue_write(
        self, context: str, page_title: str = "", rest_content: str = ""
    ) -> str:
        """Continue writing, generating more

        Args:
            context (str): context for continue
            page_title (str, optional): not sure. Defaults to "".
            rest_content (str, optional): more context. Defaults to "".

        Returns:
            str: Response from NotionAI
        """
        content = {
            "type": PromptTypeEnum.continue_writing.value,
            "pageTitle": page_title,
            "previousContent": context,
            "restContent": rest_content,
        }
        return self._post(content)

    def help_me_edit(self, prompt: str, context: str, page_title: str = "") -> str:
        """Help me edit somethings, it will change the current context

        Args:
            prompt (str): your prompt, could be anything
            context (str): context to edit
            page_title (str, optional): not sure. Defaults to "".

        Returns:
            str: Response from NotionAI
        """

        content = {
            "type": PromptTypeEnum.help_me_edit.value,
            "pageTitle": page_title,
            "prompt": prompt,
            "selectedText": context,
            "pageContent": context,
        }
        return self._post(content)

    def translate(self, language: TranslateLanguageEnum, context: str) -> str:
        """Use NotionAI to translate your context

        Args:
            language (TranslateLanguageEnum): target language
            context (str): context to translate

        Returns:
            str: translate result
        """
        content = {
            "type": PromptTypeEnum.translate.value,
            "text": context,
            "language": language.value,
        }
        return self._post(content)

    def change_tone(self, context: str, tone: ToneEnum) -> str:
        """Change the tone of your context

        Args:
            context (str): context to change
            tone (ToneEnum): target tone

        Returns:
            str: Response from NotionAI
        """
        content = {
            "type": "changeTone",
            "tone": tone.value,
            "text": context,
        }
        return self._post(content)

    def summarize(self, context: str, page_title: str = "") -> str:
        return self.writing_with_prompt(PromptTypeEnum.summarize, context)

    def improve_writing(self, context: str, page_title: str = "") -> str:
        return self.writing_with_prompt(PromptTypeEnum.improve_writing, context)

    def fix_spelling_grammar(self, context: str, page_title: str = "") -> str:
        return self.writing_with_prompt(
            PromptTypeEnum.fix_spelling_grammar,
            context,
            page_title=page_title,
        )

    def explain_this(self, context: str, page_title: str = "") -> str:
        return self.writing_with_prompt(
            PromptTypeEnum.explain_this, context, page_title=page_title
        )

    def make_longer(self, context: str, page_title: str = "") -> str:
        return self.writing_with_prompt(
            PromptTypeEnum.make_longer, context, page_title=page_title
        )

    def make_shorter(self, context: str, page_title: str = "") -> str:
        return self.writing_with_prompt(
            PromptTypeEnum.make_shorter, context, page_title=page_title
        )

    def find_action_items(self, context: str, page_title: str = "") -> str:
        return self.writing_with_prompt(
            PromptTypeEnum.find_action_items, context, page_title=page_title
        )

    def simplify_language(self, context: str, page_title: str = "") -> str:
        return self.writing_with_prompt(
            PromptTypeEnum.simplify_language, context, page_title=page_title
        )

    def blog_post(self, prompt: str) -> str:
        return self.writing_with_topic(TopicEnum.blog_post, prompt)

    def brainstorm_ideas(self, prompt: str) -> str:
        return self.writing_with_topic(TopicEnum.brainstorm_ideas, prompt)

    def outline(self, prompt: str) -> str:
        return self.writing_with_topic(TopicEnum.outline, prompt)

    def social_media_post(self, prompt: str) -> str:
        return self.writing_with_topic(TopicEnum.social_media_post, prompt)

    def creative_story(self, prompt: str) -> str:
        return self.writing_with_topic(TopicEnum.creative_story, prompt)

    def poem(self, prompt: str) -> str:
        return self.writing_with_topic(TopicEnum.poem, prompt)

    def essay(self, prompt: str) -> str:
        return self.writing_with_topic(TopicEnum.essay, prompt)

    def meeting_agenda(self, prompt: str) -> str:
        return self.writing_with_topic(TopicEnum.meeting_agenda, prompt)

    def press_release(self, prompt: str) -> str:
        return self.writing_with_topic(TopicEnum.press_release, prompt)

    def job_description(self, prompt: str) -> str:
        return self.writing_with_topic(TopicEnum.job_description, prompt)

    def sales_email(self, prompt: str) -> str:
        return self.writing_with_topic(TopicEnum.sales_email, prompt)

    def recruiting_email(self, prompt: str) -> str:
        return self.writing_with_topic(TopicEnum.recruiting_email, prompt)

    def pros_cons_list(self, prompt: str) -> str:
        self.writing_with_topic(TopicEnum.pros_cons_list, prompt)


class NotionAIStream(NotionAI):
    stream = True

    def _post(self, content: dict) -> str:
        r = self._request(content)
        for line in r.text.splitlines():
            yield self._parse_resp_line(line)
