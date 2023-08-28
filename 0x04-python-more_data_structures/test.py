def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if len(string[i:i+len(sub_string)]) != len(sub_string):
            continue
        elif len(string[i:i+len(sub_string)]) == len(sub_string):
            if string[i:i+len(sub_string)] == sub_string:
                count = count + 1
    return (count)


# if __name__ == '__main__':
# string = input().strip()
# sub_string = input().strip()

count = count_substring("ABCDCDC", "CDC")
print(count)
