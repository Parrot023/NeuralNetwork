import NeuralNetwork_simple as nn
import matrix_math as mm
# from keras.datasets import mnist
# from matplotlib import pyplot
import mnist_tools

inputs, labels = mnist_tools.read_mnist('MNIST/mnist_train.csv')

# Navnet på den fil som netværket skal gemmes i efter træningen
filename = "mnist_30000_samples"

# Antal træninger med datasættet
epochs = 1

# Et netværk med de rigtige dimensioner laves
n = nn.NeuralNetwork(28*28, 200, 10)

# For yderligere træning kan træningssættet gennemgås flere gange (epochs)
for i in range(epochs):

    # Information om fremskridt
    print("Epoch {}".format(i))

    # Netværket trænes med hele datasættet
    n.train(inputs, labels)
    
    # Gemmer efter hver epoch
    n.save("{}_epoch_{}".format(filename, i))


print("Færdiggjorde træning - netværk gemt som {}.pickle".format(filename))
