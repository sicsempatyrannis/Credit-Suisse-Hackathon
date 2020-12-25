import numpy as np

def find_min_days(prices, profit):
    # Participants code will be here
    n = len(prices) 
    memo = {}
    
    for i in range(n):
        for j in range(n):
            if prices[j] - prices[i] in memo.keys() and i < j:
                memo[prices[j] - prices[i]].append((i,j))

            elif i < j and (prices[j] - prices[i]) in profit:
                memo[prices[j] - prices[i]] = [(i, j)]

    ret = [0] * len(profit)
    for k, m in enumerate(profit):
        if m not in memo.keys():
            ret[k] = -1
        elif len(memo[m]) == 1:
            ret[k] = memo[m][0]
        else:
            curr_j = 1e7
            curr_diff = 1e7
            for i, j in memo[m]:       
                if j <= curr_j and j - i < curr_diff:
                    curr_j = j
                    curr_i = i 
            ret[k] = (curr_i, curr_j)
            
    string = ''
    for j in ret:
        if type(j) == tuple:
            string += "{} {}, ".format(j[0]+1, j[1]+1)
        else:
            string += '{}, '.format(j)

    return string[:-2]

    
n, d = map(int, input().split())
prices = list(map(int, input().split()))
profit = list()
for i in range(d):
    profit.append(int(input().strip()))
answer = find_min_days(prices,profit)
# Do not remove below line
print(answer)
# Do not print anything after this line