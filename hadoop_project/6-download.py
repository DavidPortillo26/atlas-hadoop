#!/usr/bin/python2.7
import subprocess
import os

def download(l):
    """
    Downloads each file in list l from HDFS into /tmp.
    Returns a list of dictionaries describing the result.
    """

    # Detect hdfs or hadoop command (Python 2.7 compatible)
    def cmd_exists(cmd):
        try:
            subprocess.check_output(["which", cmd])
            return True
        except subprocess.CalledProcessError:
            return False

    if cmd_exists("hdfs"):
        HDFS_CMD = ["hdfs", "dfs", "-get"]
    elif cmd_exists("hadoop"):
        HDFS_CMD = ["hadoop", "fs", "-get"]
    else:
        raise RuntimeError("Neither 'hdfs' nor 'hadoop' command found.")

    results = []
    TMP_DIR = "/tmp"

    for src in l:
        filename = os.path.basename(src)
        dest_path = os.path.join(TMP_DIR, filename)

        try:
            # Remove old file if exists (avoid merge conflicts)
            if os.path.exists(dest_path):
                os.remove(dest_path)

            # Download file from HDFS → /tmp/<filename>
            subprocess.check_call(HDFS_CMD + [src, TMP_DIR])

            # success result
            results.append({
                "path": dest_path,
                "result": True,
                "error": "",
                "source_path": src
            })

        except subprocess.CalledProcessError as e:
            # failed result
            results.append({
                "path": dest_path,
                "result": False,
                "error": str(e),
                "source_path": src
            })

    # Print results like assignment output
    for r in results:
        print(r)

    return results
