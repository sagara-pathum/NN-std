try :
    import cPicle as pickle
except ImportError:
    import pickle

import gzip
import numpy as np

def load_data():
    f = gzip.open('./data/mnist.pkl.gz', 'rb')
    training_data, validation_data, test_data = pickle.load(f)
    # we should close once we done with a gzip object
    f.close()

    return (training_data, validation_data, test_data)

def load_data_wrapper():
    tr_d, va_d, te_d = load_data()

    tr_input = [np.reshape(x, (784, 1)) for x in tr_d[0]]
    tr_result = [vectorized_result(j) for j in tr_d[1]]
    training_data =  zip(tr_input, tr_result)

    # we dont need the result data in binary format for validation and test sets
    
    va_input = [np.reshape(x, (784,1)) for x in va_d[0]]
    validation_data = zip(va_input, va_d[1])

    te_input = [np.reshape(x, (784,1)) for x in te_d[0]]
    test_data = zip(te_input, te_d[1])
    
    return (training_data, validation_data, test_data)


    

def vectorized_result(j):
    v = np.zeros((10,1))
    v[j] = 1
    return v

load_data_wrapper()

