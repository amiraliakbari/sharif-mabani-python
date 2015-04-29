num = input("tedade daneshjooha ra vared konid")
grades = {}
for i in range(num):
    name = raw_input("name daneshjooye %dom ra vared konid" % (i))
    score = input("nomre daneshjooye %dom ra vared konid" % (i))
    grades[name] = score

average = 0
for a in grades.values():
    average += a
average = float(average) / num

print average







