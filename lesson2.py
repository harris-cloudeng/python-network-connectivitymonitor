import subprocess
print("checking Google...\n")
result= subprocess.run(["ping","-n","1","1.1.1.1"])
#print("\nFinished")
print(result)