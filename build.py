#!/usr/bin/env python3

import os,re,subprocess

folder = os.environ.get("SERVER_JAR_DIR", "jars/")

jars = [(f,'-'.join(f.split('-')[0:2])) for f in sorted(os.listdir(folder), key=lambda s: [int(t) if t.isdigit() else t.lower() for t in re.split('(\d+)', s)])[::-1]]

for file,ver in jars:
    print()
    print(f"Building {ver}...")
    subprocess.run(["docker","build","-t",f"mcserver:{ver}","--build-arg",f"server_jar={os.path.join(folder, file)}","."])
    print()
