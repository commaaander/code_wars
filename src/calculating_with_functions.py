# Calculating with Functions
# This time we want to write calculations using functions and get the results. Let's have a look at some examples:
# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:
# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))


def zero(*args):
    x = 0
    return x if len(args) == 0 else int(eval(f"{x} {args[0]}"))


def one(*args):
    x = 1
    return x if len(args) == 0 else int(eval(f"{x} {args[0]}"))


def two(*args):
    x = 2
    return x if len(args) == 0 else int(eval(f"{x} {args[0]}"))


def three(*args):
    x = 3
    return x if len(args) == 0 else int(eval(f"{x} {args[0]}"))


def four(*args):
    x = 4
    return x if len(args) == 0 else int(eval(f"{x} {args[0]}"))


def five(*args):
    x = 5
    return x if len(args) == 0 else int(eval(f"{x} {args[0]}"))


def six(*args):
    x = 6
    return x if len(args) == 0 else int(eval(f"{x} {args[0]}"))


def seven(*args):
    x = 7
    return x if len(args) == 0 else int(eval(f"{x} {args[0]}"))


def eight(*args):
    x = 8
    return x if len(args) == 0 else int(eval(f"{x} {args[0]}"))


def nine(*args):
    x = 9
    return x if len(args) == 0 else int(eval(f"{x} {args[0]}"))


def plus(arg):
    return f"+ {arg}"


def minus(arg):
    return f"- {arg}"


def times(arg):
    return f"* {arg}"


def divided_by(arg):
    return f"/ {arg}"


if __name__ == "__main__":
    print(one(plus(one())))
