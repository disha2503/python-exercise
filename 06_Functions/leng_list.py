# cities=["Bangalore","Delhi","Chennai","Mumbai"]
# def print_len(list):
#     print(len(list))

# print_len(cities)



# pg2

# cities=["Bangalore","Delhi","Chennai","Mumbai"]
# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# print_list(cities)


# pg3
# def cal_fac(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)

# cal_fac(5)

# pg 4
# def convertor(usd_val):
#     inr_val=usd_val*82.74
#     print(inr_val)

# convertor(100)

# def number(num):
#     if num%2==0:
#         print("Even")
#     else:
#         print("Odd")

# number(5)


# def cal_sum(n):
#     if(n==0):
#         return 0
#     return cal_sum(n-1)+n

# sum=cal_sum(5)
# print(sum)


def print_list(list, idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits=["Apple","Banana","Mango","Grapes"]
print_list(fruits)