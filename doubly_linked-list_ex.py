class Node(object):
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class LinkedList(object):
    def __init__(self, root=None, last=None):
        self.root = root
        self.last = last
        self.size = 0

    def insert(self, data, next=None):
        new_node = Node(data, next)
        this_node = self.root
        if new_node.next_node is None:
            if self.root is None:
                self.root = new_node
                self.last = self.root
            else:
                self.last.next_node = new_node
                new_node.prev_node = self.last
                self.last = new_node
        elif self.innerfind(new_node.next_node) is True:
            while this_node:
                if this_node.data == new_node.next_node:
                    break
                this_node = this_node.next_node
            if this_node is not self.root:
                temp = this_node.prev_node
                this_node.prev_node.next_node = new_node
                this_node.prev_node = new_node
                new_node.next_node = this_node
                new_node.prev_node = temp
            else:
                this_node.prev_node = new_node
                new_node.next_node = this_node
                self.root = new_node
        else:
            print('prev_node가 linked list에 없습니다')
            self.size -= 1
        self.size += 1

    def delete(self, data):
        this_node = self.root
        if self.innerfind(data) is False:
            print('삭제할 데이터가 없습니다')
        while this_node:
            if this_node == self.root and this_node.data == data:
                if this_node.next_node is not None:
                    self.root = this_node.next_node
                    this_node.next_node.prev_node = None
                else:
                    self.root = None
                self.size -= 1
                break
            if this_node.next_node == self.last and this_node.next_node.data == data:
                this_node.next_node.prev_node = None
                this_node.next_node = None
                self.last = this_node
                self.size -= 1
                break
            if this_node.data == data:
                temp_next = this_node.next_node
                temp_prev = this_node.prev_node
                this_node.prev_node.next_node = temp_next
                this_node.next_node.prev_node = temp_prev
                self.size -= 1
                break
            this_node = this_node.next_node

    def innerfind(self, data):
        this_node = self.root
        while this_node:
            if this_node.data == data:
                return True
            elif this_node != self.last:
                this_node = this_node.next_node
            else:
                return False

    def find(self, data):
        self.innerfind(data)
        if self.innerfind(data) is True:
            print(data, '있어요')
        else:
            print(data, '없어요')

    def find_all(self):
        this_node = self.root
        while this_node:
            print(this_node.data)
            this_node = this_node.next_node

    def find_all_reverse(self):
        this_node = self.last
        while this_node:
            print(this_node.data)
            this_node = this_node.prev_node

if __name__ == '__main__':
    a = LinkedList()
    a.insert(1)
    a.insert(2)
    a.insert(3)
    a.insert(4, 1)
    a.find_all()
    print('------')
    a.delete(3)
    a.find_all()
    print('----------')
    a.find_all_reverse()
    print('----')
    print('root: ', a.root.data)
    print('last: ', a.last.data)
    print('size: ', a.size)