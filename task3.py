#1
#arr = ['a', 'o', 'y', 'e', 'u', 'i']
#inp = input().lower()
#a = ""
#for i in range(len(inp)):
#    if inp[i] not in arr:
#        a += "."
#        a += inp[i]
#print(a)

#2
#input = input()
#ans = input.split('+')
#ans.sort()
#print('+'.join(ans))

#3
#res = input()
#print(res[0].upper() + res[1:])

#4
#res = input()
#cnt = 0
#for i in range(1, len(res)):
#    if res[i] == res[i-1]:
#        cnt+=1
#    else:
#        cnt=0
#if(cnt>=6):
#    print("YES")
#    print(cnt)
#else:
#    print("NO")
#    print(cnt)

#5
#res = input()
#ans = []
#for i in range(len(res)):
#    ans.append(res[i])
#if(len(set(ans))) % 2 == 0:
#    print("CHAT WITH HER")
#else:
#    print("IGNORE HIM")

#6
#res = input()
#cnt = 0
#for i in range(len(res)):
#    if res[i].islower():
#        cnt+=1
#if(cnt >= len(res)/2): 
#    print(res.lower())
#else:
#    print(res.upper())

#7
#num = int(input())
#res = input().lower()
#ans = []
#if num >= 26:
#    for i in range(len(res)):
#        ans.append(res[i])
#    if len(set(ans)) >=26:
#        print("YES")
#    else:
#        print("NO")
#else:
#    print("NO")

#8
#s = input()
#t = input()
#if s[::-1] == t:
#    print("YES")
#else:
#    print("NO")

#9
#n = int(input())
#res = input()
#cnt = 0
#for i in range(n):
#    if res[i] == 'A':
#        cnt+=1
#if cnt > n - cnt:
#    print("Anton")
#else:
#    print("Danik")

#10
#ans = input()
#res = ans.lower()
#print(ans[0].upper() + res[1:])

#ex11
#import re
#n = int(input())
#s = input()
#z = re.findall('z', s)
#e = re.findall('e', s)
#r = re.findall('r', s)
#o = re.findall('o', s)
#n = re.findall('n', s)
#num = min(len(o), len(e), len(z), len(r))
#len(n) - num
#len(o) - num
#len(e) - num
#num2 = min(len(n), len(o), len(e))
#for i in range(num2):
#    print('1', end=' ')
#for i in range(num):
#    print('0', end=' ')

#12
#n = int(input())
#res = input()
#tripleX = "xxx"
#cnt = 1
#if tripleX not in res:
#   print(0)
#else:
#    for i in range(1,n):
#        if res[i] == res[i-1] and res[i-1] == 'x':
#            cnt+=1
#    print(cnt-2)



        