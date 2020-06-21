import os
import shutil
from pathlib import Path
import subprocess

from conf import branches

source_repo = "https://github.com/tokyoquantopian/quantopian-doc-ja.git"
home_dir = Path.cwd()
repo_dir = Path("quantopian-doc-ja")
makefile = repo_dir / "Makefile"
source_dir = repo_dir / "source"

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

shutil.move(str(makefile.resolve()), str(home_dir.resolve()))
shutil.move(str(source_dir.resolve()), str(home_dir.resolve()))
shutil.rmtree(str(home_dir / "quantopian-doc-ja"))
