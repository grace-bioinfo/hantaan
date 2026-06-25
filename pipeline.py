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
print(search_results["IdList"])

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
