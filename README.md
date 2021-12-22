# Subsampling an exact number of reads from a BAM file at random
Utility for randomly sampling an exact number of reads from a BAM file

Usage instructions:
```
$ singularity pull docker://quay.io/biocontainers/pysam:0.17.0--py36h61e5637_0
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
singularity run pysam_0.17.0--py36h61e5637_0.sif python bam_exact_subsample.py supermini.bam supermini_10.bam 10
```
