This project was made by Claire Jensen and Diego Rao for COSC-383 Fall 2022.

Files:
- utils.py: Shared utility functions across multiple forms of steganography
    decoding
- decode_image.py: Code for reading an encoded image
- decode_text.py: Code for reading encoded text
- detect_steg.py: Runner code for detecting LSB encodings
- requirements.txt: pip-readable file of required libraries
- resources.txt: Citations for external resources used in developing this code

To run:
1. Install requirements (`pip install -r requirements.txt`)
2. To decode an image: `python3 decode_image.py <IMAGE_FILENAME>`
3. To decode text: `python3 decode_text.py <IMAGE_FILENAME>`
4. To analyze LSB encodings: `python3 detect_steg.py <IMAGE_FILENAME>
