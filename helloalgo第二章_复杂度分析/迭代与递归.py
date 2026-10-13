def for_loop(n: int) -> int:
    """for 循环"""
    res = 0
    # 循环求和 1, 2, ..., n-1, n
    for i in range(1, n + 1):
        res += i
    return res

"""Driver Code"""
if __name__ == "__main__":
    n = 100
    res = for_loop(n)
    print(f"\nfor 循环的求和结果是 res = {res}")