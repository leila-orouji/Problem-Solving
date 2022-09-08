#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict


#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    arr.sort()
    brr.sort()
    result = []
    unique_result = []

    for i in brr:
        if i not in arr:
            result.append(i)
        else:
            arr.remove(i)

    for x in result:
        if x not in unique_result:
            unique_result.append(x)
    return unique_result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
