class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from an empty stack")

    def is_empty(self):
        return len(self.stack) == 0


stack_1 = Stack()

stack_1.push(4)
stack_1.push(2)
stack_1.push(1)
stack_1.push(3)

print("\nPop the element:")
print(stack_1.pop())

print("\nCheck if the stack is empty:")
print(stack_1.is_empty())

print("\nPop the elements:")
print(stack_1.pop())
print(stack_1.pop())
print(stack_1.pop())

print("\nCheck if the stack is empty:")
print(stack_1.is_empty())