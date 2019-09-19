from Bio import SeqIO

class ParserFASTA:
    def __init__(self, filename):
        self.fasta_sequences = list(SeqIO.parse(filename, "fasta"))
    
    # Returns string containing the description of the k-th molecule in the file
    def descr(self, k):
        return self.fasta_sequences[k-1].description
    
    # Returns string containing the sequence of the k-th molecule in the file
    def seq(self, k):
        return self.fasta_sequences[k-1].seq
    
    # Returns the length of the i-th sequence
    def len(self, k):
        return len(self.seq(k))
    
    # Returns the subsequence from i to j of sequance k
    def subseq(self, k, i, j):
        return self.seq(k)[i-1:j]


if __name__ == "__main__":
    fasta_parser = ParserFASTA("ls_orchid.fasta")
    print(fasta_parser.descr(1))
    print(fasta_parser.seq(1))
    print(fasta_parser.len(1))
    print(fasta_parser.subseq(1, 20, 30))
    
