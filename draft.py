import os
import shutil
from pathlib import Path
import subprocess

from conf import branches

source_repo = "https://github.com/tokyoquantopian/quantopian-doc-ja.git"
home_dir = Path.cwd()
repo_dir = Path("quantopian-doc-ja")
makefile = repo_dir / "Makefile"
makefile_prev = home_dir / "Makefile"
source_dir = repo_dir / "source"
source_dir_prev = home_dir / "source"

subprocess.run(["git", "clone", source_repo])
os.chdir(repo_dir)

for branch in branches:
    subprocess.run(["git", "fetch", "origin", branch])
for branch in branches:
    subprocess.run(["git", "checkout", branch])

subprocess.run(["git", "checkout", "master"])

for branch in branches:
    subprocess.run(["git", "checkout", branch, branches[branch]])

os.chdir(home_dir)

if makefile_prev.exists():
    os.remove(makefile_prev)

if source_dir_prev.exists():
    shutil.rmtree(str(source_dir_prev))

shutil.move(str(makefile.resolve()), str(makefile_prev.resolve()))
shutil.move(str(source_dir.resolve()), str(source_dir_prev.resolve()))
shutil.rmtree(str(repo_dir.resolve()))
