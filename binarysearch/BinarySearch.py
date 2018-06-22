def binSearchRec(data, low, high, target):
    if (low > high or low < 0 or high > len(data) - 1):
        return -1

    mid = (low + high) / 2
    mid = int(mid)

    if data[mid] == target:
        return data[mid]
    elif (data[mid] < high):
        return binSearchRec(data, mid + 1, high, target)
    else:
        return binSearchRec(data, low, mid - 1, target)


def binSearch(data, target):
    if (data is None):
        return -1

    return binSearchRec(data, 0, len(data) - 1, target)


class BinarySearch:
    data = [1, 5, 2, 3, 4]

    def binSearchRec(self, data, low, high, target):
        # print("enter binSearchRec")
        # print(data)

        if (low > high or low < 0 or high > len(data) - 1):
            return -1
            pass

        mid = (low + high) / 2
        mid = int(mid)

        if data[mid] == target:
            return mid

        if data[mid] > target:
            return self.binSearchRec(data, low, mid-1, target)
        elif data[mid] < target :
            return self.binSearchRec(data, mid+1, high, target)

        pass

    def binarySearch(self, target):
        print("enter binarySearch")
        self.data.sort()

        if (self.data is None):
            return -1

        print(self.data)

        return self.binSearchRec(self.data, 0, len(self.data) - 1, target)

        pass

    pass


if __name__ == "__main__":
    data = [4, 5, 1, 2, 3]
    data.sort()
    print(binSearch(data, 3))

    bst = BinarySearch()
    print(bst.binarySearch(5))
