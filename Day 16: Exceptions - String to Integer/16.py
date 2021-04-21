#!/bin/python3

import sys


S = input().strip()
try:
    v=int(S)
    print(v)
except:
    print("Bad String")
