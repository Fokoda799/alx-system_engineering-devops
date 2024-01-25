# Command line for the win

**CMD CHALLENGE** is an exciting game designed to enhance your Bash skills. 🎮 It's a series of command-line challenges, each more complex than the last, offering a fantastic opportunity to sharpen your command-line prowess! 💪

![CMD Challenge](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/324/06AChAO.png)

## SFTP (Introduction)

FTP, once a popular but now deprecated File Transfer Protocol 🚌, has been succeeded by **SFTP** (Secure File Transfer Protocol). Integrated into SSH, it provides a secure alternative for file transfers.

### How to Connect with SFTP

By default, SFTP leverages SSH for authentication and secure connections. For enhanced security, consider setting up SSH keys following [this guide][1].

Check SSH access with:
```bash
ssh sammy@your_server_ip_or_remote_hostname
```

Exit using:
```bash
exit
```

Initiate an SFTP session with:
```bash
sftp sammy@your_server_ip_or_remote_hostname
```

For custom SSH ports:
```bash
sftp -oPort=custom_port sammy@your_server_ip_or_remote_hostname
```

### Transferring Files with SFTP

#### Downloading from Remote Host
```bash
sftp> get remoteFile
```

#### Uploading to Remote System
```bash
sftp> put localFile
```

## CMD CHALLENGE

```bash
0 > echo 'hello world'
```

Your first challenge is to print "hello world" on the terminal in a single command. 🚀

Hint: There are various ways to print text on the command line; one way is with the 'echo' command.

---


```bash
0 > pwd
```

Print the current working directory.

---

```bash
0 > ls -1
```

List names of all the files in the current directory, one file per line.

---

```bash
0 > cat access.log
```

There is a file named *access.log* in the current directory. Print the contents.

---

```bash
0 > tail -n 5 access.log
```

Print the last 5 lines of "*access.log*".

---

```bash
0 > touch take-the-command-challenge
```

Create an empty file named *take-the-command-challenge* in the current working directory.

---

```bash
0 > mkdir -p tmp/files
```

Create a directory named **tmp**/***files*** in the current working directory

---

```bash
0 > cp take-the-command-challenge tmp/files
```

Copy the file named *take-the-command-challenge* to the directory **tmp**/***files***

---

```bash
0 > mv take-the-command-challenge tmp/files
```

Move the file named take-the-command-challenge to the directory tmp/files

---
