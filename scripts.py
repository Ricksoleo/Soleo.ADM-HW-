# Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")

# Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    somma=a+b
    diff=a-b
    prod=a*b
    print(somma)
    print(diff)
    print(prod)
# Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    int_div=a//b
    float_div=a/b
    print(int_div)
    print(float_div)

# Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i**2)

# Write a function
def is_leap(year):
    leap = False
    if year%4==0:
        if year%100==0:
            if year%400==0:
                leap=True
            else:
                leap=False
        else:
            leap=True
    else:
        leap=False

# Print Function
if __name__ == '__main__':
    n = int(input())
    nu=str(n)
    i=2
    num=str(1)
    while i<=n:
        s=str(i)
        num=num+s
        i+=1
    print(num)
   
# String Validators
if __name__ == '__main__':
    s = input()
    n=0
    r=0
    e=0
    p=0
    l=0
for i in s:
    
    if i.isalnum()==True:
        n+=1
         
    else:
         n+=0

for i in s:
    
    if i.isalpha()==True:
        r+=1
         
    else:
         r+=0
for i in s:
    
    if i.isdigit()==True:
        e+=1
         
    else:
         e+=0
for i in s:
    
    if i.islower()==True:
        p+=1
         
    else:
         p+=0
for i in s:
    
    if i.isupper()==True:
        l+=1
         
    else:
         l+=0
if n==0:
    print(False)
else:
    print(True)
if r==0:
    print(False)
else:
    print(True)
if e==0:
    print(False)
else:
    print(True)
if p==0:
    print(False)
else:
    print(True)
if l==0:
    print(False)
else:
    print(True)
# List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    new=[[i,s,k] for i in range(0,x+1) for s in range(0,y+1) for k in range(0,z+1)if i+s+k!=n]
    print(new)

# Python If-Else
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    n=int(n)
    if n%2==0 and 1<n<6:
        print("Not Weird")
    elif n%2==0 and 5<n<21:
        print("Weird")
    elif n%2==0 and n>20:
        print("Not Weird")
    else:
        print("Weird")

# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sort=sorted(arr,reverse=True)
    
    i=1
    while sort[i]==sort[i-1] and i<n+1:
        i+=1
    run_up=sort[i]
    print(run_up)
        
# Nested Lists
if __name__ == '__main__':
    lis=[]
    second=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lis.append([name,score])
    punt=sorted(set([score for name,score in lis]))
    secpunt=punt[1]
    secpunt_st=[name for name,score in lis if score==secpunt]
    for i in sorted(secpunt_st):
        print(i)
# Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    aver=(sum(student_marks[query_name])/len(student_marks[query_name]))
    print(f"{aver:.2f}")
        
# Lists
if __name__ == '__main__':
    N = int(input())
    l=[]
    
    for i in range(1,N+1):
        c=input().split()
        if c[0]=="insert":
            l.insert(int(c[1]),int(c[2]))
        elif c[0]=="remove":
            l.remove(int(c[1]))
        elif c[0]=="append":
            l.append(int(c[1]))
        elif c[0]=="sort":
            l.sort()
        elif c[0]=="pop":
            l.pop()
        elif c[0]=="reverse":
            l.reverse()
        elif c[0]=="print":
            print(l)
# Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    print(hash(t))
# sWAP cASE
def swap_case(s):
    stringa=[]
    for i in range(0,len(s)):
        
        
        if s[i].islower():
            stringa.append(s[i].upper())
        elif s[i].isupper():
            stringa.append(s[i].lower())
        else:
            stringa.append(s[i])
    string="".join(stringa)
    return string
# String Split and Join
def split_and_join(line):
    l=line.split(" ")
    res="-".join(l)
    return res

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# What's Your Name?
def print_full_name(first, last):
    print("Hello "+first+" "+last+"! You just delved into python.")
# Mutations
def mutate_string(string, position, character):
    stringa=string[0:position]+character+string[position+1:len(string)]
    return stringa
# Find a string
def count_substring(string, sub_string):
    c=0
    for i in range(len(string)-len(sub_string)+1):
        if sub_string==string[i:i+len(sub_string)]:
            c+=1
    return int(c)


# Text Wrap
def wrap(string, max_width):
    l=[string[i:i+max_width] for i in range(0,len(string),max_width)]
        
    return "\n".join(l)
# Designer Door Mat
def door_math(N,M):
    for i in range(1,N,2):
        s=(".|."*i)
        print(s.center(M,"-"))
    print("WELCOME".center(M,"-"))
    for i in range(N-2,0,-2):
        p=(".|."*i)
        print(p.center(M,"-"))
N,M=map(int,input().split())
door_math(N,M)
# String Formatting
def print_formatted(number):
    width = len(bin(number))-2
    
    dec=[str(x) for x in range(1,number+1)]
    oc=[oct(i)[2:] for i in range(1,number+1)]
    he=[hex(s)[2:] for s in range(1,number+1)]
    bi=[bin(j)[2:] for j in range(1,number+1)]
    
    for i in range(number):
        print(f"{dec[i]:>{width}} {oc[i]:>{width}} {he[i].upper():>{width}} {bi[i]:>{width}}")
        
# Alphabet Rangoli
def print_rangoli(size):
    r=[]
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    for i in range(size):
        sx = alfabeto[size-1:i:-1] 
        dx = alfabeto[i:size]         
        l = "-".join(sx + dx)
        l = l.center(4*size-3, "-")
        r.append(l)
    print("\n".join(r[::-1] + r[1:]))

# Capitalize!
def solve(s):
    
    nome=list(s.split(" "))
    nome=[i.capitalize() for i in nome]
    nomef=" ".join(nome)
    return nomef
# The Minion Game
def minion_game(string):
    vocali="AEIOU"
    consonanti="BCDFGHJKLMNPQRSTVWXYZ"
    s=0
    k=0
    for i in range(len(string)):
        if string[i] in vocali:
            k+=1
        elif string[i] in consonanti:
            s+=1
    if string[0] in vocali:
        k+=int(len(string)-1)
    elif string[0] in consonanti:
        s+=int(len(string)-1)
    for i in range(1,len(string)):
        if string[i] in vocali:
            k+=len(string)-i-1
        elif string[i] in consonanti:
            s+= len(string)-i-1
    if s<k:
        print(f"Kevin {k}")
    elif s>k:
        print(f"Stuart {s}") 
    else:
        print("Draw")    
# Merge the Tools!
def merge_the_tools(string, k):
    l=[]
    
    for i in range(0,len(string),k):
        l.append(string[i:i+k])
    for i in range(len(l)):
        
        s=set(l[i])
        print("".join(s))
# No Idea!
n, m = map(int,input().split())  
array = list(map(int,input().split())) 
A = set(map(int,input().split()))  
B = set(map(int,input().split()))  
h = 0

for i in array:
    if i in A:
        h+=1
    elif i in B:
        h-=1  
print(h)
# Introduction to Sets
def average(array):
    s=set(array)
    av=sum(s)/len(s)
    return av
# Symmetric Difference
nM=int(input())
M=set(input().split(" "))
nN=int(input())
N=set(input().split(" "))
l=[]
m=[]
l.append(N.difference(M))
l.append(M.difference(N))
for i in range(len(l)):
    for s in l[i]:
        m.append(int(s))
m.sort()
for i in m:
    print(i)
# Set .add()
N=int(input())
countries=set()
for i in range(N):
    countries.add(input())
n=0

for i in range(len(countries)):
    n+=1
print(n)
# Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
N=int(input())
for i in range(1,N+1):
    r=input().split()
    if r[0]=="pop":
        s.pop()
    elif r[0]=="remove":
        s.remove(int(r[1]))
    elif r[0]=="discard":
        s.discard(int(r[1]))
    
print(sum(s))
# Set .union() Operation
n=int(input())
en=set(map(int,input().split()))
b=int(input())
fr=set(map(int,input().split()))
l=[]
for i in en:
    l.append(i)
for i in fr:
    l.append(i)
s=set(l)
print(len(s))

# Set .intersection() Operation
n=int(input())
en=set(map(int,input().split()))
b=int(input())
fr=set(map(int,input().split()))
l=[x for x in en if x in fr]
print(len(l))
# Set .difference() Operation
n=int(input())
en=set(map(int,input().split()))
b=int(input())
fr=set(map(int,input().split()))
s=set([x for x in en if x not in fr])
print(len(s))

# Set .symmetric_difference() Operation
n=int(input())
en=set(map(int,input().split()))
b=int(input())
fr=set(map(int,input().split()))
s=set([x for x in en if x not in fr])
r=set([i for i in fr if i not in en])
print(len(s)+len(r))

# Set Mutations
nA=int(input())
A=set(map(int,input().split()))
N=int(input())
for i in range(N):
    op=input().split()[0]
    num=set(map(int,input().split()))
    if op=="intersection_update":
        A.intersection_update(num)
    if op=="symmetric_difference_update":
        A.symmetric_difference_update(num)
    if op=="difference_update":
        A.difference_update(num)
    if op=="update":
        A.update(num)
print(sum(A))

# The Captain's Room
K=int(input())
rooms=list(map(int,input().split(" ")))
s=set(rooms)
u=(sum(s)*K-sum(rooms))/(K-1)
print(int(u))
# Check Subset
T=int(input())
for i in range(T):
    nA=int(input())
    A=set(map(int,input().split()))
    nB=int(input())
    B=set(map(int,input().split()))
    c=0
    for i in A:
        if i in B:
            c+=1
    if c==nA:
        print(True)
    else:
        print(False)
# Check Strict Superset
A=set(map(int,input().split()))
n=int(input())
c=True
for i in range(n):
    s=set(map(int,input().split()))
    if not A.issuperset(s):
        c=False
        break
print(c)
# collections.Counter()
from collections import Counter
X=int(input())
shoes=list(map(int,input().split()))
N=int(input())
d= dict(Counter(shoes))
money=0
for i in range(N):
    c=list(map(int,input().split()))
    if c[0] in d and d[c[0]]>0:
        money+=c[1]
        d[c[0]]=d[c[0]]-1
print(money)
# DefaultDict Tutorial
from collections import defaultdict
nm=list(map(int,input().split()))
n=nm[0]
m=nm[1]
A=defaultdict(list)
B=defaultdict(list)
for i in range(1,n+1):
    a=input().strip()
    A[a].append(str(i))
for j in range(1,m+1):
    b=input().strip()
    if b in A:
        print(" ".join(A[b]))
    else:
        print(-1)
# Collections.namedtuple()
from collections import namedtuple
N=int(input())
columns = input().split()
Student = namedtuple('Student', columns)
students = []
for _ in range(N):
    values = input().split()
    student = Student(*values)
    students.append(student)
total_marks = 0
for student in students:
    total_marks += int(student.MARKS)

average_marks = total_marks / N
print(average_marks)
# Collections.OrderedDict()
from collections import OrderedDict
N=int(input())
d=OrderedDict()
for i in range(N):
    it=input().split()
    it1=" ".join(it[:-1])
    it2=int(it[-1])
    if it1 not in d.keys():
        d[it1]=it2
    else:
        d[it1]+=it2
for k,j in d.items():
    print(k,j)
# Word Order
from collections import OrderedDict
n=int(input())
od=OrderedDict()
for i in range(n):
    parola=input().strip()
    if parola in od:
        od[parola]+=1
    else:
        od[parola]=1
print(len(od))
for i in od:
    print(od[i],end=" ")
# Collections.deque()
from collections import deque
N=int(input())
d=deque()
for i in range(N):
    c=input().split()
    if c[0]=="append":
        d.append(c[1])
    elif c[0]=="appendleft":
        d.appendleft(c[1])
    elif c[0]=="popleft":
        d.popleft()
    elif c[0]=="pop":
        d.pop()
for k in d:
    print(k,end=" ") 
# Piling Up!
from collections import deque
T=int(input())
for i in range(T):
    n=int(input())
    l=deque(map(int,input().split()))
    m=2**31
    p=True
    while l:
        if l[0]>=l[-1]:
            k=l.popleft()
        else:
            k=l.pop()
        if k>m:
            p=False
            break
        m=k
    if p==True:
        print("Yes")
    else:
        print("No")
# Company Logo
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
from collections import OrderedDict
O=OrderedDict()
for i in s:
    if i in O:
        O[i]+=1
        
    else:
        O[i]=1
OO=list(sorted(O.items(),key=lambda x:(-x[1], x[0])))
for i in range(3):
    v=OO[i]
    print(v[0],v[1])
# Calendar Module
import calendar
giorno=list(map(int,input().split()))
se=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
g=calendar.weekday(giorno[2],giorno[0],giorno[1])
print(se[g])
# Time Delta
import math
import os
import random
import re
import sys
from datetime import datetime
def time_delta(t1, t2):
    dt1 = datetime.strptime(t1,"%a %d %b %Y %H:%M:%S %z")
    dt2 = datetime.strptime(t2,"%a %d %b %Y %H:%M:%S %z")
    diff = abs((dt1 - dt2).total_seconds())
    return str((int(diff)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')
        

    fptr.close()
# Exceptions
N=int(input())
for i in range(N):
    ab=input().split()
 
    try:
        int(ab[0])//int(ab[1])
    except ZeroDivisionError as e:
         print("Error Code:",e)
    except ValueError as m:
        print("Error Code:",m)
    else:
        print(int(ab[0])//int(ab[1]))
        
# Zipped!
nx=list(map(int,input().split()))
l=[]
for i in range(nx[1]):
    r=list(map(float,input().split()))
    l.append(r)
    

for i in zip(*l):
    print(sum(i)/nx[1])
# Athlete Sort
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
arr=sorted(arr,key=lambda x:x[k])
for i in arr:
    print(" ".join(map(str,i)))
# ginortS
s=input()
l=[]
u=[]
o=[]
e=[]
for i in s:
    if i.islower():
        l.append(i)
    elif i.isupper():
        u.append(i)
    elif int(i)%2==0:
        e.append(i)
    elif int(i)%2!=0:
        o.append(i)
l=sorted(l)
u=sorted(u)
o=sorted(o)
e=sorted(e)
for i in (l,u,o,e):
    for s in i:
        print(s,end="")
# Map and Lambda Function
def fibonacci(n):
    fib=[]
    for i in range(n):
        if i==0:
            fib.append(0)
        elif i==1:
            fib.append(1)
        else:
            fib.append(fib[i-1]+fib[i-2])
    return fib
# Detect Floating Point Number
T=int(input())
for i in range(T):
    n=input()
    
    if n[0:2]=="+-" or n[0:2]=="-+":
        print(False)
        continue 
        
    try:
        nm=float(n)
        p=n.find(".")
        if p != -1 and n[p+1:].isdigit() and len(n[p+1:]) > 0:
            print(True)
        else:
            print(False)
    except:
        print(False)
# Re.split()
import re
s = "100,200.300,400.500"
patt = r"[,.]"
result = re.split(patt, s)
print(result)
# Group(), Groups() & Groupdict()
import re
s=input()
se=set()
for i in range(len(s)):
    c=s[i]
    if c in se and c.isalnum():
        if i>0 and s[i-1]==c:
            print(c)
            break
    else:
        se.add(c)
else:
    print(-1)
# Re.findall() & Re.finditer()
import re
s=input()
p=r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou0123456789+-]*[AEIOUaeiou][AEIOUaeiou0123456789+-]*[AEIOUaeiou][AEIOUaeiou0123456789+-]*)(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'
m=re.finditer(p,s)
l=[i.group() for i in m]

if len(l)>0:
    for n in l:
        print(n)
else:
    print(-1)
# Regex Substitution
import re
n=int(input())
for e in range(n):
    l=input()
    l=re.sub(r'(?<= )&&(?= )', 'and', l)
    l=re.sub(r'(?<= )\|\|(?= )', 'or', l)
    print(l)
# Validating Roman Numerals
import re
regex_pattern = r"^^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
# Validating phone numbers
import re
N=int(input())
p=r"^[789]\d{9}$"
for i in range(N):
    s=input()
    if re.match(p,s):
        print("YES")
    else:
        print("NO") 
# Validating and Parsing Email Addresses
import email.utils
import re
n=int(input())
p=r"^<[qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM][qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890._-]*@[qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM]+\.[qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM]{1,3}>$"
for i in range(n):
    e=input()
    em=e.split()
    
    if re.match(p,em[1]):
        l=email.utils.parseaddr(e)
        print(email.utils.formataddr(l))
# Hex Color Code
import re
p=r"#([1234567890ABCDEFabcdef]{3,6})"
n=int(input())
l=[]
for i in range(n):
    l.append(input())
fl='\n'.join(l)
m=re.findall(r'\{([^}]*)\}',fl)
c=[]
for w in m:
    c.extend(re.findall(p,w))
for g in c:
    print(f"#{g}")
# HTML Parser - Part 1
from html.parser import HTMLParser
n=int(input())
html=[]
for i in range(n):
    html.append(input())
html1="".join(html)
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        if attrs:
            for attr in attrs:
                print(f"-> {attr[0]} > {attr[1]}")
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        if attrs:
            for attr in attrs:
                print(f"-> {attr[0]} > {attr[1]}")

MyHTMLParser().feed(html1)
# HTML Parser - Part 2
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)
    def handle_data(self, data):
        if data.strip():
            print (">>> Data")
            print(data)
# Re.start() & Re.end()
import re
s=input()
k=input()
p=f"(?={k})"
m=re.finditer(p,s)
ind=[]
for w in m:
    start=w.start()
    end=w.end()+len(k)-1
    ind.append((start,end))
if ind:
    for start, end in ind:
        print((start,end))
else:
    print((-1,-1))
# Detect HTML Tags, Attributes and Attribute Values
from html.parser import HTMLParser
n=int(input())
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ( tag)
        if attrs:
            for attr in attrs:
                print(f"-> {attr[0]} > {attr[1]}")
   
html_lines=[input().rstrip() for x in range(n)]  
html="\n".join(html_lines)
parser=MyHTMLParser()
parser.feed(html)
# Validating UID
import re
T=int(input())
for x in range(T):
    uid=input()
    upper=re.findall(r"[A-Z]",uid)
    dig=re.findall(r"[0-9]",uid)
    if len(upper)>=2 and len(dig)>=3 and uid.isalnum() and len(uid)==len(set(uid)) and len(uid)==10:
        print("Valid")
    else:
        print("Invalid")
# Validating Credit Card Numbers
import re
n=int(input())
p = r"^[456]\d{3}(-?\d{4}){3}$"
for i in range(n):
    c=input()
    cc=c.replace("-","")
    v=bool(re.search(r"(\d)\1{3,}",cc))
    if re.match(p,c) and v==False and len(cc)==16:
        print("Valid")
    else:
        print("Invalid")
# Validating Postal Codes
regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.

# Matrix Script
import math
import os
import random
import re
import sys
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
ma=[]
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    
for s in range(m):
    for x in matrix:
        ma.append(x[s])
l="".join(ma)
l=re.sub(r'(?<=[a-zA-Z0-9])\s*[^\w\s]+\s*(?=[a-zA-Z0-9])',' ',l)
print(l)
# XML 1 - Find the Score
def get_attr_number(node):
    c=len(node.attrib)
    for i in node:
        c+=get_attr_number(i)
    return c
# XML2 - Find the Maximum Depth
maxdepth = 0
def depth(elem, level):
    global maxdepth
    level+=1
    if level>maxdepth:
        maxdepth=level
    for i in elem:
        depth(i,level)
# Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        lista=[]
        for i in l:
            if len(i)==10:
                i="+91 "+i[0:5]+" "+i[5:10]
                lista.append(i)
            if len(i)==11:
                i="+91 "+i[1:6]+" "+i[6:11]
                lista.append(i)
            if len(i)==12:
                i="+"+i[0:2]+" "+i[2:7]+" "+i[7:12]
                lista.append(i)
            if len(i)==13:
                i=i[0:3]+" "+i[3:8]+" "+i[8:13]
                lista.append(i)
        lista=sorted(lista)
        for s in lista:
            print(s)
    return fun
# Decorators 2 - Name Directory
from operator import itemgetter
def person_lister(f):
    def inner(people):
        people.sort(key=lambda x:int(x[2]))
        return [f(p) for p in people]
    return inner
# Arrays
def arrays(arr):
    l=numpy.array(arr,float)
    return l[::-1]
# Shape and Reshape
import numpy
arr=numpy.array(list(map(int,input().split())))
print(numpy.reshape(arr,(3,3)))
# Transpose and Flatten
import numpy
nm=list(map(int,input().split()))
n=nm[0]
m=nm[1]
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
arr=numpy.array(l)
print(numpy.transpose(arr))
print(arr.flatten())   
# Concatenate
import numpy
nmp=list(map(int,input().split()))
n=nmp[0]
m=nmp[1]
p=nmp[2]
arr1=[]
arr2=[]
for i in range(n):
    arr1.append(list(map(int,input().split())))
for i in range(m):
    arr2.append(list(map(int,input().split())))
print(numpy.concatenate((arr1,arr2),axis=0))
# Zeros and Ones
import numpy
s=tuple(map(int,input().split()))
print(numpy.zeros(s,dtype=int))
print(numpy.ones(s,dtype=int))
# Eye and Identity
import numpy
numpy.set_printoptions(legacy="1.13")
s=tuple(map(int, input().split()))
print(numpy.eye(s[0],s[1],k=0))
# Array Mathematics
import numpy
nm=tuple(map(int, input().split()))
arr1=[]
arr2=[]
for i in range(nm[0]):
    arr1.append(list(map(int,input().split())))
for i in range(nm[0]):
    arr2.append(list(map(int,input().split())))
a=numpy.array(arr1)
b=numpy.array(arr2)
print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
print(a//b)
print(numpy.mod(a,b))
print(numpy.power(a,b))
# Floor, Ceil and Rint
import numpy
numpy.set_printoptions(legacy="1.13")
arr=numpy.array(list(map(float,input().split())))
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))
#Sum and Prod
import numpy
nm=tuple(map(int,input().split()))
arr=[]
for i in range(nm[0]):
    arr.append(list(map(int,input().split())))
s=numpy.sum(arr,axis=0)
print(numpy.prod(s,axis=None))
#Min and Max
import numpy
nm=tuple(map(int,input().split()))
arr=[]
for i in range(nm[0]):
    arr.append(list(map(int,input().split())))
mi=numpy.min(numpy.array(arr),axis=1)
print(numpy.max(mi))
#Mean, Var, and Std
import numpy
nm=tuple(list(map(int,input().split())))
arr=[]
for i in range(nm[0]):
    arr.append(list(map(int,input().split())))
print(numpy.mean(numpy.array(arr),axis=1))
print(numpy.var(numpy.array(arr),axis=0))
print(round(numpy.std(numpy.array(arr),axis=None),11))
#Dot and Cross
import numpy
n=int(input())
a=[]
b=[]
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    b.append(list(map(int,input().split())))
print(numpy.dot(numpy.array(a),numpy.array(b)))
#Inner and Outer
import numpy
A=numpy.array(list(map(int,input().split())))
B=numpy.array(list(map(int,input().split())))
print(numpy.inner(A,B))
print(numpy.outer(A,B))
#Polynomials
import numpy
p=numpy.array(list(map(float,input().split())))
x=float(input())
print(numpy.polyval(p,x))  
#Linear Algebra
import numpy
n=int(input())
A=numpy.array([list(map(float, input().split())) for i in range(n)])
print(round(numpy.linalg.det(A),2))
#Birthday Cake Candles
import math
import os
import random
import re
import sys
def birthdayCakeCandles(candles):
    m=max(candles)
    c=0
    for i in candles:
        if i==m:
            c+=1
    return(c)
#Number Line Jumps
def kangaroo(x1, v1, x2, v2):
    if v1==v2:
        return "YES" if x1==x2 else "NO"
    n=(x2-x1)/(v1-v2)
    if n>=0 and n.is_integer():
        return "YES"
    else:
        return "NO"
#Viral Advertising
def viralAdvertising(n):
    c=2
    l=2
    for i in range(n-1):
        g=(l*3)//2
        l=g
        c+=g
    return c
#Recursive Digit Sum
def superDigit(n, k):
    s = sum(int(x) for x in n) * k
    if len(str(s))>1:
        return superDigit(str(s),1)
    if len(str(s))==1:
        return s
#Insertion Sort - Part 1
def insertionSort1(n, arr):
    x=arr[-1]
    j=n-2
    while j>=0 and arr[j]>x:
        arr[j+1]=arr[j]
        print(*arr)
        j-=1
    arr[j+1]=x
    print(*arr)
#Insertion Sort - Part 2
def insertionSort2(n, arr):
    for i in range(1, n):  
        x = arr[i]
        j = i - 1  
        while j >= 0 and arr[j] > x:
            arr[j + 1] = arr[j]  
            j -= 1
        arr[j + 1] = x  
        print(*arr)
