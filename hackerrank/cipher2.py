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
    k = k % 26
    print("K = {} ".format(k))
    s2 = ""
    for i in range(len(s)):
        if (ord(s[i])>=65 and ord(s[i])<=90) or (ord(s[i])>=97 and ord(s[i])<=122):
            print("letter {} ord {} val = {} ".format(s[i],ord(s[i]),ord(s[i])+k))
            if ((ord(s[i])+k)>90 and ord(s[i])+k<97) or ((ord(s[i])+k)>122):
                s2 = s2+chr(ord(s[i])-26+k)
            else :
                print("S3_letter {} ord {} val = {} k = {} ".format(s[i],ord(s[i]),ord(s[i])+k,k))
                s2 = s2+chr(ord(s[i])+k)
        else :
            print("ELSE_letter {} ord {} val = {} ".format(s[i],ord(s[i]),ord(s[i])+k))
            s2 = s2+s[i]
    print("{}".format(s2))
    return s2
    # Write your code here

if __name__ == '__main__':
    n= 53
    k = 87
    #s= "6DWV95HzxTCHP85dvv3NY2crzt1aO8j6g2zSDvFUiJj6XWDlZvNNr"
    #s = "D3q4"
    s = "6DWV95HzxTCHP85dvv3NY2crzt1aO8j6g2zSDvFUiJj6XWDlZvNNr"
    result = caesarCipher(s, k)
    print("{}".format(result))
