# 比如：str1 = "epmcdcdfe"  str2 = 'eaoccddcdfe' 公共的子串是dcdfe

def initindexs(char, string):
    index = []
    length = len(string)
    for i in range(length):
        if char == string[i]:
            index.append(i + 1)  # 保存相同字符坐标+1的位置
    return index


def Substring(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)
    length = 0
    longest = 0
    startposition = 0
    start = 0
    for i in range(str1_len):
        start = i
        index = initindexs(str1[i], str2)
        index_len = len(index)
        for j in range(index_len):
            end = i + 1
            while end < str1_len and index[j] < str2_len and str1[end] == str2[index[j]]:  # 保证下标不会超出列表范围
                end += 1
                index[j] += 1
            length = end - start
            if length > longest:
                longest = length
                startposition = start

    return startposition, longest


str1 = "epmcdcdfe"
str2 = 'eaoccddcdfe'
Substring(str1, str2)
(start, longest) = Substring(str1, str2)
print(start, longest)
for i in range(longest):
    print(str1[start + i], end=' ')