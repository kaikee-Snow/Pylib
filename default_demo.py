#!/usr/bin/env python
# -*- coding: utf-8 -*-
message = 'It was a bright cold day in April, and the clocks\
were striking thirteen.'
count = {}
for char in message:
    count.setdefault(char, 0)
    count[char] += 1
print(count)
