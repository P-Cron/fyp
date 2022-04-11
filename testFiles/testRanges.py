import sys
sys.path.append(".")
from constsAndHelpers import const
from bisect import bisect, bisect_left, bisect_right
'''
bisect code taken from here:
https://docs.python.org/3/library/bisect.html#examples
'''


def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i-1]

ranges = const.FIXED_RANGES
# index = bisect(ranges['Engine RPM(rpm)'], 798)
# actualValue = ranges['Engine RPM(rpm)'][index]
# print (actualValue)

leftVal = find_le(ranges['Engine RPM(rpm)'], 825)
print(leftVal)