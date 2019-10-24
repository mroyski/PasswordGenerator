# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:23:03 2019

@author: Admin
"""

# 5-8 characters, 1 special char, 1 upper, 1 lower, 1 digit, not more than 2 uses of any character

import random as r
import string as s

# random selectors
def random_lower_letter():
    random_num = r.randrange(0, 26)
    return s.ascii_lowercase[random_num]

def random_upper_letter():
    random_num = r.randrange(0, 26)
    return s.ascii_uppercase[random_num]

def random_num():
    return r.randrange(0, 10)

def random_special():
    random_num = r.randrange(0, 32)
    return s.punctuation[random_num]

def generate():
    # no () because result of function is stored not the function itself
    func_list = [random_lower_letter, random_upper_letter, random_num, random_special]
    pw = []
    x = 0
    limit = r.randrange(4, 8)
    # pos refers to func_list index and counts how many times they have been added
    pos0, pos1, pos2, pos3 = 0, 0, 0, 0
    while x < limit:
        y = r.randrange(0, 4)
        if y == 0:
            if pos0 < 2:
                pw.append(func_list[0]())
                pos0 += 1
                x += 1
            else:
                continue
        ## can only have one number because len() is applied to end
        elif y == 1:
            if pos1 < 2:
                pw.append(func_list[1]())
                pos1 += 1
                x += 1
            else:
                continue
        elif y == 2:
            if pos2 < 1:
                pw.append(str(func_list[2]()))
                pos2 += 1
                x += 1
            else:
                continue
        elif y == 3:
            if pos3 < 2:
                pw.append(func_list[3]())
                pos3 += 1
                x += 1
            else:
                continue
            
    # guarantees one of each character
    if pos0 == 0:
        pw.append(func_list[0]())
    if pos1 == 0:
        pw.append(func_list[1]())
    if pos2 == 0:
        pw.append(str(func_list[2]()))
    if pos3 == 0:
        pw.append(func_list[3]())
    
    # add length of password to the end
    pw.append(str(len(pw) + 1))
            
    return "".join(pw)

print(generate())
