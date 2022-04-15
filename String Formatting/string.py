def print_formatted(number):
    for i in range(1, number+1):
        l = len(bin(number)[2:])
        a = oct(i)
        b = hex(i)
        c = bin(i)
        print(str(i).rjust(l),a[2:].rjust(l),b[2:].upper().rjust(l),c[2:].rjust(l))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
