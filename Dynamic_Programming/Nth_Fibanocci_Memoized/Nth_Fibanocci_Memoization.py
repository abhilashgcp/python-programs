# Memoization Steps:
# 1. Pass a hash to the function call and initialize to empty hash
# 2. Check vaule is there in memo the return that
# 3. Pass the memo in the function call
# 4. Save the computed value in memo
def fib(n, memo={}):
    if n in memo.keys():
        return memo[n]
    if (n<=2):
        return 1
    else:
        memo[n] = fib(n-1, memo)+fib(n-2,memo)
        return memo[n]


print (fib(7))
print (fib(50))