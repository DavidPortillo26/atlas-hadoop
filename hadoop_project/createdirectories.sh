#!/usr/bin/env bash
# Creates /holbies and /holbies/input directories in HDFS

# Exit immediately if a command fails
set -e

# Use hdfs dfs if available, otherwise fall back to hadoop fs
if command -v hdfs >/dev/null 2>&1; then
    CMD="hdfs dfs"
elif command -v hadoop >/dev/null 2>&1; then
    CMD="hadoop fs"
else
    echo "Error: hdfs or hadoop command not found. Please check your Hadoop installation."
    exit 1
fi

# Create directories (no error if they already exist)
$CMD -mkdir -p /holbies/input

# Print confirmation
echo "Successfully created /holbies and /holbies/input in HDFS."
