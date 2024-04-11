# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution

path: tokenB->tokenA->tokenE->tokenD->tokenC->tokenB, tokenB balance=20.042339589188174


## Each swap:
* Swap(B, A), AmountIn:5, AmountOut:5.655321988655322
* Swap(A, E), AmountIn:5.655321988655322, AmountOut:1.0583153138066885
* Swap(E, D), AmountIn:1.0583153138066885, AmountOut:2.429786260142227
* Swap(D, C), AmountIn:2.429786260142227, AmountOut:5.038996197252911
* Swap(C, B), AmountIn:5.038996197252911, AmountOut:20.042339589188174

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution

Slippage in AMM refers to the difference between the expected price of a trade and the actual price at which the trade is executed. Uniswap V2 addresses the slippage issue by implementing a constant product formula for its liquidity pools. This formula ensures that the product of the quantities of both tokens remains constant, which helps maintain a relatively stable price despite changes in trading volume.
```
function trade(uint256 amountIn, uint256 amountOutMin, address[] memory path) external {
    // Ensure the input token is the first token in the path
    require(path[0] == inputToken, "Input token mismatch");

    // Ensure the output token is the last token in the path
    require(path[path.length - 1] == outputToken, "Output token mismatch");

    // Retrieve the current reserves of input and output tokens
    (uint256 reserveIn, uint256 reserveOut) = getReserves(inputToken, outputToken);

    // Calculate the amount of output tokens to be received
    uint256 amountOut = UniswapV2Library.getAmountOut(amountIn, reserveIn, reserveOut);

    // Ensure the amount of output tokens meets the minimum specified
    require(amountOut >= amountOutMin, "Slippage exceeded");

    // Transfer input tokens from the sender to the contract
    inputToken.safeTransferFrom(msg.sender, address(this), amountIn);

    // Perform the swap
    UniswapV2Library.swapTokensForExactTokens(amountIn, amountOut, path, msg.sender, deadline);

    // Emit event or perform other actions
}
```


## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution

In the UniswapV2Pair contract, the mint function is where new liquidity tokens are created when someone adds tokens to a liquidity pool for the first time. This function subtracts a minimum amount of liquidity when the initial tokens are added.

The reason for subtracting this minimum amount of liquidity is to make sure that the liquidity pool starts off with a decent amount of liquidity. This is important because:

It helps prevent the prices of tokens in the pool from swinging wildly when people start trading. If there's not enough liquidity, even small trades can cause big price changes, which isn't good for traders.
Having enough liquidity means that bigger trades can happen without affecting the prices too much. This makes trading smoother and more reliable for everyone involved.
A well-liquidated pool tends to attract more traders because they can get better prices and have a smoother trading experience. So, by ensuring there's a minimum level of liquidity from the start, Uniswap makes the platform more attractive to traders and liquidity providers.
Lastly, having enough liquidity helps protect the pool from any malicious activities or attacks that could harm traders and liquidity providers.


## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution

In the UniswapV2Pair contract, when depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. The intention behind this is to ensure that each time liquidity is added, the newly added liquidity remains balanced with the existing liquidity. This specific formula is based on the constant product invariant of the Uniswap V2 liquidity pool, which ensures that the quantity of tokens in the pool stays relatively balanced. By enforcing this formula, Uniswap maintains stability and efficiency in the liquidity pool, providing a more reliable and predictable trading experience.


## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution

A sandwich attack is a type of front-running attack that targets decentralized exchanges and AMM like Uniswap. In a sandwich attack, an attacker exploits the predictability of the transaction execution order in the memory pool to manipulate prices in their favor. 

When initiating a swap, a sandwich attack can have significant impacts for the trader. It often leads to increased slippage, meaning traders receive fewer tokens than anticipated for their swaps. This can result in traders paying higher prices for tokens or receiving lower prices than expected due to the manipulated prices caused by the attack. Such experiences can lead to frustration among traders and deter them from using the platform in the future, especially if sandwich attacks occur frequently. Overall, the impact of a sandwich attack extends beyond immediate financial losses to affect the trader's trust and confidence in the platform.
