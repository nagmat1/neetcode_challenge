#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    s2 = ""
    k = k % 26
    print("K = {} ".format(k))
    for i in range(len(s)):
        if (ord(s[i])>=65 and ord(s[i])<=90): 
            if (ord(s[i])+k>90):
                s2 = s2+chr(ord(s[i])-26+k)
            else : 
                s2 = s2+chr(ord(s[i])+k)
        elif (ord(s[i])>=97 and ord(s[i])<=122):
            if (ord(s[i])+k>122):
                s2 = s2+chr(ord(s[i])-26+k)
            else :
                s2 = s2+chr(ord(s[i])+k)
        else :
            print("ELSE_letter {} ord {} val = {} ".format(s[i],ord(s[i]),ord(s[i])+k))
            s2 = s2+s[i]
    print("{}".format(s2))
    return s2
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
