class Matrix:
    def __init__(self):
        """Initialize the Matrix class.

        row_num - the number of rows in the matrix.
        col_num - the number of columns in the matrix.
        rows - a list of each of the rows in the matrix.
        cols - a list of each of the rows in the matrix.
        :return: None
        """
        self.row_num = 0
        self.col_num = 0
        self.rows = []
        self.cols = []

    def open_matrix_file(self, filename):
        """Parse through a text file and assign it a matrix.

        :param filename: str
        :return: None
        """
        i = 0
        file = open(filename, 'r')
        for line in file:
            #  Skip any lines starting with '#'
            if line[0] not '#':
                line = line.rstrip()
                self.rows.append([])
                self.rows[i] = list(map(int, line.split()))
                i += 1
        self.row_num = i
        print(self.rows)
        self.col_num = len(self.rows[0])
        self.update_cols()
        print("Unsolved Matrix")
        self.display_matrix()

    def update_cols(self):
        """Update the columns of a matrix given the rows.

        :rtype: None
        :return:
        """
        self.cols = []

        #  Iterate through the list of lists and append the element to the appropriate list.
        for x in range(self.row_num):
            i = 0
            for y in self.rows[x]:
                if x == 0:
                    self.cols.append([])
                self.cols[i].append(y)
                i += 1
        self.col_num = len(self.cols)

    def update_rows(self):
        """Update the rows of the matrix given the rows.
        :rtype: None
        :return:
        """
        self.rows = []

        #  Iterate through the list of lists and append the element to the appropriate list.
        for y in range(self.col_num):
            i = 0
            for x in self.cols[y]:
                if y == 0:
                    self.rows.append([])
                self.rows[i].append(x)
        self.row_num = len(self.rows)

    def row_reduce(self):
        """Row reduce the given matrix.

        :return matrix: Matrix

        """
        starting_one = False
        reduced = False
        starting_num = 0
        # reducing_row = 0
        # reducing_col = 1
        remove_rows = []
        y = 0
        #  Determine if the matrix has a non-zero element.
        for x in range(self.row_num):
            starting_one = False
            i = 0
            while i < self.col_num and not starting_one:
                if self.rows[x][i] != 0:
                    starting_one = True
                i += 1
            if not starting_one:
                remove_rows.append(x)
                self.rows.append(self.rows[x])
        remove_rows.sort(reverse=True)
        #  wtf am I doing here
        #  TODO
        for row in remove_rows:
            self.rows.remove(row)
        self.update_cols()
        if len(remove_rows) == len(self.rows):
            return None
        #  if the matrix cannot be row-reduced, return None
        for y in range(self.row_num):
            for x in range(self.col_num):
                if self.rows[y][x] != 0 and not self.reduced[y] and x != self.col_num:
                    #  Find the first non-zero number and reduce all other rows relative to it.
                    reducing_num = self.rows[y][x]
                    reducing_col = x
                    reducing_row = y
                    if reducing_num != 1:
                        for num in range(0, self.col_num):
                            self.rows[reducing_row][num] = self.rows[reducing_row][num] / reducing_num
                    for x in range(0, self.row_num):
                        if x != reducing_row:
                            reducing_coe = self.rows[x][reducing_col] / self.rows[reducing_row][reducing_col]
                            for num in range(self.col_num):
                                self.rows[x][num] -= self.rows[reducing_row][num] * reducing_coe
                    self.reduced[y] = True
        self.update_cols()

    def display_matrix(self):
        """Print the matrix

        :return:
        """
        #TODO
        longest = 0
        decimal = False
        #  Find the number with the largest amount of digits.
        for y in self.rows:
            i = 0
            for x in y:
                if x == 0:
                    x = abs(x)
                if len(str(x)) > longest:
                    if str(x) == str(str('{:.' + str(len(str(x - 2))) + 'f}').format(x)):
                        decimal = True
                    longest = len(str(x))

        #  Print each number with the same string length as the longest matrix element.
        for x in self.rows:
            i = 0
            print("[", end="")
            while i < self.col_num:
                if i == self.col_num - 1:
                    print(' |', end=' ')
                if x[i] == 0:
                    x[i] = abs(x[i])
                print(str(str('{:.' + str(len(str(longest - 2))) + 'f}').format(x[i])), end=" ")
                i += 1
            print("]")
        print("END")

    def transpose(self):
        """Transpose a given matrix.

        :return: matrix
        """
        pass
        result = Matrix()
        result.rows = self.cols
        result.cols = self.rows
        #  Switch the rows and columns and return the resulting matrix.
        result.row_num = len(result.rows)
        result.col_num = len(result.cols)

        return result

    def determinant(self):
        """Return the determinant of a given matrix.

        :return:
        :rtype: int
        """
        if self.cols != self.rows:
            return False
        result = 0
        # Iterate through the first row and all the columns and remove it.
        if self.cols == 2:
            return self.determinant_base()
        else:
            for x in range(self.col_num):
                helper = Matrix()
                helper = self
                del helper.rows[0]
                helper.update_cols()
                del helper.cols[x]
                helper.update_rows()
                #  Find the determinant of the resulting matrix.
                if x % 2 == 0:
                    result += helper.determinant
                else:
                    helper = Matrix
                    result -= helper.determinant
        return result

    def adjugate(self):
        """Return an adjugated matrix.
        :rtype: Matrix
        :return: 
        """

        result = self
        temp_matrix = Matrix()
        for y in range(self.row_num):
            for x in range(self.col_num):
                #  Iterate through each element in a matrix.
                temp_matrix = self
                del temp_matrix.rows[y]
                temp_matrix.update_cols()
                del temp_matrix.cols[x]
                temp_matrix.update_rows()
                result.rows[y][x] = temp_matrix.determinant()
        return result
    def is_diagonalizable(self):
        """Return if the matrix is diagonalizable

        :return: bool
        """
        #TODO
        pass
    def diagonalize(self):
        """Return the diagonalized matrix.

        :return: Matrix
        """
        #TODO
        pass
    def determinant_base(self):
        """Return the determinant of a matrix of size 2*2.
        :rtype: float
        :return:
        """
        return (self.rows[0][0]*self.rows[1][1]) - (self.rows[1][0]*self.rows[0][1])

    def display_solution(self):
        """

        :return:
        """
        self.row_reduce().display_matrix()

    def eigenvectors(self):
        """
        :rtype: list
        :return:
        """
        #  TODO
        pass

def is_inverse(matrix, other):
    """Return if True if two matrices are inverses of each other and False otherwise.

    :param matrix:
    :param other:
    :return:
    """
    # TODO
    return matrix_multiplication(matrix,other) == unit_matrix(matrix.row_num) and \
           matrix_multiplication(other,matrix) == unit_matrix(other.row_num)


def matrix_multiplication(matrix, other):
    """Multiply two matrices and return the result.

    :param matrix:
    :param other:
    :return:
    """
    # TODO
    b = []
    result = Matrix()
    for x in range(matrix.col_num):
        b.append(0)
    if matrix.col_num != other.row_num:
        return None
    helper = Matrix()

    #  Multiply the matrix with each column of the 'other' matrix and sum the resulting rows.
    for x in other.cols:
        helper = matrix.vector_multiplication(x)
        for y in range(helper.row_num):
            for m in helper.rows[y]:
                b[y] += m
        result.cols.append(b)
    result.update_rows()
    return result


def vector_multiplication(matrix, vector):
    """Multiply a matrix by a vector and return the result

    :param matrix:
    :param vector:
    :return:
    """
    # TODO
    if len(vector) != matrix.row_num:
        return None
    result = Matrix()
    temp_list = []

    if matrix.row_num == len(vector):
        for x in range(matrix.row_num):
            temp_list.append(0)
        for x in range(len(vector)):
            for y in matrix.cols[x]:
                temp_list[x] = vector[x] * y
            result.cols.append(b)
    result.update_cols()
    return result


def add_matrix(matrix, other):
    """Add two matrices together and return the sum.

    :param matrix:
    :param other:
    :return:
    """
    # TODO
    if matrix.row_num != other.row_num or matrix.col_num != other.col_num:
        return None
    result = Matrix

    for y in range(matrix.row_num):
        for x in range(matrix.col_num):
            result.rows[y][x] += other.rows[y][x]
    result.update_cols()
    return result

def scalar_multiplication(matrix, multiple):
    # TODO: doctests
    """Multiply a matrix by a scalar value.
    :type matrix: Matrix
    :type multiple: float
    :param matrix:
    :param multiple:
    :return:
    :rtype: Matrix
    """
    result = matrix
    for y in result.rows:
        for x in y:
            x *= multiple
    result.update_cols()
    return result


def is_communative(matrix, other):
    """Return whether two matrices are communitiative.

    :param matrix:
    :param other:
    :return:
    """
    return matrix_multiplication(matrix, other) == matrix_multiplication(other, matrix)


def unit_matrix(size):
    """Return the unit matrix (identity matrix) of size n*n where param size = n

    :param size:
    :return:
    """
    #TODO
    result = Matrix()
    for y in range(size):
        result.rows.append([])
    for y in result.rows:
        for x in range(size):
            result.append(0)
    for y in range(size):
        result.rows[y][y] = 1
    return result

