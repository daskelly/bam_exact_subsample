# Subsampling an exact number of reads from a BAM file at random
Utility for randomly sampling an exact number of reads from a BAM file

usage: bam_exact_subsample.py [-h] [--seed N] infile.bam outfile.bam n_reads

positional arguments:
  infile.bam
  outfile.bam
  n_reads

optional arguments:
  -h, --help  show this help message and exit
  --seed N    Seed for random read selection
