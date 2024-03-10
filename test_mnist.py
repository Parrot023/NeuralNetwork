import NeuralNetwork as nn
import MnistTools

# Antal gange netværket testes
number_of_test_samples = 1000

# Det netværk som skal testes loades ind i hukommelsen
n = nn.NeuralNetwork.load("mnist_model_epoch_3")

# Test datasættet læses
inputs, labels = MnistTools.read_mnist('MNIST/mnist_test.csv')

# Variabel som tæller antal korrekte gæt
n_correct = 0

# Looper gennem alle testsæt
for i in range(len(inputs[0:number_of_test_samples])):
    
    # Inputtet føres gennem netværket. Netværket returnere værdierne i det skjulte lag og output laget
    hidden_layer_values, output_layer_values = n.feed_forward(inputs[i])

    # Output matrixet konverteres til en talværdi
    guess = output_layer_values.index_of_max_value()

    # Det samme gøres med label matrixet
    label = labels[i].index_of_max_value()

    print("Test {}/{}".format(i, len(inputs)))
    print("Gæt: {}".format(guess))
    print("Mål: {}".format(label))

    # De 2 sammenlignes
    if (guess == label):
        n_correct += 1

# Succes raten printes
print("SUCCES RATE: {}".format(n_correct/number_of_test_samples))
        
