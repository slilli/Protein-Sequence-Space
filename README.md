# **Protein Sequence Space** 

In this master's thesis project we mapped the protein sequence space of the ACE2 receptor binding domain of the SARS-CoV-2 virus. We applied structure predction algorithms to predict the three-dimensional structure of protein variants. The code provided here provides tools to analyze the output of the structure prediction algorithms.

The full results can be found on [OSF](https://doi.org/10.17605/OSF.IO/PMJ9X)

## Files

+ **input/** \
 Contains the input sequence (ACE2 RBD) in amino acid and nucleotide format
+ **reference/** \
  Contains the reference structure file in PDB format
+ **Contact Matrix.ipynb** \
  Calculates and analyses contact matrices from pdb files
+ **ESMFold_analysis.ipynb** \
  Analyses output from ESMFold
+ **RDF_annotation.py** \
  Annotates sequence variants in RDF format
+ **SARS_COV2_homopolymer_generator.ipynb** \
  Generates sequence variants along trajectories
+ **colabfold_analysis.ipynb** \
  Analyzes ColabFold  output 
+ **variant_analysis.ipynb** \
  Analyzes genetic constraint on the sequences and permutated sequences.

