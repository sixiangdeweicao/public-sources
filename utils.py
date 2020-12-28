import subprocess

def shell(command):
    proc=subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    result=proc.stdout.read()+proc.stderr.read()
    return  result.decode() # bytes 转 str