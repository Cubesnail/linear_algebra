class Matrix:
    def __init__(self,filename):
        file = open(filename,'r')
        self.row_num = 0
        self.col_num = 0
        self.rows = []
        self.cols = []
        self.solved = []
        self.reduced = []
        i = 0
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
        for x in range(self.row_num):
            i = 0
            for y in self.rows[x]:
                if x == 0:
                    self.cols.append([])
                self.cols[i].append(y)
                i += 1

    def row_reduce(self):
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
                if self.rows[y][x] != 0 and not self.reduced[y]:
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
    def display_matrix(self):
        for x in self.rows:
            i = 0
            print("[",end="")
            while i < self.col_num:
                if i == self.col_num - 1:
                    print(' |', end=' ')
                print(x[i],end=" ")
                i+=1
            print("]")
        print("END")
    def add_matrix(self,matrix: 'Matrix'):
        pass
    def scalar_multiple(self,multiple: 'integer'):
        pass
    def transpose(self):
        pass
    def display_solution(self):
        pass
Matrix('matrix.txt')