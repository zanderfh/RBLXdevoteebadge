import datetime
counter = 0

file = open('input.txt')

content = file.readlines()

with open("input.txt") as f:
    for i, l in enumerate(f):
        pass
len = i + 1


x = range(1,len)

for i in x:
    ln = content[i]

    cont = ln.strip()
    dy = int(cont.split('/')[0])
    mn = int(cont.split('/')[1])
    yr = int(cont.split('/')[2])

    date = datetime.datetime(yr,mn,dy)
    yesterday = date + datetime.timedelta(days = -1)

    frmt = str(date)[0:10]
    frmt2 = str(yesterday)[0:10]

    ln2 = content[i-1]
    cont2 = ln2.strip()

    dy2 = int(cont2.split('/')[0])
    mn2 = int(cont2.split('/')[1])
    yr2 = int(cont2.split('/')[2])

    date2 = datetime.datetime(yr2,mn2,dy2)
    frmt3 = str(date2)[0:10]

    if frmt2 == frmt3:
        counter += 1

    elif frmt2 != frmt3:
        counter = 0

print(f"So far you have a streak of {counter} days!")
print(f"You only need {365-counter} days until you get the Devotee badge!")
input("Press ENTER to exit:  ")
