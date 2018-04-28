# Markdown to SSML converter

This is a super simple script to generate **SSML** from markdown.

An example SSML parser is the [google cloud text-to-speech API](https://cloud.google.com/text-to-speech/)

## Installation

just run `pip install -r requirements.txt` to install the dependencies.

## Running

When you run the script, it reads STD-in to it's end, then prints the output to STD-out.

An example usage would be to run `python convert.py < README.md`
