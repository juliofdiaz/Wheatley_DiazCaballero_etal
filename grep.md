Count reads supporting the known ***oprD*** variant

```bash
# Run from ~/all/031143/results/minimap2/ont8
$ ~/bin/bioawk-master/bioawk -c fastx '{print substr($seq, 4965960,15)}' ~/all/031143/results/circlator/pb1/EP22/EP22.fa
CACCACCTGGTCCCT
$ grep -c CACCACCTGGTCCCT /media/data/DATA/ONT8/guppy/*fastq
$ grep -c CACCACCTAGTCCCT /media/data/DATA/ONT8/guppy/*fastq
```
