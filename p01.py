def min_subsequence(source, target):
    if source is None or source == '':
        return -1
    dp = []
    return process3(source, target, dp)


def process3(source, target, dp):
    dic = {}
    for char in source:
        dic[char] = 1
    if dic.get(target[0]) is None:
        return -1

    index = source.index(target[0]) + 1
    dp.append(1)

    for i in range(1, len(target)):
        while index < len(source):
            if target[i] == source[index]:
                dp.append(dp[-1])
                index += 1
                break
            else:
                index += 1
        else:
            if dic.get(target[i]) is not None:
                dp.append(dp[-1] + 1)
            else:
                return -1
            index = source.index(target[i]) + 1
    return dp[-1]


if __name__ == '__main__':
    tests = [
        ['abc', 'abcbc'],
        ['abc', 'acdbc'],
        ['xyz', 'xzyxz'],
    ]
    for test in tests:
        print(min_subsequence(test[0], test[1]))
