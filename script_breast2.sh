FILE_NAME=`basename $INPUT_FILE_PATH`
OUTPUT_FILE="$TMP_OUTPUT_DIR/$FILE_NAME"

python3 /opt/graph.py --input $INPUT_FILE_PATH

zip "$FILE_NAME".zip picture1.png picture2.png picture3.png
mv "$FILE_NAME".zip "$OUTPUT_FILE".zip
