import subprocess
for i in str(subprocess.check_output(["git", "log", "--oneline"])).split("\n"):
    print(i)
    
# print(subprocess.run(["git", "add", "."]))
# print(subprocess.run(["git", "commit", "-m", "\"Commitest\""]))