from Bio.Seq import Seq
from Bio import SeqIO

htnv = SeqIO.read("hantaan_s.fasta", "fasta")
snv = SeqIO.read("Sin_Nombre_s.fasta", "fasta")

# Now we translate to proteins
# dna-mrna-protein
# dna-mrna= transcription, mrna-protein=translation

htnv_protein = htnv.seq.translate()
snv_protein = snv.seq.translate()

print("HTNV nucleocaspid protein:" + str(len(htnv_protein)) + "aa")
print("SNV nucleocaspid protein:" + str(len(snv_protein)) + "aa")

