# yfie -- wrapper for qrcode
#
# (C) jahinzee <jahinzee@outlook.com> 2024

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

__package__ = "yfie"

from qrcode import QRCode, make
from io import StringIO


def print_qr(connection_string, invert):
    qr_code = QRCode()
    qr_code.add_data(connection_string)
    qr_code.print_ascii(invert=invert)


def preview_qr(connection_string):
    image = make(connection_string)
    image.show()


def save_qr(connection_string, file_name):
    image = make(connection_string)
    image.save(file_name)
