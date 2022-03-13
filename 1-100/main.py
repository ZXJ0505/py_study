# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    count = len(t)
    require = [0] * 128
    chSet = [False] * 128
    for i in range(count):
        require[ord(t[i])] += 1
        chSet[ord(t[i])] = True
    i = -1
    j = 0
    minLen = 999999999
    minIdx = 0
    while i < len(s) and j < len(s):
        if count > 0:
            i += 1
            if i == len(s):
                index = 0
            else:
                index = ord(s[i])
            require[index] -= 1
            if chSet[index] and require[index] >= 0:
                count -= 1
        else:
            if minLen > i - j + 1:
                minLen = i - j + 1
                minIdx = j
            require[ord(s[j])] += 1
            if chSet[ord(s[j])] and require[ord(s[j])] > 0:
                count += 1
            j += 1
    if minLen == 999999999:
        return ""
    return s[minIdx:minIdx + minLen]


if __name__ == '__main__':
    print_hi('PyCharm')
    s = "ADOBECODEBANC"
    t = "ABC"
    print(minWindow(s, t))
