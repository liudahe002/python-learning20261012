# 迭代--for循环
def for_loop(n: int) -> int:
    """for 循环"""
    res = 0
    # 循环求和 1, 2, ..., n-1, n
    for i in range(1, n + 1):
        res += i
    return res

# 迭代--while循环
def while_loop_ii(n: int) -> int:
    """while 循环(两次更新)"""
    res = 0
    i = 1 # 初始化条件变量
    # 循环求和 1, 4, 10
    while i <= n:
        res += i
        i += 1 # 更新条件变量
        i *= 2
    return res

# 迭代--嵌套循环
def nested_for_loop(n: int) -> str:
    """双层 for 循环"""
    res = ""
    # 循环 i = 1, 2, ..., n-1, n
    for i in range(1, n + 1):
        # 循环 j = 1, 2, ..., n-1, n
        for j in range(1, n + 1):
            res += f"({i},{j}),"
    return res

# 递归
def recur(n: int) -> int:
    """递归"""
    # 终止条件
    if n == 1:
        return 1
    # 递：递归调用
    res = recur(n - 1)
    # 归：返回结果
    return n + res

# 尾递归
def tail_recur(n, res):
    """尾递归"""
    # 终止条件
    if n == 0:
        return res
    # 尾递归调用
    return tail_recur(n - 1, res + n)
# 递归树（斐波那契数列）
def fib(n: int) -> int:
    """斐波那契数列：递归"""
    # 终止条件 f(1) = 0, f(2) = 1
    if n == 1 or n==2:
        return n - 1
    # 递归调用 f(n) = f(n-1) + f(n-2)
    res = fib(n - 1) + fib(n - 2)
    # 返回结果 f(n)
    return res
    

"""Driver Code"""
if __name__ == "__main__":
    res1 = for_loop(5)
    res2 = while_loop_ii(5)
    res3 = nested_for_loop(5)
    res4 = recur(5)
    res5 = tail_recur(5, 0)
    res6 = fib(5)
    print(f"\nfor循环的结果是{res1}")
    print(f"\nwhile循环的结果是{res2}")
    print(f"\n嵌套循环的结果是{res3}")
    print(f"\n递归的结果是{res4}")
    print(f"\n尾递归的结果是{res5}")
    print(f"\n斐波那契数列的第n项的结果是{res6}")
