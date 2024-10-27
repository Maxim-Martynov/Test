def count_substring(string, sub_string):
    k = 0
    for i in range(len(string)):
        if string[i:len(string)].startswith(sub_string):
            k += 1
    return k


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)