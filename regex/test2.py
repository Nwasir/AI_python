import subprocess
import os
# subprocess.run(["date"])
# subprocess.run(['sleep', '2'])
# result = subprocess.run(["ls", "this_file_does_not_exist"])
# print(result.returncode)

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)