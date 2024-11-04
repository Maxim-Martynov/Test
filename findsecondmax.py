if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())


    def find_second_largest(numbers):
        largest = second_largest = float('-inf')

        for num in numbers:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
                second_largest = num

        return second_largest


    second_largest = find_second_largest(arr)
    print(second_largest)