import argparse
from Bio import SeqIO

class ParserFASTA:
    def __init__(self, filename):
        self.fasta_sequences = list(SeqIO.parse(filename, "fasta"))
        self.ns = len(self.fasta_sequences)
    
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
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="Path to a fasta file.")
    ap.add_argument("-s", "--sequence", type=int, default=1, help="prints information about a sequence")
    
    args = ap.parse_args()
    
    try:
        fasta_parser = ParserFASTA(args.path)
        if args.sequence:
            k = args.sequence
            print("Description: {}".format(fasta_parser.descr(k)))
            print("Length: {}".format(fasta_parser.len(k)))
            print("Sequence:")
            print(fasta_parser.seq(k))
    except FileNotFoundError:
        print("File '{}' could not be opened.".format(args.path))
    except IndexError:
        print("There are only {} sequences".format(fasta_parser.ns))
    
