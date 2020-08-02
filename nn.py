
import matrix_math as mm
import math
import pickle
import time
from scipy.special import expit

# Activation function
# def sigmoid(x):
#     """
#     At the moment non working sigmoid function.
#     Therefore the scipy expit function is used instead
#     - Another sigmoid function
#     """
#
#     print(x)
#     return 1 / (1 + math.exp(-x))


# Function to calculate gradient when doing gradient descent
def dsigmoid(y):
    """
    Function used to calculate the gradient.
    When doing gradient descent
    """
    return y * (1 - y)

# Using the expit sigmoid instead of my own
sigmoid = expit


# Translate function
def translate(x, min1 = 0, max1 = 255, min2 = 0, max2 = 1):

    """
    Takes an integer in one range and translates it to another range
    The defualt values translates an integer from a range between 0 and 255 to a range between 0 and 1
    """

    # Figure out how 'wide' each range is
    leftSpan = max1 - min1
    rightSpan = max2 - min2

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(x - min1) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return min2 + (valueScaled * rightSpan)

class NeuralNetwork():
    """
    This class contains all data and functions to make and use a fully connected neural network
    The network can be configured with any number of layers and any number of nodes per layer
    """

    def __init__(self, layers):

        self.layers = layers

        self.weights = []
        self.biases = []

        self.lr = 0.1

        # Creating a weight and bias matrix for every layer in the network (The input layer does not have biases)
        for i in range(1, len(self.layers)):

            # The columns in the weight matrix are based on the layer to the left the rows are based on the layer to the right
            self.weights.append(mm.Matrix(self.layers[i], self.layers[i-1]))

            self.biases.append(mm.Matrix(self.layers[i], 1))

            self.biases[i-1].randomize()
            self.weights[i-1].randomize()

    def feed_forward(self, input):

        """
        This function feeds the inputs through the neural network and returns the final output
        """

        # The first input is the input from the user
        self.input = input
        self.total_out = [input]

        # 1 is subtracted because this loop does not apply to the input layer
        for i in range(len(self.layers) - 1):

            # The output of the layer is the dot product of the weights and the outputs from the prevous layer
            self.out = mm.Matrix.dot_product(self.weights[i], self.input)
            # Plus the bias
            self.out.add(self.biases[i])
            # Then through the activation function
            self.out.map(sigmoid)

            self.total_out.append(self.out)

            # The ouptut of this layer is then the input of the next
            self.input = self.out


        # Returning the last output
        return self.out, self.total_out

    def train(self, inputs, labels):

        """
        Function to train the neural network using backpropagation and gradient descent
        """
        start = int(time.time())

        for i in range(len(inputs)):
            try:
                print("Training with input {}/{}".format(i, len(inputs)))

                # Makes a guess based on the inputs
                guess, total_out = self.feed_forward(inputs[i])

                # Looping through every layer of weights
                for l in range(len(self.weights) - 1, -1, -1):

                    if l == len(self.weights) - 1:

                        error = mm.Matrix.subtract(labels[i], guess)

                    else: #DOT PRUDOCT: TRANSPOSED WEIGHT AND ERROS IS THE ERROR FOR THE NEXT LAYER

                        # Uses the weights of the previous layer to calculate errror of next
                        error = mm.Matrix.dot_product(mm.Matrix.transpose(self.weights[l+1]), error)

                    # Calculating the gradients
                    # GRADIENT IS BASED ON OUTPUT OF WEIGHT LAYER !!!!!!!!!!!!!
                    # GIANT TODO: GET A BETTER UNDERSTANDING OF WHAT THIS MATH DOES!!!!!!!!!!!!!!!!
                    gradient = mm.Matrix.static_map(total_out[l+1], dsigmoid)
                    gradient.mult(error)
                    gradient.mult(self.lr)

                    # Calculating the changes in weights
                    delta_w = mm.Matrix.dot_product(gradient, mm.Matrix.transpose(total_out[l]))

                    self.biases[l].add(gradient)

                    self.weights[l].add(delta_w)

            except Exception as e:
                print("error skipped training set", i)
                print(e)
        print("Went through {} inputs in {} seconds".format(len(inputs), int(time.time()) - start))

    def test(self,inputs, labels):

        wrong = 0
        correct = 0

        for i in range(len(inputs)):
            result, data = self.feed_forward(inputs[i])
            guess = result.values.index(max(result.values))
            target = labels[i].values.index(max(labels[i].values))

            print("Input:", i, "Target:", target, "Guess:", guess)

            if guess == target:
                correct += 1
            else:
                wrong += 1


        print("score: {}/{} ({})".format(correct, correct + wrong, correct/(correct+wrong)))

    # Function to save the model to a pickle file
    def save(self, name):
        with open(str(name) + ".pickle", 'wb') as file:
            pickle.dump(self, file)

    # Static method to load in model and return it
    # A static method is called like NeuralNetwork.load(name) (Called on class name)
    # Instead of nn.load(name) (Called on instance like most other methods)
    @staticmethod
    def load(name):
        with open(str(name) + ".pickle", 'rb') as file:
            return pickle.load(file)
