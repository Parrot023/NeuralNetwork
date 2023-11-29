
import random

class Matrix():

    """
    This contains all the values of a matrix and the functions needed to do basic math with them
    Most list operations in this class are done using list comprehension as this i faster than standard for loops
    I have chosen to keep a standard for loop version of most list comprehensions for easier reading

    Many of the below functions have a static and a normal version the static version takes in inputs and returns an output
    the normal ones change the matrix they are called on
    """

    # Static methods are used like Matrix.mult(m1,m2) instead of m1.mult(m2)

    def __init__(self, rows, cols):

        self.rows = rows
        self.cols = cols
        self.default_value = 0

        self.values = [[self.default_value for c in range(cols)] for r in range(rows)]
        # for r in range(self.rows):
        #     self.matrix.append([])
        #     for c in range(self.cols):
        #         r.append(1)

    def mult(self, multiplier):

        """
        Multiplies every element in the matrix with a given multiplier
        if the given multiplier is a matrix every element in the matrix
        wil be multiplied with the corresponding element in the multiplier matrix

        Otherwise every element will be multiplied by the given integer or float

        This function changes the matrix it is called on
        """

        if isinstance(multiplier, Matrix):
            self.values = [[self.values[r][c] * multiplier.values[r][c] for c in range(self.cols)] for r in range(self.rows)]
        else:
            self.values = [[c * multiplier for c in r] for r in self.values]

        # for r in range(m.rows):
        #     for c in range(m.cols):
        #         self.matrix[r][c] *= multiplier

    def add(self, adder):

        """
        Adds every element in the matrix with a given adder
        if the given adder is a matrix every element in the matrix
        wil be added with the corresponding element in the adder matrix

        Otherwise every element will be added by the given integer or float

        This function changes the matrix it is called on
        """

        if isinstance(adder, Matrix):
            self.values = [[self.values[r][c] + adder.values[r][c] for c in range(self.cols)] for r in range(self.rows)]
        else:
            self.values = [[c + adder for c in r] for r in self.values]
        # for r in range(m.rows):
        #     for c in range(m.cols):
        #         self.matrix[r][c] += adder

    def randomize(self):
        """
        Gives every element in the matrix a random value between -1 and 1
        """
        self.values = [[round(random.uniform(-1,1),2) for c in r] for r in self.values]

    def map(self, function, **kwargs):

        """
        Applies a function (f) to every element in the matrix
        if the function needs more arguments than x (the element itself) they can be given to the map function (m) as kwargs
        the map function (m) will then pass the kwargs on to the function (f)

        This function changes the matrix it is called on
        """

        self.values = [[function(c, **kwargs) for c in r] for r in self.values]

        # for r in range(self.rows):
        #     for c in range(self.cols):
        #         self.values[r][c] = function(c)

    def pretty_print(self):

        """
        Function to print the matrix like a table
        """

        for r in self.values:
            print(r)
        print("")

    @staticmethod
    def list_2_matrix(list):

        """
        Converts a given list into a matrix

        This function returns a new matrix
        """

        result = Matrix(len(list), 1)

        for i in range(len(list)):
            result.values[i][0] = list[i]

        return result
    
    @staticmethod
    def static_map(m, function, **kwargs):

        """
        Applies a function (f) to every element in the matrix
        if the function needs more arguments than x (the element itself) they can be given to the map function (m) as kwargs
        the map function (m) will then pass the kwargs on to the function (f)

        This function returns a new matrix
        """

        result = Matrix(m.rows, m.cols)

        result.values = [[function(c, **kwargs) for c in r] for r in m.values]

        return result
    
    @staticmethod
    def transpose(m):
        """
        Function to turn the matrix every row becomes a col and every col becomes a row
        Running the function twice will turn the matrix back to its original dimensions
        """

        result = Matrix(m.cols, m.rows)

        result.values = [[m.values[r][c] for r in range(m.rows)] for c in range(m.cols)]
        # The orientation can be changed by changing whether we loop through the cols or rows first look below
        # ---------------------------------------------------------------------------------------------------
        # self.values = [[m.values[r][c] for c in range(m.cols)] for r in range(m.rows)]
        # ----------------------------------------------------------------------------------------------------

        # m.rotated = []
        # for c in range(self.cols):
        #     m.rotated.append([])
        #     for r in range(self.rows):
        #         m.rotated[c].append(self.values[r][c])
        # result.values = m.rotated

        return result
    
    @staticmethod
    def subtract(m, subtracter):

        """
        Subtracts every element in the matrix with a given subtracter
        if the given subtracter is a matrix every element in the matrix
        wil be subtractet with the corresponding element in the subtracter matrix

        Otherwise every element will be subtractet by the given integer or float

        This function changes the matrix it is called on
        """

        result = Matrix(m.rows, m.cols)

        if isinstance(subtracter, Matrix):
            result.values = [[m.values[r][c] - subtracter.values[r][c] for c in range(m.cols)] for r in range(m.rows)]
        else:
            result.values = [[c - subtracter for c in r] for r in m.values]

        return result
        # for r in range(m.rows):
        #     for c in range(m.cols):
        #         self.matrix[r][c] += adder

    @staticmethod
    def static_add(m, adder):

        """
        Adds every element in the matrix with a given adder
        if the given adder is a matrix every element in the matrix
        wil be added with the corresponding element in the adder matrix

        Otherwise every element will be added by the given integer or float

        This function returns a new matrix
        """

        result = Matrix(m.rows, m.cols)

        if isinstance(adder, Matrix):
            result.values = [[m.values[r][c] + adder.values[r][c] for c in range(m.cols)] for r in range(m.rows)]
        else:
            result.values = [[c + adder for c in r] for r in m.values]

        return result
        # for r in range(m.rows):
        #     for c in range(m.cols):
        #         self.matrix[r][c] += adder

    @staticmethod
    def static_mult(m, multiplier):

        """
        Multiplies every element in a matrix with a given multiplier
        if the given multiplier is a matrix every element in the matrix
        wil be multiplied with the corresponding element in the multiplier matrix

        Otherwise every element will be multiplied by the given integer or float

        This function returns a new matrix
        """

        result = Matrix(m.rows, m.cols)
        if isinstance(multiplier, Matrix):
            result.values = [[m.values[r][c] * multiplier.values[r][c] for c in range(m.cols)] for r in range(m.rows)]
        else:
            result.values = [[c * multiplier for c in r] for r in m.values]

        return result
    
    @staticmethod
    def dot_product(m1, m2):

        """
        Calculates the dot product between to matricies

        This function returns a new matrix
        """

        # This is a list comprehension version of the below for-loop nightmare. i have chosen to keep the for loops as comment for easier understanding
        # This madness loops over every row in this matrix makes a list then loops over every col in the other matrix where every index is the sum of a third list
        # The third list is a list containing all the products off multiplying the row and the col we looped through first
        # As this i quite hard to read i would advice looking at the longer version doing the same

        if m1.cols == m2.rows:

            result = Matrix(m1.rows, m2.cols)
            result.values = [[sum([m1.values[r][r2] * m2.values[r2][c] for r2 in range(m2.rows)]) for c in range(m2.cols)] for r in range(m1.rows)]

            # dp_values = []
            # for r in range(m1.rows):
            #     dp_values.append([])
            #     for c in range(m2.cols):
            #         products = []
            #         for r2 in range(m2.rows):
            #             products.append(m1.values[r][r2] * m2.values[r2][c])
            #         dp_values[r].append(sum(products))
            # result.values = dp_values

        else:
            print("Row of m1 is not equal col of m2")
            result = None

        return result


