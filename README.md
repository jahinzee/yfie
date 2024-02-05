# yfie

A command-line app that creates Wi-Fi network connection QR codes.

By default, the app will output the QR code as ASCII text to the terminal, but you can also export to an image, or simply get the unconverted connection code (if you need that for whatever reason).

**NOTE:** The app currently cannot generate codes for WPA2-EAP networks. This is a planned feature.

## Installation

Use either `pipx` (recommended) or `pip`.

```sh
pipx install git+https://github.com/jahinzee/wifiqr.git  
```


## Usage

```
usage: yfie [-h] -s SSID [-a {WEP,WPA}] [-p PASSWORD] [-i] [-v] [-t] [-r]
            [-o OUTPUT]

Generate and save Wi-Fi network connection QR codes.

options:
  -h, --help            show this help message and exit
  -s SSID, --ssid SSID  The SSID (name) of the Wi-Fi network.
  -a {WEP,WPA}, --auth {WEP,WPA}
                        The authentication method. If unspecified, network is
                        assumed to be unsecured.
  -p PASSWORD, --password PASSWORD
                        The network password; required if auth is either WPA
                        or WEP.
  -i, --hidden          Specifies a hidden network.
  -v, --invert-ascii    Invert the ASCII output colours.
  -t, --text            Instead of printing ASCII, print only the encoded
                        connection string.
  -r, --preview         Instead of printing ASCII, preview image with default
                        image viewer.
  -o OUTPUT, --output OUTPUT
                        Instead of printing ASCII, save image to a target
                        file.

NOTE: WPA2-EAP connections are currently unsupported.
```