# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/saad/.spyder2/.temp.py
"""
import time

def time_stamp(func):
    def wrapper(*arg):
        t1 = time.clock()
        res = func(*arg)
        t2 = time.clock()
        print '%s took %0.3fms' % (func.func_name, (t2-t1)*1000.0)
        return res
    return wrapper
    

@time_stamp       
def insertion(lst):
    """This is the function to implement insertion
    sort. 
    """
    for index in range(len(lst)):
        value = lst[index]
        i = index - 1
        while i >= 0 and (value <= lst[i]):
            lst[i+1] = lst[i]
            lst[i] = value
            i -= 1
    return lst

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
    
@time_stamp
def mergesort(lst):
    if len(lst) <= 1:
        return lst
    middle = len(lst)/2
    left = mergesort(lst[:middle])
    right = mergesort(lst[middle:])
    return merge(left, right)




if __name__ == '__main__':
    a = [5,2,3,5,6,7,1,2,1,0,8,9]
    
    print "insertion: ", insertion(a)
    print "merge: ", mergesort(a)