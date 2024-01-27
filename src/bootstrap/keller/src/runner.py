import runpy
import os
os.chdir("../")
r=runpy.run_path("webXFS_aarch64_linux_experiment.py",run_name="__main__")
# cannot reach native path.
print(type(r),r)
# so it is working, and can be think out of brain IF HAVE EXPERIENCE.
# not running as main. cannot reach the content.
