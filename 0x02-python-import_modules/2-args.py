#!/usr/bin/python3
import sys

args = sys.argv[1:]

num_args = len(args)

print(f"{num_args} argument{'s' if num_args != 1 else ''}: ", end="")
print(f"{', '.join(args)}." if num_args > 0 else ".", end="\n\n")

for i in range(num_args):
    print(f"{i+1}: {args[i]}")
