#!/usr/bin/env python
# coding: utf-8

# In[1]:


import paramiko
import sys


# In[7]:


from getpass import getpass
passwd = getpass()


# In[6]:


try:
    # Note that the parameters below represent a low-level Python Socket, and 
    # they must be represented as such.
    tp = paramiko.Transport("10.2.2.38", 22)
    
    # Note that while you *can* connect without checking the hostkey, you really
    # shouldn't. Without checking the hostkey, a malicious actor can steal
    # your credentials by impersonating the server.
    tp.connect (username = "pi", password=passwd)
    try:
        sftpClient = paramiko.SFTPClient.from_transport(tp)
        fileCount = 0
        # Proof of concept - List First 10 Files
        for file in sftpClient.listdir():
            print (str(file))
            fileCount = 1 + fileCount
            if 10 == fileCount:
              break
        sftpClient.close()
    except Exception as err:
        print ("SFTP failed due to [" + str(err) + "]")
except paramiko.ssh_exception.AuthenticationException as err:
    print ("Can't connect due to authentication error [" + str(err) + "]")
except Exception as err:
    print ("Can't connect due to other error [" + str(err) + "]")

tp.close()


# In[ ]:





# In[9]:


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("10.2.2.38", username='pi', password=passwd)
ftp = ssh.open_sftp()
file=ftp.file('python/bblais_test.txt', "a")
file.write('This is a test.\n')
file.flush()
ftp.close()
ssh.close()


# In[10]:


get_ipython().run_line_magic('pinfo', 'ftp.put')


# In[11]:


import classy


# In[ ]:




