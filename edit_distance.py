class EditDistance:
    def __init__(self, seq_a, seq_b):
        self.seq_a = seq_a
        self.seq_b = seq_b
        self.score = []
        self.trace = []
    
    def dist(self):
        m = len(self.seq_a)
        n = len(self.seq_b)
        score = [[0 for x in range(n+1)] for x in range(m+1)]
        trace = [["" for x in range(n+1)] for x in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    score[i][j] = j
                    trace[i][j] = "Left"
                elif j == 0:
                    score[i][j] = i
                    trace[i][j] = "Up"
                elif self.seq_a[i-1] == self.seq_b[j-1]:
                    score[i][j] = score[i-1][j-1]
                    trace[i][j] = "Diag"
                else:
                    ins = score[i][j-1] + 1 # insert
                    rem = score[i-1][j] + 1 # remove
                    rep = score[i-1][j-1] + 1 # replace
                    score[i][j] = min(ins, rem, rep)
                    
                    if score[i][j] == ins:
                        trace[i][j] = "Left"
                    elif score[i][j] == rem:
                        trace[i][j] = "Up"
                    else:
                        trace[i][j] = "Diag"
        
        self.score = score
        self.trace = trace                
        
        return self.score[m][n]
    
    def align(self):
        if len(self.score) == 0:
            self.dist()
        
        align_a = ""
        align_b = ""
        i = len(self.seq_a)
        j = len(self.seq_b)
        while (i, j) != (0, 0):
            if self.trace[i][j] == "Diag":
                align_a = self.seq_a[i-1] + align_a
                align_b = self.seq_b[j-1] + align_b
                i -= 1
                j -= 1
            elif self.trace[i][j] == "Up":
                align_a = self.seq_a[i-1] + align_a
                align_b = "-" + align_b
                i -= 1
            else:
                align_a = "-" + align_a
                align_b = self.seq_b[j-1] + align_b
                j -= 1
        return (align_a, align_b)
        

        
if __name__ == "__main__":
    print("Insert two strings...")
    print("String x")
    x = input()
    print("String y")
    y = input()
    ed = EditDistance(x, y)
    print("The edit distance of x and y is {}.".format(ed.dist()))
    print("Alignment:")
    a = ed.align()
    print(a[0])
    print(a[1])
    
