import json

from twarc_edits import edits
from click.testing import CliRunner

runner = CliRunner()


def test_edits():
    result = runner.invoke(edits, ["test-data/tweets.jsonl"])
    assert result.exit_code == 0
    tweets = [json.loads(line) for line in result.output.splitlines()]
    assert len(tweets) == 1
