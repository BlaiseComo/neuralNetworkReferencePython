# There is an input layer, hidden layers (no limit to num of hidden layers), and an output layer
# In a network, every neuron in a layer is connected to every neuron in the layers next to it 

import sys
import numpy as np
import matplotlib

# Below code simulates 3 neurons (hence 3 sets of weights and biases) with 4 inputs, each output neuron has there own set of weights, but each input neuron can have 3 connections 
# coming from it, each with it's own unique weight (depends on output neuron it connects to)

inputs = [1, 2, 3, 2.5]

weights1 = [0.2, 0.8, -0.5, 1.0]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

bias1 = 2
bias2 = 3
bias3 = 0.5

# Output for neural network
output = [inputs[0] * weights1[0] + inputs[1] * weights1[1] + inputs[2] * weights1[2] + inputs[3] * weights1[3] + bias1, 
          inputs[0] * weights2[0] + inputs[1] * weights2[1] + inputs[2] * weights2[2] + inputs[3] * weights2[3] + bias2,
          inputs[0] * weights3[0] + inputs[1] * weights3[1] + inputs[2] * weights3[2] + inputs[3] * weights3[3] + bias3]
  


