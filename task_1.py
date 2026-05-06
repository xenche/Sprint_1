time_string = '1h 45m,360s,25m,30m 120s,2h 60s'
count_time = 0
time_string = time_string.replace(" ", ",").replace("h", "*60").replace("s", "/60").replace("m", "")
time_lst = time_string.split(",")

for t1 in time_lst:
    t2 = int(eval(t1))
    count_time += t2
print(count_time)