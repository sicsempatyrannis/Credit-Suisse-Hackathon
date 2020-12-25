# You may change this function parameters
def dfs(node, graph, dp, vis, n):
    vis[node] = True
    
    for i in range(n):
        if not vis[node]:
            dfs(i, graph, dp, vis, n)
        if (node, i) in graph.keys():
            dp[i] = max(graph[(node, i)][0], graph[(node, i)][0] + dp[node])
            if dp[i] != 0:
                return dp
    return dp
 
def findMaxProfit(numOfPredictedTimes, predictedSharePrices):
    # Participants code will be here
    n = numOfPredictedTimes 
    memo = {}
    
    for i in range(n):
        for j in range(n):
            if (i,j) in memo.keys() and i < j:
                memo[(i,j)].append(predictedSharePrices[j] - predictedSharePrices[i])

            elif i < j:
                memo[(i,j)] = [predictedSharePrices[j] - predictedSharePrices[i]]

    print(memo)
    dp = [0] * n
    vis = [False] * n
    num = n
    track = [0] * n
    
    for i in range(n):
        dp = [0] * n
        vis = [False] * n
        print(dfs(i, memo, dp, vis, num))
        track[i] = dfs(i, memo, dp, vis, num)
    
    k = 0
    ret = 0
    
    for i in track:
        k = [v for v, g in enumerate(i) if g != 0]
        if len(k) == 0:
            continue 
        if k[0] == n -1:
            ret += sum(i)
            return ret
        
        elif sum(i) > 0:
            ret += sum(i)
        
    return ret

def main():
    line = [14,5,1,6,3,2,5,6,1,3,6,2,5,5,10]
    numOfPredictedTimes = int(line[0])
    predictedSharePrices = list(map(int, line[1:]))

    answer = findMaxProfit(numOfPredictedTimes, predictedSharePrices)
    # Do not remove below line
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()