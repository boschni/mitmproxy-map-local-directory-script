import os
import argparse
import mimetypes
import urllib

class Replacer:
    def __init__(self, src, path):
        self.src = src
        self.path = path

    def request(self, flow):
        flow.request.anticache()
        flow.request.anticomp()

    def response(self, flow):
        relative_filepath = remove_prefix(flow.request.path.strip("/"), self.path.strip("/")).strip("/")
        filepath = os.path.join(self.src, relative_filepath)
        if os.path.isfile(filepath):
            url = urllib.request.pathname2url(filepath)
            mimetype = mimetypes.guess_type(url)[0]
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                flow.response.content = f.read().encode("utf-8")
                flow.response.status_code = 200
                flow.response.reason = "OK"
                flow.response.headers["Content-Type"] = mimetype if mimetype is not None else "text/plain; charset=utf-8"

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

def start():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, default="")
    parser.add_argument("--src", type=str, default=".")
    args = parser.parse_args()
    return Replacer(args.src, args.path)
