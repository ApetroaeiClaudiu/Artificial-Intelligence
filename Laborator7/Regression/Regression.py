from Matrix.Matrix import MatrixOperations
import numpy as np
from numpy.linalg import inv

class Regression:
    def __init__(self):
        self.intercept_ = 0.0
        self.coef_ = []

    def fit(self, x,y,z):
        input = [[1,el1, el2] for el1, el2 in zip(x, y)]
        output = [[el] for el in z]
        op = MatrixOperations()
        transposeX = op.transpose(input)
        # (invers( transp(input) * input ) * transp(input) ) *output)
        weights = op.matrix_multiply(op.matrix_multiply(op.invert_matrix(op.matrix_multiply(transposeX,input)),transposeX),output)
        self.intercept_ = weights[0][0]
        self.coef_.append(weights[1][0])
        self.coef_.append(weights[2][0])

    def predict(self, x):
        return [self.intercept_ + self.coef_[0] * val[0] + self.coef_[1] * val[1] for val in x]