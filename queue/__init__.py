# LIFO (Last Input First Out)
class MyStack:
    topNum = 0
    mylist = []

    def push(self, item):
        self.mylist.append(item)
        self.topNum + 1
        pass

    def pop(self):
        return self.mylist.pop(self.topNum - 1)

    def peek(self):
        if self.isEmpty() == 'empty':
            raise Exception("Stack is Empty")

        return self.topNum

    def isEmpty(self):
        if self.topNum == 0:
            return 'empty'
        else:
            return 'no empty'

    pass


# FIFO (Fist Input Last Out)
def callqueue():
    st = MyStack()
    st.push(3)
    st.push(2)
    st.push(1)

    print("입력")

    print(st.pop())
    print(st.pop())
    print(st.pop())

    pass


def callstack():
    st = MyStack()

    st.push(5)
    st.push(3)
    st.push(1)

    print(st.pop(), st.pop(), st.pop())

    # print(st.peek())
    print(st.isEmpty())
    pass


if __name__ == '__main__':
    callstack()
    callqueue()

    pass
