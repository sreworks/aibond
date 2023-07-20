#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys

sys.path.insert(0, os.path.split(os.path.realpath(__file__))[0] + "/../../")

from aibond import AI
from tools.SREWorks.Frontend import table
from langchain import OpenAI

ai = AI()

resp = ai.run("帮我生成一个表格的json schema", llm=OpenAI(temperature=0), tools=[table], verbose=True)
print("=== resp ===")
print(resp)
