def print_formatted(n):
    if n<1 or n>99:
        print('Error')
        return
    width = len(bin(n)) - 2  # Width based on the binary representation of n
    for i in range(1, n + 1):
        decimal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexadecimal = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
        print(f"{decimal} {octal} {hexadecimal} {binary}")
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)