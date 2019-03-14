import qrcode
import sys
import os
import base64


def init_check():
    if 4 != len(sys.argv):
        print("Usage:", sys.argv[0], "input-file output-directory chunk-size")
        sys.exit(1)


init_check()


input_file_name = sys.argv[1]
output_directory = sys.argv[2]
chunk_size = int(sys.argv[3])
input_mode = "rb"

input_file = open(input_file_name, input_mode)

file_index = 0
while True:
    read_bytes = input_file.read(chunk_size)

    if b'' == read_bytes:
        break

    read_bytes = base64.b64encode(read_bytes)

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(read_bytes)
    qr.make(fit=True)

    qr.make_image(fill_color="black", back_color="white")\
        .save(os.path.join(output_directory, str(file_index) + '.png'))

    file_index += 1
