# Markdown to SSML converter

This is a super simple script to generate **SSML** from markdown.

An example SSML parser is the [google cloud text-to-speech API](https://cloud.google.com/text-to-speech/)

## Installation

just run `pip install -r requirements.txt` to install the dependencies.

## Running

When you run the script, it reads STD-in to it's end, then prints the output to STD-out.

An example usage would be to run `python convert.py < README.md`

### With the Google TTS API

You can use the google TTS API to generate an `.ogg` audio file with the `--get_ogg` flag.

You must set up your machine to have an API key for Google text-to-speech.

To do this you must [create a project in the google cloud dashboard](https://console.cloud.google.com/projectcreate), if you haven't already, then [create a new 'service account' credential](https://console.cloud.google.com/apis/credentials) for the tex-to-speech API, download it as a JSON file, then set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to be the path of the JSON file.
