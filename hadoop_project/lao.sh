#!/usr/bin/env bash
# Upload lao.txt to /holbies/input in HDFS

set -euo pipefail

# Detect Hadoop or HDFS command
if command -v hdfs >/dev/null 2>&1; then
  HDFS_CMD=(hdfs dfs)
elif command -v hadoop >/dev/null 2>&1; then
  HDFS_CMD=(hadoop fs)
else
  echo "Error: Hadoop/HDFS command not found. Make sure Hadoop is installed and in PATH." >&2
  exit 1
fi

# File and destination paths
LOCAL_FILE="lao.txt"
DEST_DIR="/holbies/input"
DEST_PATH="${DEST_DIR}/$(basename "$LOCAL_FILE")"

# Check file existence
if [[ ! -f "$LOCAL_FILE" ]]; then
  echo "Error: File '$LOCAL_FILE' not found in current directory." >&2
  exit 1
fi

echo "Uploading '$LOCAL_FILE' to HDFS directory '$DEST_DIR'..."
"${HDFS_CMD[@]}" -put -f "$LOCAL_FILE" "$DEST_DIR"

echo "Upload complete. Verifying..."
"${HDFS_CMD[@]}" -ls "$DEST_DIR"
