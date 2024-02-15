
import matrix_math as mm
import math
import pickle
#import time
#import random

def sigmoid(x):
    """
    Aktiveringsfunktion
    Et eller andet er galt med den her funktion (måske)
    """

    return 1 / (1 + math.exp(-x))


def dsigmoid(y):
    """
    Den differentierede sigmoid funktion
    """

    return y * (1 - y)


class NeuralNetwork():
    """
    This class contains all data and functions to make and use a fully connected neural network
    The network can be configured with any number of layers and any number of nodes per layer
    """

    def __init__(self, number_of_input_nodes, number_of_hidden_nodes, number_of_output_nodes):

        """
        Parametre: Objektet NeuralNetwork tager 3 parametre.
        number_of_input_nodes: Antallet af noder i input laget (en skalar værdi)
        number_of_hidden_nodes: Antallet af noder i det skjulte lage (en skalar værdi)
        number_of_output_nodes: Antallet af noder i output laget (en skalar værdi)

        Der er altså i dette objekt tale om et neuralt netværk bestående af 3 lag.

        """

        # Rækkefølgen her vil være: Rækkerne er laget som vægten fører til, 
        # kollonerne vil være laget som vægten kommer fra
        self.hidden_layer_weights = mm.Matrix(number_of_hidden_nodes, number_of_input_nodes)
        self.output_layer_weights = mm.Matrix(number_of_output_nodes, number_of_hidden_nodes)

        # Her initialiseres de 2 vægt matricer med tilfældige værdier fra 0 - 1
        self.hidden_layer_weights.randomize()
        self.output_layer_weights.randomize()

        # Learning rate eller læringsraten benyttes til at bestemme størrelse af de
        # skridt det tages under gradient descent når netværket trænes
        self.lr = 0.1

    def feed_forward(self, input):

        """
        This function feeds the inputs through the neural network and returns the final output
        Denne funktion fører et input gennem netværket og returnere et output matrix

        Parametre: funktionen feed_forward tager en parameter.
        input: Et n*1 matrix som indeholder de værdier der ønsker ført ind i netværket.
        """
        
        # Her tages prikproduktet af vægtenen mellem input laget og det skjulte lag og 
        ## det input der kommer fra input laget. Dette er nu værdierne i det skjulte lag
        self.hidden_layer_values = mm.Matrix.dot_product(self.hidden_layer_weights, input)

        #self.hidden_layer_values.pretty_print()

        # Værdiene i det sjulte lag føres nu igennem aktiveringsfunktionen
        self.hidden_layer_values.map(sigmoid)

        #self.hidden_layer_values.pretty_print()


        # Her tages prikproduktet af vægtenen mellem det sjulte lag og output laget og 
        ## det input der kommer fra det skjulte lag laget. Dette er nu værdierne i det skjulte lag
        self.output_layer_values = mm.Matrix.dot_product(self.output_layer_weights, self.hidden_layer_values)
        
        # Værdiene i output laget føres nu igennem aktiveringsfunktionen
        # Disse værdier kan nu betragtes som netværkets output.
        self.output_layer_values.map(sigmoid)

        # Output laget returneres
        return self.hidden_layer_values, self.output_layer_values

    def train(self, inputs, labels, learning_rate=-0.1):

        """
        Funktionen train looper igennem de givne inputs og beregne ved hjælp af gradient descent
        hvordan de enkelte vægte skal ændres for at minimere cost funktionen
        """

        for i in range(len(inputs)):

            # Lidt information om træningens fremgang
            print("TRÆNER: {}%".format(int(i/len(inputs) * 100)))

            hidden_layer_values, output_layer_values = self.feed_forward(inputs[i])

            # ------------------------------------------------------------->

            # Ouput lagets fejlmatrice
            oe = mm.Matrix.subtract(output_layer_values, labels[i])

            gradient = mm.Matrix.static_map(output_layer_values, dsigmoid)
            gradient.mult(oe)
            gradient.mult(learning_rate)
            
            # Ændrings matricets for vægtene mellem det skjulte lag og output laget
            delta_output_layer_weights = mm.Matrix.dot_product(gradient, mm.Matrix.transpose(hidden_layer_values))

            # ------------------------------------------------------------->

            # Det skjulte lags fejlmatrice
            he = mm.Matrix.dot_product(mm.Matrix.transpose(self.output_layer_weights), oe)


            gradient = mm.Matrix.static_map(hidden_layer_values, dsigmoid)
            gradient.mult(he)
            gradient.mult(learning_rate)
          
            # Ændrings matricets for vægtene mellem input laget og det skjulte lag  
            delta_hidden_layer_weights = mm.Matrix.dot_product(gradient, mm.Matrix.transpose(inputs[i]))

            # -------------------------------------------------------------->

            # Vægtene ændres
            self.output_layer_weights.add(delta_output_layer_weights)
            self.hidden_layer_weights.add(delta_hidden_layer_weights)


    def save(self, name):

        """
        Saves the neural network to a pickle file
        """

        with open(str(name) + ".pickle", 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load(name):

        """
        Static method to load in model and return it
        A static method is called like NeuralNetwork.load(name) (Called on class name)
        Instead of nn.load(name) (Called on instance like most other methods)
        """

        with open(str(name) + ".pickle", 'rb') as file:
            return pickle.load(file)




