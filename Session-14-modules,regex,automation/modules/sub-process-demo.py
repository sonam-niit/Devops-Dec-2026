import subprocess

subprocess.run(["echo","Hello World"])
#capturing Output
result = subprocess.run(["ls"], capture_output=True, text=True)

print("Output", result.stdout)