class Matrix:
    def __init__(self):
        '''

        :return:
        '''
        self.row_num = 0
        self.col_num = 0
        self.rows = []
        self.cols = []
        self.solved = []
        self.reduced = []
    def open_matrix_file(self,filename):
        '''

        :param filename:
        :return: false
        '''
        i = 0
        file = open(filename,'r')
        for line in file:
            line = line.rstrip()
            self.rows.append([])
            self.reduced.append(False)
            self.rows[i] = list(map(int,line.split()))
            i += 1
        self.row_num = i
        print(self.rows)
        self.col_num = len(self.rows[0])
        self.update_cols()
        print(self.cols)
        print("Unsolved Matrix")
        self.display_matrix()
        print(self.col_num)
        self.row_reduce()
        print("Row-Reduced Echelon Matrix")
        self.display_matrix()
        print(self.col_num)
    def update_cols(self):
        '''

        :rtype: object
        :return:
        '''
        self.cols = []
        for x in range(self.row_num):
            i = 0
            for y in self.rows[x]:
                if x == 0:
                    self.cols.append([])
                self.cols[i].append(y)
                i += 1
        self.col_num = len(self.cols)
    def update_rows(self):
        '''
        :return:
        '''
        self.rows = []
        for y in range(self.col_num):
            i = 0
            for x in self.cols[y]:
                if y == 0:
                    self.rows.append([])
                self.rows[i].append(x)
        self.row_num = len(self.rows)
    def row_reduce(self):
        '''

        :return matrix:

        '''
        starting_one = False
        reduced = False
        starting_num = 0
        reducing_row = 0
        reducing_col = 1
        remove_rows = []
        y = 0
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
        for row in remove_rows:
            self.rows.remove(row)
        self.update_cols()
        if len(remove_rows) == len(self.rows):
            return
        for y in range(self.row_num):
            for x in range(self.col_num):
                if self.rows[y][x] != 0 and not self.reduced[y] and x != self.col_num:
                    print(True)
                    reducing_num = self.rows[y][x]
                    reducing_col = x
                    reducing_row = y
                    if reducing_num != 1:
                        for num in range(0,self.col_num):
                            self.rows[reducing_row][num] = self.rows[reducing_row][num] / reducing_num
                    for x in range(0,self.row_num):
                        if x != reducing_row:
                            reducing_coe = self.rows[x][reducing_col]/self.rows[reducing_row][reducing_col]
                            for num in range(self.col_num):
                                self.rows[x][num] -= self.rows[reducing_row][num] * reducing_coe
                    self.reduced[y] = True
        self.update_cols()
    def display_matrix(self):
        '''

        :return:
        '''
        longest = 0
        decimal = False
        for y in self.rows:
            i = 0
            for x in y:
                if x == 0:
                    x = abs(x)
                if len(str(x)) > longest:
                    if str(x) == str(str('{:.'+str(len(str(x-2)))+'f}').format(x)):
                        decimal = True
                    longest = len(str(x))

        for x in self.rows:
            i = 0
            print("[",end="")
            while i < self.col_num:
                if i == self.col_num - 1:
                    print(' |', end=' ')
                if x[i] == 0:
                    x[i] = abs(x[i])
                print(str(str('{:.'+str(len(str(longest-2)))+'f}').format(x[i])),end=" ")
                i+=1
            print("]")
        print("END")
    def add_matrix(self, other_matrix: 'Matrix'):
        '''
        :param other_matrix: matrix
        :return: matrix
        '''
        pass
    def scalar_multiplication(self,multiple: 'integer'):
        '''

        :param multiple: integer
        :return: matrix
        '''
        for y in self.rows:
            for x in y:
                x = x * multiple
    def transpose(self):
        '''

        :return: matrix
        '''
        pass
        result = Matrix()
        result.rows = self.cols
        result.cols = self.rows

        result.row_num = len(result.rows)
        result.col_num = len(result.cols)

        return result
    def vector_multiplication(self, vector: 'List'):
        '''

        :param vector: list
        :return result: matrix
        '''
        result = Matrix()
        b = []
        if self.row_num == len(vector):
            for x in range(self.row_num):
                b.append(0)
            for x in range(len(vector)):
                for y in self.cols[x]:
                    b[x] = vector[x]*y
                result.cols.append(b)
        result.update_cols()
        return result
    def matrix_multiplication(self,other):
        '''

        :param other:
        :return:
        '''
        b = []
        result = Matrix()
        for x in range(self.col_num):
            b.append(0)
        if self.col_num != other.row_num:
            return False
        helper = Matrix()
        for x in other.cols:
            helper = self.vector_multiplication(x)
            for y in range(helper.row_num):
                for m in helper.rows[y]:
                    b[y] += m
            result.cols.append(b)
        result.update_rows()
        return result

    def is_inverse(self,other: 'Matrix'):
        '''
        :param other:
        :return:
        '''
        pass
        if self.matrix_multiplication(other) == other.matrix_multiplication(self):
            return True
        else:
            return False
    def display_solution(self):
        '''

        :return:
        '''
        pass

