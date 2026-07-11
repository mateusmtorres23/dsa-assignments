from src.my_stack import MyStack

def is_valid_parentheses(string: str) -> bool:
    stack = MyStack()
    for i in string:
        if i in '([{':
            stack.push(i)
        elif i == ')' and stack.peek() == '(':
            stack.pop()
        elif i == ']' and stack.peek() == '[':
            stack.pop()
        elif i == '}' and stack.peek() == '{':
            stack.pop()
        else:
            stack.push(i)

    if stack.size() == 0:
        return True
    return False
