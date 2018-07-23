def alphabetrec(num, result, list):
    if int(num) == len(result):
        list.append(result)
        return list;

    for i in range(0, int(num)):
        if chr(97 + i) in result:
            continue

        alphabetrec(num, result + chr(97 + i), list)

    return list


if __name__ == "__main__":
    num = input()
    list = []
    alphabetrec(num, "", list)

    print("list: ", list)

    # print(chr(96+1))

    pass
