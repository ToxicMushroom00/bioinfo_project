import sys

# ! make sure to make all codons uppercase when comparing!
codons = {
    "start": ["ATG"],
    "stop": ["TAA", "TAG", "TGA"],
    "Phe": ["TTT", "TTC"],
    "Leu": ["TTA", "TTG", "CTT", "CTC", "CTA", "CTG"],
    "lle": ["ATT", "ATC", "ATA"],
    "Met": ["ATG"],
    "Val": ["GTT", "GTC", "GTA", "GTG"],
    "Ser": ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"],
    "Pro": ["CCT", "CCC", "CCA", "CCG"],
    "Thr": ["ACT", "ACC", "ACA", "ACG"],
    "Ala": ["GCT", "GCC", "GCA", "GCG"],
    "Tyr": ["TAT", "TAC"],
    "His": ["CAT", "CAC"],
    "Gin": ["CAA", "CAG"],
    "Asn": ["AAT", "AAC"],
    "Lys": ["AAA", "AAG"],
    "Asp": ["GAT", "GAC"],
    "Glu": ["GAA", "GAG"],
    "Cys": ["TGT", "TGC"],
    "Trp": ["TGG"],
    "Arg": ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"],
    "Gly": ["GGT", "GGC", "GGA", "GGG"]
}

# Find the Amino Acid that the given codon codes for
def findAmino(codon):
    for key in codons:
        for value in codons.get(key):
            if value == codon:
                print(key)

# file = "NC_005363_HEG_NT.fasta"
file = "test.fasta"
with open(file) as curr:
    for line in curr.readlines():
        # look for carrot ">" line
        if line[0] == '>':
            # if found ">" line, skip
            continue
        else:  # now we're working with the gene line!
            # look for start codon
            if line[:3] == "lol":
                print("found start codon!")
                print(line[:3])
            # filter start codon out
            filtered_line = line[3:]




