# Mitmproxy map local directory script
This mitmproxy 0.18+ script will map requests to files on the local file system.

## Example
When running mitmproxy with the following arguments:

```bash
mitmproxy --ignore '^(?!myproject\.localhost)' -s "/path/to/map_local_directory.py /projects/myproject"
```

Requests like `http://myproject.localhost/somedir/somefile.js` will be mapped to `/projects/myproject/somedir/somefile.js`.
Any request that does not match the domain or with a file on the local file system will pass through unchanged.
