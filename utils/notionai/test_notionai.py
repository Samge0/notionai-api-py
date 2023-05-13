#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2023-05-10 23:59
# describe：
import os
import sys

from notionai import NotionAI

os.environ['NOTION_TOKEN'] = 'v02%3Auser_token_or_cookies%3AL1gW6pCD9MaLvGEwxm5Rl2wdd9ps5q2tXsghT9-2m22p2KnSlwKWyU6OAja3i5rB8kavFPJ1sZPghqGZEYrvFTv-s-BN8J6WkX1xQ4napxyaA9zBdA5F6IZ1Jh05Yh7EfRd4'
os.environ['NOTION_SPACE_ID'] = 'a6111fb9-7784-4a6a-bd43-fa6b0d8e3a59'

TOKEN = os.getenv("NOTION_TOKEN")
SPACE_ID = os.getenv("NOTION_SPACE_ID")

API_URL = "https://notiontest.samgeai.top"


def write_blog(prompt: str):
    res = ai.blog_post(prompt)
    print(f"NotionAI:{res}")


def main():
    while True:
        prompt = input("\nUser：")
        write_blog(prompt)


if __name__ == "__main__":
    ai = NotionAI(TOKEN, SPACE_ID, api_url=API_URL)
    main()
