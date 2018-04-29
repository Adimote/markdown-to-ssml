# Markdown to SSML converter

This is a super simple script to generate **SSML** from markdown. It can also optionally generate an `.ogg` audio file from the SSML it generates.

An example SSML parser is the [google cloud text-to-speech API](https://cloud.google.com/text-to-speech/)

## Installation

just run `pip install -r requirements.txt` to install the dependencies.

## Running

When you run the script, it reads *STD-in* to it's end, then prints the output to *STD-out*.

An example usage would be to run `python convert.py < README.md`

### With the Google text-to-speech API

You can use the google text-to-speech API to generate an `.ogg` audio file with the `--get_ogg` flag.

You must set up your machine to have an API key for Google text-to-speech.

To do this you must [create a project in the google cloud dashboard](https://console.cloud.google.com/projectcreate), if you haven't already, then [create a new 'service account' credential](https://console.cloud.google.com/apis/credentials) of the type 'App Engine default service account' for the text-to-speech API, download it as a JSON file, then set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to be the path of the JSON file.
