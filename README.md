# Mitmproxy map local directory script
This mitmproxy 2.0.2+ script will map requests to files on the local file system.

## Example
When running mitmproxy with the following arguments:

```bash
mitmproxy -s "/path/to/map_local_directory.py --map http://site1.com/url/to/statics /projects/site1/statics http://site2.com/public/js /projects/site2/js"
```

Requests like `http://site1.com/url/to/statics/js/somefile.js` will be mapped to `/projects/site1/statics/js/somefile.js` and requests like `http://site2.com/public/js/main.js` will be mapped to `/projects/site2/js/main.js`.
Any request that does not match the url or with a file on the local file system will pass through unchanged.

## Only process requests to site1.com
```bash
mitmproxy --ignore '^(?!site1\.com)' -s "/path/to/map_local_directory.py --map http://site1.com/url/to/statics /projects/site1/statics"
```

## Enabling/disabling the OS-X proxy from the terminal
Command to enable the OS-X proxy on the Wi-Fi interface and set it to localhost:8080:
```bash
sudo networksetup -setwebproxy Wi-Fi localhost 8080 off
```
Command to disable the OS-X proxy on the Wi-Fi interface:
```bash
sudo networksetup -setwebproxystate Wi-Fi off
```
