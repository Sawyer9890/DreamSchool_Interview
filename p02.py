def matching_parentheses(string):
    stack = []
    lefts, rights = [], []
    for i, char in enumerate(string):
        if char == '(':
            stack.append(char)
            lefts.append(i)
        elif char == ')':
            if stack:
                stack.pop()
                lefts.pop()
            else:
                rights.append(i)

    print(string)
    for i in range(0, len(string)):
        if i in lefts:
            print('x', end='')
        elif i in rights:
            print('?', end='')
        else:
            print(" ", end='')
    print()
    return


if __name__ == '__main__':
    tests = [
        'bge)))))))))',
        '((IIII))))))',
        '()()()()(uuu',
        '))))UUUU((()',
    ]
    for test in tests:
        matching_parentheses(test)
