# twarc-edits

[![Build Status](https://github.com/docnow/twarc-edits/workflows/tests/badge.svg)](https://github.com/DocNow/twarc-edits/actions/workflows/main.yml)

*twarc-edits* adds a new `edits` [twarc] command that lets you filter collected twitter data to find tweets that have been edited. Outputted data is [flattened] since not all tweets in a single response from the Twitter API may contain edited tweets.

## Install

To install you will need to:

    pip3 install twarc-edits

## Use

First you will need to collect some data with [twarc]:

    twarc2 search politics tweets.jsonl

Then you can filter it:

    twarc2 edits tweets.jsonl edited-tweets.jsonl

Or use a pipeline if you only want to keep the edits:

    twarc2 search politics | twarc2 edits - edited-tweets.jsonl

[twarc]: https://github.com/docnow/twarc
[flattened]: https://twarc-project.readthedocs.io/en/latest/twarc2_en_us/#flatten
