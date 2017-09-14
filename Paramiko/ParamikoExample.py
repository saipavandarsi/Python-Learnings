import sys, Paramiko

if len(sys.argv) <5:
    print "Args are missing"
    sys.exit(1)


hostname = sys.argv[1]
password = sys.argv[2]
source = sys.argv[3]
dest = sys.argv[4]

username = "root"
port = 22

try:
    client = Paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(Paramiko.WarningPolicy())

    client.connect(hostname, port=port, username=username,password=password)

    stdin, stdout, stderr = client.exec_command(command)
    print stdout.read(),

finally:
    client.close()



try:
    t = Paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = Paramiko.SFTPClient.from_transport(t)
    sftp.get(source, dest)



