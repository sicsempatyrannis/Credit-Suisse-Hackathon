import collections
import sys
import numpy as np
import random
# Participants may update the following function parameters
def finalSus(sus_index, questionList, final_list, sus_set):
    curr_set = len(sus_set)
    for i, j in enumerate(questionList):
            count = 0
            for v, k in enumerate(j):
                if v != 0:
                    if k-1 in sus_index:
                        count += 1
                        if count >= 2:
                            final_list[j[0]-1] = 1
                            
    sus_index = [v for v, k in enumerate(final_list) if k == 1]                       
    sus_set = set([str(t+1) for t, j in enumerate(final_list) if j == 1])
    
    if curr_set < len(sus_set):
        finalSus(sus_index, questionList, final_list, sus_set)
                            
    return final_list, sus_set, sus_index

def findSuspiciousUserId(numOfQuestions, questionAndAnswerListOfList):
    # # Participants code will be here
    print('Num of qs', numOfQuestions)
    print('Q list', questionAndAnswerListOfList)
    max_ = 0
    for i in questionAndAnswerListOfList:
        if max(i) > max_:
            max_ = max(i)
            
    users = [0] * int(max_)
    print('Num of users', len(users))
    
    q_a = {}
    
    for i, j in enumerate(questionAndAnswerListOfList):
        for k, v in enumerate(j):
            if k != 0:
                q_a[(j[0]-1, v-1)] = 1
                
    for i in range(len(users)):
        for j in range(len(users)):
            if (i,j) in q_a.keys() and (j,i) in q_a.keys():
                users[i] = 1
                users[j] = 1
    
    inds = [v for v, k in enumerate(users) if k == 1]
    sus_set = set([str(t+1) for t, j in enumerate(users) if j == 1])
    users, sus_set, inds = finalSus(inds, questionAndAnswerListOfList, users, sus_set)
    
        
    res = [str(t+1) for t, j in enumerate(users) if j == 1]
    print('Seq', res)
    ret = ",".join(res)
      
    return ret


def main():
    # firstLine = input().split(" ")
    # secondLine = input()

    # Sample input:
    # 3
    # 1 2,2 1,3 1 2

    numOfQuestions = 4
    # questionAndAnswers = secondLine.split(",")
    questionAndAnswerListOfList = [[1,2],[2,1],[3,1,4],[4,1,2]]

    # Participants may update the following function parameters
    answer = findSuspiciousUserId(numOfQuestions, questionAndAnswerListOfList)

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line


# def parseQuestionAndAnswer(questionAndAnswers):
#     questionAndAnswerListOfList = []
#     for index in range(0, len(questionAndAnswers)):
#         questionAndAnswerList = questionAndAnswers[index].split(" ")
#         questionAndAnswerListOfList.append([int(x) for x in questionAndAnswerList])
#     return questionAndAnswerListOfList


if __name__ == '__main__':
    main()