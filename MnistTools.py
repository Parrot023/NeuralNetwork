import MatrixMath as mm

def read_mnist(filename):

    print("Læser MNIST data")

    # Åbner filen med data
    data_file = open(filename, 'r')

    # Læser datafilen
    data_list = data_file.readlines()

    # Lukker data filen
    data_file.close()

    inputs = []
    labels = []

    #Looper gennem alle dataene
    for i in range(len(data_list)):

        # Den første del af data'ene er inputtets label. Denne skal ikke bruges til at kreere inputtet
        data = data_list[i][2:len(data_list[i]) - 1].split(',')

        # Hver indeks i data'ene konverteres fra string til int
        data = [(float(data[i]) / 255 * 0.99) + 0.01 for i in range(len(data))]

        # Konvertere input listen til et matrix
        input = mm.Matrix.list_2_matrix(data)
        # input.pretty_print()

        # Skaber en liste med længden 10 bestående kun af 0'er
        label = [0.01 for i in range(10)]

        # Sætter det korrektre indeks i listen til 1
        label[int(data_list[i][0:1])] = 0.99

        # Konvertere labal matrixet fra en liste til et matrix objekt
        label = mm.Matrix.list_2_matrix(label)

        inputs.append(input)
        labels.append(label)

        # Information om fremskridt
        if (i % (len(data_list)/20) == 0):
            print("{}%".format(int(i/len(data_list)*100)))

    print("Færdiggjorde læsning af MNIST data")
    return inputs, labels