import mistune
import sys

class Renderer(mistune.Renderer):
    def header(self,text,level,raw=None):
        return f"{text}<break time=\"{max(4-level,0)}00ms\"/>\n"
    def emphasis(self,text):
        return f"<emphasis level=\"moderate\">{text}</emphasis>"
    def double_emphasis(self,text):
        return f"<emphasis level=\"strong\">{text}</emphasis>"
    def linebreak(self):
        return f"<break time=\"400ms\"/>\n"
    def paragraph(self, text):
        return f"{text}<break time=\"100ms\"/>\n"

renderer = Renderer()
markdown = mistune.Markdown(renderer=renderer)
out_text = markdown("\n".join(sys.stdin.readlines()))

print(f"<speak>{out_text}</speak>")
