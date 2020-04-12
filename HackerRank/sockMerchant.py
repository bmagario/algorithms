#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    myDict = {}
    result = 0
    for i in range(n):
        el = ar[i]
        if el in myDict:
            myDict[el] += 1
        else:
            myDict[el] = 1
            
    for el in myDict:
        result += myDict[el] // 2
    
    return result