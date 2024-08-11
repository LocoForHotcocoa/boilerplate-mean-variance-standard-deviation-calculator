import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.reshape(list, (3, 3))

    # initialize dictionary to store values
    calculations = {
        'mean': [[],[]], 
        'variance': [[],[]], 
        'standard deviation': [[],[]], 
        'max': [[],[]], 
        'min': [[],[]], 
        'sum': [[],[]]
        }
    
    # calculate horizontal and vertical axis values
    for j in range(2):
        for i in range(3):
            if j == 0:
                seq = matrix[:,i]
            elif j==1:
                seq = matrix[i,:]

            calculations['mean'][j].append(float(np.mean(seq)))
            calculations['variance'][j].append(float(np.var(seq)))
            calculations['standard deviation'][j].append(float(np.std(seq)))
            calculations['max'][j].append(int(np.max(seq)))
            calculations['min'][j].append(int(np.min(seq)))
            calculations['sum'][j].append(int(np.sum(seq)))


    # calculating the flattened matrix values
    calculations['mean'].append(float(np.mean(list)))
    calculations['variance'].append(float(np.var(list)))
    calculations['standard deviation'].append(float(np.std(list)))
    calculations['max'].append(int(np.max(list)))
    calculations['min'].append(int(np.min(list)))
    calculations['sum'].append(int(np.sum(list)))

    return calculations
