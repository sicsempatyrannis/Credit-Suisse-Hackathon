import numpy as np
def organizingContainers(container):
    # Participants code will be here
    res = [0] * len(container)
    container = np.array(container)
    for i, k in enumerate(container):
        for j, v in enumerate(container):
            count = np.sum(container, axis=1)[i] - container[i][i]
            tot = 0
            if i != j:
                tot += container[i][j]
                
        if tot == count:
            res[i] = 1
            
    ret = ""
    if sum(res) == len(container):
        ret += 'Possible,'
    else:
        ret += 'Impossible,'
        
    return ret[:-1]

if __name__ == "__main__":
    q = int(input().strip())
    answer=""
    for a0 in range(q):
        n = int(input().strip())
        container = []
        for container_i in range(n):
           container_t = [int(container_temp) for container_temp in input().strip().split(' ')]
           container.append(container_t)
        result = organizingContainers(container)
        if(answer == ""):
             answer = str(result)
        else:
            answer = answer +  "," +str(result)
    # Do not remove below line
    print(answer)    
    # Do not print anything after this line