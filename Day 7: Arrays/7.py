#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    a= ""
    arr = list(map(int, input().rstrip().split()))
    z = arr[::-1]
    for x in z :
        a+= str(x)+" "
    print(a)
