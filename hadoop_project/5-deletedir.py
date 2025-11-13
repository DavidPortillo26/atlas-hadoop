#!/usr/bin/python2.7
import subprocess

def deletedir(l):
    """
    Deletes each directoy path in the list l from HDFS.
    Returns a dict for each path with {'path': path, 'result': True/False}.
    """

    # Python2.7-compatible command detection
    def cmd_exists(cmd):
        try:
            subprocess.check_output(['which', cmd])
            return True
        except subprocess.CalledProcessError:
            return False
        
    # Choose hdfs or hadoop command
    if cmd_exists("hdfs"):
        BASE_CMD = ["hdfs", "dfs", "-rm", "-r", "-skipTrash"]
    elif cmd_exists("hadoop"):
        BASE_CMD = ["hadoop", "fs", "-rm", "-r", "-skipTrash"]
    else:
        raise RuntimeError("Neither 'hdfs' nor 'hadoop' command found in PATH.")
    
    results = []

    # Important: delete deepest directory first (reverese order)
    for path in reversed(l):
        cmd = BASE_CMD + [path]
        try:
            subprocess.check_call(BASE_CMD + [path])
            results.append({"path": path, "result": True})
        except subprocess.CalledProcessError:
            # directory might not exist → failure
            results.append({"path": path, "result": False})
    
    # Print results exactly like expected output
    for r in results:
        print(r)

    return results
