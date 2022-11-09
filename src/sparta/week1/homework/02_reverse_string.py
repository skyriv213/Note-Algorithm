input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    cnt0 = 0
    cnt1 = 0
    if string[0] == '0':
        cnt1 += 1
    elif string[0] == '1':
        cnt0 += 1

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == '1':
                cnt0 += 1
            if string[i + 1] == '0':
                cnt1 += 1
    return min(cnt0, cnt1)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
