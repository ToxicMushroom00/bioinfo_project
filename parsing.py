import sys
import itertools

# ! make sure to make all codons uppercase when comparing!
codons = {
    # "start": ["AUG"], #no start codon in the fasta file?
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
def find_amino(codon):
    for key in codons:
        for value in codons.get(key):
            if value == codon:
                return key


# I use this method below to help group the input strings into 3s
def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


start_count = 0
carrot_count = 0
file = "NC_005363_HEG_NT.fasta"
# file = "test.fasta"
codon_parsed = []
with open(file) as curr:
    carrot_line = ''
    for line in curr.readlines():
        # look for carrot ">" line
        if line[0] == '>':
            # if found ">" line, save it and skip
            carrot_line = line.replace("\n", "")
            carrot_count += 1
            continue
        else:  # now we're working with the gene line!
            line = line.upper()

            # # look for start codon
            # # if line[:3] == "lol": # using test data
            # if line[:3] == ''.join(codons["start"]):  # using actual data
            #     start_count += 1
            #     # print(line[:3])
            # # filter start codon out
            # # filtered_line = line[3:]
            filtered_line = line

            # print(filtered_line)
            # use filtered_line to perform analysis from here on out
            codon_parsed.append(carrot_line)
            for chunk in grouper(filtered_line, 3, ''):
                codon_parsed.append(''.join(chunk))


codon_count = {}
for codon in codon_parsed:
    result = find_amino(codon)
    if result in codon_count:
        codon_count[result] += 1
    else:
        codon_count[result] = 1

print(start_count)
print(carrot_count)
print(codon_count)

