# Participants may update the following function parameters
def countNumberOfWays(numOfUnits, numOfCoinTypes, coins):
    # Participants code will be here
    dp = [1] + [0]*numOfUnits
    
    for coin in coins:
        for i in range(coin, numOfUnits+1):
            dp[i] += dp[i-coin]
            
    return dp[numOfUnits]
    
def main():
    firstLine = input().split(" ")
    secondLine = input().split(" ")

    numOfUnits = int(firstLine[0])
    numOfCoinTypes = int(firstLine[1])
    coins = list(map(int, secondLine))

    # Participants may update the following function parameters
    answer = countNumberOfWays(numOfUnits, numOfCoinTypes, coins)

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()