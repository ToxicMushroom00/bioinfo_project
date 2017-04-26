import itertools

# ! make sure to make all codons uppercase when comparing!
# if you use parse_fasta(), it will return an array with all capitalized (read more below)
CODON_DICT = {
    # "start": [""], # no start codon in the fasta file!
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
    for key in CODON_DICT:
        for value in CODON_DICT.get(key):
            if value == codon:
                return key


# I use this method below to help group the INPUT DNA into 3s (perfect codon format)
def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


# parses fasta file into an array with the pattern
# [ ">____", "codon", "codon", "codon" ... ">____", "codon", "codon", "codon" ]
def parse_fasta(file):
    return_me = []
    with open(file) as INPUT:
        for line in INPUT.readlines():
            if line[0] == '>':  # we found carrot ">" line!
                return_me.append(line.replace("\n", ""))  # for some reason /n get included, lets take that out
                continue  # nothing else to do with current INPUT line, so let go to the next INPUT line
            else:  # we found the line with the DNAs!
                line = line.upper()  # our reference DNA in the dict above is all uppercase, so lets make it the same
                for chunk in grouper(line, 3, ''):
                    return_me.append(''.join(chunk))
    return return_me


# IMPORTANT!: this counts codons for the WHOLE fasta file
def count_codons(codons):
    return_me = {}
    for codon in codons:
        result = find_amino(codon)
        if result in return_me:
            return_me[result] += 1
        else:
            return_me[result] = 1  # this adds both the key and value into return_me dict
    return return_me


file = "NC_005363_HEG_NT.fasta"
print(count_codons(parse_fasta(file)))
