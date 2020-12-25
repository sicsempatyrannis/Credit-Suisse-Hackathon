import numpy as np
import random
from collections import Counter
# You may change this function parameters
def calculateMinimumSession(numOfBankers, numOfParticipants, bankersPreferences, participantsPreferences):
  
    if numOfBankers <= 0 or numOfParticipants <= 0:
        return 0
    memo = np.zeros(shape=(numOfBankers, numOfParticipants))
    
    for i, j in enumerate(bankersPreferences):
        for k in j:
            if k-1 <= numOfParticipants-1:
                memo[i][k-1] += 1
            
    for i, j in enumerate(participantsPreferences):
        k_count = Counter(j)
        for k in j:       
            if k-1 <= numOfBankers-1 and memo[k-1][i] < k_count[k]:
                memo[k-1][i] += 1
    
    col = max(np.sum(memo, axis=1))
    row = max(np.sum(memo, axis=0))
            
    
    ret = max(col, row)
    
    return int(ret)


def main():
    # firstLine = "21,2&3"
    # secondLine = "31,2,2"
    # Sample input:
    # 3 1,1,1&2
    # 3 3&2,1,1
    numOfBankers = int(random.uniform(0, 5))
    numOfParticipants = int(random.uniform(0, 5))
    bankersPreferencesListOfList = [[int(random.uniform(1, numOfParticipants+1)) for _ in range(int(random.uniform(1, 10)))] for _ in range(numOfBankers)]
    participantsPreferencesListOfList = [[int(random.uniform(1, numOfBankers+1)) for _ in range(int(random.uniform(1, 10)))] for _ in range(numOfParticipants)]

    # bankersPreferencesListOfList = parsePreferences(bankersPreferences)
    # participantsPreferencesListOfList = parsePreferences(participantsPreferences)

    answer = calculateMinimumSession(
        numOfBankers,
        numOfParticipants,
        bankersPreferencesListOfList,
        participantsPreferencesListOfList
    )

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line


# def parsePreferences(preferences):
#     preferenceListOfList = []
#     for index in range(0, len(preferences)):
#         preferenceArr = preferences[index].split("&")
#         preferenceListOfList.append([int(p) for p in preferenceArr])
#     return preferenceListOfList


if __name__ == '__main__':
    main()
    
    

