#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Simple test script for hai-hai skill."""

import datetime

now = datetime.datetime.now()
weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
weekday = weekdays[now.weekday()]

print(f"🐍 Python 腳本測試成功！")
print(f"   今天是 {now.year} 年 {now.month} 月 {now.day} 日，{weekday}")
print(f"   Python 版本：{__import__('sys').version.split()[0]}")
