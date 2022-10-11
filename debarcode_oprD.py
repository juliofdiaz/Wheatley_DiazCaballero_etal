from Bio.Seq import Seq
import subprocess
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

fwd_primers = open("fwd_primers.txt","r")
rev_primer = "GTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT"
rev_primer_rc = "AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC"

data = []

# Each primer represents a distinct sample date
for i in fwd_primers:
    id,fwd = i.strip().split()

    # Find forward primer
    temp = subprocess.run(["grep", fwd, "guppy/oprD.fastq"], capture_output=True, text=True)
    reads = temp.stdout.strip().split("\n")
    reads = list(filter(None, reads))

    # Check presence of revere primer
    for i in reads:
        has_rev = "yes" if rev_primer in i else "no"

        data.append([id,i,len(i), has_rev, "fwd"])

    # Find reverse complement of forward primer
    fwd = str( Seq(fwd).reverse_complement() )
    temp = subprocess.run(["grep", fwd, "guppy/oprD.fastq"], capture_output=True, text=True)
    reads_rc = temp.stdout.strip().split("\n")
    reads_rc = list(filter(None, reads_rc))

    # Check presence of reverse primer
    for i in reads_rc:
        has_rev = "yes" if rev_primer_rc in i else "no"
        
        data.append([id,str( Seq(i).reverse_complement() ),len(i),has_rev,"rvs"])
    
# Save as dataframe
df = pd.DataFrame(data, columns=["primer","seq","length","has_rev_prim","fwd_or_rvs"])

# Save as pickle
df.to_pickle("all.pkl")
