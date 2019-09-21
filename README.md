# Bioinformatics toolbox

This project contains solutions to excercises for a course on bioinformatics algorithms at the Faculty of Mathematics and Physics at Charles University.
It implements several basic methods from the field of sequence and structural bioinformatics such as parsing files or assesing similarity of sequences and structures.


## Instalation

The project requires ``biopython``, which can be installed using the following command:
```
pip install biopython
```

To run text the project on your computer it is sufficient to clone the repository:
```
git clone https://github.com/a1eska/BioToolbox.git
```

## Implemented classes and methods

The project implements wrapping classes of parsers for PDB files, FASTA files, and CLUSTAL files.
It also implements function for counting Hamming distance and edit distance of two strings.
The correspoding source files are named accordingly.

The test files for the parsers are provied in the directory ``test_data``.
Every file can be run with several arguments for which the information is provided by using the argument ``--help``.

For example the following can be used to print some information about the 10-th sequence in the FASTA file ``ls_orchid.fasta``:
```
python fasta_parser.py test_data/ls_orchid.fasta -s 10
```
