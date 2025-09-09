def MaximumDiscount(N: int, price: list[int]) -> int:
    return sum(sorted(price, reverse=True)[2::3])
