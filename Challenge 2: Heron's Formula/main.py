'''
See README.md for challenge info

'''

import math
a = float(input("what is a? "))
b = float(input("what is b? "))
c = float(input("what is c? "))
def calculateTriangleArea():
    perimiter = a + b + c
    s = perimiter / 2
    sa = s - a
    sb = s - b
    sc = s - c
    sabc = sa * sb * sc
    insideRadical = s * sabc
    area = math.sqrt(insideRadical)
    return area
print(calculateTriangleArea())