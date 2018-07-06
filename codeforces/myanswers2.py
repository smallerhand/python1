#Codeforces Round #487
#A
s = input()
output = 'No'
for i in range(len(s)-2):
    if s[i:i+3] in ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']:
        output = 'Yes'
        break;
    
print(output)

#lst = [int(i) for i in s]
#B (wrong in pretest 6)
n, p = map(int, input().split(' '))
s = input()
output = 'No'
x = int(n/p)
if n > p:
    for i in range(len(s)):
        if s[i] == '0':
            for j in range(x):
                if i+(j+1)*p < len(s):
                    if s[i+(j+1)*p] == '.':
                        check = i+(j+1)*p
                        output = ''
                        for k in range(len(s)):
                            if k < check:
                                if s[k] in ['0','1']:
                                    output += s[k]
                                else:
                                    output += '0'
                            elif k == check:
                                output += '1'
                            else:
                                if s[k] in ['0','1']:
                                    output += s[k]
                                else:
                                    output += '0'    
        elif s[i] == '1':
            for j in range(x):
                if i+(j+1)*p < len(s):
                    if s[i+(j+1)*p] == '.':
                        check = i+(j+1)*p
                        output = ''
                        for k in range(len(s)):
                            if k < check:
                                if s[k] in ['0','1']:
                                    output += s[k]
                                else:
                                    output += '0'
                            elif k == check:
                                output += '0'
                            else:
                                if s[k] in ['0','1']:
                                    output += s[k]
                                else:
                                    output += '0'
        else:
            for j in range(x):
                if i+(j+1)*p < len(s):
                    if s[i+(j+1)*p] == '0':
                        check = i
                        output = ''
                        for k in range(len(s)):
                            if k < check:
                                if s[k] in ['0','1']:
                                    output += s[k]
                                else:
                                    output += '0'
                            elif k == check:
                                output += '1'
                            else:
                                if s[k] in ['0','1']:
                                    output += s[k]
                                else:
                                    output += '0'
                    if s[i+(j+1)*p] == '1':
                        check = i
                        output = ''
                        for k in range(len(s)):
                            if k < check:
                                if s[k] in ['0','1']:
                                    output += s[k]
                                else:
                                    output += '0'
                            elif k == check:
                                output += '0'
                            else:
                                if s[k] in ['0','1']:
                                    output += s[k]
                                else:
                                    output += '0'

print(output)

#C. (문제를 잘 모르겠음)
a, b, c, d = map(int, input().split(' '))

#output1 = str(x) + ' ' + str(y)
output = []
output[1] = ''

#print(output1)
for i in range(x):
    print(output[i])
    
#D. (error)
n, l, w = map(int, input().split(' '))
x = []
v = []
for i in range(n):
    xi, vi = map(int, input().split(' '))
    x.append(xi)
    v.append(vi)
output = 0

for i in range(n-1):
    for j in range(i+1, n):
        if x[i] * x[j] > 0:
            if v[i] * v[j] > 0:
                output += 1
            else:
                if abs(v[i]) < w and abs(v[j]) < w:
                    output += 1
        elif x[i] * x[j] < 0:
            if v[i] * v[j] < 0:
                output += 1
            else:
                if abs(v[i]) < w and abs(v[j]) < w:
                    output += 1
        elif x[i] == 0:
            if abs(v[i]) < w:
                if (v[j] - x[i])*x[j] < 0:
                    output += 1
        elif x[j] == 0:
            if abs(v[j]) < w:
                if (v[i] - x[j])*x[i] < 0:
                    output += 1
                    
print(output)

#510B. Fox And Two Dots (보류)
n, m = map(int, input().split(' '))
matrix = [['' for col in range(m)] for row in range(n)]
dic = dict()
for i in range(n):
    lst = input()
    for j in range(m):
        matrix[i][j] = lst[j]
        if lst[j] in dic.keys():
            dic[lst[j]].append((i,j))
        else:
            dic[lst[j]] = [(i,j)]
            
output = 'No'        

for factor in dic.keys():
    if len(dic[factor]) >= 4:
        for i in range(n):
            lst = []
            for k in dic[factor]:
                if k[0] == i:
                    lst.append(k[1])
            start = min(lst)
            end = max(lst)
            print(start, end)
        for j in range(m):
            lst = []
            for l in dic[factor]:
                if l[1] == j:
                    lst.append(l[0])
            start = min(lst)
            end = max(lst)
            print(start, end)

cnt = 1

if cnt >= 4:
    output = 'Yes'
    
print(output)

#339B. Xenia and Ringroad
n, m = map(int, input().split(' '))
alist = input().split(' ')
alist = [int(i) for i in alist]

time = 0

for i in range(m):
    if i == m-1:
        time += alist[i] - 1
    elif alist[i] > alist[i+1]:
        time += n
    else:
        continue
    
print(time)

#492B. Vanya and Lanterns
n, l = map(int, input().split(' '))
alist = input().split(' ')
a = [int(i) for i in alist]

a.sort()
if a[0] != 0:
    max = a[0]*2
else:
    max = 0

if a[-1] != l:
    if max < (l - a[-1])*2:
        max = (l - a[-1])*2

for i in range(n-1):
    if max < a[i+1] - a[i]:
        max = a[i+1] - a[i]

d = max/2
print("{0:.10f}".format(d))

#200B. Drinks
n = int(input())
line = input().split(' ')
p = [int(i) for i in line]

print(sum(p)/n)

#4C. Registration system
n = int(input())
line = ['' for i in range(n)]
dic = dict()
for i in range(n):
    inp = input()
    if inp in dic.keys():
        dic[inp] += 1
        line[i] = inp + str(dic[inp])
    else:
        dic[inp] = 0
        line[i] = inp
        
for i in range(n):
    if line[i].isalpha():
        print('OK')
    else:
        print(line[i])

#230B. T-primes (wrong on test16)
n = int(input())
xline = input().split(' ')
x = [int(i) for i in xline]

for i in range(n):
    end = False
    integer = x[i]
    if integer in [1,2,3,16,36,64]:
        print('NO')
    else:
        root = int(integer**(1/2))
        root_of_root = int(root**(1/2))
        if root ** 2 == integer:
            if root_of_root <= 2:
                print('YES')
            else:
                for j in range(2, root_of_root):
                    if root%j == 0:
                        break
                    elif j == root_of_root-1:
                        print('YES')
                        end = True
                if not end:
                    print('NO')                
        else:
            print('NO')
                    
#230B. T-primes (wrong on test16)
n = int(input())
xline = input().split(' ')
x = [int(i) for i in xline]

for i in range(n):
    obj = x[i]
    end = True
    if obj == 1:
        end = False
    else:
        root = int(obj**(1/2))
        if root**2 == obj:
            root_of_root = int(root**(1/2))
            if root_of_root**2 == root:
                for j in range(root_of_root):
                    if j in [0,1]:
                        continue
                    elif root % j == 0:
                        end = False
                        break
            else:
                for j in range(root_of_root+1):
                    if j in [0,1]:
                        continue
                    elif root % j == 0:
                        end = False
                        break
        else:
            end = False
    if end:
        print('YES')
    else:
        print('NO')
                        
#489C. Given Length and Sum of Digits... (time limit on test5)
m, s = map(int, input().split(' '))
