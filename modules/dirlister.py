from os import listdir

def run(**rags):
    print("[*] In dirlister module")
    files = listdir(".")
    
    return files

if __name__ == '__main__':
    print(run())

