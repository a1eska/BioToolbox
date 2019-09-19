from Bio import AlignIO
from Bio.SubsMat import MatrixInfo

class UnknownMatrix(Exception):
    pass

class ParserCLUSTAL:
    def __init__(self, filename):
        self.msa = AlignIO.read(filename, "clustal")

    def get_seq(self, i):
        return self.msa[i]
    
    def get_column(self, i):
        return self.msa[:,i]
    
    # expect on input matrix name from the matrices available in Bio.SubsMat.MatrixInfo
    def sp_col(self, c, gap, matrix):
        score = 0
        col = self.get_column(c)
        
        for i in range(0, len(col)):
            for j in range(i+1, len(col)):
                if col[i] == col[j] and col[i] == '-':
                    score += 1
                elif col[i] == '-' or col[j] == '-':
                    score += gap
                else:
                    score += matrix[col[i], col[j]] if (col[i], col[j]) in matrix else matrix[col[j], col[i]]
        
        return score
    
    def sp_msa(self, gap, matrix):
        score = 0

        for i in range(len(self.get_seq(0))):
            score += self.sp_col(i, gap, matrix)
        
        return score
        
    def get_scores(self, gep, matrix):
        scores = []
        
        for i in range(len(self.get_seq(0))):
            scores.append(sp_col(i, gap, matrix))
        
        return scores

if __name__ == "__main__":
    parser = ParserCLUSTAL("p53_mafft_clustal.txt")
    print(parser.get_seq(0))
    print(parser.get_column(0))
    print(parser.sp_col(0, -4, MatrixInfo.blosum62))
    print(parser.sp_msa(-4, MatrixInfo.blosum62))
    
