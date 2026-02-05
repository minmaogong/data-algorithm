"""
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

    有效字符串需满足：

    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
    每个右括号都有一个对应的相同类型的左括号。
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            match char:
                case '(' | '[' | '{':
                    stack.append(char)
                case ')':
                    if not stack or stack.pop() != '(': # not stack: stack没有值，为空
                        return False
                case ']':
                    if not stack or stack.pop() != '[':
                        return False
                case '}':
                    if not stack or stack.pop() != '{':
                        return False
        return True if not stack else False # not stack: 栈为空

solu = Solution()
print(solu.isValid("()[]{}"))
print(solu.isValid("([)] "))