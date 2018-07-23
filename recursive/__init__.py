def bitrec(n, result, list):
    # print("n: ", n)
    # print("result: ", len(result))

    if int(n) == len(result):
        list.append(result)
        return list

    bitrec(n, result + "0", list)
    bitrec(n, result + "1", list)

    return list


def bitcombination():
    print("input Bit number: ")
    n = input()
    list = []

    bitrec(n, "", list)

    print("result: ", list)

    pass


if __name__ == "__main__":
    print("recursive Test")

    bitcombination()
    pass
