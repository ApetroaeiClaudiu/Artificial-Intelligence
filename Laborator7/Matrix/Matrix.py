
class MatrixOperations:


    def print_matrix(self ,M):
        for row in M:
            print([round(x, 3) + 0 for x in row])

    def zeros_matrix(self,rows, cols):
        M = []
        while len(M) < rows:
            M.append([])
            while len(M[-1]) < cols:
                M[-1].append(0.0)
        return M

    def identity_matrix(self,n):
        IdM = self.zeros_matrix(n, n)
        for i in range(n):
            IdM[i][i] = 1.0
        return IdM

    def copy_matrix(self,M):
        rows = len(M)
        cols = len(M[0])
        MC = self.zeros_matrix(rows, cols)
        for i in range(rows):
            for j in range(rows):
                MC[i][j] = M[i][j]
        return MC

    def transpose(self,M):
        rows = len(M)
        cols = len(M[0])
        MT = self.zeros_matrix(cols, rows)
        for i in range(rows):
            for j in range(cols):
                MT[j][i] = M[i][j]
        return MT

    def matrix_multiply(self,A, B):
        rowsA = len(A)
        colsA = len(A[0])
        rowsB = len(B)
        colsB = len(B[0])
        C = self.zeros_matrix(rowsA, colsB)
        for i in range(rowsA):
            for j in range(colsB):
                total = 0
                for ii in range(colsA):
                    total += A[i][ii] * B[ii][j]
                C[i][j] = total
        return C

    def invert_matrix(self,A):
        #Gaussian elimination
        #Make copies of A & I, AM & IM, to use for row operations
        #IM will be the invert of A
        n = len(A)
        AM = self.copy_matrix(A)
        I = self.identity_matrix(n)
        IM = self.copy_matrix(I)
        #Perform row operations
        indices = list(range(n))
        #row looping
        for fd in range(n):
            #focus diagonal
            #working on making the diagonal 1's
            fdScaler = 1.0 / AM[fd][fd]
            #scale fd row with fd inverse.
            for j in range(n):
                #column looping.
                AM[fd][j] = AM[fd][j] * fdScaler
                IM[fd][j] = AM[fd][j] * fdScaler
            #operate on all rows except fd row:
            for i in indices[0:fd] + indices[fd + 1:]:
                #current row
                crScaler = AM[i][fd]
                for j in range(n):
                    #crScaler * fdRow, one element at a time
                    #working on making the rest 0's
                    AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                    IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
        return IM