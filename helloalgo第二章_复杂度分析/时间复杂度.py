# 在某运行平台下
def algorithm(n: int):
    a = 2       # 1 ns
    a = a + 1   # 1 ns
    a = a * 2   # 10 ns
    # 循环 n 次
    for _ in range(n):  # 1 ns
        print(0)        # 5 ns

# 算法 A 的时间复杂度：常数阶
def algorithm_A(n: int):
    print(0)
# 算法 B 的时间复杂度：线性阶
def algorithm_B(n: int):
    for _ in range(n):
        print(0)
# 算法 C 的时间复杂度：常数阶
def algorithm_C(n: int):
    for _ in range(1000000):
        print(0)
        
# 函数渐进上界
def algorithm(n: int):
    a = 1       # +1
    a = a + 1   # +1
    a = a * 2   # +1
    # 循环 n 次
    for i in range(n):  # +1
        print(0)        # +1
    """T(n) = 3 + 2n"""
    
def algorithm(n: int):
    a = 1       # +0 (技巧 1)
    a = a + n   # +0 (技巧 1)
    # +n (技巧 2)
    for i in range(5 * n + 1):
        print(0)
    # +n*n (技巧 3)
    for i in range(2 * n):
        for j in range(n + 1):
            print(0)
    """T(n) = 2n(n + 1) + (5n + 1) + 2"""
    
# 常数阶
def constant(n: int) -> int:
    """常数阶"""
    count = 0
    size = 100000
    for _ in range(size):
        count += 1
    return count

# 线性阶
def linear(n: int) -> int:
    """线性阶"""
    count = 0
    for _ in range(n):
        count += 1
    return count

def array_traversal(nums: list[int]) -> int:
    """线性阶（遍历数组）"""
    count = 0
    # 循环次数与数组长度成正比
    for num in nums:
        count += 1
    return count

# 平方阶
def quadratic(n: int) ->int:
    """平方阶"""
    count = 0
    # 循环次数与数据大小 n 成平方关系
    for i in range(n):
        for j in range(n):
            count += 1
    return count

def bubble_sort(nums: list[int]) -> int:
    """平方阶（冒泡顺序）"""
    count = 0   # 计数器
    # 外循环：未排序区间为 [0, i]
    for i in range(len(nums) - 1, 0, -1):
        # 内循环：将未排序区间 [0, i] 中最大元素交换至该区间的最右端
        for j in range(i):
            if nums[j] > nums[j + 1]:
                # 交换 nums[j] 与 nums[j + 1]
                tmp: int = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = tmp
                count += 3      # 元素交换包含 3 个单元操作
    return count

# 指数阶
def exponential(n: int) -> int:
    """指数阶（循环实现）"""
    count = 0
    base = 1
    # 细胞每轮一分为二， 形成数列1， 2， 4， 8， ..., 2^(n-1)
    for _ in range(n):
        for _ in range(base):
            count += 1
        base *= 2
    # count = 1 + 2 + 4 + 8 + .. + 2^(n-1) = 2^n -1
    return count

def exp_recur(n: int) -> int:
    """指数阶（递归实现）"""
    if n == 1:
        return 1
    return exp_recur(n - 1) + exp_recur(n - 1) + 1

# 对数阶
def logarithmic(n: int) -> int:
    """对数阶（循环实现）"""
    count = 0
    while n > 1:
        n = n / 2
        count += 1
    return count

def log_recur(n: int) -> int:
    """对数阶（递归实现）"""
    if n <= 1:
        return 0
    return log_recur(n / 2) + 1

# 线性对数阶
def linear_log_recur(n: int) -> int:
    """线性对数阶"""
    if n <= 1:
        return 1
    # 一分为二，子问题的规模减小一半
    count = linear_log_recur(n // 2) + linear_log_recur(n // 2)
    # 当前子问题包含 n 个操作
    for _ in range(n):
        count += 1
    return count

# 阶乘阶
def factorial_recur(n: int) -> int:
    """阶乘阶（递归实现）"""
    if n == 0:
        return 1
    count = 0
    # 从 1 个分裂出 n 个
    for _ in range(n):
        count += factorial_recur(n - 1)
    return count

# 最差、最佳、平均时间复杂度
import random
def random_numbers(n: int) -> list[int]:
    """生成一个数组，元素为: 1, 2, ..., n ,顺序被打乱"""
    # 生成数组 nums =: 1, 2, 3, ..., n
    nums = [i for i in range(1, n + 1)]
    # 随机打乱数组元素
    random.shuffle(nums)
    return nums

def find_one(nums: list[int]) -> int:
    """查找数组 nums 中数字 1 所在索引"""
    for i in range(len(nums)):
        # 当元素 1 在数组头部时，达到最佳时间复杂度 0(1)
        # 当元素 1 在数组尾部时，达到最差时间复杂度 0(n)
        if nums[i] == 1:
            return i
    return -1
"""Driver Code"""
if __name__ == "__main__":
    n = 10
    nums = random_numbers(n)
    index = find_one(nums)
    print("\n数组 [1, 2, ..., n] 被打乱后 =", nums)
    print("数字 1 的索引为", index)