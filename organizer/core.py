from pathlib import Path
import shutil

Documents = [".pdf", ".docx", ".txt", ".md"]
Images = [".png", ".jpeg", ".jpg", ".mov", ".mp4", ".MOV"]
Code = [".py", ".c", ".js", ".html"]
Archives = [".zip", ".tar"]

docs = "docs"
Img = "Img"
CS = "CS"
arch = "Archives"
other = "other"

def read(file):
    a = file.suffix
    return a

def scan(folder):
    Folder = []
    for i in folder.iterdir():
        if i.is_file():
            Folder.append(i)
    return Folder

def org(file):
    if file in Documents:
        return docs
    elif file in Images:
        return Img
    elif file in Code:
        return CS
    elif file in Archives:
        return arch
    else:
        return other

def run(target):
    target = target.resolve()
    if target.exists() == False:
        print("No such File or Directory")
        return 1
    a = target / docs
    b = target / Img
    c = target / CS
    d = target / other
    e = target / arch
    a.mkdir(parents=True, exist_ok=True)
    b.mkdir(parents=True, exist_ok=True)
    c.mkdir(parents=True, exist_ok=True)
    d.mkdir(parents=True, exist_ok=True)
    e.mkdir(parents=True, exist_ok=True)
    Folder = scan(target)
    for i in Folder:
        suf = read(i)
        category = org(suf)
        if category == docs:
            shutil.move(i, a)
        elif category == Img:
            shutil.move(i, b)
        elif category == CS:
            shutil.move(i, c)
        elif category == arch:
            shutil.move(i, e)
        elif category == other:
            shutil.move(i, d)
        else:
            return 1
    return 0
a = Path(input("What Folder should be organized?"))
b = run(a)
if b == 0:
    print("Your files are sorted!")
else:
    print("Something went wrong!")
