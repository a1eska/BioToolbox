import argparse
from Bio import PDB

class ParserPDB:
    def __init__(self, filename):
        p = PDB.PDBParser()
        self.__structure = p.get_structure("structure", filename)
        self.__num_models = len(self.__structure)
        self.__num_chains = len(PDB.Selection.unfold_entities(self.__structure, 'C'))
        self.__num_residues = len(PDB.Selection.unfold_entities(self.__structure, 'R'))
        self.__num_atoms = len(PDB.Selection.unfold_entities(self.__structure, 'A'))
        
    def get_model(self, i):
        models = self.__structure.get_models()
        return model[i]
        
    def get_chain(self, model, chain_id):
        return model[chain_id]
    
    def get_residue(self, chain, residue_id):
        return chain[residue_id]
    
    def get_atom(self, residue, atom_id):
        return residue[atom_id]
    
    def get_atom(self, i):
        atoms = list(self.__structure.get_atoms())
        return atoms[i]
    
    def num_models(self):
        return self.__num_models
        
    def num_chains(self):
        return self.__num_chains
        
    def num_residues(self):
        return self.__num_residues
    
    def num_atoms(self):
        return self.__num_atoms
    
    def width(self):
        max_width = 0
        atoms = self.__structure.get_atoms()
        for a in atoms:
            for b in atoms:
                max_width = max(max_width, a - b)
        return max_width
    
    def get_atoms_in_dist(self, atom, dist):
        ans = []
        for a in self.__structure.get_atoms():
            if a - atom <= dist:
                ans.append(a)
        return ans
    
    def get_residues_in_dist(self, atom, dist):
        atoms_in_dist = self.get_atoms_in_dist(atom, dist)
        ans = PDB.Selection.unfold_entities(atoms_in_dist, "R")
        return ans
    
class StructProp:
    pass
    
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="Path to a fasta file.")
    ap.add_argument("-i", "--info", action="store_true", help="prints information about the structure")
    ap.add_argument("-a", "--atoms", nargs=2, help="gives the number of atoms around a given atom")
    ap.add_argument("-r", "--residues", nargs="*", help="gives the number of residues around a given atom")
    
    args = ap.parse_args()
    
    try:
        pdb_parser = ParserPDB(args.path)
        if args.info:
            print("Number of models: {}.".format(pdb_parser.num_models()))
            print("Number of chains: {}.".format(pdb_parser.num_chains()))
            print("Number of residues: {}.".format(pdb_parser.num_residues()))
            print("Number of atoms: {}.".format(pdb_parser.num_atoms()))
            print("Width: {}.".format(pdb_parser.width()))
        if args.atoms:
            atom = int(args.atoms[0])
            dist = float(args.atoms[1])
            print("The following atoms are within distance {} from the atom {}:".format(dist, atom))
            print(pdb_parser.get_atoms_in_dist(pdb_parser.get_atom(atom), dist))
        if args.residues:
            atom = int(args.residues[0])
            dist = float(args.residues[1])
            print("The following residues are within distance {} from the atom {}:".format(dist, atom))
            print(pdb_parser.get_residues_in_dist(pdb_parser.get_atom(atom), dist))
            
    except FileNotFoundError:
        print("File '{}' could not be opened.".format(args.path))
    
    
