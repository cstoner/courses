#!/usr/bin/python

def get_area(l,w,h):
    """The area we are of wrapping paper needed is 2*l*w + 2*w*h + 2*h*l + min([l*w,w*h,h*l])"""
    return 2*l*w + 2*w*h + 2*h*l + min([l*w,w*h,h*l])

assert(get_area(2,3,4) == 58)
assert(get_area(1,1,10) == 43)

with open('day2_data.txt') as f_hdl:
    data = f_hdl.read()

total_area = 0
for line in data.split('\n'):
    (l, h, w) = (int(num) for num in line.split('x'))
    total_area += get_area(l, h, w)

print "Total area needed: {}".format(total_area)