'''

字符A-Z可以编码为0-25。"A"->"0", "B"->"1", ..., "Z"->"25"
现在输入一个数字序列，计算有多少种方式可以解码成字符A-Z组成的序列。

例如：

输入：19
输出：2

输入：258
输出：2

输入：0219
输出：3


'''

def how_many_ways(digitarray):
    digitarray=str(digitarray)
    dp_list = [0] * (len(digitarray) + 1)
    dp_list[0] = 1
    for i in range(1, len(dp_list)):
        if digitarray[i - 1] != '0':
            dp_list[i] = dp_list[i - 1]
        if i != 1 and '0' < digitarray[i - 2:i] < '26':
            dp_list[i] += dp_list[i - 2]
        print(dp_list)
    print(dp_list[-1])
how_many_ways(19)