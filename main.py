import subprocess
path = r"C:\Users\Rishi\Documents\GitHub\PPA1_Rishabh_Patel"
processes = ['WebApp.py', 'CommandLineApp.py']
p1=subprocess.Popen(r'python %s\%s' % (path, processes[0]), shell=True)
p2=subprocess.Popen(r'python %s\%s' % (path, processes[1]), shell=True)
p1.wait()
p2.wait()
