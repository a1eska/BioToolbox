from Bio import PDB

class ParserPDB:
    def __init__(self, filename):
        p = PDB.PDBParser()
        self.__structure = p.get_structure("structure", filename)
        
        # number of models in the structure
        self.__num_models = len(self.__structure)
        
        # number of chains in the structure
        self.__num_chains = len(PDB.Selection.unfold_entities(self.__structure, 'C'))
        
        # number of residues in the structure
        self.__num_residues = len(PDB.Selection.unfold_entities(self.__structure, 'R'))
        
        # number of chains in the structure
        self.__num_atoms = len(PDB.Selection.unfold_entities(self.__structure, 'A'))
        
    # returns object ith representing model in structure or an IndexError
    def get_model(self, model_id):
        return self.__structure[model_id]
        
    def get_chain(self, model, chain_id):
        return model[chain_id]
    
    def get_residue(self, chain, residue_id):
        return chain[residue_id]
    
    def get_atom(self, residue, atom_id):
        return residue[atom_id]
    
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
    
if __name__ == "__main__":
    parser = ParserPDB("2mpj.pdb")
    model = parser.get_model(0)
    print(parser.num_models())
    print(parser.num_chains())
    print(parser.num_residues())
    print(parser.num_atoms())
    print(parser.width())
    atoms = list(model.get_atoms())
    print(parser.get_atoms_in_dist(atoms[0], 1))
    print(parser.get_residues_in_dist(atoms[0], 1))
    
