from os import environ

def run(**args):
    print("[*] In environment module")
    return str(environ)

if __name__ == '__main__':
    print(run())