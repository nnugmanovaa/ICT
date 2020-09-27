#ex 1
#x1 = int(input())
#y1 = int(input())
#x2 = int(input())
#y2 = int(input())
#if x1 == x2 or y1 == y2:
#    print("YES")
#else:
#    print("NO")

#ex 2
#x1 = int(input())
#y1 = int(input())
#x2 = int(input())
#y2 = int(input())
#if abs(x1 - x2 == 1) or abs(y1 - y2 == 1):
#    print("YES")
#else:
#    print("NO")

#ex 3
#x1 = int(input())
#y1 = int(input())
#x2 = int(input())
#y2 = int(input())
#if abs(x1 - x2) == abs(y1 - y2):
#    print("YES")
#else:
#    print("NO")

#ex 5
#x1 = int(input())
#y1 = int(input())
#x2 = int(input())
#y2 = int(input())
#if abs(x2 - x1) == 2 and abs(y2 - y1) == 1:
#    print("YES")
#else:
#    print("NO")

#ex 6
#n = int(input())
#m = int(input())
#k = int(input())
#if k > n * m:
#    print("NO")
#if(k % n == 0) or (k % m == 0):
#    print("YES")
#else:
#    print("NO")

#ex 7
#n = int(input())
#m = int(input())
#x = int(input())
#y = int(input())
#print(min(x,y))

#ex 8
#a = int(input())
#b = int(input())
#c = int(input())
#arr = (a,b,c)
#print(sorted(arr))

#ex 9 ----

#ex 10
#n = int(input())
#x = 1
#while (x**2 < n):
#    print(x**2)
#    x += 1

#ex 11
#n = int(input())
#div = 2
#while(div <= n):
#    if(n % div == 0):
#        print(div)
#        break 
#    else:
#        div +=1

#ex 12
#n = int(input())
#m = 1
#while(2**m < n):
#    print(2**m)
#    m += 1

#ex 13
#sum = 0
#while(1):
#    x = int(input())
#    sum += x
#    if(x == 0):
#        break
#print(sum)

#ex 14
#maxi = 0
#counter = 0
#while(1):
#    x = int(input())
#    if(x > maxi):
#        maxi = x
#        counter = 0
#    if(x == maxi):
#        counter += 1
#    if(x == 0):
#        break
#print(counter)

#ex 15
#n = int(input("Give an n: "))
#count = 1
#fib0 = 0
#fib1 = 1
#fibn = 1
#while fibn<n:
#    fibn = fib0 + fib1
#    fib0 = fib1
#    fib1 = fibn
#    count = count+1
#if fibn==n:
#    print(count)
#else:
#    print(-1)

#ex 16
#input_list = []
#cnt = 0
#while True:
#    el = int(input())
#    if el == 0:
#        break
#    input_list.append(el)
#i = 1
#while i < len(input_list)-1:
#    if input_list[i] > input_list[i-1] and input_list[i] > input_list[i+1]:
#        cnt+=1
#    i += 1
#print(cnt)

#ex 17
#n = int(input())
#inputList = []
#for i in range(0, n):
#    ele = int(input())
#    inputList.append(ele)
#print(sorted(inputList))

#ex 18
#a = input().split()
#print(a[len(a)-1])
#for i in range(0,len(a)-1):
#    print(a[i])


#ex 19
#n = int(input())
#my_list = []
#cnt = 0
#for i in range(0,n):
#    el = int(input())
#    my_list.append(el)
#my_list.sort
#x = 0
#while x < (n-1):
#    if(my_list[x] == my_list[x+1]):
#        cnt +=1
#        x = x+2
#    else:
#        x += 1
#print(cnt)

#ex 20

