"""
The XOR, or “exclusive or”, problem is a classic
problem in ANN research. It is the problem of using a neural network
to predict the outputs of XOR logic gates given two binary inputs.
An XOR function should return a true value if the two inputs are not equal
and a false value if they are equal
"""

import NeuralNetwork_simple as nn
import matrix_math as mm
import random

n = nn.NeuralNetwork(2,8,1)

# XOR PROBLEM DATA
inputs = [

    mm.Matrix.list_2_matrix([0,1]),
    mm.Matrix.list_2_matrix([1,0]),
    mm.Matrix.list_2_matrix([1,1]),
    mm.Matrix.list_2_matrix([0,0])
]

labels = [
    mm.Matrix.list_2_matrix([1]),
    mm.Matrix.list_2_matrix([1]),
    mm.Matrix.list_2_matrix([0]),
    mm.Matrix.list_2_matrix([0]),

]

t_inputs = []
t_labels = []

# Creates training data with a given number of randomized inputs and labels
for i in range(20000):
    index = random.randint(0,3)
    t_inputs.append(inputs[index])
    t_labels.append(labels[index])

# Telling the network to train with the given data
n.train(t_inputs, t_labels)

# Trying all inputs to verify the result
for i in inputs:
    h, o = n.feed_forward(i)

    print("INPUT:")
    i.pretty_print()

    print("OUTPUT:")
    o.pretty_print()


# Saving the network as XOR_model (Dont write a filetype - the filetype is handled by the library)
n.save("XOR_model")
