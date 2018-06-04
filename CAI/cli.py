import click
from Bio import SeqIO
from Bio.Seq import Seq
from .CAI import CAI

@click.command()
@click.argument("sequence_fasta", type=click.Path(exists=True, dir_okay=False))
@click.argument("reference_fasta", type=click.Path(exists=True, dir_okay=False))
def cli(reference_fasta, sequence_fasta):
    sequence = SeqIO.read(sequence_fasta, "fasta").seq
    reference = [str(x.seq) for x in SeqIO.parse(reference_fasta, "fasta")]
    print(CAI(sequence, sequences=reference))

if __name__ == '__main__':
    cli()
