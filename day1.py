with open("input_day1.txt") as f:
    l = [int(line) for line in f.readlines()]
l.sort(reverse=True)

def task1():
    for i in l:
        for j in l[::-1]:
            if i+j > 2020:
                break
            if i+j == 2020:
                print(i*j)
                return

def task2():
    for idx, i in enumerate(l):
         for j in l[idx:]:
             if i+j < 2020:
                 for k in l[::-1]:
                     if i+j+k > 2020:
                         break
                     if i+j+k == 2020:
                         print(i*j*k)
                         return

task1()
task2()