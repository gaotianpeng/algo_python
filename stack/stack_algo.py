def is_bracket_valid(test_str:str) -> bool:
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    for char in test_str:
        if char not in bracket_map:
            stack.append(char)
        elif not stack or bracket_map[char] != stack.pop():
            return False
    return not stack


if __name__ == "__main__":
    # test case
    test_str = '(([{()}]))'
    test_str_b = '[[)]]'
    print(is_bracket_valid(test_str))
    print(is_bracket_valid(test_str_b))
