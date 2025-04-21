def solution(chars: str) -> bool:
    stack = []
    for c in chars:
        if c == '{':
            stack.append('}')
        elif c == '[':
            stack.append(']')
        elif c == '(':
            stack.append(')')
        else:
            if len(stack) == 0:
                return False
            
            if c == stack[-1]:
                stack.pop()
            else:
                return False
    
    if len(stack) == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    # {[[[[[((((()))))]]]]]}
    chars = str(input())
    print(solution(chars))
            