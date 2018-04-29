import mistune
import sys
import argparse
import html

class Renderer(mistune.Renderer):
    def header(self, text, level, raw=None):
        return f"{text}<break time=\"{max(4-level,0)}00ms\"/>\n"
    def emphasis(self, text):
        return f"<emphasis level=\"moderate\">{text}</emphasis>"
    def double_emphasis(self, text):
        return f"<emphasis level=\"strong\">{text}</emphasis>"
    def linebreak(self):
        return f"<break time=\"400ms\"/>\n"
    def paragraph(self, text):
        return f"{text}<break time=\"100ms\"/>\n"
    def footnote_ref(self, key, index):
        return key
    def autolink(self, link, is_email=False):
        return ""
    def link(self, link, title, content):
        return content
    def text(self, text):
        return html.escape(text)
    def block_code(self, text):
        return self.text(text)
    def codespan(self, text):
        return self.text(text)

renderer = Renderer()
markdown = mistune.Markdown(renderer=renderer)
out_text = markdown("\n".join(sys.stdin.readlines()))
ssml = f"<speak>{out_text}</speak>"

print(ssml)

def get_ogg(ssml):
    """
    Get the MP3 from google cloud TTS API
    """
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(ssml=ssml)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        name="en-US-Wavenet-F"
        )

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.OGG_OPUS)

    response = client.synthesize_speech(input_text, voice, audio_config)

    # The response's audio_content is binary.
    with open('output.ogg', 'wb') as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.ogg"')

parser = argparse.ArgumentParser()
parser.add_argument("--get_ogg", action='store_true', default=False)
args = parser.parse_args()
if args.get_ogg:
    get_ogg(ssml)
