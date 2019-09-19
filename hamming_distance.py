import fasta_parser

class HammingError(Exception):
    pass

def hd(bio_seq_a, bio_seq_b):
    seq_a = str(bio_seq_a)
    seq_b = str(bio_seq_b)
    if len(seq_a) != len(seq_b):
        raise HammingError
    else:
        dist = 0
        for i in range(len(seq_a)):
            if seq_a[i] != seq_b[i]:
                dist += 1
        return dist

if __name__ == "__main__":
    parser = fasta_parser.ParserFASTA("ls_orchid.fasta")
    print(hd(parser.seq(1), parser.seq(1)))
    
