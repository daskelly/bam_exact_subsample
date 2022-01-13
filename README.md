# Utilities or sampling from BAM files

This repository contains several utilities useful for sampling from BAM files,
with a main focus on 10X CellRanger BAMs.

In order to run these scripts we need a container that has python and the `pysam` package:
```
$ singularity pull docker://quay.io/biocontainers/pysam:0.17.0--py36h61e5637_0
```

## `10x_bam_split_CB.py`

This is a small utility for dividing a 10X CellRanger BAM into thousands of
"mini" BAMs, one for each cell barcode.

Usage instructions for this script:
```
$ singularity run pysam_0.17.0--py36h61e5637_0.sif python 10x_bam_split_CB.py -h
usage: 10x_bam_split_CB.py [-h] [--verbose]
                           infile.bam barcodes.tsv.gz /path/to/outdir

positional arguments:
  infile.bam
  barcodes.tsv.gz
  /path/to/outdir

optional arguments:
  -h, --help       show this help message and exit
  --verbose
```


## `bam_exact_subsample.py`

This is a small utility for randomly sampling an exact number of reads from a BAM file.

Usage instructions for this script:
```
$ singularity run pysam_0.17.0--py36h61e5637_0.sif python bam_exact_subsample.py -h
usage: bam_exact_subsample.py [-h] [--seed N] infile.bam outfile.bam n_reads

positional arguments:
  infile.bam
  outfile.bam
  n_reads

optional arguments:
  -h, --help  show this help message and exit
  --seed N    Seed for random read selection
```

Sample usage of this script. Subsample a random 10 reads from a very small
BAM (only 26 reads):
```
$ singularity run pysam_0.17.0--py36h61e5637_0.sif \
    python bam_exact_subsample.py \
    supermini.bam supermini_10.bam 10
```
