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
  

# Code below is similar to above code but more dynamic
weights = [[0.2, 0.8, -0.5, 1.0], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

layer_outputs = []

for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input*weight
    
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)

# Shape Explanation!!!:
'''
array = [1,5,6,2]
shape of this array is (4,)
type of this array is 1D array, Vector

array2 = [[1,5,6,2], [3,2,1,3]]
shape of this array is (2,4)
type of this array is 2D Array, Matrix

array3 = [[[1,5,6,2], [3,2,1,3]], [[1,5,6,2], [3,2,1,3]], [[1,5,6,2], [3,2,1,3]]]
shape of this array is (3,2,4)
type of this array is 3D Array

'''

# Dot Product Example Below

inputs = [1,2,3,2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2

output = np.dot(weights, inputs) + bias


inputs = [1,2,3,2.5]
weights = [[0.2, 0.8, -0.5, 1.0], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]

output = np.dot(weights, inputs) + biases # Very important that weights are the first argument
print(type(output))