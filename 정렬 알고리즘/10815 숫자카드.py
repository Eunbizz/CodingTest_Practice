from sys import stdin, stdout

n = stdin.readline()
card = set(stdin.readline().split())
m = stdin.readline()
x = stdin.readline().split()

for i in x:
    stdout.write('1 ') if i in card else stdout.write('0 ')
