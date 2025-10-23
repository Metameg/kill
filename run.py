import subprocess

script_path = "./script.sh"

# Make sure it’s executable
subprocess.run(["chmod", "+x", script_path])

# Run the script
subprocess.run(["bash", script_path], check=True)