import argparse
from Bio import AlignIO
from Bio.SubsMat import MatrixInfo

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
        
    def get_scores(self, gap, matrix):
        scores = []
        
        for i in range(len(self.get_seq(0))):
            scores.append(self.sp_col(i, gap, matrix))
        
        return scores

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="Path to a clustal file.")
    
    args = ap.parse_args()
    
    try:
        clustal_parser = ParserCLUSTAL(args.path)
        print("Sum of pairs: {}.".format(clustal_parser.sp_msa(-4, MatrixInfo.blosum62)))
        print("List of conservation-like scores of positions:")
        print(clustal_parser.get_scores(-4, MatrixInfo.blosum62))
    except FileNotFoundError:
        print("File '{}' could not be opened.".format(args.path))
