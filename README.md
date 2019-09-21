# Bioinformatics toolbox

This project contains solutions to excercises for a course on bioinformatics algorithms at the Faculty of Mathematics and Physics at Charles University.
It implements several basic methods from the field of sequence and structural bioinformatics such as parsing files or assesing similarity of sequences and structures.


## Instalation

The project requires ``biopython``, which can be installed using the following command:
```
pip install biopython
```

To run the project on your computer it is sufficient to clone the repository:
```
git clone https://github.com/a1eska/BioToolbox.git
```

## Implemented classes and methods

The project implements wrapping classes of parsers for PDB files, FASTA files, and CLUSTAL files.
It also implements function for counting Hamming distance and edit distance of two strings.
The correspoding source files are named accordingly.

## Testing

The test files for the parsers are provied in the directory ``test_data``.
Every file can be run with several arguments for which the information is provided by using the argument ``--help``.
Several example follow.

### FASTA parser

The following can be used to print some information about the 10-th sequence in the FASTA file ``ls_orchid.fasta``:
```
python fasta_parser.py test_data/ls_orchid.fasta -s 10
```

### PDB parser

The following prints information about the structure in the PDB file ``2mpj.pdb``:
```
python pdb_parser.py test_data/ls_orchid.fasta -i
```


This command gives the list of atoms in distance ``2`` from atom number ``10``:
```
python pdb_parser.py test_data/ls_orchid.fasta -a 10 2
```

### CLUSTAL parser

This prints sum of pair of the multiple sequence alignment and the list of conservation-like scores of the positions:
```
python pdb_parser.py test_data/p53_mafft_clustal.txt
```
