# 오영식 자체적으로 K개의 랜선 보유 하지만 K의 랜선의 길이는 제 각각

# 박성원은 N개의 같은 길이의 랜선을 만들고 싶었기때문에 K개의 랜선을 잘라서 만든다.

# 최대 랜선의 길이를 구하는 프로그램.

# K는 오영식이 가지고 있는 랜선의 갯수 ( 1<= k <10,000)
# N은 필요한 랜선의 갯수 (1<= N <=1,000,000)
# K<=N
import sys

K, N = map(int, sys.stdin.readline().rstrip().split())
stick = []
for _ in range(K):
    stick.append(int(sys.stdin.readline().rstrip()))

stickMin = min(stick)
num1 =1
stickMin1 =0
over1 =0 
ddnum = 1
total = 0
t = 0
flag =True
max_length =[]
while True:
    if flag:
        num1 +=1
        # print("1(1)",stickMin1 , stickMin//num1 , over1,stickMin,num1)
        stickMin1_1 = stickMin * over1 + stickMin // num1
        stickMin1 = stickMin1_1
        ddnum = 1
        # print("1(2)",stickMin1)
    else:
        num1 =1
        ddnum +=1
        over1=1
        # print("2(1) : ",stickMin1, int(stickMin1 * (1 / ddnum)), ddnum)
        stickMin2 = stickMin1_1 * over1 + int(stickMin1_1 * (1 / ddnum))
        stickMin = stickMin2
        stickMin1 = stickMin2
        # print("2(2) : ",stickMin1)
        
    total = 0
    for j in range(len(stick)): 
        count =1
        while stickMin1 * count < stick[j]:
                count +=1
        total = total + count - 1
    if total >=N:
        # print("----전환----")
        flag =not(flag)
        if len(max_length) !=0 and max(max_length) == stickMin1:
            break
        max_length.append(stickMin1)
    # print("StickMin : ",stickMin,"total : ",total,"StickMin1 : ",stickMin1)

print(stickMin1)





# count =0
# dnum = 2
# flag =True
# while flag:
#     count =0
#     print(dnum)
#     for i in range(len(stick)):
#         mcnt = 0
#         while stick[i] > (stickMin // dnum) * mcnt:
#             mcnt +=1
#         count = count + mcnt -1
#     if  count >=N:
#         print(count,  stickMin // dnum,dnum)
#         flag = False
#     else:
#         print(count,  stickMin // dnum,dnum)
#         dnum +=1
    
# if not(flag):
#     if count !=N:
#         flag=True
#         ddnum = 2
#         while flag:
#             count =0
#             for i in range(len(stick)):
#                 mcnt = 0
#                 while stick[i] > ((stickMin // dnum) + (stickMin // dnum) * (1/ddnum)) *mcnt:
#                     mcnt +=1
#                 count = count + mcnt -1
#             if  count >=N:
#                 print(count,  ((stickMin // dnum) + (stickMin // dnum) * (1/ddnum)),dnum)
#                 flag = False
#             else:
#                 print(count,  ((stickMin // dnum) + (stickMin // dnum) * (1/ddnum)),dnum)
#                 ddnum +=1


# if not(flag):
#     print("Rmx?sdasd")
#     flag=True
#     dddnum = 2
#     while flag:
#         count =0
#         for i in range(len(stick)):
#             mcnt = 0
#             while stick[i] > int((((stickMin // dnum) + (stickMin // dnum) * (1/ddnum)) + (((stickMin // dnum) + (stickMin // dnum) * (1/ddnum))* (1/dddnum)))) *mcnt:
#                 mcnt +=1
#             count = count + mcnt -1
#         if  count >=N:
#             print(count,  int(((((stickMin // dnum) + (stickMin // dnum) * (1/ddnum)) + (((stickMin // dnum) + (stickMin // dnum) * (1/ddnum))* (1/dddnum))))),dnum)
#             flag = False
#         else:
#             print(count,  int((((stickMin // dnum) + (stickMin // dnum) * (1/ddnum)) + (((stickMin // dnum) + (stickMin // dnum) * (1/ddnum))* (1/dddnum)))),dnum)
#             dddnum +=1
