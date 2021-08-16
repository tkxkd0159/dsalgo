class Solution:
    def isValid(self, s: str) -> bool:
        l = len(s)
        if l % 2 != 0:
            return False
        if s is None or l <= 1:
            return False
        left_ = "({["
        right_ = ")}]"
        set_ = ["[]", "{}", "()"]
        map_ = {"{":"}", "(":")", "[":"]"}
        ord_q = []
        skip_ = 0

        for i in range(l):
            if skip_ != 0:
                skip_ -= 1
                continue
            if s[i:i+2] not in set_ and s[i] in left_ and (i+1) < l:
                if s[i+1] in right_:
                    return False
                ord_q.append(s[i])
                continue

            elif s[i:i+2] in set_:
                skip_ = 1
                continue

            elif s[i] in right_:
                if ord_q == []:
                    return False
                tmp = ord_q.pop()

                if map_[tmp] == s[i]:
                    continue
                else:
                    return False

            else:
                False

        if ord_q == []:
            return True
        else:
            return False
        
        
        
    def isValid2(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        lefts = "({["
        set_dict = {")":"(", "]":"[", "}":"{"}

        stack = []

        for i in s:
            if i in lefts:
                stack.append(i)
            elif i in set_dict:
                if len(stack) != 0 and set_dict[i] == stack.pop():
                    continue
                else:
                    return False
            else:
                return False

        return len(stack) == 0
