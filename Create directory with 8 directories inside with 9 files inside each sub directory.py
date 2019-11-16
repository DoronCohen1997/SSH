import paramiko

def dirs_fiIes(full_name , dir_name , file_name):

    key = paramiko.RSAKey.from_private_key_file("C:/Users/Dafna Cohen/PycharmProjects/doron/rsa_private_key.pem")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("Connecting")
    client.connect(hostname="ec2-52-59-204-217.eu-central-1.compute.amazonaws.com", username="ubuntu", pkey=key)
    print("Connected")
    stdin, stdout, stderr = client.exec_command(f"mkdir {full_name}")
    stdin, stdout, stderr = client.exec_command(f"cd {full_name} \n pwd")
    print(stdout.read())
    for i in range(1,9):
        stdin, stdout, stderr = client.exec_command(f"cd {full_name} \n mkdir {dir_name}" +str(i))
        print(stdout.read())
        for j in range(1,10):
            stdin, stdout, stderr = client.exec_command(f"cd {full_name} \n  cd {dir_name + str(i)}  \n touch {file_name}" +str(j))
        print(stdout.read())




    print(stdout.read())
    client.close()



dirs_fiIes("doroncohen7" , "dir_doron" , "file_doron")