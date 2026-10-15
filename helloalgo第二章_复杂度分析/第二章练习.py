"""迭代与递归的时间和空间"""
def sum_iter(n: int) -> int:
    """迭代求和"""
    res = 0
    for i in range(i, n + 1):
        res += i
    return res

def sum_recur(n: int) -> int:
    """递归求和"""
    if n == 1:
        return 1
    return n + sum_recur(n - 1)
"""
1.输入 n = 4 执行迭代函数时，每轮循环结束后，累加变量 res 的值分别是多少？
res = 0, res = 1, res = 3, res = 6, res = 10

2.输入 n = 4 执行递归函数时，参数 n 会依次取哪些值？从最深的一层开始返回时，结果怎样得到？
n=4, n=3, n=2, n=1, return 4+3+2+1 = 10

3.两种写法的时间复杂度和空间复杂度分别是多少?结合第1、2问的执行过程说明理由。
时间复杂度:迭代函数为O(n),递归函数为O(n)
空间复杂度的:迭代函数为O(1),递归函数为O(n)
"""

"""三段代码的时间复杂度"""
def linear_Loop(n: int) -> int:
    """线性阶循环"""
    res = 0
    for i in range(n):
        res += i
    return res

def quadratic_loop(n: int) -> int:
    """平方阶循环"""
    res = 0
    for i in range(n):
        for j in range(i, n):
            res += j
    return res

def logarithmic_loop(n: int) -> int:
    """对数阶循环"""
    while n > 1:
        n // 2
        return n
"""
以上三个代码片段的输入均为正整数 n 。
请按时间复杂度从低到高排序，并写出各自的复杂度。
quadratic_loop > linear_loop > logarithimic_loop 
O(n^2) > O(n) > O(logn)
"""

"""那种反转更节省空间"""
def reverse_method1(nums: list) -> list:
    n = len(nums)
    res = [0] * n   # 新建等长数组
    for i in range(n):
        res[i] = nums[n - 1 - i]    # 倒序复制
    return res

def reverse_method2(nums: list) -> list:
    i = 0               # 左指针，从头开始
    j = len(nums) - 1   # 右指针，从尾部开始
    while i < j:
        # 交换两个位置元素
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    # 原地修改，不需要return(也可以return nums 方便链式调用)
    return nums
"""
要将数组 nums 中的元素全部反转，有两种做法：
1.新建一个等长数组res,倒叙复制后返回;
2.用两个索引 i 和 j 分别从首、尾向中间移动,逐对交换 nums[i] 与 nums[j]。
两种做法的空间复杂度各是多少？哪种属于"原地"操作？
空间复杂度分别是O(1) and O(n)
"""

"""斐波那契数列"""
"""
请使用循环计算并返回 f(n) ，不使用递归。
"""
def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 0
    c = 1
    for i in range(2, n + 1):
        a, b = b ,c
        c = a + b 
    return c
