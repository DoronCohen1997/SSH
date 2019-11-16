import paramiko

def print_is():

    key = paramiko.RSAKey.from_private_key_file("C:/Users/Dafna Cohen/PycharmProjects/doron/rsa_private_key.pem")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("Connecting")
    client.connect(hostname="ec2-52-59-204-217.eu-central-1.compute.amazonaws.com", username="ubuntu", pkey=key)
    print("Connected")
    stdin, stdout, stderr = client.exec_command("cd a \n cd b \n cd c \n cd d \n cat secretFile.txt | grep is \n ")
    print(stdout.read())



    # cat secretFile.txt | grep "is"
    client.close()



print_is()