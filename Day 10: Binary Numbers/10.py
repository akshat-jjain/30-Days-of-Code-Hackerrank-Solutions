#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    a = []
    maxi = 0
    n = int(input())
    a = bin(n).split("0")
    for x in a :
        if x.count("1") > maxi :
            maxi = x.count("1")
    print(maxi)
