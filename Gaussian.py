#!/usr/bin/env python 3
# -*- coding: utf-8 -*- 

###
# Name: Andrew_Papilion
# Student ID: 2265916
# Email: papil103@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2017
# Assignment: Classwork_04
###

import math
import numpy as np

import math
import numpy as np

def gen_gaussian_list(a, b, n=1000):

    dx = (b-a)/(n-1)                         # spacing between points
    x = [a + k*dx for k in range(n)]         # domain list
    
    # Local implementation of a Gaussian function
    def gauss(x):
        return (1/math.sqrt(2*math.pi))*math.exp(-x**2/2)
    
    g = [gauss(xk) for xk in x]                  # range list
    return (x, g)


def gen_gaussian_array(a, b, n=1000):
  
    pass


def main(a,b,n=1000):
  
    # You can unpack tuples as return values easily
    x, g = gen_gaussian_list(a,b,n)
    # The zip function takes two lists and generates a list of matched pairs
    for (xk, gk) in zip(x, g):
        # The format command replaces each {} with the value of a variable
        print("({}, {})".format(xk, gk))


# Protected main block for command line operation
if __name__ == "__main__":
    # The sys module contains features for running programs
    import sys
    # The sys.argv list variable contains all command line arguments
    #    sys.argv[0] is the program name always
    #    sys.argv[1] is the first command line argument, etc
    if len(sys.argv) == 4:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        n = int(sys.argv[3])
        main(a,b,n)
    elif len(sys.argv) == 3:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        main(a,b)
    else:
        print("Usage: cw04.py a b [n]")
        print("  a : float, lower bound of domain")
        print("  b : float, upper bound of domain")
        print("  n : integer, number of points in domain")
        exit(1)
