from Bio.Seq import Seq
from Bio import Entrez, SeqIO, pairwise2
import time

Entrez.email = "gkbioinfo@gmail.com"

search_term = "Hantaan virus s segment complete"
search_handle = Entrez.esearch(
    db="nucleotide",
    term=search_term,
    retmax=1
)
search_results = Entrez.read(search_handle)
search_handle.close()


seq_id = search_results["IdList"][0]

fetch_handle = Entrez.efetch(
    db="nucleotide",
    id=seq_id,
    rettype="fasta",
    retmode="text"
)
sequence = fetch_handle.read()
fetch_handle.close()
print(sequence[:500])

with open ("hantaan_s.fasta", "w") as h:
    h.write(sequence)

print("Sequence saved !!!")

# now we search and fetch the other kind of hanta virus; sin nombre virus
search_term = "Sin Nombre virus s segment complete"
search_handle = Entrez.esearch(
    db="nucleotide",
    term=search_term,
    retmax=1
)
search_results = Entrez.read(search_handle)
search_handle.close()
# will probably return a sequence id

seq_id = search_results["IdList"][0]
fetch_handle= Entrez.efetch(
    db="nucleotide",
    rettype="fasta",
    retmode="text"
)
sequence = fetch_handle.read()
fetch_handle.close()
print(sequence[:500])

with open("Sin_Nombre_s.fasta", "w") as s:
    s.write(sequence)


