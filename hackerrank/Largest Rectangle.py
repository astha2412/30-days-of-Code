#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def getMaxArea(arr):
    n = len(arr)
    # print(arr, n)
    maxarea = 0
    stack = []
    limitforleftbar = [None for x in range(n)]

    limitforrightbar = [None for x in range(n)]
    # traverse the array
    for i in range(len(arr)):
        # print(i)
        # find left bar less than current
        # print("left bar")

        if len(stack) == 0:
            # print("stack is empty")
            stack.append(i)
            limitforleftbar[i] = 0
        else:
            # print("stack is not empty ",stack)
            if len(stack)!=0 and arr[stack[-1]]>=arr[i]:
                while(len(stack)!=0 and arr[stack[-1]]>=arr[i]):
                    stack.pop()
                if len(stack) == 0:
                    limitforleftbar[i] = 0
                else:
                    limitforleftbar[i] = stack[-1] + 1
                stack.append(i)
            else:
                limitforleftbar[i] = i
                stack.append(i)
        # print("left limits",limitforleftbar,"and stack is",stack)
    stack = []
    for i in range(len(arr)-1,-1,-1):
        # print(i)
        #find right bar less than current
        # print("right bar")
        if len(stack) == 0:
            # print("stack is empty")
            stack.append(i)
            limitforrightbar[i] = i
            # print("right limits",limitforrightbar,"and stack is\n",stack)
        else:
            # print("stack is not empty",stack)
            if len(stack)!=0 and arr[stack[-1]] >= arr[i]:
                while(len(stack)!=0 and arr[stack[-1]] >= arr[i]):
                    stack.pop()
                if len(stack) == 0:
                    limitforrightbar[i] = n-1
                else:
                    limitforrightbar[i] = stack[-1] - 1
                stack.append(i)
            else:
                limitforrightbar[i] = i
                stack.append(i)
            # print("right limits",limitforrightbar,"and stack is\n",stack)
    # now traverse both the limits and find the area
    maxarea = 0
    for i in range(n):
        no_of_bars = limitforrightbar[i] - limitforleftbar[i] + 1
        area = arr[i]*no_of_bars
        if area>maxarea:
            maxarea=area
        # print("for bar ",i,"no of bars covered",no_of_bars,"and area is",area)
    return maxarea
def largestRectangle(h):
    return getMaxArea(h)

if __name__ == '__main__':

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)
    print("area",result)
