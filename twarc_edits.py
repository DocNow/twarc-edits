import json
import click

from twarc.expansions import ensure_flattened
from twarc.decorators2 import FileSizeProgressBar

@click.command()
@click.argument("infile", type=click.File("r"), default="-")
@click.argument("outfile", type=click.File("w"), default="-")
def edits(infile, outfile):
    """
    Extract edited tweets. 
    """
    for line in infile:
        for tweet in ensure_flattened(json.loads(line)):
            if 'edit_history_tweet_ids' in tweet and len(tweet['edit_history_tweet_ids']) > 1:
                click.echo(json.dumps(tweet), file=outfile, nl=False)
