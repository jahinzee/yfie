# yfie -- main cli script
#
# (C) jahinzee <jahinzee@outlook.com> 2024

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

__package__ = "yfie"
__description__ = "A command-line app that creates Wi-Fi network connection QR codes."

from qrcode import QRCode
import argparse

from yfie.encoder import encode_connection_string, SUPPORTED_AUTHS
from yfie.generator import print_qr, preview_qr, save_qr


def get_args():

    epilog = "NOTE: WPA2-EAP connections are currently unsupported."

    parser = argparse.ArgumentParser(
        prog=__package__, description=__description__, epilog=epilog
    )
    parser.add_argument(
        "-s", "--ssid", required=True, help="The SSID (name) of the Wi-Fi network."
    )
    parser.add_argument(
        "-a",
        "--auth",
        required=False,
        choices=SUPPORTED_AUTHS,
        help="The authentication method. If unspecified, network is assumed to be unsecured.",
    )
    parser.add_argument(
        "-p",
        "--password",
        required=False,
        help="The network password; required if auth is either WPA or WEP.",
    )
    parser.add_argument(
        "-i", "--hidden", action="store_true", help="Specifies a hidden network."
    )
    parser.add_argument(
        "-v",
        "--invert-ascii",
        action="store_true",
        help="Invert the ASCII output colours.",
    )
    parser.add_argument(
        "-t",
        "--text",
        action="store_true",
        help="Instead of printing ASCII, print only the encoded connection string.",
    )
    parser.add_argument(
        "-r",
        "--preview",
        action="store_true",
        help="Instead of printing ASCII, preview image with default image viewer.",
    )
    parser.add_argument(
        "-o",
        "--output",
        required=False,
        help="Instead of printing ASCII, save image to a target file.",
    )
    return parser.parse_args()


def main():
    args = get_args()
    connection: str

    try:
        connection = encode_connection_string(
            ssid=args.ssid, auth=args.auth, password=args.password, hidden=args.hidden
        )
    except ValueError as err:
        print(f"Encoding error: {err}")
        exit(1)
    except NotImplementedError as err:
        print(f"Encoding error: {err}")
        exit(1)

    if args.text:
        print(connection)
        exit(0)

    if args.preview:
        preview_qr(connection)
        exit(0)

    if args.output is not None:
        save_qr(connection, args.output)
        exit(0)

    print_qr(connection, invert=args.invert_ascii)
    exit(0)


if __name__ == "__main__":
    main()
