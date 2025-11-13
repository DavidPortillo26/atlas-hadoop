#!/usr/bin/python2.7
import subprocess

def createdir(l):
    """
    Creates each directory path in the list l inside HDFS.
    Returns a dict for each path with { 'path': ..., 'result': True/False }.
    """

    # Try to detect hdfs or hadoop command
    # Python 2.7 doesn't support shutil.which
    def cmd_exists(cmd):
        try:
            subprocess.check_output(["which", cmd])
            return True
        except subprocess.CalledProcessError:
            return False

    if cmd_exists("hdfs"):
        HDFS_CMD = ["hdfs", "dfs", "-mkdir", "-p"]
    elif cmd_exists("hadoop"):
        HDFS_CMD = ["hadoop", "fs", "-mkdir", "-p"]
    else:
        raise RuntimeError("Neither 'hdfs' nor 'hadoop' command found in PATH.")

    results = []

    for path in l:
        try:
            # Create directory path on HDFS
            subprocess.check_call(HDFS_CMD + [path])
            results.append({"path": path, "result": True})
        except subprocess.CalledProcessError:
            results.append({"path": path, "result": False})

    # Print results exactly like the provided example
    for r in results:
        print(r)

    return results