"""
空间复杂度用于衡量算法占用内存空间随着数据量变大时的增长趋势。
这个概念与时间复杂度非常类似，只需将“运行时间”替换为“占用内存空间”。
"""
# 算法使用的相关空间
class Node:
    """类"""
    def __init__(self, x: int):
        self.val: int = x               # 节点值
        self.next: Node | None = None   # 指向下一节点的引用

def function() -> int:
    """函数"""
    # 执行某些操作...
    return 0

def algorithm(n) -> int:    # 输入数据
    A = 0                   # 暂存数据（常量，一般用大写字母表示）
    b = 0                   # 暂存数据（变量）
    node = Node(0)          # 暂存数据（对象）
    c = function()          # 栈帧空间（调用函数）
    return A + b + c        # 输出数据

# 推算方法
def algorithm(n: int):
    a = 0               # O(1)
    b = [0] * 10000     # O(1)
    if n > 10:
        nums = [0] * n  # O(n)

# 递归函数中，需要注意统计栈帧空间
def function() -> int:
    # 执行某些操作
    return 0

def loop(n: int):
    """循环的空间复杂度为 O(1)"""
    for _ in range(n):
        function()
        
def recur(n: int):
    """递归的空间复杂度为 O(n)"""
    if n == 1:
        return
    return recur(n - 1)

# 常数阶（常数阶常见于数量与输入数据大小 n 无关的常量、变量、对象。）
def function() -> int:
    """函数"""
    # 执行某些操作
    return 0

def constant(n: int):
    """常数阶"""
    # 常量、变量、对象占用 O(1) 空间
    a = 0
    nums = [0] * 10000
    node = Node(0)
    # 循环中的变量占用 O(1) 空间
    for _ in range(n):
        c = 0
    # 循环中的函数占用 O(1) 空间
    for _ in range(n):
        function()
        
# 线性阶（线性阶常见于元素数量与 n 成正比的数组、链表、栈、队列等）
def linear(n: int):
    """线性阶"""
    # 长度为 n 的列表占用 O(n) 空间
    nums = [0] * n
    # 长度为 n 的哈希表占用 O(n) 空间
    hmap = dict[int, str]()
    for i in range(n):
        hmap[i] = str(i)

def linear_recur(n: int):
    """线性阶（递归实现）"""
    print("递归 n =", n)
    if n == 1:
        return
    linear_recur(n - 1)

# 平方阶
def quadratic(n: int):
    """平方阶"""
    # 二维列表占用 O(n^2) 空间
    num_matrix = [[0] * n for _ in range(n)]
    
def quadratic_recur(n: int) -> int:
    """平方阶（递归实现）"""
    if n <= 0:
        return 0
    # 数组 nums 长度为 n, n-1, ..., 2,1
    nums = [0] * n
    print("平方递归 n = ", n)
    return quadratic_recur(n - 1)

# 指数阶(指数阶常见于二叉树)
def build_tree(n: int) -> Node | None:
    """指数阶（建立满二叉树）"""
    if n == 0:
        return None
    root = Node(0)
    root.left = build_tree(n - 1)
    root.right = build_tree(n - 1)
    return root

# 对数阶(对数阶常见于分治算法)

"""Driver Code"""
if __name__ == "__main__":
    n = 5
    print("输入数据大小 n =", n)
    # 线性阶
    linear_recur(n)
    # 平方阶
    quadratic_recur(n)




