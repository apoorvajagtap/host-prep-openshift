import threading
import paramiko
import subprocess as sb


def main_funtion(ip):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port=22, username='root', password='redhat')

        stdin, stdout, stderr = ssh.exec_command("sh ~/new.sh")
        output  = stdout.readlines()
        error = stderr.readlines()
        print(output)
        print(ip, ": ", error)

node_list = ['10.74.254.196', '10.74.254.155', '10.74.253.55', '10.74.255.94']

threads = []

for ip in node_list:
    thread_nodes = threading.Thread(target=main_funtion, args=(ip,))
    thread_nodes.start()
    threads.append(thread_nodes)

for thread in threads:
    thread.join()