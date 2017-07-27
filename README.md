# Mitmproxy map local directory script
This mitmproxy 2.0.2+ script will map requests to files on the local file system.

## Example
When running mitmproxy with the following arguments:

```bash
mitmproxy --ignore '^(?!myproject\.localhost)' -s "/path/to/map_local_directory.py --path /url/to/statics/directory --src /projects/myproject/statics"
```

Requests like `http://myproject.localhost/url/to/statics/directory/js/somefile.js` will be mapped to `/projects/myproject/statics/js/somefile.js`.
Any request that does not match the domain or with a file on the local file system will pass through unchanged.
