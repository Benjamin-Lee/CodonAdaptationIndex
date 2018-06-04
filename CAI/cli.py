import click
from Bio import SeqIO
from Bio.Seq import Seq
from .CAI import CAI

@click.command()
@click.argument("sequence_fasta", type=click.Path(exists=True, dir_okay=False))
@click.argument("reference_fasta", type=click.Path(exists=True, dir_okay=False))
@click.option("-g", "--genetic-code", type=int, default=11, help="The genetic code to use. Defaults to 11.")
def cli(reference_fasta, sequence_fasta, genetic_code):
    sequence = SeqIO.read(sequence_fasta, "fasta").seq
    reference = [str(x.seq) for x in SeqIO.parse(reference_fasta, "fasta")]
    print(CAI(sequence, reference=reference, genetic_code=genetic_code))

if __name__ == '__main__':
    cli()
