# @author: Broglio Matteo - 1200739
# @title: Homework_1


#######################
#                     #
# INTRODUCTION        #
#                     #
#######################

# --------------------------------------------------------------- 
# Say "Hello, World!" With Python
print("Hello, World!")

# --------------------------------------------------------------- 
# Python If-Else
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    
    is_odd = n % 2 # if 1 == else 0 == False
    is_min_6 = n < 6
    is_min_21 = n < 21
    
    if is_odd:
        print('Weird')
    else:
        if is_min_6:
            print('Not Weird')
        elif is_min_21:
            print('Weird')
        else: 
            # n >= 21
            print('Not Weird')

# ---------------------------------------------------------------            
# Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    assert a >= 1 and a <= 10 ** 10, 'Constraint failed for a!'
    assert b >= 1 and b <= 10 ** 10, 'Constraint failed for b!'
    
    print(a + b)
    print(a - b)
    print(a * b)

# --------------------------------------------------------------- 
# Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a // b)
    print(a / b)

# --------------------------------------------------------------- 
# Loops
if __name__ == '__main__':
    n = int(input())
    
    assert n >= 1 and n <= 20
    
    for i in range(n):
        print(i ** 2)
    
# --------------------------------------------------------------- 
# Write a function
def is_leap(year):
    assert 1900 <= year <= 10 ** 5, 'Constraint failed!'
    
    div_4 = not year % 4
    div_100 = not year % 100
    div_400 = not year % 400
    
    if (div_100 and div_400) or (div_4 and not div_100):
        return True
    return False

# --------------------------------------------------------------- 
#Print Function
if __name__ == '__main__':
    n = int(input())
    
    assert 1 <= n <= 150, 'Constraint failed!'
    
    for i in range(1, n + 1):
        print(i, end='')


#######################
#                     #
# BASIC-DATA-TYPES    #
#                     #
#######################

# --------------------------------------------------------------- 
# List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print(
        [
            [i,j,k] for i in range(x + 1) 
                    for j in range(y + 1)
                    for k in range(z + 1)
                    if i + j + k != n
        ]
    )
    
# ---------------------------------------------------------------  
# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    print(
        max([i for i in arr if i != max(arr)])
    )

# --------------------------------------------------------------- 
# Nested Lists
if __name__ == '__main__':
    records = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    min_grade = min([score for _, score in records])
    min_2d_grade = min([score for _, score in records if score != min_grade])
    min_2d_grade_names = sorted(
            [name for name, score in records if score == min_2d_grade]
        )
        
    for name in min_2d_grade_names:
        print(name)
 
# ---------------------------------------------------------------  
# Finding the percentage
if __name__ == '__main__':
    n = int(input())
    assert 2 <= n <= 10, 'Constraint error!'
    
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        assert len(scores) == 3, 'Constraint error!'
        student_marks[name] = scores
    query_name = input()
    
    print(
        format(
            sum(student_marks[query_name]) / 3, '.2f'
        )
        
    )
 
# ---------------------------------------------------------------  
# Lists
if __name__ == '__main__':
    N = int(input())
    my_list = []
        
    for n in range(N):
        command, *params = input().split()
        params = list(map(int, params))
        
        if command == 'print':
            print(my_list)
        else:
            getattr(my_list, command)(*params)
            
 
# ---------------------------------------------------------------  
# Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split(" ")))

    print(hash(integer_list))

    
#######################
#                     #
# STRINGS             #
#                     #
#######################
# --------------------------------------------------------------- 
#sWAP cASE
def swap_case(s):
    return s.swapcase()
    
# ---------------------------------------------------------------    
# String Split and Join
def split_and_join(line):
    return "-".join(
                line.split(" ")
                )
                
# ---------------------------------------------------------------                 
# What's Your Name?
def print_full_name(first, last):
    print(f'Hello {first} {last}! You just delved into python.')

# --------------------------------------------------------------- 
# Mutations
def mutate_string(string, position, character):
    string = list(string)
    string[position] = character
    return ''.join(string)
    
# ---------------------------------------------------------------     
# Find a string
import re
def count_substring(string, sub_string):
    return len(
                re.findall(f'(?={sub_string})', string)
                )
                
# ---------------------------------------------------------------                 
# String Validators
if __name__ == '__main__':
    s = input()
    
    for check in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        print(
            any([getattr(char, check)() for char in s])
            )
            
# ---------------------------------------------------------------             
# Text Alignment
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    
# ---------------------------------------------------------------     
# Text Wrap    
def wrap(string, max_width):
    return textwrap.fill(string, max_width)
    
# ---------------------------------------------------------------     
# Designer Door Mat
N, M = map(int, input().split())

assert N % 2, 'Constraint error!'

portion = N // 2

for p in range(portion):
    print(
        ('.|.' + '.|.' * (p * 2)).center(M, '-') 
        )    
print('WELCOME'.center(M, '-'))
for p in range(portion - 1, -1, -1):
    print(
        ('.|.' + '.|.' * (p * 2)).center(M, '-') 
        ) 
 
# ---------------------------------------------------------------  
# String Formatting
def print_formatted(number):
    width = len('{:b}'.format(number))
    for n in range(1, number + 1):
        print('{0:{1}d} {2:{3}o} {4:{5}X} {6:{7}b}'.format(
            n, width, n, width, n, width, n, width))

# --------------------------------------------------------------- 
# Alphabet Rangoli         
import string
string.ascii_lowercase

def print_rangoli(size):
    rows = size - 1
    words = list(string.ascii_lowercase[:size])
    rev_words = words[::-1]

    w = rev_words[:size - 1]
    w2 = list(reversed(rev_words[:size]))
    size = len(list("-".join(w + w2)))
    
    for row in range(rows + 1):
            w = rev_words[:row + 1]
            w2 = list(reversed(rev_words[:row]))
            print(("-".join(w + w2)).center(size, '-'))
        
    for row in range(rows -1, -1, -1):
        w = rev_words[:row + 1]
        w2 = list(reversed(rev_words[:row]))
        print(("-".join(w + w2)).center(size, '-'))        
        
  
# ---------------------------------------------------------------   
# Capitalize!
def solve(s):
    s_list = s.split(' ')
    return ' '.join([word.capitalize() for word in s_list])

# --------------------------------------------------------------- 
# The Minion Game
# DUE TO TIMEOUT ISSUES, I'VE OPTIMIZED THE FUNCTION WITH THE FORUM SUPPORT
def minion_game(string):  
    VOWELS = 'AEIOU'
    str_len = len(string)
    stuart = 0
    kevin = 0
    
    for sub_idx in range(len(string)):
        sub_str = string[sub_idx]
        if sub_str in VOWELS:
            kevin += str_len - sub_idx
        else:
            stuart += str_len - sub_idx
                
    win_kevin = kevin > stuart
    win_stuart = kevin < stuart
    winner = f'Kevin {kevin}' if win_kevin else f'Stuart {stuart}' if win_stuart else 'Draw'
    print(winner)
    
# ---------------------------------------------------------------    
# Merge the Tools!
import re
from collections import OrderedDict

def merge_the_tools(string, k):
    chunks = re.findall('.{%d}' % k, string)

    for chunk in chunks:
        print(''.join(OrderedDict.fromkeys(chunk).keys()))
        
#######################
#                     #
# SETS                #
#                     #
#######################
# --------------------------------------------------------------- 
#Introduction to Sets
def average(array):
    set_array = set(array)
    return '{:.3f}'.format(sum(set_array) / len(set_array))

# --------------------------------------------------------------- 
# No Idea!
n, m = map(int, input().split())
array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happiness = 0

for i in array:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1

print(happiness)
 
# ---------------------------------------------------------------     
# Symmetric Difference
m = int(input())
set_m = set(map(int, input().split()))
n = int(input())
set_n = set(map(int, input().split()))

diff = (
    set_m.difference(set_n)
        ).union(
            set_n.difference(set_m)
            )
            
diff = sorted(list(diff)) 
           
for i in diff:
    print(i)

# --------------------------------------------------------------- 
# Set .add()
n = int(input())
stamps_set = set()

for i in range(n):
    stamps_set.add(input())
    
print(len(stamps_set))

# --------------------------------------------------------------- 
# Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
n_commands = int(input())

for i in range(n_commands):
    command, *params = input().split()
    params = map(int, params)
    getattr(s, command)(*params)

print(sum(s))

# --------------------------------------------------------------- 
# Set .union() Operation
n = int(input())
n_set = set(map(int, input().split()))
b = int(input())
b_set = set(map(int, input().split()))

print(
    len(n_set.union(b_set))
    )

# --------------------------------------------------------------- 
# Set .intersection() Operation
n = int(input())
n_set = set(map(int, input().split()))
b = int(input())
b_set = set(map(int, input().split()))

print(
    len(n_set.intersection(b_set))
    )

# --------------------------------------------------------------- 
# Set .difference() Operation
n = int(input())
n_set = set(map(int, input().split()))
b = int(input())
b_set = set(map(int, input().split()))

print(
    len(n_set.difference(b_set))
    )

# --------------------------------------------------------------- 
# Set .symmetric_difference() Operation
n = int(input())
n_set = set(map(int, input().split()))
b = int(input())
b_set = set(map(int, input().split()))

print(
    len(n_set.symmetric_difference(b_set))
    )

# --------------------------------------------------------------- 
# Set Mutations
n = int(input())
s = set(map(int, input().split()))
n_commands = int(input())

for i in range(n_commands):
    command, *params = input().split()
    params = map(int, params)
    values = set(map(int, input().split()))
    getattr(s, command)(values)

print(sum(s))

# --------------------------------------------------------------- 
# The Captain's Room
from collections import Counter

n =int(input())
n_list = list(map(int, input().split()))

counter = Counter(n_list)
print(counter.most_common()[-1][0])

# --------------------------------------------------------------- 
#Check Subset
n_tests = int(input())

for _ in range(n_tests):
    n_a = int(input())
    a = set(map(int, input().split()))
    n_b = int(input())
    b = set(map(int, input().split()))
    
    print(
        len(a.union(b)) == len(b)
    )

# ---------------------------------------------------------------  
# Check Strict Superset
a = set(map(int, input().split()))
n = int(input())
checks = []

for _ in range(n):
    test = set(map(int, input().split()))
    checks.append(
        len(a.union(test)) == len(a) and len(a.difference(test)) > 0
    )
    
print(all(checks))
  

#######################
#                     #
# COLLECTIONS         #
#                     #
#######################
# --------------------------------------------------------------- 
# collections.Counter()
from  collections import Counter
x = int(input())
x_sizes = Counter(map(int, input().split()))
n_costumers = int(input())
total = 0

for _ in range(n_costumers):
    shoes = tuple(map(int, input().split()))
    shoes_n = shoes[0]
    shoes_price = shoes[1]
    available = int(x_sizes[shoes_n])
    
    if available:
        total += shoes_price
        x_sizes.subtract({shoes_n: 1})
        
print(total)

# --------------------------------------------------------------- 
#  DefaultDict Tutorial
from collections import defaultdict

n, m = map(int, input().split())
dd = defaultdict(list)

for _ in range(n):
    dd['A'].append(input())
for _ in range(m):
    test = input()
    indexes = [str(idx + 1) for idx, value in enumerate(dd['A']) if value == test]
    
    if indexes:
        print(' '.join(indexes))
    else:
        print(-1)
        
# ---------------------------------------------------------------         
# Collections.namedtuple()
from collections import namedtuple
n = int(input())
cols_names = input().split()
Student = namedtuple('Student', cols_names)
sum_marks = 0
for _ in range(n):
    student = Student(
        *[int(value) if value.isdigit() else value for value in input().split()]
        )
    sum_marks += student.MARKS

print('{:.2f}'.format(sum_marks / n))

# --------------------------------------------------------------- 
# Collections.OrderedDict()
from collections import OrderedDict

n = int(input())
items = OrderedDict()

for _ in range(n):
    *item_name, price = input().split()
    item_name = ' '.join(item_name)
    price = int(price)
    try:
        items[item_name] += price
    except KeyError:
        items[item_name] = price

for item in items.keys():
    print(item, items[item])
 
# --------------------------------------------------------------- 
# Word Order
from collections import OrderedDict

n = int(input())
words = OrderedDict()

for _ in range(n):
    word = input()
    try:
        words[word] += 1
    except KeyError:
        words[word] = 1
        
print(len(words.keys()))
print(' '.join([str(value) for value in words.values()]))

# --------------------------------------------------------------- 
# Collections.deque()
from collections import deque

n_commands = int(input())
d = deque()

for i in range(n_commands):
    command, *params = input().split()
    params = map(int, params)
    getattr(d, command)(*params)

print(' '.join(map(str, d)))

# --------------------------------------------------------------- 
# Company Logo
from collections import Counter

if __name__ == '__main__':
    s = input()
    counter = Counter(s).most_common()
    counter_sorted = sorted(counter, key=lambda x: (-x[1], x[0]))
    top_3 = counter_sorted[:3]

    for item in top_3:
        print(' '.join(map(str, item)))

# --------------------------------------------------------------- 
# Piling Up!
from collections import deque

n_tests = int(input())

for _ in range(n_tests):
    prev_value = float('inf')
    n_blocks = int(input())
    blocks = deque(map(int, input().split()))
    
    while blocks:
        command = 'popleft' if blocks[0] > blocks[-1] else 'pop'
        pop_value = getattr(blocks, command)()
        
        if pop_value <= prev_value:
            prev_value = pop_value
        else:
            break
        
    if not blocks:
        print('Yes')
    else:
        print('No')


#######################
#                     #
# DATE & TIME         #
#                     #
#######################
# --------------------------------------------------------------- 
# Calendar Module
from calendar import day_name, weekday

month, day, year = map(int, input().split())
print(day_name[weekday(year, month, day)].upper())

# --------------------------------------------------------------- 
# Time Delta
#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    t1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    return str(
               abs(
                    int(
                        (t2 - t1).total_seconds()
                    )
                )
            )

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()



#######################
#                     #
# EXCEPTIONS          #
#                     #
#######################
# --------------------------------------------------------------- 
# Exceptions
n = int(input())

for _ in range(n):
    try:
        a, b = map(int, input().split())
        print(int(a / b))
    except ZeroDivisionError as e:
        print('Error Code: integer division or modulo by zero')
    except ValueError as e:
        print(f'Error Code: {e}')


#######################
#                     #
# BUILT-INS           #
#                     #
#######################
# --------------------------------------------------------------- 
# Zipped!
n, x = map(int, input().split())
grades = []

for _ in range(x):
    grades.append(tuple(map(float, input().split())))

avg = zip(*grades)

for i in avg:
    print(sum(i) / x)

# --------------------------------------------------------------- 
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
    arr_sorted = sorted(arr, key= lambda x: x[k])
    for i in arr_sorted:
        print(*i)

# --------------------------------------------------------------- 
# Any or All
n = int(input())
m = input().split()

def is_palindrome(x):
    return x == x[::-1]

if all(int(i) > 0 for i in m):
    print(
        any(
            map(is_palindrome, m)    
        )
    )
else:
    print(False)

# --------------------------------------------------------------- 
# ginortS
string = input()

lowers = sorted([x for x in string if x.islower()])
uppers = sorted([x for x in string if x.isupper()])
odds = sorted([x for x in string if x.isdigit() and int(x) % 2 ])
evens = sorted([x for x in string if x.isdigit() and not int(x) % 2])
sorted_word = lowers + uppers + odds + evens

print(*sorted_word, sep='')


#######################
#                     #
# PYTHON FUNCTIONALS  #
#                     #
#######################
# --------------------------------------------------------------- 
# Map and Lambda Function
cube = lambda x: x ** 3 # complete the lambda function 

def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        yield a 
        a, b = b, a + b
        
        
#######################
#                     #
# REGEX & PARSING     #
#                     #
#######################
# --------------------------------------------------------------- 
# Detect Floating Point Number
import re

n = int(input())

for _ in range(n):
    string = input().strip()
    print(
        bool(re.search(r'^[-+]?[0-9]*\.[0-9]+$', string))
    )
    
# ---------------------------------------------------------------     
# Re.split()
regex_pattern = r"[,\.]"	# Do not delete 'r'.

# --------------------------------------------------------------- 
# Group(), Groups() & Groupdict()
import re
string = input()
match = re.search(r'(\w(?!_))\1+', string)

if match is None:
    print('-1')
else:
    print(match.group(1))

# --------------------------------------------------------------- 
# Re.findall() & Re.finditer()
import re

string = input()
c = "qwrtypsdfghjklzxcvbnm"
matches = re.findall(r'(?<=[%s])([aeiou]{2,})(?=[%s])' % (c, c), string, re.I)

if matches:
    for match in matches:
        print(match)
else:
    print('-1')

# --------------------------------------------------------------- 
# Re.start() & Re.end()
import re
string = input()
sub = input()
sub_len = len(sub) - 1

matches = list(re.finditer(r'(?={})'.format(sub), string))
if matches:
    print(
        ''.join(
            ['({}, {})\n'.format(match.start(), match.end() + sub_len) for match in matches]
            )
        )
else:
    print((-1, -1,))
 
# ---------------------------------------------------------------  
# Regex Substitution
import re
n = int(input())

for _ in range(n):
    s = input()
    string = re.sub(r'(?<=\s)&&(?=\s)', 'and', s)
    string = re.sub(r'(?<=\s)\|\|(?=\s)', 'or', string)
    print(string)
    
# ---------------------------------------------------------------     
# Validating Roman Numerals
regex_pattern = r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|X{0,3}|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

# --------------------------------------------------------------- 
# Validating phone numbers
import re
n = int(input())

for _ in range(n):
    phone_number = input()
    is_phone_number = re.search('^[789]\d{9}$', phone_number)
    print(f"{'YES' if is_phone_number else 'NO'}")

# --------------------------------------------------------------- 
# Validating and Parsing Email Addresses
import email.utils
import re

n =int(input())

for _ in range(n):
    e_mail = input()
    e_mail = email.utils.parseaddr(e_mail)
    match = re.fullmatch('^[a-zA-Z][\w\.\-_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}', e_mail[1])
    if match:
        print(email.utils.formataddr(e_mail))

# --------------------------------------------------------------- 
# Hex Color Code
import re

n = int(input())

for _ in range(n):
    string = input()
    matches = re.findall('(#([0-9a-fA-F]{6}|[0-9a-fA-F]{3}))(?=[;,\)])', string)
    if matches:
        for match in matches:
           print(match[0])
           
# ---------------------------------------------------------------           
# HTML Parser - Part 1
from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        if attrs:
            for attr in attrs:
                print('-> %s > %s' % attr)
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        if attrs:
            for attr in attrs:
                print('-> %s > %s' % attr)

n = int(input())
rows = []

for _ in range(n):
    rows.append(input())

html_code = ''.join(rows)    

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(html_code)

# --------------------------------------------------------------- 
# HTML Parser - Part 2
from html.parser import HTMLParser
import re

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        multi_line = re.search('\n', data)
        if multi_line:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        print(data)
    def handle_data(self, data):
        if data != '\n': 
            print('>>> Data')
            print(data)

html = ""  
     
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

# Detect HTML Tags, Attributes and Attribute Values
from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print (tag)
        if attrs:
            for attr in attrs:
                print('-> %s > %s' % attr)
    #def handle_endtag(self, tag):
    #    print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print(tag)
        if attrs:
            for attr in attrs:
                print('-> %s > %s' % attr)

n = int(input())
rows = []

for _ in range(n):
    rows.append(input())

html_code = ''.join(rows)    

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(html_code)

# --------------------------------------------------------------- 
# Detect HTML Tags, Attributes and Attribute Values
from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print (tag)
        if attrs:
            for attr in attrs:
                print('-> %s > %s' % attr)
    #def handle_endtag(self, tag):
    #    print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print(tag)
        if attrs:
            for attr in attrs:
                print('-> %s > %s' % attr)

n = int(input())
rows = []

for _ in range(n):
    rows.append(input())

html_code = ''.join(rows)    

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(html_code)

# --------------------------------------------------------------- 
# Validating UID
import re
n = int(input())

for _ in range(n):
    uid = input()
    
    two_upper_case = len(re.findall('[A-Z]', uid)) >= 2
    three_digits = len(re.findall('[0-9]', uid)) >= 3
    only_alphanum = re.fullmatch('\w{10}', uid)
    ten_unique = len(set(uid)) == 10
    
    if all([two_upper_case, three_digits, only_alphanum, ten_unique]):
        print('Valid')
    else:
        print('Invalid')

# --------------------------------------------------------------- 
# Validating Credit Card Numbers
import re
n = int(input())

for _ in range(n):
    uid = input()
    if '-' in uid:
        four_digit_blocks = all([len(x) == 4 for x in uid.split('-')])
    else:
        four_digit_blocks = True
    uid = uid.replace('-', '')
    
    only_digits = re.fullmatch(r'^[456]\d{15}$', uid)
    not_too_repetitions = not re.findall(r'(\d)\1{3,}', uid)
    
    if all([four_digit_blocks, only_digits, not_too_repetitions]):
        print('Valid')
    else:
        print('Invalid')
        
# --------------------------------------------------------------- 
# Validating Postal Codes
regex_integer_in_range = r"^[1-9]\d{5}$"
regex_alternating_repetitive_digit_pair = r"(?=((\d)\d\2))"

# --------------------------------------------------------------- 
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

for _ in range(n):
    matrix_item = input()
    matrix.append(list(matrix_item))

matrix_cols = list(zip(*matrix))
raw_sentence = ''.join(
    [''.join(col) for col in matrix_cols]
    )
clean_sentence = re.sub(r'(?<=\w)\W+(?=\w)', ' ', raw_sentence)
print(clean_sentence)


#######################
#                     #
# XML                 #
#                     #
#######################
# --------------------------------------------------------------- 
# XML 1 - Find the Score
def get_attr_number(node):
    return sum(
            [len(child.attrib) for child in node.iter()]
        )

# --------------------------------------------------------------- 
# XML2 - Find the Maximum Depth
maxdepth = 0
def depth(elem, level):
    global maxdepth
    if level == maxdepth:
        maxdepth += 1
    for child in elem:
        depth(child, level + 1) 


#########################
#                       #
# CLOSURE & DECORATIONS #
#                       #
#########################
# --------------------------------------------------------------- 
# Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        f([f'+91 {el[-10:-5]} {el[-5:]}' for el in l])
    return fun

# --------------------------------------------------------------- 
# Decorators 2 - Name Directory
def person_lister(f):
    def inner(people):
        return [f(p) for p in sorted(people, key=lambda x: int(x[2]))]
    return inner

#######################
#                     #
# NUMPY               #
#                     #
#######################
# --------------------------------------------------------------- 
# Arrays
def arrays(arr):
    return numpy.array(arr[::-1], float)

# --------------------------------------------------------------- 
# Shape and Reshape
import numpy

print(
    numpy.reshape(
        numpy.array(
            input().split(' '), int
            ), 
        (3,3,)
        )
)

# --------------------------------------------------------------- 
# Transpose and Flatten
import numpy

n, m = map(int, input().split())
arr = numpy.array([input().split(' ') for _ in range(n)], int)
print(arr.transpose())
print(arr.flatten())

# --------------------------------------------------------------- 
# Concatenate
import numpy as np

n, m, p = map(int, input().split(' '))
arr_1 = np.array(
    [list(map(int, input().split(' '))) for _ in range(n)]
    ) 
arr_2 = np.array(
    [list(map(int, input().split(' '))) for _ in range(m)]
    ) 
print(np.concatenate((arr_1, arr_2)))

# --------------------------------------------------------------- 
# Zeros and Ones
import numpy as np

dims = tuple(map(int, input().split(' ')))

print(np.zeros(dims, int))
print(np.ones(dims, int))

# --------------------------------------------------------------- 
# Eye and Identity
import numpy as np
np.set_printoptions(legacy='1.13')

n, m = map(int, input().split(' '))
print(np.eye(n, m))

# --------------------------------------------------------------- 
# Array Mathematics
import numpy as np
np.set_printoptions(legacy='1.13')

n, m = map(int, input().split(' '))

A = np.array([list(map(int, input().split(' '))) for _ in range(n)], int)
B = np.array([list(map(int, input().split(' '))) for _ in range(n)], int)

for task in ('add', 'subtract', 'multiply', 'floor_divide', 'mod', 'power'):
    print(
        getattr(np, task)(A, B)
        )
      
# ---------------------------------------------------------------       
# Floor, Ceil and Rint
import numpy as np
np.set_printoptions(legacy='1.13')

arr = np.array(list(map(float, input().split(' '))))

for task in ('floor','ceil','rint'):
    print(
        getattr(np, task)(arr)
        )
        
 # ---------------------------------------------------------------        
# Sum and Prod
import numpy as np

n, m = map(int, input().split(' '))
arr = np.array(
    [list(map(int, input().split())) for _ in range(n)]
)
print(
    np.product(
        np.sum(arr, axis=0)
    )
)

# --------------------------------------------------------------- 
# Min and Max
import numpy as np

n, m = map(int, input().split(' '))
arr = np.array(
    [list(map(int, input().split())) for _ in range(n)]
)
print(
    np.max(
        np.min(arr, axis=1)
    )
)

# --------------------------------------------------------------- 
# Mean, Var, and Std
import numpy as np

n, m = map(int, input().split(' '))
arr = np.array(
    [list(map(int, input().split())) for _ in range(n)]
)
for task, param in (('mean', 1,), ('var', 0,),):
    print(
        getattr(np, task)(arr, axis=param)
        )
#CODE  FOR BUG FIXING ISSUE IN HACKERRANK
print(
    round(
       np.std(arr) , 11
    )
)

# --------------------------------------------------------------- 
# Dot and Cross
import numpy as np
np.set_printoptions(legacy='1.13')

n = int(input())

A = np.array([list(map(int, input().split(' '))) for _ in range(n)], int)
B = np.array([list(map(int, input().split(' '))) for _ in range(n)], int)

print (np.dot(A, B))

# --------------------------------------------------------------- 
# Inner and Outer
import numpy as np

A = np.array(list(map(int, input().split(' '))), int)
B = np.array(list(map(int, input().split(' '))), int)

print (f'{np.inner(A, B)}\n{np.outer(A, B)}')

# --------------------------------------------------------------- 
# Polynomials
import numpy as np

arr = list(map(float, input().split(' ')))
n = int(input())

print(np.polyval(arr, n))

# --------------------------------------------------------------- 
# Linear Algebra
import numpy as np

n = int(input())
arr = [list(map(float, input().split(' '))) for _ in range(n)]

print(
    round(
        np.linalg.det(arr), 2
        )
    )
    

#######################
#                     #
# CHALLENGES          #
#                     #
#######################
# --------------------------------------------------------------- 
# Birthday Cake Candles
#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    return candles.count(max(candles))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
    
# ---------------------------------------------------------------     
# Number Line Jumps
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if x1 == x2:
        return 'YES'
    elif x1 > x2 and v1 < v2:
        first, f_jump = x1, v1
        second, s_jump = x2, v2
    elif x1 < x2 and v1 > v2:
        first, f_jump = x2, v2
        second, s_jump = x1, v1
    else:
        return 'NO'
        
    while second < first:
        second += s_jump
        first += f_jump
        
    if second == first:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

# --------------------------------------------------------------- 
# Viral Advertising
#!/bin/python3

from math import floor
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
def get_daily_liked(n):
    i = 0
    liked = 2
    while i < n:
        yield liked
        i += 1
        liked = floor(
                    (liked * 3) / 2
                      )

def viralAdvertising(n):
    return sum(
            get_daily_liked(n)
            )

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

# --------------------------------------------------------------- 
# Recursive Digit Sum
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    if not int(n) // 10:
        return int(n)
    
    int_super_digit = sum((int(digit) for digit in n)) * k
    super_digit = str(int_super_digit)
      
    while int_super_digit // 10:
        int_super_digit = sum((int(digit) for digit in super_digit))
        super_digit = str(int_super_digit)
    return int_super_digit

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

# --------------------------------------------------------------- 
# Insertion Sort - Part 1
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    pivot = arr[n - 1]
    is_last = True
    
    for i in range(n - 1, 0, -1):
        idx = i - 1
        if pivot < arr[idx]:
            arr[i] = arr[idx]
            print(*arr)
        else:
            arr[i] = pivot
            print(*arr)
            is_last = False
            break
    if is_last:
        arr[0] = pivot
        print(*arr)
               
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

# --------------------------------------------------------------- 
# Insertion Sort - Part 2
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    pivot = arr[n - 1]
    is_last = True
    
    for i in range(n - 1, 0, -1):
        idx = i - 1
        if pivot < arr[idx]:
            arr[i] = arr[idx]
        else:
            arr[i] = pivot
            is_last = False
            break
    if is_last:
        arr[0] = pivot
    print(*arr)
        
def insertionSort2(n, arr):
    for k in range(1, n):
        insertionSort1(k + 1, arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
