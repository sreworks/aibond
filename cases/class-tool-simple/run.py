#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
from subprocess import Popen, PIPE

sys.path.insert(0, os.path.split(os.path.realpath(__file__))[0] + "/../../")

from aibond import AI
from aaa import page_read
from langchain import OpenAI

ai = AI()

resp = ai.run("帮我看看 https://aa.com/k https://aa.com/b 这两个网址中有什么内容", llm=OpenAI(temperature=0.2), tools=[page_read], verbose=True)
print("=== resp ===")
print(resp)
