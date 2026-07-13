import numpy as np

# making the network object
# refere the site : http://neuralnetworksanddeeplearning.com/chap1.html

class Network(object):

    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) 
                        for x, y in zip(sizes[:-1], sizes[1:])]

# lets give this as the size [2, 3, 1] in the following examples
# two input neurons
# three hidden layer neurons
# 1 output


    # better to define a function for sigmoi
    def sigmoid(z):
        return 1.0/(1.0+np.exp(-z))


    # network is feedforward learning. so we define a fucntion to do the feedforward calculations of the network
    # here a is the output of the previous layer
    def feedforward(self, a):
        for b, w in zip(self.biases, slef.weights):
            a = sigmoid(np.dot(w, a) + b)
        return a


# lets give this as the size [2, 3, 1]
# two input neurons
# three hidden layer neurons
# 1 output

# lets make a Network object

net = Network([2, 3, 1])
