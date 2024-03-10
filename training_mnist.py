import NeuralNetwork as nn
import MnistTools
import time

# Trænings datasættet læses
inputs, labels = MnistTools.read_mnist('MNIST/mnist_train.csv')

# Navnet på den fil som netværket skal gemmes i efter træningen
filename = "mnist_model"

# Antal træninger med datasættet
epochs = 4

# Et netværk med de rigtige dimensioner laves
# n = nn.NeuralNetwork(28*28, 200, 10)
n = nn.NeuralNetwork.load("SUCCESFULLY_TRAINED_NETWORKS/mnist_model_epoch_0_sr_87")

# Notering af start tidspunkt
start_time = time.time()

# For yderligere træning kan træningssættet gennemgås flere gange (epochs)
for i in range(epochs):

    # Information om fremskridt
    print("Starter epoch {}".format(i))

    # Netværket trænes med hele datasættet
    n.train(inputs, labels)
    
    # Gemmer efter hver epoch
    n.save("{}_epoch_{}".format(filename, i))

    print("Færdiggjorde epoch {}".format(i))
    print("Tid brugt: {} minutter".format((time.time() - start_time) / 60))
    print("Netværk gemt som {}_epoch_{}.pickle".format(filename, i))
