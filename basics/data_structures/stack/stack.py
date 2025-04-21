from typing import Any

class Stack(object):
    
    def __init__(self) -> None:
        self.stack = []
    
    def push(self, data) -> None:
        self.stack.append(data)
    
    def pop(self) -> Any:
        if self.stack:
            return self.stack.pop()
    
    def print(self) -> None:
        reversed_stack = reversed(self.stack)
        for num in reversed_stack:
            print(num)


if __name__ == "__main__":
    stack = Stack()
    stack.push(4)
    stack.push(10)
    stack.push(5)
    stack.print()
    print(stack.pop())
    print('-----pop-----')
    stack.print()