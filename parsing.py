import sys

'''
stop_codon = ["TAA", "TAG", "TGA"] 
start_codon = ["TAG"] 
'''

stop_codon = ["TAA", "TAG", "TGA"]
start_codon = ["TAG"]

codons: {
    "Phe": ["TTT", "TTC"],
    "Leu": ["TTA", "TTG", "CTT", "CTC", "CTA", "CTG"],
    "lle": ["ATT", "ATC", "ATA"],
    "Met": ["ATG"]
    "Val": ["GTT", "GTC", "GTA", "GTG"],
    "Ser": ["TCT", "TCC", "TCA", "TCG"],
    "Pro": ["CCT", "CCC", "CCA", "CCG"],
    "Thr": ["ACT", "ACC", "ACA", "ACG"],
    "Ala": ["GCT", "GCC", "GCA", "GCG"],
    "Tyr": ["TAT", "TAC"],
    "His": ["CAT", "CAC"],
    "Gin": ["CAA", "CAG"],
    "Asn": [""]
}

def findAmino(codon):
    for key in codons:
        for value in key:
            if value == codon:
                return key

file = ""
with open(file) as curr:
    # parse "landing strip"
    landing_strip = "TCTATA"
    landing_strip_input = curr.readline()
    if landing_strip != landing_strip_input:
        print("error: input genome is not correct")
        sys.exit(1)
    0start_codon = "TAC"



