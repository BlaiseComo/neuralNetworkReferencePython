# There is an input layer, hidden layers (no limit to num of hidden layers), and an output layer
# In a network, every neuron in a layer is connected to every neuron in the layers next to it 

import sys
import numpy as np
import matplotlib

# The code for a single neuron
# The inputs are 3 neurons feeding into a single neuron calculated by the output using the dot product of inputs and weights plus bias
inputs = [1.2, 5.1, 2.1]

weights = [3.1, 2.1, 8.7]

bias = 3

# Output for neural network
output = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + bias

