# yfie -- encoder for wifi details to MECARD-style syntax
#
# (C) jahinzee <jahinzee@outlook.com> 2024

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

__package__ = "yfie"

from io import StringIO

SUPPORTED_AUTHS = ["WEP", "WPA"]


def _escape_literals(string):
    output = string
    chars_to_escape = ["\\", ";", ",", '"', ":"]
    for char in chars_to_escape:
        output = output.replace(char, f"\\{char}")
    return output


def encode_connection_string(
    ssid,
    auth=None,
    hidden=False,
    password=None,
    eap_method=None,
    eap_id=None,
    eap_anon_id=None,
    eap_phase2=None,
):

    # configuration syntax specs sourced from:
    # https://github.com/zxing/zxing/wiki/Barcode-Contents#wi-fi-network-config-android-ios-11

    # TODO: implement WPA2-EAP networks
    if auth == "WPA2-EAP":
        raise NotImplementedError("WPA2-EAP authenticated networks not supported yet.")

    # header
    base = StringIO()
    base.write("WIFI:")

    # SSID
    base.write(f"S:{_escape_literals(ssid)};")

    # hidden network
    if hidden:
        base.write("H:true;")

    # authentication method
    if auth == "nopass":
        auth = None
    if auth is not None:
        valid_auths = ["WEP", "WPA", "WPA2-EAP"]
        if not auth in SUPPORTED_AUTHS:
            raise ValueError(
                f"Invalid authentication type: '{auth}'; must be [{', '.join(valid_auths)}]."
            )
        base.write(f"T:{_escape_literals(auth)};")

        # password (if required)
        if password is None:
            raise ValueError(f"Password cannot be None unless auth is None.")
        base.write(f"P:{_escape_literals(password)};")

    # footer
    base.write(";")
    return base.getvalue()
