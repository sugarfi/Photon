import re
from sys import exit
from os import listdir
import replit

replit.clear()

print('Photon v 1.0')
print('File Loader')
print()

f = listdir('.')
for file in f:
    if 'photon' in file.split('.'):
        print(file)
f = input('file or type help> ')
if f == 'help':
    f = open('help').read().split('\n')
    for i in range(0, 59, 30):
        replit.clear()
        for line in f[i:i+30]:
            print(line)
        input('Enter for more')
    exit(0)
if '.' not in f or f.split('.')[1] != 'photon':
    print('Invalid file')
    exit(1)
try:
    file = open(f).read()
except:
    print('Invalid file')
    exit(1)
line = re.compile(r'\[[#:].,[#:].>.\]')
lines = re.findall(line, file)

mem = {
    '$':0,
    '-':None,
}

def isnull(arg):
    return arg == None
def getab(args):
    if isnull(args[0]):
        a = mem.get('a', 0)
    else:
        a = args[0]
    if isnull(args[1]):
        b = mem.get('b', 0)
    else:
        b = args[1]
    try:
        a = int(a)
    except:
        pass
    try:
        b = int(b)
    except:
        pass
    return a, b
def vararg(arg, t):
    if t == ':' and arg not in ('$', '-'):
        return mem[arg]
    elif arg == '$':
        return mem[arg]
    else:
        return arg
def add(args, t):
    global mem
    a, b = getab(args) 
    a, b = vararg(a, t[0]), vararg(b, t[1])
    mem['$'] = a + b
def sub(args, t):
    global mem
    a, b = getab(args) 
    a, b = vararg(a, t[0]), vararg(b, t[1])
    mem['$'] = max(a - b, 0)
def mul(args, t):
    global mem
    a, b = getab(args) 
    a, b = vararg(a, t[0]), vararg(b, t[1])
    mem['$'] = a * b
def div(args, t):
    global mem
    a, b = getab(args) 
    a, b = vararg(a, t[0]), vararg(b, t[1])
    mem['$'] = a // b
def out(args, t):
    a = getab(args)[0]
    a = vararg(a, t[0])
    print(a, end='')
def clear(args, t):
    global mem
    mem = {'$':0, '-':None}
def ascii(args, t):
    a = getab(args)[0]
    a = vararg(a, t[0])
    print(chr(a), end='')
def new(args, t):
    print()
def var(args, t):
    global mem
    b = vararg(getab(args)[1], t[1])
    a = int(args[0])
    mem[a] = b
def get(args, t):
    global mem
    a = int(args[0])
    v = input('? ')[0]
    if v.isdigit():
        mem[a] = int(v) 
    else:
        mem[a] = ord(v)
def goto(args, t):
    global l
    a = vararg(getab(args)[0], t[0])
    l = a - 1
def branch(args, t):
    global l
    a, b = getab(args) 
    a, b = vararg(a, t[0]), vararg(b, t[1])
    if a != 0:
        l = b - 1    
funcs = {
    '+':add,
    '-':sub,
    '*':mul,
    '/':div,
    '_':out,
    '.':clear,
    '@':ascii,
    '~':new,
    '=':var,
    '?':get,
    '^':goto,
    '{':branch,
}

l = 0
while l < len(lines):
    line = lines[l]
    line = line.lstrip('[').rstrip(']')
    line = re.split('[,>]', line)
    args, func = line[:2], line[2]
    t = [args[0][0], args[1][0]]
    for i in range(len(args)):
        arg = args[i]
        if arg[0] == '#':
            arg = int(arg[1])
        elif arg[0] == ':':
            if arg[1] in ('$', '-'):
                t[i] = '#'
            arg = arg[1]
        args[i] = arg
    if func in funcs:
        funcs[func](args, t)
    l += 1
    
