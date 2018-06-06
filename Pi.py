#! /usr/bin/python3
#-*-conding:utf-8-*-
# Copyright (c) 2018 - SUN Lei <leisun@genetics.ac.cn>
#割圆术
#Liu Hui's π algorithm

import numpy 

num = 10000 #number of iterative

r = 1
n = 6
M = r
PI = (M*n)/(2*r)
OUTPUT = "Number of edges of polygon : " + n + "approximation of π for now is : " + PI
print(OUTPUT)
for i in range(0,num):
    G = numpy.sqrt(numpy.square(r)-numpy.square(M/2))
    j = r - G
    m = numpy.sqrt(numpy.square(j)+numpy.square(M/2))
    PI = (M*n)/(2*r)
    n = 6 * pow(2,i)
    OUTPUT = "Number of edges of polygon : " + n + "approximation of π for now is : " + PI
    print(OUTPUT)
    M = m