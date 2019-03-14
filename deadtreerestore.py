import sys
import base64
from pyzbar import pyzbar
import cv2


if 3 > len(sys.argv):
    print('Usage:', sys.argv[0], 'output-file input-file-1 [input-file-2 [input-file-3 ...]]')
    sys.exit(1)

output_file_path = sys.argv[1]
decode_image_paths = sys.argv[slice(2, len(sys.argv))]

output_file = open(output_file_path, 'w+b')

for input_file in decode_image_paths:
    input_image = pyzbar.decode(cv2.imread(input_file))

    for code in input_image:
        data = code.data.decode('utf-8')
        # print("{}: Found {}".format(input_file, data))
        data = base64.b64decode(data)
        output_file.write(bytes(data))
