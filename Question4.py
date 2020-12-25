import numpy as np
import random 

def maximumExpectedMoney(noOfTradesAvailable, maximumTradesAllowed,p,x,y):
    E_profit = (np.array(x) * np.array(p)) - ((1-np.array(p)) * np.array(y))
    print(E_profit)
    print('Max trades', maximumTradesAllowed)
    print('Trade available', noOfTradesAvailable)
    track = []
    max_curr = max_glob = E_profit[0]
    # if max_curr > 0:
    #     track.append(max_curr)
    for i in range(noOfTradesAvailable):
        max_curr = max(E_profit[i], max_curr + E_profit[i])
        if E_profit[i] > 0:
            track.append(E_profit[i])
        if max_curr > max_glob:
            max_glob = max_curr
            
     
    track_sorted = sorted(track)
    ind = maximumTradesAllowed
    print('Profitable trades', len(track))
    print('Trades', track_sorted)
    print('Summed', len(track_sorted[-ind:]))
    ret = sum(track_sorted[-ind:])
        
    return "%.2f" % ret

def main():
    # This part may require participants to fill in as well.
    noOfTradesAvailable, maximumTradesAllowed = [int(random.uniform(1, 100)) for j in range(2)]
    p = [random.uniform(0, 1) for j in range(noOfTradesAvailable)]
    x = [random.uniform(0, 100) for j in range(noOfTradesAvailable)]
    y = [random.uniform(0, 100) for j in range(noOfTradesAvailable)]

    # Participants may update the following function parameters
    answer = maximumExpectedMoney(noOfTradesAvailable, maximumTradesAllowed,p,x,y)
    # Do not remove below line
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()
    

