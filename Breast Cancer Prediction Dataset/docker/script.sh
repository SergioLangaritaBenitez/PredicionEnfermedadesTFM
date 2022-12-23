FILE_NAME=`basename $INPUT_FILE_PATH`
OUTPUT_FILE="$TMP_OUTPUT_DIR/$FILE_NAME".txt
echo "$OUTPUT_FILE"
python3 /opt/main.py --input "$INPUT_FILE_PATH" --output "$OUTPUT_FILE"

