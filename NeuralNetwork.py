import MatrixMath as mm
import math
import pickle

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
    Dette klasse indeholder alle data og funktioner som er nødvændige for at skabe og benytte
    et fuldt forbundet neuralt netværk. Netværket kan konfigures med et valgfrit antal noder
    i alle lag. Netværket er dog begrænset af altid at bestå af 3 lag. 
    
    Netværkets struktur:

    Input lag
    Skjult lag
    Output lag
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

        self.number_of_output_nodes = number_of_output_nodes
        self.number_of_hidden_nodes = number_of_hidden_nodes


        # Learning rate eller læringsraten benyttes til at bestemme størrelse af de
        # skridt det tages under gradient descent når netværket trænes
        self.lr = -0.1

    def feed_forward(self, input):

        """
        Denne funktion fører et input gennem netværket og returnere et matrix for værdierne
        i det skjulte lagt og et output matrix

        Parametre: funktionen feed_forward tager en parameter.
        input: Et n*1 matrix som indeholder de værdier der ønsker ført ind i netværket.
        """
        
        # Her tages prikproduktet af vægtenen mellem input laget og det skjulte lag og 
        ## det input der kommer fra input laget. Dette er nu værdierne i det skjulte lag
        self.hidden_layer_values = mm.Matrix.dot_product(self.hidden_layer_weights, input)

        # Værdiene i det sjulte lag føres nu igennem aktiveringsfunktionen
        self.hidden_layer_values.map(sigmoid)

        # Her tages prikproduktet af vægtenen mellem det sjulte lag og output laget og 
        ## det input der kommer fra det skjulte lag laget. Dette er nu værdierne i det skjulte lag
        self.output_layer_values = mm.Matrix.dot_product(self.output_layer_weights, self.hidden_layer_values)
        
        # Værdiene i output laget føres nu igennem aktiveringsfunktionen
        # Disse værdier kan nu betragtes som netværkets output.
        self.output_layer_values.map(sigmoid)

        # Output laget returneres
        return self.hidden_layer_values, self.output_layer_values

    def train(self, inputs, labels):

        """
        Funktionen train looper igennem de givne inputs og beregne ved hjælp af gradient descent
        hvordan de enkelte vægte skal ændres for at minimere cost funktionen
        """
      
        for i in range(len(inputs)):

            # Lidt information om træningens fremgang
            if (i % (len(inputs)/20) == 0): 
                print("Status: {}% af nuværende epoch ".format(int(i/len(inputs) * 100)))

            hidden_layer_values, output_layer_values = self.feed_forward(inputs[i])

            # ------------------------------------------------------------->

            # Ouput lagets fejlmatrice
            oe = mm.Matrix.subtract(output_layer_values, labels[i])

            gradient = mm.Matrix.static_map(output_layer_values, dsigmoid)
            gradient.mult(oe)
            gradient.mult(self.lr)
            
            # Ændrings matricet for vægtene mellem det skjulte lag og output laget
            delta_output_layer_weights = mm.Matrix.dot_product(gradient, mm.Matrix.transpose(hidden_layer_values))

            # ------------------------------------------------------------->

            # Det skjulte lags fejlmatrice
            he = mm.Matrix.dot_product(mm.Matrix.transpose(self.output_layer_weights), oe)


            gradient = mm.Matrix.static_map(hidden_layer_values, dsigmoid)
            gradient.mult(he)
            gradient.mult(self.lr)
        
            # Ændrings matricets for vægtene mellem input laget og det skjulte lag  
            delta_hidden_layer_weights = mm.Matrix.dot_product(gradient, mm.Matrix.transpose(inputs[i]))

            # -------------------------------------------------------------->

            # Vægtene ændres
            self.output_layer_weights.add(delta_output_layer_weights)
            self.hidden_layer_weights.add(delta_hidden_layer_weights)

    def save(self, name):

        """
        Gemmer neværket som funktionen kaldes på i en pickle fil
        """

        file = open(str(name) + ".pickle", 'wb')
        
        pickle.dump(self, file)

        file.close()

    @staticmethod
    def load(name):

        """
        En statisk funktion som indlæser et allerede eksisterende netværk
        og returnere det. Funktionen kaldes således
        NeuralNetwork.load(filnavn)
        """

        file = open(str(name) + ".pickle", 'rb')
        
        nn = pickle.load(file)

        file.close()

        return nn




