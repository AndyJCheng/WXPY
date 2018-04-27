#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.6
@author: andy cheng
@file: test.py
@time: 2018/4/27 0:14
"""
from wxpy import *
bot = Bot()
my_friends = bot.friends()
print(my_friends)
