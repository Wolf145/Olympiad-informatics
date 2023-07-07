dat1 = int(input())
year1 = int(input())
if abs(dat1) == abs(year1):
    print(1)
if dat1 > 0 < year1 or dat1 < 0 > year1:
    print(dat1 + year1)
if dat1 > 0 > year1 and abs(year1) < dat1 :
    print(dat1 + year1)
if dat1 > 0 > year1 and abs(year1) > dat1 :
    print(dat1 + year1 - 1)
if dat1 < 0 < year1 and abs(dat1) < year1:
    print(dat1 + year1 + 1)
if dat1 < 0 < year1 and abs(dat1) > year1:
    print(dat1 + year1)
