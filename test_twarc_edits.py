import json

from twarc_edits import edits
from click.testing import CliRunner

runner = CliRunner()


def test_edits():
    result = runner.invoke(edits, ["test-data/tweets.jsonl"])
    assert result.exit_code == 0, "command worked"
    tweets = [json.loads(line) for line in result.output.splitlines()]
    assert tweets[0]['id'] == '1575590534529556480', "tweet is there"
    assert tweets[0]['author']['username'] == 'TwitterBlue', "tweet is flattened"
