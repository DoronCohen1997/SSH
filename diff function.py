import paramiko

def isDiff(firstFile, secondFile):

    key = paramiko.RSAKey.from_private_key_file("C:/Users/Dafna Cohen/PycharmProjects/doron/rsa_private_key.pem")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("Connecting")
    client.connect(hostname="ec2-52-59-204-217.eu-central-1.compute.amazonaws.com", username="ubuntu", pkey=key)
    print("Connected")
    #stdin, stdout, stderr = client.exec_command(f"cd {firstFile} \n pwd")
    stdin, stdout, stderr = client.exec_command(f"diff -q firstFile/{firstFile} secondFile/secondFile/{secondFile}")
    DIFFERENT=str(stdout.read())
    if "differ"in DIFFERENT:
        print(True)
    else:
        print(False)





    # cat secretFile.txt | grep "is"
    client.close()



isDiff("firstFile.txt", "secondFile.txt")