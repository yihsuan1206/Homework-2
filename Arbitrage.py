liquidity = {
    # delta x = 5
    ("tokenA", "tokenB"): (17, 10), 
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

# x * y = x' * y'

# getAmountOut from uniswapV2 library

def getAmountOut(amountIn, reserveIn, reserveOut): # (# of x swap in, original x, original y)
    amountInWithFee = amountIn * 997
    numerator = amountInWithFee * reserveOut
    denominator = reserveIn * 1000 + amountInWithFee
    amountOut = numerator / denominator
    return amountOut # swap out # of y

# check if liquidity key is reversed
def consider_liquidity_reverse(t0, t1):
    if (t0, t1) in liquidity:
        return liquidity[(t0, t1)]
    else:
        return (liquidity[(t1, t0)][1], liquidity[(t1, t0)][0])

def getPerMutation():
    from itertools import permutations
    swap_list = ["A", "B", "C", "D", "E"]

    # Find the index of "B"
    start_index = swap_list.index("B")

    # Generate all permutations
    all_permutations = permutations(swap_list)

    # Filter permutations that start with "B" and end with "B"
    filtered_permutations = [p for p in all_permutations if p[-1] == "B"]

    # Print the filtered permutations
    # for perm in filtered_permutations:
    #     print(perm)
    return filtered_permutations

def test(test_path):
    amount_in = 5
    token_1st = "B"
    swap_list = test_path
    rt_paths = []
    for token_2nd in swap_list:
        
        reserve0, reserve1 = consider_liquidity_reverse("token"+token_1st, "token"+token_2nd)
        delta_y = getAmountOut(amount_in, reserve0, reserve1)

        # print(f"Swap({token_1st}, {token_2nd}), AmountIn:{amount_in}, AmountOut:{delta_y}")
        # print(f"->token{token_2nd}", end="")
        rt_paths.append(f"token{token_2nd}")
        token_1st = token_2nd
        amount_in = delta_y

    
    return amount_in, rt_paths

## main function, by cassandra

all_test_path = getPerMutation()
# print(f"get {len(all_test_path)} paths")

max_profit = 0
max_profit_path = []
for path in all_test_path:
    profit, rt_paths = test(path)
    # print(profit)
    if profit > max_profit:
        max_profit = profit
        max_profit_path = rt_paths

print("path: tokenB", end='')
for token in max_profit_path:
    print(f"->{token}", end="")
print(f", tokenB balance={max_profit}")
    







