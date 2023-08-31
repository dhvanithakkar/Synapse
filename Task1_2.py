#Task 1.2
lst = ['0001', '0011', '0101', '1011']
lst = [int(bin,2) for bin in lst]
lst.sort()
barbie = lst[-1]
ken = 0
index = 0
for num in lst[-2::-1]:
    if ken + num <= barbie: 
        ken += num
    else:
        barbie += num

new_lst = [ken, barbie]
print(new_lst)
