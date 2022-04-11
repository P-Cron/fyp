from bisect import bisect_right

'''
bisect code taken from here:
https://docs.python.org/3/library/bisect.html#examples
'''
def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i-1]