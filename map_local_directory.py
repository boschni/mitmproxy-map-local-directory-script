import os
import argparse
import mimetypes
import urllib

class Replacer:
    def __init__(self, mappings):
        self.mappings = mappings

    def find_mapping(self, flow):
        return next((m for m in self.mappings if flow.request.url.startswith(m[0])), None)

    def request(self, flow):
        mapping = self.find_mapping(flow)
        if mapping is not None:
            flow.request.anticache()
            flow.request.anticomp()

    def response(self, flow):
        mapping = self.find_mapping(flow)
        if mapping is not None:
            path_after_url = remove_prefix(flow.request.url, mapping[0]).strip("/")
            filepath = os.path.join(mapping[1], path_after_url)
            if os.path.isfile(filepath):
                url = urllib.request.pathname2url(filepath)
                mimetype = mimetypes.guess_type(url)[0]
                with open(filepath, "rb") as f:
                    flow.response.content = f.read()
                    flow.response.status_code = 200
                    flow.response.reason = "OK"
                    flow.response.headers["Content-Type"] = mimetype if mimetype is not None else "text/plain; charset=utf-8"

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

def start():
    parser = argparse.ArgumentParser()
    parser.add_argument("--map", nargs="*", type=str, default=[])
    args = parser.parse_args()

    mappings = []
    for i in range(0, len(args.map)):
        if i % 2 == 0:
            mappings.append((args.map[i * 2], args.map[i * 2 + 1]))

    return Replacer(mappings)
