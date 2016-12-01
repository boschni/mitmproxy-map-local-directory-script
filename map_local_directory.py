from os.path import isfile
import argparse
import mimetypes
import urllib

class Replacer:
    def __init__(self, src):
        self.src = src

    def request(self, flow):
        flow.request.anticache()
        flow.request.anticomp()

    def response(self, flow):
        filepath = self.src + flow.request.path
        if isfile(filepath):
            url = urllib.pathname2url(filepath)
            mimetype = mimetypes.guess_type(url)[0]
            with open(filepath) as f:
                flow.response.content = f.read()
                flow.response.status_code = 200
                flow.response.reason = 'OK'
                flow.response.headers['Content-Type'] = mimetype if mimetype is not None else 'text/plain; charset=utf-8'

def start():
    parser = argparse.ArgumentParser()
    parser.add_argument('src', type=str)
    args = parser.parse_args()
    return Replacer(args.src)
