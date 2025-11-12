#!/usr/bin/env bash
# Display the content of lao.txt from HDFS

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

HDFS_FILE="/holbies/input/lao.txt"

echo "Displaying content of $HDFS_FILE ..."
"${HDFS_CMD[@]}" -cat "$HDFS_FILE"
