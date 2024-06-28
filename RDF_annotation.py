#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from Bio import SeqIO

UP = Namespace("http://purl.uniprot.org/core/")
FALDO = Namespace("http://biohackers.net/faldo#")
input_folder = "ESM/input_esm/trajectories_sepfiles/"

# parent sequence (ACE2 RBD) identifier
parent_sequence = "ACE2_RBD_GUPRI"

os.makedirs("rdf_annotations", exist_ok=True)
amino_acids = "ACDEFGHIKLMNPQRSTVWY"

for fasta_file in os.listdir(input_folder):
    if fasta_file.endswith(".fasta") and fasta_file != "mutations.fasta":
        fasta_file_path = os.path.join(input_folder, fasta_file)

        file_name_parts = fasta_file.split(".")[0].split("_")
        amino_acid = file_name_parts[0]
        trajectory_number = file_name_parts[-1]

        #new RDF graph
        g = Graph()

        for record in SeqIO.parse(fasta_file_path, "fasta"):
            sequence = str(record.seq)
            composition_vector = ",".join(str(sequence.count(aa)) for aa in amino_acids)

            # Create a new sequence resource
            sequence_resource = UP[f"{amino_acid}_{trajectory_number}"]
            g.add((sequence_resource, RDF.type, UP.Sequence))
            g.add((sequence_resource, RDF.type, UP.Modified_Sequence))
            g.add((sequence_resource, RDFS.label, Literal(f"{amino_acid} {trajectory_number}")))
            g.add((sequence_resource, UP.sequence, Literal(sequence)))
            g.add((sequence_resource, UP.referred_to_as, UP[f"identifier_{amino_acid}_{trajectory_number}"]))
            g.add((sequence_resource, UP.sequence_length, Literal(len(sequence))))
            g.add((sequence_resource, UP.composition_vector, Literal(composition_vector)))

            # Add the is_missense_mutation_of property
            if trajectory_number == "1":
                g.add((sequence_resource, UP.is_missense_mutation_of, UP[parent_sequence]))
            else:
                parent_trajectory = f"{amino_acid}_{int(trajectory_number) - 1}"
                g.add((sequence_resource, UP.is_missense_mutation_of, UP[parent_trajectory]))

            # Add an annotation for the identifier
            identifier = UP[f"identifier_{amino_acid}_{trajectory_number}"]
            g.add((identifier, RDFS.label, Literal(f"Amino acid trajectory identifier for {amino_acid} {trajectory_number}")))

        output_file = os.path.join("rdf_annotations", f"{amino_acid}_{trajectory_number}.rdf")
        g.serialize(destination=output_file, format="xml")


# In[ ]:




