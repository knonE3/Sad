#pyramid
n = 5

def pattern(n):
    for i in  range(n):
        num_start = 2 * i + 1
        print(' ' * (n - i - 1) + '*' * num_start)

pattern(n)