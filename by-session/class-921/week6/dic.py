grades = {"ali": 20, "hassan":19, "ali":9}
print grades

grades[(1, 2)] = 1
grades["farhad"] = 10
print grades

del grades["ali"]
print grades

if "farhad" in grades:
    print grades["farhad"]
else:
    print "NO!!!"

print grades.keys()
print grades.values()
print grades.items()

for a in grades.keys():
    print a, grades[a]

for [key, value] in grades_dic.items():
    print "name:", key
    print "nomre:", value

