IP: 10.10.11.125
# Nmap
```bash
nmap -sC -sV 10.10.11.125

Starting Nmap 7.93 ( https://nmap.org ) at 2022-10-30 07:36 EDT
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 b4de43384657db4c213b69f3db3c6288 (RSA)
|   256 aac9fc210f3ef4ec6b3570262253ef66 (ECDSA)
|_  256 d28be4ec0761aacaf8ec1cf88cc1f6e1 (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-generator: WordPress 5.8.1
|_http-title: Backdoor &#8211; Real-Life
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

# Port 80
domain name of backdoor.htb

feroxbuster finds wp-content/plugins has a ebook reader plugin. This has a LFI.
wp-confg doesn't provide valid creds.

# Full port scan
port 1337 is open?