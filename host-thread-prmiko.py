import threading
import paramiko
import subprocess as sb


def main_funtion(ip):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port=22, username='root', password='password')

        stdin, stdout, stderr = ssh.exec_command("sh ~/new.sh")
        output  = stdout.readlines()
        error = stderr.readlines()
        print(output)
        print(ip, ": ", error)

node_list = ['ip1', 'ip2', 'ip3', 'ip4']

threads = []

for ip in node_list:
    thread_nodes = threading.Thread(target=main_funtion, args=(ip,))
    thread_nodes.start()
    threads.append(thread_nodes)

for thread in threads:
    thread.join()
