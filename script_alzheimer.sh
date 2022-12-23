#!/bin/bash

FILE_NAME=`basename $INPUT_FILE_PATH`
OUTPUT_FILE="$TMP_OUTPUT_DIR/$FILE_NAME"

echo "$INPUT_FILE_PATH"
echo "$FILE_NAME"
mv $INPUT_FILE_PATH /opt/image/class/$FILE_NAME.jpeg
python3 /opt/main.py $OUTPUT_FILE

