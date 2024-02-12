def solution(s):
    if not s:
        return []

    result = []

    for i in range(0, len(s), 2):
        sub_string = s[i: i+2]
        result.append(sub_string)

    if len(result[-1]) == 1:
        result[-1] += '_'

    return result
