import random

class Stack(object):
    def __init__(self, max_size= 30):
        self.stack = []
        if max_size is float:
            print('Please enter an integer')
        else:
            if max_size <= 0:
                print('Please enter an integer greater than 0')
            else:
                self.max_size = max_size

    def push(self, object):
        if len(self.stack) < self.max_size:
            self.stack.append(object)
            print('Your Stack: ', self.stack, ' Remaining Romm: ', self.max_size - len(self.stack)
                  , ' top: ', self.top())
        else:
            print('There is no room. Stack overflow!! Boom~~')

    def pop(self):
        if len(self.stack) == 0:
            print('There is no object. Stack underflow!! Boom~~')
        else:
            print('Your Stack: ', self.stack, '  Pop: ', self.stack.pop(),
                  ' Remaining Romm: ', self.max_size - len(self.stack), ' top: ', self.top())

    def top(self):
        if len(self.stack) == 0:
            return None
        else:
            return (self.stack[-1])

    def __len__(self):
        return len(self.stack)



class Queue(object):
    def __init__(self, max_size= 30):
        self.queue = []
        if max_size is float:
            print('Please enter an integer')
        else:
            if max_size <= 0:
                print('Please enter an integer greater than 0')
            else:
                self.max_size = max_size

    def front(self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue[0]

    def rear(self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue[-1]

    def enQueue(self, object):
        if len(self.queue) < self.max_size:
            self.queue.append(object)
            print('Your Queue: ', self.queue, ' Remaining room: ', self.max_size - len(self.queue),
                  ' front: ', self.front(), ' rear: ', self.rear())
        else:
            print('There is no room. Queue overflow!! Boom~~')


    def deQueue(self):
        if len(self.queue) == 0:
            print('There is no object. Queue underflow!! Boom~~')
        else:
            print('Your Queue: ', self.queue, ' Pop: ', self.queue.pop(0), ' Remaining room: ',
                  self.max_size - len(self.queue), ' front: ', self.front(), ' rear: ', self.rear())


if __name__ == '__main__':
    s = Stack(5)
    for x in range(6):
        s.push(random.randint(0, 100))
    for x in range(6):
        s.pop()

    q = Queue(5)
    for x in range(6):
        q.enQueue(random.randint(0, 100))
    for x in range(6):
        q.deQueue()

# 파이썬 종료할 때 뜨는 disconnect 는 뭔가여..? 이것도 process??


