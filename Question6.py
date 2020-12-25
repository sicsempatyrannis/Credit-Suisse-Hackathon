import math
import numpy as np
# You may change this function parameters
def matrixSize(row, col, token):
    check = row * col
    while check < len(token):
        if row < col:
            row += 1
            check = row * col
        elif row * col < len(token) and row == col:
            col += 1
            check = row * col
    return row, col
        
def encrypt(words):
    # Participants code will be here
    token = words.replace(' ', '')

    floor_ = int(math.floor(len(token)**0.5))
    ceil_ = int(math.ceil(len(token)**0.5))
    
    rows, cols = matrixSize(floor_, ceil_, token)
    word_matrix = np.empty(shape=(rows, cols), dtype=str)
    
    ind = 0
    for i in range(rows):
        for j in range(cols):
            if ind > len(token)-1:
                break
            else:
                word_matrix[i][j] = token[ind]
                ind += 1
                
    ret = ""
    for i in range(cols):
        ret += ' '
        for j in range(rows):
            ret += word_matrix[j][i]
            
    return ret[1:]


def main():
    words = 'wclwfoznbmyycxvaxagjhtexdkwjqhlojykopldsxesbbnezqmixfpujbssrbfhlgubvfhpfliimvmnny'

    answer = encrypt(words)

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()
    
