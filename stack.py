class Stack(object):
    def __init__(self):
        self.array = [[], []]

    def l_push(self, data):
        self.array[0].append(data)

    def l_pop(self):
        if len(self.array[0]) == 0:
            print('Stack l is empty')
        else:
            self.array[0].pop()

    def r_push(self, data):
            self.array[1].append(data)

    def r_pop(self):
            if len(self.array[1]) == 0:
                print('Stack r is empty')
            else:
                self.array[1].pop()

    def show(self):
            if len(self.array[0]) == 0:
                print('Stack l is empty')
            else:
                print('Stack l:', self.array[0])
            if len(self.array[1]) == 0:
                print('Stack r is empty')
            else:
                print('Stack r:', self.array[1])


stack = Stack()
stack.l_push(1)
stack.l_push(2)
stack.l_push(3)
stack.l_pop()
stack.r_push(1)
stack.r_push(2)
stack.r_push(3)
stack.r_pop()
stack.show()
