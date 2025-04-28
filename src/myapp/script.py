import subprocess

def run():
       subprocess.run(["chainlit" , "run" ,".//src//myapp//chatbot.py" ,"-w"])