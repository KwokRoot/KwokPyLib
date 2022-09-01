import paramiko


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.199.91', 22, 'root', '123456')

stdin, stdout, stderr = client.exec_command("source /etc/profile && jps -l")

data = stdout.read()
if len(data) > 0:

    # print("=" * 36)
    # # 输出 stdout 流
    # print(data.decode('utf-8').strip())
    # print("=" * 36)

    ps_list = str(data.decode('utf-8').strip()).split("\n")
    for ps in ps_list:
        pid = ps.split()[0]
        server = ps.split()[1]
        print(">>> pid: {}, server: {}".format(pid, server))


err = stderr.read()
if len(err) > 0:
    # 输出 stderr 流
    print(err.decode('utf-8').strip())


client.close()

