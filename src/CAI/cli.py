import click
from Bio import SeqIO
from Bio.Seq import Seq
from .CAI import CAI


@click.command()
@click.option(
    "-s",
    "--sequence",
    type=click.Path(exists=True, dir_okay=False),
    help="The sequence to calculate the CAI for.",
    required=True,
)
@click.option(
    "-r",
    "--reference",
    type=click.Path(exists=True, dir_okay=False),
    help="The reference sequences to calculate CAI against.",
    required=True,
)
@click.option(
    "-g",
    "--genetic-code",
    type=int,
    default=11,
    help="The genetic code to use. Defaults to 11.",
)
def cli(reference, sequence, genetic_code):
    sequence = SeqIO.read(sequence, "fasta").seq
    reference = [str(x.seq) for x in SeqIO.parse(reference, "fasta")]
    print(CAI(sequence, reference=reference, genetic_code=genetic_code))


if __name__ == "__main__":
    cli()
