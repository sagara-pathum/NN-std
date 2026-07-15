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
    
    def SGD(self, training_data, mini_batch_size, epochs, eta, testing_data=None):
        if testing_data: n_test = len(testing_data)
        n = len(training_data)

        for j in xrange(epochs):
            random.shuffle(training_data)
            mini_batches = [
                training_data[k : k+mini_batch_size]
                for k in xrange(0, n, mini_batch_size)
                    ]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta) # this is the function for SGD training

        if training_data:
            pass

    def update_mini_batch(self, mini_batch, eta):
        
        # we need to initialize the gradients for the mini_batch. remember that as per the matrix equation, we need the gradient dimentions as same as 
        # weight and bias matrix's dimention. other wise we cannot do adding operations. (just look the equation)

        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        
        for x, y in mini_batch:
            # lets calculate the minibatch's gradient by calculating gradient for each of the sample separately
            # lets say the we are doing it using back propergation for each sample.
            # for simplycity we can impliment the backpropergation function separately. here we call it backprop(x, y)

            delta_nabla_w, delta_nabla_b = self.backprop(x, y)

            # no we can accumilate the those delta values to get the total minibatch's gradient 
            nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]

        # now we have the total gradient for our minibatch. so lets update our weights and biases according to the gradient.
        # but recall that we are not we are adding so much of gradient together. (actually we are plotting cost functions for each x, y tupple on same space, like wave interference)
        # so that it makes a overall cost function. but the here problem is we are adding the unit vectors as well. so if we do this for n samples. our unit vector will 1*n long 
        # on the curve
        # so we need to divede by n to make the unit vector an actual unit vector on our overall surface.
        # further 
        # now we have the direction by gradient.
        # what we do it go goes the opposite of that direction by eta amount. from where we are at now.
    
        # also remember our nabla values are set of values for each of the layer. so we need to assign weights for each layer using a for loop
        self.weights = [(w - (eta/len(mini_batch)* nw)) for w, nw in zip(self.weights, nabla_w))]
        self.biases = [(b - (eta/len(mini_batch)* nb)) for b, nb in zip(self.biases, nabla_b)]
    

        

# lets give this as the size [2, 3, 1]
# two input neurons
# three hidden layer neurons
# 1 output

# lets make a Network object

net = Network([2, 3, 1])
