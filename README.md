# Proiect site cu flori - exemplu personal Liliac

Am instalat toate librariile necesare(git,gedit,pytest,pip,jenkins,docker,etc) si am creat un director "git" in care am lucrat la proiect. Continutul acestuia l-am pus intr-un repository pe GitHub( https://github.com/andrei162/curs_vcgj_444D_flori/tree/devel/Gabello8_flori).
Am ales floarea "Liliac" si am completat toate functiile si fisierele cu trasaturiile specifice acesteia(culoare(), anotimp(), clasificare() si biblioteca_flori, 444D_flori, etc)
Am creat un host local pe 127.0.0.1:5001 unde pentru afisarea programului 444D_flori.py, iar cu extensia /liliac ni se vor afisare si trasaturile acestei flori.
Pentru a testa ca nu suntem erori, am creat programul biblioteca_flori care prin intermediul pytest verifica daca fisierele sunt completate bine.
Dupa ce am verificat ca totul este in regula, am conectat GitHub si am dat push documentelor updatate.
In continuare am instalat Jenkins pentru testare. Am facut cont pe site-ul acestuia si am instalat Blue Ocean. Pentru testare in pipeline Jenkins am folosit un mediu virtual(venv) si flask.
Pentru containerizarea cu Docker am instalat libraria si am creat un dockerfile pentru rulare.

Poze pentru a demonstra functionarea proiectului :

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/133673312/0868ab5c-b4e7-4c3f-9af2-d160453fb02c)

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/133673312/b6c425a4-b4b2-4138-93b5-eb9216559af3)
Jenkins:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/133673312/6a32b7f0-45cc-4093-ad93-f20caf95565a)
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/133673312/9fa05e9e-6657-430f-b253-3f47db0f2796)
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/133673312/df253d9a-3c0b-4820-b19f-dd6a656caed7)
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/133673312/9e352bd0-cffc-4f95-ba94-ed036d0f2e68)
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/133673312/8d2f0c8d-65f9-4ecb-a172-8c49b65f0425)

Docker:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/133673312/b9e98754-2171-4abe-8c3d-c3db442deb51)



Atasez mai jos toate comenzile executate pentru realizarea proiectului:

gabriel@gabriel-VirtualBox:~$ sudo apt install build-essential dkms linux-headers-$(uname -r)
[sudo] password for gabriel: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
build-essential is already the newest version (12.9ubuntu3).
linux-headers-5.19.0-41-generic is already the newest version (5.19.0-41.42).
linux-headers-5.19.0-41-generic set to manually installed.
Suggested packages:
  debtags menu
The following NEW packages will be installed:
  dctrl-tools dh-dkms dkms
0 upgraded, 3 newly installed, 0 to remove and 2 not upgraded.
Need to get 118 kB of archives.
After this operation, 531 kB of additional disk space will be used.
Get:1 http://ro.archive.ubuntu.com/ubuntu kinetic/main amd64 dctrl-tools amd64 2.24-3build2 [66,9 kB]
Get:2 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/main amd64 dh-dkms all 3.0.6-2ubuntu2 [9.642 B]
Get:3 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/main amd64 dkms all 3.0.6-2ubuntu2 [41,4 kB]
Fetched 118 kB in 0s (338 kB/s)
Selecting previously unselected package dctrl-tools.
(Reading database ... 255589 files and directories currently installed.)
Preparing to unpack .../dctrl-tools_2.24-3build2_amd64.deb ...
Unpacking dctrl-tools (2.24-3build2) ...
Selecting previously unselected package dh-dkms.
Preparing to unpack .../dh-dkms_3.0.6-2ubuntu2_all.deb ...
Unpacking dh-dkms (3.0.6-2ubuntu2) ...
Selecting previously unselected package dkms.
Preparing to unpack .../dkms_3.0.6-2ubuntu2_all.deb ...
Unpacking dkms (3.0.6-2ubuntu2) ...
Setting up dh-dkms (3.0.6-2ubuntu2) ...
Setting up dctrl-tools (2.24-3build2) ...
Setting up dkms (3.0.6-2ubuntu2) ...
Processing triggers for man-db (2.10.2-2) ...
gabriel@gabriel-VirtualBox:~$ sudo apt install git
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  git-man
Suggested packages:
  git-daemon-run | git-daemon-sysvinit git-doc git-email git-gui gitk gitweb
  git-cvs git-mediawiki git-svn
The following packages will be upgraded:
  git git-man
2 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
Need to get 4.305 kB of archives.
After this operation, 115 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/main amd64 git-man all 1:2.37.2-1ubuntu1.5 [975 kB]
Get:2 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/main amd64 git amd64 1:2.37.2-1ubuntu1.5 [3.330 kB]
Fetched 4.305 kB in 2s (2.456 kB/s)
(Reading database ... 255645 files and directories currently installed.)
Preparing to unpack .../git-man_1%3a2.37.2-1ubuntu1.5_all.deb ...
Unpacking git-man (1:2.37.2-1ubuntu1.5) over (1:2.37.2-1ubuntu1.4) ...
Preparing to unpack .../git_1%3a2.37.2-1ubuntu1.5_amd64.deb ...
Unpacking git (1:2.37.2-1ubuntu1.5) over (1:2.37.2-1ubuntu1.4) ...
Setting up git-man (1:2.37.2-1ubuntu1.5) ...
Setting up git (1:2.37.2-1ubuntu1.5) ...
Processing triggers for man-db (2.10.2-2) ...
gabriel@gabriel-VirtualBox:~$ sudo apt install gedit
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  gedit-common gir1.2-gtksource-4 libgtksourceview-4-0
  libgtksourceview-4-common
Suggested packages:
  gedit-plugins
The following NEW packages will be installed:
  gedit gedit-common gir1.2-gtksource-4 libgtksourceview-4-0
  libgtksourceview-4-common
0 upgraded, 5 newly installed, 0 to remove and 0 not upgraded.
Need to get 2.863 kB of archives.
After this operation, 20,3 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://ro.archive.ubuntu.com/ubuntu kinetic/universe amd64 gedit-common all 42.2-1 [1.575 kB]
Get:2 http://ro.archive.ubuntu.com/ubuntu kinetic/universe amd64 libgtksourceview-4-common all 4.8.3-1ubuntu1 [592 kB]
Get:3 http://ro.archive.ubuntu.com/ubuntu kinetic/universe amd64 libgtksourceview-4-0 amd64 4.8.3-1ubuntu1 [235 kB]
Get:4 http://ro.archive.ubuntu.com/ubuntu kinetic/universe amd64 gir1.2-gtksource-4 amd64 4.8.3-1ubuntu1 [20,2 kB]
Get:5 http://ro.archive.ubuntu.com/ubuntu kinetic/universe amd64 gedit amd64 42.2-1 [441 kB]
Fetched 2.863 kB in 2s (1.605 kB/s)
Selecting previously unselected package gedit-common.
(Reading database ... 255645 files and directories currently installed.)
Preparing to unpack .../gedit-common_42.2-1_all.deb ...
Unpacking gedit-common (42.2-1) ...
Selecting previously unselected package libgtksourceview-4-common.
Preparing to unpack .../libgtksourceview-4-common_4.8.3-1ubuntu1_all.deb ...
Unpacking libgtksourceview-4-common (4.8.3-1ubuntu1) ...
Selecting previously unselected package libgtksourceview-4-0:amd64.
Preparing to unpack .../libgtksourceview-4-0_4.8.3-1ubuntu1_amd64.deb ...
Unpacking libgtksourceview-4-0:amd64 (4.8.3-1ubuntu1) ...
Selecting previously unselected package gir1.2-gtksource-4:amd64.
Preparing to unpack .../gir1.2-gtksource-4_4.8.3-1ubuntu1_amd64.deb ...
Unpacking gir1.2-gtksource-4:amd64 (4.8.3-1ubuntu1) ...
Selecting previously unselected package gedit.
Preparing to unpack .../gedit_42.2-1_amd64.deb ...
Unpacking gedit (42.2-1) ...
Setting up gedit-common (42.2-1) ...
Setting up libgtksourceview-4-common (4.8.3-1ubuntu1) ...
Setting up libgtksourceview-4-0:amd64 (4.8.3-1ubuntu1) ...
Setting up gir1.2-gtksource-4:amd64 (4.8.3-1ubuntu1) ...
Processing triggers for gnome-menus (3.36.0-1ubuntu3) ...
Processing triggers for libglib2.0-0:amd64 (2.74.3-0ubuntu1) ...
Processing triggers for libc-bin (2.36-0ubuntu4) ...
Processing triggers for man-db (2.10.2-2) ...
Processing triggers for mailcap (3.70+nmu1ubuntu1) ...
Processing triggers for desktop-file-utils (0.26-1ubuntu4) ...
Processing triggers for hicolor-icon-theme (0.17-2) ...
Setting up gedit (42.2-1) ...
update-alternatives: using /usr/bin/gedit to provide /usr/bin/gnome-text-editor 
(gnome-text-editor) in auto mode
update-alternatives: warning: not replacing /usr/bin/gnome-text-editor with a li
nk
gabriel@gabriel-VirtualBox:~$ ls -la
total 27832
drwxr-x--- 17 gabriel gabriel     4096 apr 29 05:08 .
drwxr-xr-x  3 root    root        4096 apr 29 04:38 ..
-rw-------  1 gabriel gabriel     1152 apr 29 05:08 .bash_history
-rw-r--r--  1 gabriel gabriel      220 apr 29 04:38 .bash_logout
-rw-r--r--  1 gabriel gabriel     3771 apr 29 04:38 .bashrc
drwx------ 11 gabriel gabriel     4096 apr 29 05:04 .cache
drwx------ 10 gabriel gabriel     4096 mai 19 15:12 .config
drwxr-xr-x  2 gabriel gabriel     4096 apr 29 04:51 Desktop
drwxr-xr-x  2 gabriel gabriel     4096 apr 29 04:51 Documents
drwxr-xr-x  2 gabriel gabriel     4096 apr 29 04:51 Downloads
drwx------  2 gabriel gabriel     4096 mai 19 15:09 .gnupg
drwx------  4 gabriel gabriel     4096 apr 29 04:51 .local
drwxr-xr-x  2 gabriel gabriel     4096 apr 29 04:51 Music
drwxrwxr-x  7 gabriel gabriel     4096 apr 29 05:15 ns-allinone-3.33
-rw-rw-r--  1 gabriel gabriel 28412785 apr 27  2022 ns-allinone-3.33.tar.bz2
drwxr-xr-x  2 gabriel gabriel     4096 apr 29 04:51 Pictures
-rw-r--r--  1 gabriel gabriel      807 apr 29 04:38 .profile
drwxr-xr-x  2 gabriel gabriel     4096 apr 29 04:51 Public
drwx------  4 gabriel gabriel     4096 apr 29 04:52 snap
drwx------  2 gabriel gabriel     4096 apr 29 04:53 .ssh
-rw-r--r--  1 gabriel gabriel        0 apr 29 04:54 .sudo_as_admin_successful
drwxr-xr-x  2 gabriel gabriel     4096 apr 29 04:51 Templates
drwxr-xr-x  2 gabriel gabriel     4096 apr 29 04:51 Videos
gabriel@gabriel-VirtualBox:~$ mkdir git
gabriel@gabriel-VirtualBox:~$ cd git
gabriel@gabriel-VirtualBox:~/git$ cd
gabriel@gabriel-VirtualBox:~$ ls -la
total 27836
drwxr-x--- 18 gabriel gabriel     4096 mai 19 15:14 .
drwxr-xr-x  3 root    root        4096 apr 29 04:38 ..
-rw-------  1 gabriel gabriel     1152 apr 29 05:08 .bash_history
-rw-r--r--  1 gabriel gabriel      220 apr 29 04:38 .bash_logout
-rw-r--r--  1 gabriel gabriel     3771 apr 29 04:38 .bashrc
drwx------ 11 gabriel gabriel     4096 apr 29 05:04 .cache
drwx------ 10 gabriel gabriel     4096 mai 19 15:12 .config
drwxr-xr-x  2 gabriel gabriel     4096 apr 29 04:51 Desktop
drwxr-xr-x  2 gabriel gabriel     4096 apr 29 04:51 Documents
drwxr-xr-x  2 gabriel gabriel     4096 apr 29 04:51 Downloads
drwxrwxr-x  2 gabriel gabriel     4096 mai 19 15:14 git
drwx------  2 gabriel gabriel     4096 mai 19 15:09 .gnupg
drwx------  4 gabriel gabriel     4096 apr 29 04:51 .local
drwxr-xr-x  2 gabriel gabriel     4096 apr 29 04:51 Music
drwxrwxr-x  7 gabriel gabriel     4096 apr 29 05:15 ns-allinone-3.33
-rw-rw-r--  1 gabriel gabriel 28412785 apr 27  2022 ns-allinone-3.33.tar.bz2
drwxr-xr-x  2 gabriel gabriel     4096 apr 29 04:51 Pictures
-rw-r--r--  1 gabriel gabriel      807 apr 29 04:38 .profile
drwxr-xr-x  2 gabriel gabriel     4096 apr 29 04:51 Public
drwx------  4 gabriel gabriel     4096 apr 29 04:52 snap
drwx------  2 gabriel gabriel     4096 apr 29 04:53 .ssh
-rw-r--r--  1 gabriel gabriel        0 apr 29 04:54 .sudo_as_admin_successful
drwxr-xr-x  2 gabriel gabriel     4096 apr 29 04:51 Templates
drwxr-xr-x  2 gabriel gabriel     4096 apr 29 04:51 Videos
gabriel@gabriel-VirtualBox:~$ ls -l
total 27792
drwxr-xr-x 2 gabriel gabriel     4096 apr 29 04:51 Desktop
drwxr-xr-x 2 gabriel gabriel     4096 apr 29 04:51 Documents
drwxr-xr-x 2 gabriel gabriel     4096 apr 29 04:51 Downloads
drwxrwxr-x 2 gabriel gabriel     4096 mai 19 15:14 git
drwxr-xr-x 2 gabriel gabriel     4096 apr 29 04:51 Music
drwxrwxr-x 7 gabriel gabriel     4096 apr 29 05:15 ns-allinone-3.33
-rw-rw-r-- 1 gabriel gabriel 28412785 apr 27  2022 ns-allinone-3.33.tar.bz2
drwxr-xr-x 2 gabriel gabriel     4096 apr 29 04:51 Pictures
drwxr-xr-x 2 gabriel gabriel     4096 apr 29 04:51 Public
drwx------ 4 gabriel gabriel     4096 apr 29 04:52 snap
drwxr-xr-x 2 gabriel gabriel     4096 apr 29 04:51 Templates
drwxr-xr-x 2 gabriel gabriel     4096 apr 29 04:51 Videos
gabriel@gabriel-VirtualBox:~$ cd git
gabriel@gabriel-VirtualBox:~/git$ sudo apt-getupdate
sudo: apt-getupdate: command not found
gabriel@gabriel-VirtualBox:~/git$ sudo apt-get update
Get:1 http://security.ubuntu.com/ubuntu kinetic-security InRelease [109 kB]
Hit:2 http://ro.archive.ubuntu.com/ubuntu kinetic InRelease
Get:3 http://ro.archive.ubuntu.com/ubuntu kinetic-updates InRelease [118 kB]
Get:4 http://security.ubuntu.com/ubuntu kinetic-security/main amd64 Packages [204 kB]
Get:5 http://security.ubuntu.com/ubuntu kinetic-security/main i386 Packages [110 kB]
Get:6 http://security.ubuntu.com/ubuntu kinetic-security/main Translation-en [66,4 kB]
Get:7 http://security.ubuntu.com/ubuntu kinetic-security/main amd64 DEP-11 Metadata [30,1 kB]
Get:8 http://security.ubuntu.com/ubuntu kinetic-security/main amd64 c-n-f Metadata [6.900 B]
Get:9 http://security.ubuntu.com/ubuntu kinetic-security/restricted amd64 Packages [156 kB]
Get:10 http://security.ubuntu.com/ubuntu kinetic-security/restricted Translation-en [24,4 kB]
Get:11 http://security.ubuntu.com/ubuntu kinetic-security/universe amd64 Packages [175 kB]
Get:12 http://ro.archive.ubuntu.com/ubuntu kinetic-backports InRelease [99,9 kB]
Get:13 http://security.ubuntu.com/ubuntu kinetic-security/universe i386 Packages [106 kB]
Get:14 http://security.ubuntu.com/ubuntu kinetic-security/universe Translation-en [76,1 kB]
Get:15 http://security.ubuntu.com/ubuntu kinetic-security/universe amd64 DEP-11 Metadata [7.864 B]
Get:16 http://security.ubuntu.com/ubuntu kinetic-security/universe amd64 c-n-f Metadata [7.524 B]
Get:17 http://security.ubuntu.com/ubuntu kinetic-security/multiverse amd64 Packages [5.984 B]
Get:18 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/main amd64 Packages [316 kB]
Get:19 http://security.ubuntu.com/ubuntu kinetic-security/multiverse Translation-en [1.672 B]
Get:20 http://security.ubuntu.com/ubuntu kinetic-security/multiverse amd64 c-n-f Metadata [320 B]
Get:21 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/main i386 Packages [187 kB]
Get:22 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/main Translation-en [97,6 kB]
Get:23 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/main amd64 DEP-11 Metadata [85,9 kB]
Get:24 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/main amd64 c-n-f Metadata [9.272 B]
Get:25 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/restricted amd64 Packages [157 kB]
Get:26 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/restricted Translation-en [24,6 kB]
Get:27 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/universe i386 Packages [146 kB]
Get:28 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/universe amd64 Packages [282 kB]
Get:29 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/universe Translation-en [109 kB]
Get:30 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/universe amd64 DEP-11 Metadata [41,2 kB]
Get:31 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/universe amd64 c-n-f Metadata [9.652 B]
Get:32 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/multiverse amd64 Packages [6.620 B]
Get:33 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/multiverse Translation-en [2.056 B]
Get:34 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/multiverse amd64 DEP-11 Metadata [212 B]
Get:35 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/multiverse amd64 c-n-f Metadata [348 B]
Get:36 http://ro.archive.ubuntu.com/ubuntu kinetic-backports/universe amd64 DEP-11 Metadata [10,6 kB]
Fetched 2.790 kB in 4s (621 kB/s)                                     
WARNING:root:cannot read /var/lib/command-not-found/commands.db.metadata: Expecting value: line 1 column 1 (char 0)
Reading package lists... Done
gabriel@gabriel-VirtualBox:~/git$ git clone https://github.com/andrei162/curs_vcgj_444D_flori.git
Cloning into 'curs_vcgj_444D_flori'...
remote: Enumerating objects: 116, done.
remote: Counting objects: 100% (116/116), done.
remote: Compressing objects: 100% (92/92), done.
remote: Total 116 (delta 41), reused 60 (delta 13), pack-reused 0
Receiving objects: 100% (116/116), 27.12 KiB | 925.00 KiB/s, done.
Resolving deltas: 100% (41/41), done.
gabriel@gabriel-VirtualBox:~/git$ ls -l
total 4
drwxrwxr-x 4 gabriel gabriel 4096 mai 19 15:19 curs_vcgj_444D_flori
gabriel@gabriel-VirtualBox:~/git$ cd curs_vcgj_444D_flori/
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ cd app
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ ls -l
total 12
-rw-rw-r-- 1 gabriel gabriel 1119 mai 19 15:19 444D_flori.py
drwxrwxr-x 2 gabriel gabriel 4096 mai 19 15:19 lib
drwxrwxr-x 2 gabriel gabriel 4096 mai 19 15:19 tests
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ gedit 444D_flori.py 
^C
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ sudo apt install python3
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
python3 is already the newest version (3.10.6-1).
python3 set to manually installed.
0 upgraded, 0 newly installed, 0 to remove and 30 not upgraded.
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ python3 444D_flori.py 
Traceback (most recent call last):
  File "/home/gabriel/git/curs_vcgj_444D_flori/app/444D_flori.py", line 1, in <module>
    from flask import Flask
ModuleNotFoundError: No module named 'flask'
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ sudo apt install flask
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package flask
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ sudo apt install python3-flask
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-itsdangerous python3-openssl python3-pyinotify python3-simplejson
  python3-werkzeug
Suggested packages:
  python3-asgiref python3-dotenv python-flask-doc python-openssl-doc
  python3-openssl-dbg python-pyinotify-doc python-werkzeug-doc
  python3-watchdog
The following NEW packages will be installed:
  python3-flask python3-itsdangerous python3-openssl python3-pyinotify
  python3-simplejson python3-werkzeug
0 upgraded, 6 newly installed, 0 to remove and 30 not upgraded.
Need to get 402 kB of archives.
After this operation, 2.011 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://ro.archive.ubuntu.com/ubuntu kinetic/main amd64 python3-itsdangerous all 2.1.2-2 [14,5 kB]
Get:2 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/main amd64 python3-werkzeug all 2.0.2+dfsg1-3ubuntu0.22.10.1 [181 kB]
Get:3 http://ro.archive.ubuntu.com/ubuntu kinetic/main amd64 python3-flask all 2.0.3-1ubuntu1 [81,5 kB]
Get:4 http://ro.archive.ubuntu.com/ubuntu kinetic/main amd64 python3-openssl all 21.0.0-1 [45,2 kB]
Get:5 http://ro.archive.ubuntu.com/ubuntu kinetic/main amd64 python3-pyinotify all 0.9.6-2 [25,3 kB]
Get:6 http://ro.archive.ubuntu.com/ubuntu kinetic/main amd64 python3-simplejson amd64 3.17.6-1build1 [54,7 kB]
Fetched 402 kB in 1s (770 kB/s)          
Selecting previously unselected package python3-itsdangerous.
(Reading database ... 257623 files and directories currently installed.)
Preparing to unpack .../0-python3-itsdangerous_2.1.2-2_all.deb ...
Unpacking python3-itsdangerous (2.1.2-2) ...
Selecting previously unselected package python3-werkzeug.
Preparing to unpack .../1-python3-werkzeug_2.0.2+dfsg1-3ubuntu0.22.10.1_all.deb 
...
Unpacking python3-werkzeug (2.0.2+dfsg1-3ubuntu0.22.10.1) ...
Selecting previously unselected package python3-flask.
Preparing to unpack .../2-python3-flask_2.0.3-1ubuntu1_all.deb ...
Unpacking python3-flask (2.0.3-1ubuntu1) ...
Selecting previously unselected package python3-openssl.
Preparing to unpack .../3-python3-openssl_21.0.0-1_all.deb ...
Unpacking python3-openssl (21.0.0-1) ...
Selecting previously unselected package python3-pyinotify.
Preparing to unpack .../4-python3-pyinotify_0.9.6-2_all.deb ...
Unpacking python3-pyinotify (0.9.6-2) ...
Selecting previously unselected package python3-simplejson.
Preparing to unpack .../5-python3-simplejson_3.17.6-1build1_amd64.deb ...
Unpacking python3-simplejson (3.17.6-1build1) ...
Setting up python3-openssl (21.0.0-1) ...
Setting up python3-pyinotify (0.9.6-2) ...
Setting up python3-itsdangerous (2.1.2-2) ...
Setting up python3-simplejson (3.17.6-1build1) ...
Setting up python3-werkzeug (2.0.2+dfsg1-3ubuntu0.22.10.1) ...
Setting up python3-flask (2.0.3-1ubuntu1) ...
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ python3 444D_flori.py 
444D_flori
 * Serving Flask app '444D_flori' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5001/ (Press CTRL+C to quit)
^Cgabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ cd llib
bash: cd: llib: No such file or directory
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ cd lib
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app/lib$ ls -l
total 8
-rw-rw-r-- 1 gabriel gabriel  152 mai 19 15:19 biblioteca_flori.py
drwxrwxr-x 2 gabriel gabriel 4096 mai 19 15:37 __pycache__
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app/lib$ gedit biblioteca_flori.py 
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app/lib$ cd ..
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ ls -l
total 12
-rw-rw-r-- 1 gabriel gabriel 2008 mai 19 15:30 444D_flori.py
drwxrwxr-x 3 gabriel gabriel 4096 mai 19 15:42 lib
drwxrwxr-x 2 gabriel gabriel 4096 mai 19 15:19 tests
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ cd tests
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app/tests$ gedit test_biblioteca_flori.py 
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app/tests$ cd ..
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ cd ..
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ python3 -m pytest
/usr/bin/python3: No module named pytest
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ pip install pytest
Defaulting to user installation because normal site-packages is not writeable
Collecting pytest
  Downloading pytest-7.3.1-py3-none-any.whl (320 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 320.5/320.5 kB 1.5 MB/s eta 0:00:00
Collecting iniconfig
  Downloading iniconfig-2.0.0-py3-none-any.whl (5.9 kB)
Collecting pluggy<2.0,>=0.12
  Downloading pluggy-1.0.0-py2.py3-none-any.whl (13 kB)
Collecting exceptiongroup>=1.0.0rc8
  Downloading exceptiongroup-1.1.1-py3-none-any.whl (14 kB)
Collecting tomli>=1.0.0
  Downloading tomli-2.0.1-py3-none-any.whl (12 kB)
Requirement already satisfied: packaging in /usr/lib/python3/dist-packages (from pytest) (21.3)
Installing collected packages: tomli, pluggy, iniconfig, exceptiongroup, pytest
  WARNING: The scripts py.test and pytest are installed in '/home/gabriel/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed exceptiongroup-1.1.1 iniconfig-2.0.0 pluggy-1.0.0 pytest-7.3.1 tomli-2.0.1
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ sudo apt install python3-pip
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
python3-pip is already the newest version (22.2+dfsg-1ubuntu0.2).
0 upgraded, 0 newly installed, 0 to remove and 30 not upgraded.
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ touch fisier.py
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ ls -l
total 8
drwxrwxr-x 4 gabriel gabriel 4096 mai 19 15:30 app
-rw-rw-r-- 1 gabriel gabriel    0 mai 19 15:46 fisier.py
-rw-rw-r-- 1 gabriel gabriel   28 mai 19 15:19 README.md
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ pip install pytest
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: pytest in /home/gabriel/.local/lib/python3.10/site-packages (7.3.1)
Requirement already satisfied: packaging in /usr/lib/python3/dist-packages (from pytest) (21.3)
Requirement already satisfied: tomli>=1.0.0 in /home/gabriel/.local/lib/python3.10/site-packages (from pytest) (2.0.1)
Requirement already satisfied: pluggy<2.0,>=0.12 in /home/gabriel/.local/lib/python3.10/site-packages (from pytest) (1.0.0)
Requirement already satisfied: exceptiongroup>=1.0.0rc8 in /home/gabriel/.local/lib/python3.10/site-packages (from pytest) (1.1.1)
Requirement already satisfied: iniconfig in /home/gabriel/.local/lib/python3.10/site-packages (from pytest) (2.0.0)
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ ls -l
total 8
drwxrwxr-x 4 gabriel gabriel 4096 mai 19 15:30 app
-rw-rw-r-- 1 gabriel gabriel    0 mai 19 15:46 fisier.py
-rw-rw-r-- 1 gabriel gabriel   28 mai 19 15:19 README.md
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ cd app
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ cd lib
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app/lib$ ls -l
total 8
-rw-rw-r-- 1 gabriel gabriel  313 mai 19 15:42 biblioteca_flori.py
drwxrwxr-x 2 gabriel gabriel 4096 mai 19 15:37 __pycache__
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app/lib$ gedit biblioteca_flori.py 
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app/lib$ cd ..
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ cd ..
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ cd app
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ ls -l
total 12
-rw-rw-r-- 1 gabriel gabriel 2008 mai 19 15:30 444D_flori.py
drwxrwxr-x 3 gabriel gabriel 4096 mai 19 15:42 lib
drwxrwxr-x 2 gabriel gabriel 4096 mai 19 15:43 tests
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ cd tests
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app/tests$ ls -l
total 4
-rw-rw-r-- 1 gabriel gabriel 963 mai 19 15:43 test_biblioteca_flori.py
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app/tests$ gedit test_biblioteca_flori.py 
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app/tests$ c d..
c: command not found
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app/tests$ cd ..
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ cd ..
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ ls -l
total 8
drwxrwxr-x 4 gabriel gabriel 4096 mai 19 15:30 app
-rw-rw-r-- 1 gabriel gabriel    0 mai 19 15:46 fisier.py
-rw-rw-r-- 1 gabriel gabriel   28 mai 19 15:19 README.md
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ cd app
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ ls -l
total 12
-rw-rw-r-- 1 gabriel gabriel 2008 mai 19 15:30 444D_flori.py
drwxrwxr-x 3 gabriel gabriel 4096 mai 19 15:42 lib
drwxrwxr-x 2 gabriel gabriel 4096 mai 19 15:59 tests
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ python3 444D_flori.py 
444D_flori
 * Serving Flask app '444D_flori' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5001/ (Press CTRL+C to quit)
^Cgabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ python3 444D_flori.py 
444D_flori
 * Serving Flask app '444D_flori' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5001/ (Press CTRL+C to quit)
127.0.0.1 - - [19/May/2023 16:06:02] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [19/May/2023 16:06:02] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [19/May/2023 16:07:31] "GET /liliac HTTP/1.1" 308 -
127.0.0.1 - - [19/May/2023 16:07:31] "GET /liliac/ HTTP/1.1" 200 -
^Cgabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ pip install pytest
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: pytest in /home/gabriel/.local/lib/python3.10/site-packages (7.3.1)
Requirement already satisfied: exceptiongroup>=1.0.0rc8 in /home/gabriel/.local/lib/python3.10/site-packages (from pytest) (1.1.1)
Requirement already satisfied: pluggy<2.0,>=0.12 in /home/gabriel/.local/lib/python3.10/site-packages (from pytest) (1.0.0)
Requirement already satisfied: packaging in /usr/lib/python3/dist-packages (from pytest) (21.3)
Requirement already satisfied: tomli>=1.0.0 in /home/gabriel/.local/lib/python3.10/site-packages (from pytest) (2.0.1)
Requirement already satisfied: iniconfig in /home/gabriel/.local/lib/python3.10/site-packages (from pytest) (2.0.0)
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ python3 -m pytest -v
============================= test session starts ==============================
platform linux -- Python 3.10.7, pytest-7.3.1, pluggy-1.0.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/gabriel/git/curs_vcgj_444D_flori/app
collected 6 items                                                              

tests/test_biblioteca_flori.py::test_culoare_crin PASSED                 [ 16%]
tests/test_biblioteca_flori.py::test_anotimp_crin PASSED                 [ 33%]
tests/test_biblioteca_flori.py::test_clasificare_crin PASSED             [ 50%]
tests/test_biblioteca_flori.py::test_culoare_liliac PASSED               [ 66%]
tests/test_biblioteca_flori.py::test_anotimp_liliac PASSED               [ 83%]
tests/test_biblioteca_flori.py::test_clasificare_liliac PASSED           [100%]

============================== 6 passed in 0.01s ===============================
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ cd..
cd..: command not found
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ touch JenkinsFile
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ gedit JenkinsFile 
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ touch activeaza_venv
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ gedit activeaza_venv 
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ touch activeaza_venv_jenkins
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ getdit activeaza_venv_jenkins 
Command 'getdit' not found, did you mean:
  command 'gedit' from snap gedit (42.2)
  command 'gedit' from deb gedit (42.1-1)
See 'snap info <snapname>' for additional versions.
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ gedit activeaza_venv_jenkins 
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ touch ruleaza_aplicatia
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ gedit ruleaza_aplicatia 
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ cd ..
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ touch Jenkinsfile
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ gedit Jenkinsfile 
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ cd app
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ rm -rf Jenkinsfile
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ ls -l
total 28
-rw-rw-r-- 1 gabriel gabriel 2008 mai 19 15:30 444D_flori.py
-rw-rw-r-- 1 gabriel gabriel  360 mai 19 16:24 activeaza_venv
-rw-rw-r-- 1 gabriel gabriel  290 mai 19 16:25 activeaza_venv_jenkins
-rw-rw-r-- 1 gabriel gabriel 1539 mai 19 16:23 JenkinsFile
drwxrwxr-x 3 gabriel gabriel 4096 mai 19 15:42 lib
-rw-rw-r-- 1 gabriel gabriel  110 mai 19 16:27 ruleaza_aplicatia
drwxrwxr-x 3 gabriel gabriel 4096 mai 19 16:13 tests
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ rm -rf JenkinsFile
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ ls -l
total 24
-rw-rw-r-- 1 gabriel gabriel 2008 mai 19 15:30 444D_flori.py
-rw-rw-r-- 1 gabriel gabriel  360 mai 19 16:24 activeaza_venv
-rw-rw-r-- 1 gabriel gabriel  290 mai 19 16:25 activeaza_venv_jenkins
drwxrwxr-x 3 gabriel gabriel 4096 mai 19 15:42 lib
-rw-rw-r-- 1 gabriel gabriel  110 mai 19 16:27 ruleaza_aplicatia
drwxrwxr-x 3 gabriel gabriel 4096 mai 19 16:13 tests
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ cd ..
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ git branch devel/Gabello8_flori
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ git branch
  devel/Gabello8_flori
* main
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ git checkout devel/Gabello8_flori
M	app/444D_flori.py
M	app/lib/biblioteca_flori.py
M	app/tests/test_biblioteca_flori.py
Switched to branch 'devel/Gabello8_flori'
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ git branch
* devel/Gabello8_flori
  main
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ git status
On branch devel/Gabello8_flori
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   app/444D_flori.py
	modified:   app/lib/biblioteca_flori.py
	modified:   app/tests/test_biblioteca_flori.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	Jenkinsfile
	app/activeaza_venv
	app/activeaza_venv_jenkins
	app/ruleaza_aplicatia
	fisier.py

no changes added to commit (use "git add" and/or "git commit -a")
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ git add .
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ git status
On branch devel/Gabello8_flori
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   Jenkinsfile
	modified:   app/444D_flori.py
	new file:   app/activeaza_venv
	new file:   app/activeaza_venv_jenkins
	modified:   app/lib/biblioteca_flori.py
	new file:   app/ruleaza_aplicatia
	modified:   app/tests/test_biblioteca_flori.py
	new file:   fisier.py

gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ git commit -m "Pregatire Jenkis"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'gabriel@gabriel-VirtualBox.(none)')
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ git config --global user.email "gabrieljuganaru8@gmail.com"
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ git config --global user.name "Gabello8"
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ git commit -m "Pregatire Jenkis"
[devel/Gabello8_flori 3a527be] Pregatire Jenkis
 8 files changed, 165 insertions(+)
 create mode 100644 Jenkinsfile
 create mode 100644 app/activeaza_venv
 create mode 100644 app/activeaza_venv_jenkins
 create mode 100644 app/ruleaza_aplicatia
 create mode 100644 fisier.py
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ git status
On branch devel/Gabello8_flori
nothing to commit, working tree clean
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ git config --global credential.helper store
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ git push
fatal: The current branch devel/Gabello8_flori has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin devel/Gabello8_flori

To have this happen automatically for branches without a tracking
upstream, see 'push.autoSetupRemote' in 'git help config'.

gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ git push --set-upstream origin devel/Gabello8_flori
Username for 'https://github.com': Gabello8
Password for 'https://Gabello8@github.com': 
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/andrei162/curs_vcgj_444D_flori.git/'
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ git push --set-upstream origin devel/Gabello8_flori
Username for 'https://github.com': Gabello8
Password for 'https://Gabello8@github.com': 
remote: Permission to andrei162/curs_vcgj_444D_flori.git denied to Gabello8.
fatal: unable to access 'https://github.com/andrei162/curs_vcgj_444D_flori.git/': The requested URL returned error: 403
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ git push --set-upstream origin devel/Gabello8_flori
Username for 'https://github.com': Gabello8
Password for 'https://Gabello8@github.com': 
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/andrei162/curs_vcgj_444D_flori.git/'
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ git push --set-upstream origin devel/Gabello8_flori
Username for 'https://github.com': Gabello8
Password for 'https://Gabello8@github.com': 
remote: Permission to andrei162/curs_vcgj_444D_flori.git denied to Gabello8.
fatal: unable to access 'https://github.com/andrei162/curs_vcgj_444D_flori.git/': The requested URL returned error: 403
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ git push --set-upstream origin devel/Gabello8_flori
Username for 'https://github.com': Gabello8
Password for 'https://Gabello8@github.com': 
remote: Permission to andrei162/curs_vcgj_444D_flori.git denied to Gabello8.
fatal: unable to access 'https://github.com/andrei162/curs_vcgj_444D_flori.git/': The requested URL returned error: 403
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ git push --set-upstream origin devel/Gabello8_flori
Username for 'https://github.com': Gabello8
Password for 'https://Gabello8@github.com': 
remote: Permission to andrei162/curs_vcgj_444D_flori.git denied to Gabello8.
fatal: unable to access 'https://github.com/andrei162/curs_vcgj_444D_flori.git/': The requested URL returned error: 403
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ git push --set-upstream origin devel/Gabello8_flori
Username for 'https://github.com': Gabello8
Password for 'https://Gabello8@github.com': 
remote: Permission to andrei162/curs_vcgj_444D_flori.git denied to Gabello8.
fatal: unable to access 'https://github.com/andrei162/curs_vcgj_444D_flori.git/': The requested URL returned error: 403
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ git push --set-upstream origin devel/Gabello8_flori
Username for 'https://github.com': Gabello8
Password for 'https://Gabello8@github.com': 
remote: Permission to andrei162/curs_vcgj_444D_flori.git denied to Gabello8.
fatal: unable to access 'https://github.com/andrei162/curs_vcgj_444D_flori.git/': The requested URL returned error: 403
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ git push --set-upstream origin devel/Gabello8_flori
Username for 'https://github.com': Gabello8
Password for 'https://Gabello8@github.com': 
Enumerating objects: 19, done.
Counting objects: 100% (19/19), done.
Delta compression using up to 4 threads
Compressing objects: 100% (11/11), done.
Writing objects: 100% (13/13), 2.07 KiB | 2.07 MiB/s, done.
Total 13 (delta 1), reused 3 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
remote: 
remote: Create a pull request for 'devel/Gabello8_flori' on GitHub by visiting:
remote:      https://github.com/andrei162/curs_vcgj_444D_flori/pull/new/devel/Gabello8_flori
remote: 
To https://github.com/andrei162/curs_vcgj_444D_flori.git
 * [new branch]      devel/Gabello8_flori -> devel/Gabello8_flori
branch 'devel/Gabello8_flori' set up to track 'origin/devel/Gabello8_flori'.
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ java - version
Command 'java' not found, but can be installed with:
sudo apt install default-jre              # version 2:1.11-72build2, or
sudo apt install openjdk-11-jre-headless  # version 11.0.19+7~us1-0ubuntu1~22.10.1
sudo apt install openjdk-18-jre-headless  # version 18.0.1+10-1
sudo apt install openjdk-17-jre-headless  # version 17.0.7+7~us1-0ubuntu1~22.10.2
sudo apt install openjdk-19-jre-headless  # version 19.0.2+7-0ubuntu3~22.10
sudo apt install openjdk-20-jre-headless  # version 20.0.1+9~us1-0ubuntu1~22.10
sudo apt install openjdk-8-jre-headless   # version 8u372-ga~us1-0ubuntu1~22.10
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ sudo apt install openjdk-11-jdk
[sudo] password for gabriel: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  linux-headers-5.19.0-21 linux-headers-5.19.0-21-generic linux-image-5.19.0-21-generic
  linux-modules-5.19.0-21-generic linux-modules-extra-5.19.0-21-generic
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  ca-certificates-java fonts-dejavu-extra java-common libatk-wrapper-java
  libatk-wrapper-java-jni openjdk-11-jdk-headless openjdk-11-jre openjdk-11-jre-headless
Suggested packages:
  default-jre openjdk-11-demo openjdk-11-source visualvm fonts-ipafont-gothic
  fonts-ipafont-mincho fonts-wqy-microhei | fonts-wqy-zenhei
The following NEW packages will be installed:
  ca-certificates-java fonts-dejavu-extra java-common libatk-wrapper-java
  libatk-wrapper-java-jni openjdk-11-jdk openjdk-11-jdk-headless openjdk-11-jre
  openjdk-11-jre-headless
0 upgraded, 9 newly installed, 0 to remove and 26 not upgraded.
1 not fully installed or removed.
Need to get 119 MB of archives.
After this operation, 268 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/main amd64 ca-certificates-java all 20220719ubuntu0.1 [12,6 kB]
Get:2 http://ro.archive.ubuntu.com/ubuntu kinetic/main amd64 fonts-dejavu-extra all 2.37-2build1 [2.041 kB]
Get:3 http://ro.archive.ubuntu.com/ubuntu kinetic/main amd64 java-common all 0.72build2 [6.782 B]
Get:4 http://ro.archive.ubuntu.com/ubuntu kinetic/main amd64 libatk-wrapper-java all 0.40.0-2 [53,1 kB]
Get:5 http://ro.archive.ubuntu.com/ubuntu kinetic/main amd64 libatk-wrapper-java-jni amd64 0.40.0-2 [48,6 kB]
Get:6 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/main amd64 openjdk-11-jre-headless amd64 11.0.19+7~us1-0ubuntu1~22.10.1 [42,3 MB]
Get:7 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/main amd64 openjdk-11-jre amd64 11.0.19+7~us1-0ubuntu1~22.10.1 [208 kB]
Get:8 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/main amd64 openjdk-11-jdk-headless amd64 11.0.19+7~us1-0ubuntu1~22.10.1 [73,5 MB]
Get:9 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/main amd64 openjdk-11-jdk amd64 11.0.19+7~us1-0ubuntu1~22.10.1 [1.328 kB]
Fetched 119 MB in 21s (5.739 kB/s)                                                              
Selecting previously unselected package ca-certificates-java.
(Reading database ... 294213 files and directories currently installed.)
Preparing to unpack .../0-ca-certificates-java_20220719ubuntu0.1_all.deb ...
Unpacking ca-certificates-java (20220719ubuntu0.1) ...
Selecting previously unselected package fonts-dejavu-extra.
Preparing to unpack .../1-fonts-dejavu-extra_2.37-2build1_all.deb ...
Unpacking fonts-dejavu-extra (2.37-2build1) ...
Selecting previously unselected package java-common.
Preparing to unpack .../2-java-common_0.72build2_all.deb ...
Unpacking java-common (0.72build2) ...
Selecting previously unselected package libatk-wrapper-java.
Preparing to unpack .../3-libatk-wrapper-java_0.40.0-2_all.deb ...
Unpacking libatk-wrapper-java (0.40.0-2) ...
Selecting previously unselected package libatk-wrapper-java-jni:amd64.
Preparing to unpack .../4-libatk-wrapper-java-jni_0.40.0-2_amd64.deb ...
Unpacking libatk-wrapper-java-jni:amd64 (0.40.0-2) ...
Selecting previously unselected package openjdk-11-jre-headless:amd64.
Preparing to unpack .../5-openjdk-11-jre-headless_11.0.19+7~us1-0ubuntu1~22.10.1_amd64.deb ...
Unpacking openjdk-11-jre-headless:amd64 (11.0.19+7~us1-0ubuntu1~22.10.1) ...
Selecting previously unselected package openjdk-11-jre:amd64.
Preparing to unpack .../6-openjdk-11-jre_11.0.19+7~us1-0ubuntu1~22.10.1_amd64.deb ...
Unpacking openjdk-11-jre:amd64 (11.0.19+7~us1-0ubuntu1~22.10.1) ...
Selecting previously unselected package openjdk-11-jdk-headless:amd64.
Preparing to unpack .../7-openjdk-11-jdk-headless_11.0.19+7~us1-0ubuntu1~22.10.1_amd64.deb ...
Unpacking openjdk-11-jdk-headless:amd64 (11.0.19+7~us1-0ubuntu1~22.10.1) ...
Selecting previously unselected package openjdk-11-jdk:amd64.
Preparing to unpack .../8-openjdk-11-jdk_11.0.19+7~us1-0ubuntu1~22.10.1_amd64.deb ...
Unpacking openjdk-11-jdk:amd64 (11.0.19+7~us1-0ubuntu1~22.10.1) ...
Setting up java-common (0.72build2) ...
Setting up linux-image-5.19.0-42-generic (5.19.0-42.43) ...
Setting up fonts-dejavu-extra (2.37-2build1) ...
Setting up libatk-wrapper-java (0.40.0-2) ...
Setting up ca-certificates-java (20220719ubuntu0.1) ...
Adding debian:ACCVRAIZ1.pem
Adding debian:AC_RAIZ_FNMT-RCM.pem
Adding debian:AC_RAIZ_FNMT-RCM_SERVIDORES_SEGUROS.pem
Adding debian:Actalis_Authentication_Root_CA.pem
Adding debian:AffirmTrust_Commercial.pem
Adding debian:AffirmTrust_Networking.pem
Adding debian:AffirmTrust_Premium_ECC.pem
Adding debian:AffirmTrust_Premium.pem
Adding debian:Amazon_Root_CA_1.pem
Adding debian:Amazon_Root_CA_2.pem
Adding debian:Amazon_Root_CA_3.pem
Adding debian:Amazon_Root_CA_4.pem
Adding debian:ANF_Secure_Server_Root_CA.pem
Adding debian:Atos_TrustedRoot_2011.pem
Adding debian:Autoridad_de_Certificacion_Firmaprofesional_CIF_A62634068.pem
Adding debian:Baltimore_CyberTrust_Root.pem
Adding debian:Buypass_Class_2_Root_CA.pem
Adding debian:Buypass_Class_3_Root_CA.pem
Adding debian:CA_Disig_Root_R2.pem
Adding debian:Certigna.pem
Adding debian:Certigna_Root_CA.pem
Adding debian:certSIGN_Root_CA_G2.pem
Adding debian:certSIGN_ROOT_CA.pem
Adding debian:Certum_EC-384_CA.pem
Adding debian:Certum_Trusted_Network_CA_2.pem
Adding debian:Certum_Trusted_Network_CA.pem
Adding debian:Certum_Trusted_Root_CA.pem
Adding debian:CFCA_EV_ROOT.pem
Adding debian:Comodo_AAA_Services_root.pem
Adding debian:COMODO_Certification_Authority.pem
Adding debian:COMODO_ECC_Certification_Authority.pem
Adding debian:COMODO_RSA_Certification_Authority.pem
Adding debian:Cybertrust_Global_Root.pem
Adding debian:DigiCert_Assured_ID_Root_CA.pem
Adding debian:DigiCert_Assured_ID_Root_G2.pem
Adding debian:DigiCert_Assured_ID_Root_G3.pem
Adding debian:DigiCert_Global_Root_CA.pem
Adding debian:DigiCert_Global_Root_G2.pem
Adding debian:DigiCert_Global_Root_G3.pem
Adding debian:DigiCert_High_Assurance_EV_Root_CA.pem
Adding debian:DigiCert_Trusted_Root_G4.pem
Adding debian:D-TRUST_Root_Class_3_CA_2_2009.pem
Adding debian:D-TRUST_Root_Class_3_CA_2_EV_2009.pem
Adding debian:EC-ACC.pem
Adding debian:emSign_ECC_Root_CA_-_C3.pem
Adding debian:emSign_ECC_Root_CA_-_G3.pem
Adding debian:emSign_Root_CA_-_C1.pem
Adding debian:emSign_Root_CA_-_G1.pem
Adding debian:Entrust.net_Premium_2048_Secure_Server_CA.pem
Adding debian:Entrust_Root_Certification_Authority_-_EC1.pem
Adding debian:Entrust_Root_Certification_Authority_-_G2.pem
Adding debian:Entrust_Root_Certification_Authority_-_G4.pem
Adding debian:Entrust_Root_Certification_Authority.pem
Adding debian:ePKI_Root_Certification_Authority.pem
Adding debian:e-Szigno_Root_CA_2017.pem
Adding debian:E-Tugra_Certification_Authority.pem
Adding debian:GDCA_TrustAUTH_R5_ROOT.pem
Adding debian:GlobalSign_ECC_Root_CA_-_R4.pem
Adding debian:GlobalSign_ECC_Root_CA_-_R5.pem
Adding debian:GlobalSign_Root_CA.pem
Adding debian:GlobalSign_Root_CA_-_R2.pem
Adding debian:GlobalSign_Root_CA_-_R3.pem
Adding debian:GlobalSign_Root_CA_-_R6.pem
Adding debian:GlobalSign_Root_E46.pem
Adding debian:GlobalSign_Root_R46.pem
Adding debian:GLOBALTRUST_2020.pem
Adding debian:Go_Daddy_Class_2_CA.pem
Adding debian:Go_Daddy_Root_Certificate_Authority_-_G2.pem
Adding debian:GTS_Root_R1.pem
Adding debian:GTS_Root_R2.pem
Adding debian:GTS_Root_R3.pem
Adding debian:GTS_Root_R4.pem
Adding debian:Hellenic_Academic_and_Research_Institutions_ECC_RootCA_2015.pem
Adding debian:Hellenic_Academic_and_Research_Institutions_RootCA_2011.pem
Adding debian:Hellenic_Academic_and_Research_Institutions_RootCA_2015.pem
Adding debian:Hongkong_Post_Root_CA_1.pem
Adding debian:Hongkong_Post_Root_CA_3.pem
Adding debian:IdenTrust_Commercial_Root_CA_1.pem
Adding debian:IdenTrust_Public_Sector_Root_CA_1.pem
Adding debian:ISRG_Root_X1.pem
Adding debian:Izenpe.com.pem
Adding debian:Microsec_e-Szigno_Root_CA_2009.pem
Adding debian:Microsoft_ECC_Root_Certificate_Authority_2017.pem
Adding debian:Microsoft_RSA_Root_Certificate_Authority_2017.pem
Adding debian:NAVER_Global_Root_Certification_Authority.pem
Adding debian:NetLock_Arany_=Class_Gold=_Főtanúsítvány.pem
Adding debian:Network_Solutions_Certificate_Authority.pem
Adding debian:OISTE_WISeKey_Global_Root_GB_CA.pem
Adding debian:OISTE_WISeKey_Global_Root_GC_CA.pem
Adding debian:QuoVadis_Root_CA_1_G3.pem
Adding debian:QuoVadis_Root_CA_2_G3.pem
Adding debian:QuoVadis_Root_CA_2.pem
Adding debian:QuoVadis_Root_CA_3_G3.pem
Adding debian:QuoVadis_Root_CA_3.pem
Adding debian:Secure_Global_CA.pem
Adding debian:SecureSign_RootCA11.pem
Adding debian:SecureTrust_CA.pem
Adding debian:Security_Communication_RootCA2.pem
Adding debian:Security_Communication_Root_CA.pem
Adding debian:SSL.com_EV_Root_Certification_Authority_ECC.pem
Adding debian:SSL.com_EV_Root_Certification_Authority_RSA_R2.pem
Adding debian:SSL.com_Root_Certification_Authority_ECC.pem
Adding debian:SSL.com_Root_Certification_Authority_RSA.pem
Adding debian:Staat_der_Nederlanden_EV_Root_CA.pem
Adding debian:Starfield_Class_2_CA.pem
Adding debian:Starfield_Root_Certificate_Authority_-_G2.pem
Adding debian:Starfield_Services_Root_Certificate_Authority_-_G2.pem
Adding debian:SwissSign_Gold_CA_-_G2.pem
Adding debian:SwissSign_Silver_CA_-_G2.pem
Adding debian:SZAFIR_ROOT_CA2.pem
Adding debian:TeliaSonera_Root_CA_v1.pem
Adding debian:Trustwave_Global_Certification_Authority.pem
Adding debian:Trustwave_Global_ECC_P256_Certification_Authority.pem
Adding debian:Trustwave_Global_ECC_P384_Certification_Authority.pem
Adding debian:T-TeleSec_GlobalRoot_Class_2.pem
Adding debian:T-TeleSec_GlobalRoot_Class_3.pem
Adding debian:TUBITAK_Kamu_SM_SSL_Kok_Sertifikasi_-_Surum_1.pem
Adding debian:TWCA_Global_Root_CA.pem
Adding debian:TWCA_Root_Certification_Authority.pem
Adding debian:UCA_Extended_Validation_Root.pem
Adding debian:UCA_Global_G2_Root.pem
Adding debian:USERTrust_ECC_Certification_Authority.pem
Adding debian:USERTrust_RSA_Certification_Authority.pem
Adding debian:XRamp_Global_CA_Root.pem
done.
Setting up openjdk-11-jre-headless:amd64 (11.0.19+7~us1-0ubuntu1~22.10.1) ...
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/java to provide /usr/bin/java (
java) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/jjs to provide /usr/bin/jjs (jj
s) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/keytool to provide /usr/bin/key
tool (keytool) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/rmid to provide /usr/bin/rmid (
rmid) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/rmiregistry to provide /usr/bin
/rmiregistry (rmiregistry) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/pack200 to provide /usr/bin/pac
k200 (pack200) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/unpack200 to provide /usr/bin/u
npack200 (unpack200) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/lib/jexec to provide /usr/bin/jexec
 (jexec) in auto mode
Setting up libatk-wrapper-java-jni:amd64 (0.40.0-2) ...
Processing triggers for man-db (2.10.2-2) ...
Processing triggers for mailcap (3.70+nmu1ubuntu1) ...
Processing triggers for fontconfig (2.13.1-4.4ubuntu1) ...
Processing triggers for desktop-file-utils (0.26-1ubuntu4) ...
Processing triggers for hicolor-icon-theme (0.17-2) ...
Processing triggers for gnome-menus (3.36.0-1ubuntu3) ...
Processing triggers for ca-certificates-java (20220719ubuntu0.1) ...
done.
Setting up openjdk-11-jdk-headless:amd64 (11.0.19+7~us1-0ubuntu1~22.10.1) ...
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/jar to provide /usr/bin/jar (ja
r) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/jarsigner to provide /usr/bin/j
arsigner (jarsigner) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/javac to provide /usr/bin/javac
 (javac) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/javadoc to provide /usr/bin/jav
adoc (javadoc) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/javap to provide /usr/bin/javap
 (javap) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/jcmd to provide /usr/bin/jcmd (
jcmd) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/jdb to provide /usr/bin/jdb (jd
b) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/jdeprscan to provide /usr/bin/j
deprscan (jdeprscan) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/jdeps to provide /usr/bin/jdeps
 (jdeps) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/jfr to provide /usr/bin/jfr (jf
r) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/jimage to provide /usr/bin/jima
ge (jimage) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/jinfo to provide /usr/bin/jinfo
 (jinfo) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/jlink to provide /usr/bin/jlink
 (jlink) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/jmap to provide /usr/bin/jmap (
jmap) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/jmod to provide /usr/bin/jmod (
jmod) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/jps to provide /usr/bin/jps (jp
s) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/jrunscript to provide /usr/bin/
jrunscript (jrunscript) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/jshell to provide /usr/bin/jshe
ll (jshell) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/jstack to provide /usr/bin/jsta
ck (jstack) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/jstat to provide /usr/bin/jstat
 (jstat) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/jstatd to provide /usr/bin/jsta
td (jstatd) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/rmic to provide /usr/bin/rmic (
rmic) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/serialver to provide /usr/bin/s
erialver (serialver) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/jaotc to provide /usr/bin/jaotc
 (jaotc) in auto mode
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/jhsdb to provide /usr/bin/jhsdb
 (jhsdb) in auto mode
Setting up openjdk-11-jre:amd64 (11.0.19+7~us1-0ubuntu1~22.10.1) ...
Setting up openjdk-11-jdk:amd64 (11.0.19+7~us1-0ubuntu1~22.10.1) ...
update-alternatives: using /usr/lib/jvm/java-11-openjdk-amd64/bin/jconsole to provide /usr/bin/jc
onsole (jconsole) in auto mode
Processing triggers for linux-image-5.19.0-42-generic (5.19.0-42.43) ...
/etc/kernel/postinst.d/dkms:
 * dkms: running auto installation service for kernel 5.19.0-42-generic
   ...done.
/etc/kernel/postinst.d/initramfs-tools:
update-initramfs: Generating /boot/initrd.img-5.19.0-42-generic
/etc/kernel/postinst.d/vboxadd:
run-parts: failed to exec /etc/kernel/postinst.d/vboxadd: Exec format error
run-parts: /etc/kernel/postinst.d/vboxadd exited with return code 1
dpkg: error processing package linux-image-5.19.0-42-generic (--configure):
 installed linux-image-5.19.0-42-generic package post-installation script subprocess returned err
or exit status 1
Errors were encountered while processing:
 linux-image-5.19.0-42-generic
E: Sub-process /usr/bin/dpkg returned an error code (1)
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ sudo apt install curl
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  linux-headers-5.19.0-21 linux-headers-5.19.0-21-generic linux-image-5.19.0-21-generic
  linux-modules-5.19.0-21-generic linux-modules-extra-5.19.0-21-generic
Use 'sudo apt autoremove' to remove them.
The following NEW packages will be installed:
  curl
0 upgraded, 1 newly installed, 0 to remove and 26 not upgraded.
1 not fully installed or removed.
Need to get 199 kB of archives.
After this operation, 472 kB of additional disk space will be used.
Get:1 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/main amd64 curl amd64 7.85.0-1ubuntu0.5 [199 kB]
Fetched 199 kB in 0s (676 kB/s)
Selecting previously unselected package curl.
(Reading database ... 294777 files and directories currently installed.)
Preparing to unpack .../curl_7.85.0-1ubuntu0.5_amd64.deb ...
Unpacking curl (7.85.0-1ubuntu0.5) ...
Setting up linux-image-5.19.0-42-generic (5.19.0-42.43) ...
Setting up curl (7.85.0-1ubuntu0.5) ...
Processing triggers for man-db (2.10.2-2) ...
Processing triggers for linux-image-5.19.0-42-generic (5.19.0-42.43) ...
/etc/kernel/postinst.d/dkms:
 * dkms: running auto installation service for kernel 5.19.0-42-generic
   ...done.
/etc/kernel/postinst.d/initramfs-tools:
update-initramfs: Generating /boot/initrd.img-5.19.0-42-generic
/etc/kernel/postinst.d/vboxadd:
run-parts: failed to exec /etc/kernel/postinst.d/vboxadd: Exec format error
run-parts: /etc/kernel/postinst.d/vboxadd exited with return code 1
dpkg: error processing package linux-image-5.19.0-42-generic (--configure):
 installed linux-image-5.19.0-42-generic package post-installation script subprocess returned err
or exit status 1
Errors were encountered while processing:
 linux-image-5.19.0-42-generic
E: Sub-process /usr/bin/dpkg returned an error code (1)
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ ^[[200~curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
>   /usr/share/keyrings/jenkins-keyring.asc > /dev/null~
bash: /dev/null~: Permission denied
curl: command not found
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee   /usr/share/keyrings/jenkins-keyring.asc > /dev/null~
bash: /dev/null~: Permission denied
curl: (23) Failed writing body
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee   /usr/share/keyrings/jenkins-keyring.asc > /dev/null
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ sudo apt-get update
Get:1 http://security.ubuntu.com/ubuntu kinetic-security InRelease [109 kB]
Ign:2 https://pkg.jenkins.io/debian-stable binary/ InRelease                                    
Hit:3 http://ro.archive.ubuntu.com/ubuntu kinetic InRelease                                     
Get:4 https://pkg.jenkins.io/debian-stable binary/ Release [2.044 B]
Get:5 https://pkg.jenkins.io/debian-stable binary/ Release.gpg [833 B]                   
Get:6 http://ro.archive.ubuntu.com/ubuntu kinetic-updates InRelease [118 kB]
Get:7 http://security.ubuntu.com/ubuntu kinetic-security/main amd64 DEP-11 Metadata [30,1 kB]
Get:8 https://pkg.jenkins.io/debian-stable binary/ Packages [24,8 kB]                           
Get:9 http://security.ubuntu.com/ubuntu kinetic-security/universe amd64 DEP-11 Metadata [7.840 B]
Get:10 http://ro.archive.ubuntu.com/ubuntu kinetic-backports InRelease [99,9 kB]
Get:11 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/main amd64 DEP-11 Metadata [85,7 kB]
Get:12 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/universe amd64 DEP-11 Metadata [41,4 kB]
Get:13 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/multiverse amd64 DEP-11 Metadata [212 B]
Get:14 http://ro.archive.ubuntu.com/ubuntu kinetic-backports/universe amd64 DEP-11 Metadata [10,5 kB]
Fetched 530 kB in 1s (380 kB/s)              
Reading package lists... Done
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ sudo apt-get install jenkins
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  linux-headers-5.19.0-21 linux-headers-5.19.0-21-generic linux-image-5.19.0-21-generic
  linux-modules-5.19.0-21-generic linux-modules-extra-5.19.0-21-generic
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  net-tools
The following NEW packages will be installed:
  jenkins net-tools
0 upgraded, 2 newly installed, 0 to remove and 26 not upgraded.
1 not fully installed or removed.
Need to get 98,1 MB of archives.
After this operation, 99,3 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://ro.archive.ubuntu.com/ubuntu kinetic/main amd64 net-tools amd64 1.60+git20181103.0eebece-1ubuntu5 [204 kB]
Get:2 https://pkg.jenkins.io/debian-stable binary/ jenkins 2.387.3 [97,9 MB]     
Fetched 98,1 MB in 19s (5.094 kB/s)                                                             
Selecting previously unselected package net-tools.
(Reading database ... 294784 files and directories currently installed.)
Preparing to unpack .../net-tools_1.60+git20181103.0eebece-1ubuntu5_amd64.deb ...
Unpacking net-tools (1.60+git20181103.0eebece-1ubuntu5) ...
Selecting previously unselected package jenkins.
Preparing to unpack .../jenkins_2.387.3_all.deb ...
Unpacking jenkins (2.387.3) ...
Setting up net-tools (1.60+git20181103.0eebece-1ubuntu5) ...
Setting up jenkins (2.387.3) ...
Created symlink /etc/systemd/system/multi-user.target.wants/jenkins.service → /lib/systemd/system/jenkins.service.
Setting up linux-image-5.19.0-42-generic (5.19.0-42.43) ...
Processing triggers for man-db (2.10.2-2) ...
Processing triggers for linux-image-5.19.0-42-generic (5.19.0-42.43) ...
/etc/kernel/postinst.d/dkms:
 * dkms: running auto installation service for kernel 5.19.0-42-generic
   ...done.
/etc/kernel/postinst.d/initramfs-tools:
update-initramfs: Generating /boot/initrd.img-5.19.0-42-generic
/etc/kernel/postinst.d/vboxadd:
run-parts: failed to exec /etc/kernel/postinst.d/vboxadd: Exec format error
run-parts: /etc/kernel/postinst.d/vboxadd exited with return code 1
dpkg: error processing package linux-image-5.19.0-42-generic (--configure):
 installed linux-image-5.19.0-42-generic package post-installation script subprocess returned error exit status 1
Errors were encountered while processing:
 linux-image-5.19.0-42-generic
E: Sub-process /usr/bin/dpkg returned an error code (1)
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ ^C
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ sudo dpkg --configure -a
Setting up linux-image-5.19.0-42-generic (5.19.0-42.43) ...
Processing triggers for linux-image-5.19.0-42-generic (5.19.0-42.43) ...
/etc/kernel/postinst.d/dkms:
 * dkms: running auto installation service for kernel 5.19.0-42-generic
   ...done.
/etc/kernel/postinst.d/initramfs-tools:
update-initramfs: Generating /boot/initrd.img-5.19.0-42-generic
/etc/kernel/postinst.d/vboxadd:
run-parts: failed to exec /etc/kernel/postinst.d/vboxadd: Exec format error
run-parts: /etc/kernel/postinst.d/vboxadd exited with return code 1
dpkg: error processing package linux-image-5.19.0-42-generic (--configure):
 installed linux-image-5.19.0-42-generic package post-installation script subprocess returned error exit status 1
Errors were encountered while processing:
 linux-image-5.19.0-42-generic
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]   https://pkg.jenkins.io/debian-stable binary/ | sudo tee   /etc/apt/sources.list.d/jenkins.list > /dev/null
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ sudo apt-get update
Hit:1 http://security.ubuntu.com/ubuntu kinetic-security InRelease
Ign:2 https://pkg.jenkins.io/debian-stable binary/ InRelease                                    
Hit:3 http://ro.archive.ubuntu.com/ubuntu kinetic InRelease
Hit:4 https://pkg.jenkins.io/debian-stable binary/ Release
Hit:5 http://ro.archive.ubuntu.com/ubuntu kinetic-updates InRelease
Hit:7 http://ro.archive.ubuntu.com/ubuntu kinetic-backports InRelease
Reading package lists... Done
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ sudo apt-get install jenkins
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
jenkins is already the newest version (2.387.3).
The following packages were automatically installed and are no longer required:
  linux-headers-5.19.0-21 linux-headers-5.19.0-21-generic linux-image-5.19.0-21-generic
  linux-modules-5.19.0-21-generic linux-modules-extra-5.19.0-21-generic
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 26 not upgraded.
1 not fully installed or removed.
After this operation, 0 B of additional disk space will be used.
Do you want to continue? [Y/n] y
Setting up linux-image-5.19.0-42-generic (5.19.0-42.43) ...
Processing triggers for linux-image-5.19.0-42-generic (5.19.0-42.43) ...
/etc/kernel/postinst.d/dkms:
 * dkms: running auto installation service for kernel 5.19.0-42-generic
   ...done.
/etc/kernel/postinst.d/initramfs-tools:
update-initramfs: Generating /boot/initrd.img-5.19.0-42-generic
/etc/kernel/postinst.d/vboxadd:
run-parts: failed to exec /etc/kernel/postinst.d/vboxadd: Exec format error
run-parts: /etc/kernel/postinst.d/vboxadd exited with return code 1
dpkg: error processing package linux-image-5.19.0-42-generic (--configure):
 installed linux-image-5.19.0-42-generic package post-installation script subprocess returned error exit status 1
Errors were encountered while processing:
 linux-image-5.19.0-42-generic
E: Sub-process /usr/bin/dpkg returned an error code (1)
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ sudo systemctl status jenkins
● jenkins.service - Jenkins Continuous Integration Server
     Loaded: loaded (/lib/systemd/system/jenkins.service; enabled; preset: enabled)
     Active: active (running) since Fri 2023-05-19 17:26:52 EEST; 6min ago
   Main PID: 29006 (java)
      Tasks: 44 (limit: 9448)
     Memory: 2.1G
        CPU: 1min 5.996s
     CGroup: /system.slice/jenkins.service
             └─29006 /usr/bin/java -Djava.awt.headless=true -jar /usr/share/java/jenkins.war --w>

mai 19 17:26:30 gabriel-VirtualBox jenkins[29006]: 5088c14b3b094022942504a52e086633
mai 19 17:26:30 gabriel-VirtualBox jenkins[29006]: This may also be found at: /var/lib/jenkins/s>
mai 19 17:26:30 gabriel-VirtualBox jenkins[29006]: *********************************************>
mai 19 17:26:30 gabriel-VirtualBox jenkins[29006]: *********************************************>
mai 19 17:26:30 gabriel-VirtualBox jenkins[29006]: *********************************************>
mai 19 17:26:52 gabriel-VirtualBox jenkins[29006]: 2023-05-19 14:26:52.045+0000 [id=30]        I>
mai 19 17:26:52 gabriel-VirtualBox jenkins[29006]: 2023-05-19 14:26:52.060+0000 [id=23]        I>
mai 19 17:26:52 gabriel-VirtualBox systemd[1]: Started Jenkins Continuous Integration Server.
mai 19 17:26:52 gabriel-VirtualBox jenkins[29006]: 2023-05-19 14:26:52.789+0000 [id=51]        I>
mai 19 17:26:52 gabriel-VirtualBox jenkins[29006]: 2023-05-19 14:26:52.790+0000 [id=51]        I>
lines 1-20/20 (END)

















































● jenkins.service - Jenkins Continuous Integration Server
     Loaded: loaded (/lib/systemd/system/jenkins.service; enabled; preset: enabled)
     Active: active (running) since Fri 2023-05-19 17:26:52 EEST; 6min ago
   Main PID: 29006 (java)
      Tasks: 44 (limit: 9448)
     Memory: 2.1G
        CPU: 1min 5.996s
     CGroup: /system.slice/jenkins.service
             └─29006 /usr/bin/java -Djava.awt.headless=true -jar /usr/share/java/jenkins.war --webroot=>

mai 19 17:26:30 gabriel-VirtualBox jenkins[29006]: 5088c14b3b094022942504a52e086633
mai 19 17:26:30 gabriel-VirtualBox jenkins[29006]: This may also be found at: /var/lib/jenkins/secrets/>
mai 19 17:26:30 gabriel-VirtualBox jenkins[29006]: ****************************************************>
mai 19 17:26:30 gabriel-VirtualBox jenkins[29006]: ****************************************************>
mai 19 17:26:30 gabriel-VirtualBox jenkins[29006]: ****************************************************>
mai 19 17:26:52 gabriel-VirtualBox jenkins[29006]: 2023-05-19 14:26:52.045+0000 [id=30]        INFO    >
mai 19 17:26:52 gabriel-VirtualBox jenkins[29006]: 2023-05-19 14:26:52.060+0000 [id=23]        INFO    >
mai 19 17:26:52 gabriel-VirtualBox systemd[1]: Started Jenkins Continuous Integration Server.
mai 19 17:26:52 gabriel-VirtualBox jenkins[29006]: 2023-05-19 14:26:52.789+0000 [id=51]        INFO    >
mai 19 17:26:52 gabriel-VirtualBox jenkins[29006]: 2023-05-19 14:26:52.790+0000 [id=51]        INFO    >
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
lines 1-20/20 (END)

















































● jenkins.service - Jenkins Continuous Integration Server
     Loaded: loaded (/lib/systemd/system/jenkins.service; enabled; preset: enabled)
     Active: active (running) since Fri 2023-05-19 17:26:52 EEST; 6min ago
   Main PID: 29006 (java)
      Tasks: 44 (limit: 9448)
     Memory: 2.1G
        CPU: 1min 5.996s
     CGroup: /system.slice/jenkins.service
             └─29006 /usr/bin/java -Djava.awt.headless=true -jar /usr/share/java/jenkins.war --w>

mai 19 17:26:30 gabriel-VirtualBox jenkins[29006]: 5088c14b3b094022942504a52e086633
mai 19 17:26:30 gabriel-VirtualBox jenkins[29006]: This may also be found at: /var/lib/jenkins/s>
mai 19 17:26:30 gabriel-VirtualBox jenkins[29006]: *********************************************>
mai 19 17:26:30 gabriel-VirtualBox jenkins[29006]: *********************************************>
mai 19 17:26:30 gabriel-VirtualBox jenkins[29006]: *********************************************>
mai 19 17:26:52 gabriel-VirtualBox jenkins[29006]: 2023-05-19 14:26:52.045+0000 [id=30]        I>
mai 19 17:26:52 gabriel-VirtualBox jenkins[29006]: 2023-05-19 14:26:52.060+0000 [id=23]        I>
mai 19 17:26:52 gabriel-VirtualBox systemd[1]: Started Jenkins Continuous Integration Server.
mai 19 17:26:52 gabriel-VirtualBox jenkins[29006]: 2023-05-19 14:26:52.789+0000 [id=51]        I>
mai 19 17:26:52 gabriel-VirtualBox jenkins[29006]: 2023-05-19 14:26:52.790+0000 [id=51]        I>
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~

gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ sudo cat /var/lib/jenkins/secrets/initialAdminPassword
5088c14b3b094022942504a52e086633
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ git branch
* devel/Gabello8_flori
  main
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ ls -l
total 12
drwxrwxr-x 5 gabriel gabriel 4096 mai 19 16:33 app
-rw-rw-r-- 1 gabriel gabriel    0 mai 19 15:46 fisier.py
-rw-rw-r-- 1 gabriel gabriel 1539 mai 19 16:32 Jenkinsfile
-rw-rw-r-- 1 gabriel gabriel   28 mai 19 15:19 README.md
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ cd app
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ source activeaza_venv
bash: ../.venv/bin/activate: No such file or directory
FAIL: cannot activate venv
Trying to create the venv in the folder: .venv
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt install python3.10-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.

Failing command: ['/home/gabriel/git/curs_vcgj_444D_flori/.venv/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']

Activating virtual environment
bash: ../.venv/bin/activate: No such file or directory
Installing the dependencies
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: flask in /usr/lib/python3/dist-packages (2.0.3)
Defaulting to user installation because normal site-packages is not writeable
Collecting flask-bootstrap
  Downloading Flask-Bootstrap-3.3.7.1.tar.gz (456 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 456.4/456.4 kB 2.0 MB/s eta 0:00:00
  Preparing metadata (setup.py) ... done
Requirement already satisfied: Flask>=0.8 in /usr/lib/python3/dist-packages (from flask-bootstrap) (2.0.3)
Collecting dominate
  Downloading dominate-2.7.0-py2.py3-none-any.whl (29 kB)
Collecting visitor
  Downloading visitor-0.1.3.tar.gz (3.3 kB)
  Preparing metadata (setup.py) ... done
Building wheels for collected packages: flask-bootstrap, visitor
  Building wheel for flask-bootstrap (setup.py) ... done
  Created wheel for flask-bootstrap: filename=Flask_Bootstrap-3.3.7.1-py3-none-any.whl size=460123 sha256=ce9c25f74a2b37159e0d110f63f56210392799019c09008c69d4260e02a756df
  Stored in directory: /home/gabriel/.cache/pip/wheels/6f/33/ad/26540e84a28334e5dfeda756df270f95353779f03bc5cf40d4
  Building wheel for visitor (setup.py) ... done
  Created wheel for visitor: filename=visitor-0.1.3-py3-none-any.whl size=3946 sha256=ff466fe43bfd26b30d93ad9ec9f969e2eed124dd1a998a9d548db0b952e233bb
  Stored in directory: /home/gabriel/.cache/pip/wheels/19/31/99/2ec5b4459cac4d801d6201d501a354366d180afc9f8bb2d333
Successfully built flask-bootstrap visitor
Installing collected packages: visitor, dominate, flask-bootstrap
Successfully installed dominate-2.7.0 flask-bootstrap-3.3.7.1 visitor-0.1.3
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: pytest in /home/gabriel/.local/lib/python3.10/site-packages (7.3.1)
Requirement already satisfied: iniconfig in /home/gabriel/.local/lib/python3.10/site-packages (from pytest) (2.0.0)
Requirement already satisfied: exceptiongroup>=1.0.0rc8 in /home/gabriel/.local/lib/python3.10/site-packages (from pytest) (1.1.1)
Requirement already satisfied: tomli>=1.0.0 in /home/gabriel/.local/lib/python3.10/site-packages (from pytest) (2.0.1)
Requirement already satisfied: packaging in /usr/lib/python3/dist-packages (from pytest) (21.3)
Requirement already satisfied: pluggy<2.0,>=0.12 in /home/gabriel/.local/lib/python3.10/site-packages (from pytest) (1.0.0)
Defaulting to user installation because normal site-packages is not writeable
Collecting pylint
  Downloading pylint-2.17.4-py3-none-any.whl (536 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 536.6/536.6 kB 2.3 MB/s eta 0:00:00
Collecting tomlkit>=0.10.1
  Downloading tomlkit-0.11.8-py3-none-any.whl (35 kB)
Collecting dill>=0.2
  Downloading dill-0.3.6-py3-none-any.whl (110 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 110.5/110.5 kB 3.8 MB/s eta 0:00:00
Collecting isort<6,>=4.2.5
  Downloading isort-5.12.0-py3-none-any.whl (91 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 91.2/91.2 kB 2.9 MB/s eta 0:00:00
Requirement already satisfied: tomli>=1.1.0 in /home/gabriel/.local/lib/python3.10/site-packages (from pylint) (2.0.1)
Collecting mccabe<0.8,>=0.6
  Downloading mccabe-0.7.0-py2.py3-none-any.whl (7.3 kB)
Collecting platformdirs>=2.2.0
  Downloading platformdirs-3.5.1-py3-none-any.whl (15 kB)
Collecting astroid<=2.17.0-dev0,>=2.15.4
  Downloading astroid-2.15.5-py3-none-any.whl (278 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 278.1/278.1 kB 4.1 MB/s eta 0:00:00
Collecting lazy-object-proxy>=1.4.0
  Downloading lazy_object_proxy-1.9.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (63 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 63.3/63.3 kB 3.8 MB/s eta 0:00:00
Requirement already satisfied: wrapt<2,>=1.11 in /usr/lib/python3/dist-packages (from astroid<=2.17.0-dev0,>=2.15.4->pylint) (1.13.3)
Collecting typing-extensions>=4.0.0
  Downloading typing_extensions-4.5.0-py3-none-any.whl (27 kB)
Installing collected packages: typing-extensions, tomlkit, platformdirs, mccabe, lazy-object-proxy, isort, dill, astroid, pylint
  WARNING: The scripts isort and isort-identify-imports are installed in '/home/gabriel/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts epylint, pylint, pylint-config, pyreverse and symilar are installed in '/home/gabriel/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed astroid-2.15.5 dill-0.3.6 isort-5.12.0 lazy-object-proxy-1.9.0 mccabe-0.7.0 platformdirs-3.5.1 pylint-2.17.4 tomlkit-0.11.8 typing-extensions-4.5.0
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ source activeaza_venv_jenkins
Trying to create the venv in the folder: .venv
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt install python3.10-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.

Failing command: ['/home/gabriel/git/curs_vcgj_444D_flori/.venv/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']

Activating virtual environment
bash: ../.venv/bin/activate: No such file or directory
Installing the dependencies
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: flask in /usr/lib/python3/dist-packages (2.0.3)
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: flask-bootstrap in /home/gabriel/.local/lib/python3.10/site-packages (3.3.7.1)
Requirement already satisfied: dominate in /home/gabriel/.local/lib/python3.10/site-packages (from flask-bootstrap) (2.7.0)
Requirement already satisfied: visitor in /home/gabriel/.local/lib/python3.10/site-packages (from flask-bootstrap) (0.1.3)
Requirement already satisfied: Flask>=0.8 in /usr/lib/python3/dist-packages (from flask-bootstrap) (2.0.3)
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: pytest in /home/gabriel/.local/lib/python3.10/site-packages (7.3.1)
Requirement already satisfied: pluggy<2.0,>=0.12 in /home/gabriel/.local/lib/python3.10/site-packages (from pytest) (1.0.0)
Requirement already satisfied: packaging in /usr/lib/python3/dist-packages (from pytest) (21.3)
Requirement already satisfied: tomli>=1.0.0 in /home/gabriel/.local/lib/python3.10/site-packages (from pytest) (2.0.1)
Requirement already satisfied: iniconfig in /home/gabriel/.local/lib/python3.10/site-packages (from pytest) (2.0.0)
Requirement already satisfied: exceptiongroup>=1.0.0rc8 in /home/gabriel/.local/lib/python3.10/site-packages (from pytest) (1.1.1)
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: pylint in /home/gabriel/.local/lib/python3.10/site-packages (2.17.4)
Requirement already satisfied: astroid<=2.17.0-dev0,>=2.15.4 in /home/gabriel/.local/lib/python3.10/site-packages (from pylint) (2.15.5)
Requirement already satisfied: isort<6,>=4.2.5 in /home/gabriel/.local/lib/python3.10/site-packages (from pylint) (5.12.0)
Requirement already satisfied: tomlkit>=0.10.1 in /home/gabriel/.local/lib/python3.10/site-packages (from pylint) (0.11.8)
Requirement already satisfied: tomli>=1.1.0 in /home/gabriel/.local/lib/python3.10/site-packages (from pylint) (2.0.1)
Requirement already satisfied: mccabe<0.8,>=0.6 in /home/gabriel/.local/lib/python3.10/site-packages (from pylint) (0.7.0)
Requirement already satisfied: platformdirs>=2.2.0 in /home/gabriel/.local/lib/python3.10/site-packages (from pylint) (3.5.1)
Requirement already satisfied: dill>=0.2 in /home/gabriel/.local/lib/python3.10/site-packages (from pylint) (0.3.6)
Requirement already satisfied: lazy-object-proxy>=1.4.0 in /home/gabriel/.local/lib/python3.10/site-packages (from astroid<=2.17.0-dev0,>=2.15.4->pylint) (1.9.0)
Requirement already satisfied: typing-extensions>=4.0.0 in /home/gabriel/.local/lib/python3.10/site-packages (from astroid<=2.17.0-dev0,>=2.15.4->pylint) (4.5.0)
Requirement already satisfied: wrapt<2,>=1.11 in /usr/lib/python3/dist-packages (from astroid<=2.17.0-dev0,>=2.15.4->pylint) (1.13.3)
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ git status
On branch devel/Gabello8_flori
Your branch is up to date with 'origin/devel/Gabello8_flori'.

nothing to commit, working tree clean
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ sudo apt install python3-venv
[sudo] password for gabriel: 
Sorry, try again.
[sudo] password for gabriel: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  linux-headers-5.19.0-21 linux-headers-5.19.0-21-generic linux-image-5.19.0-21-generic
  linux-modules-5.19.0-21-generic linux-modules-extra-5.19.0-21-generic
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  python3-pip-whl python3-setuptools-whl python3.10-venv
The following NEW packages will be installed:
  python3-pip-whl python3-setuptools-whl python3-venv python3.10-venv
0 upgraded, 4 newly installed, 0 to remove and 26 not upgraded.
1 not fully installed or removed.
Need to get 2.430 kB of archives.
After this operation, 2.847 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/universe amd64 python3-pip-whl all 22.2+dfsg-1ubuntu0.2 [1.636 kB]
Get:2 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/universe amd64 python3-setuptools-whl all 59.6.0-1.2ubuntu0.22.10.1 [788 kB]
Get:3 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/universe amd64 python3.10-venv amd64 3.10.7-1ubuntu0.3 [5.718 B]
Get:4 http://ro.archive.ubuntu.com/ubuntu kinetic/universe amd64 python3-venv amd64 3.10.6-1 [1.036 B]
Fetched 2.430 kB in 2s (1.393 kB/s)      
Selecting previously unselected package python3-pip-whl.
(Reading database ... 294847 files and directories currently installed.)
Preparing to unpack .../python3-pip-whl_22.2+dfsg-1ubuntu0.2_all.deb ...
Unpacking python3-pip-whl (22.2+dfsg-1ubuntu0.2) ...
Selecting previously unselected package python3-setuptools-whl.
Preparing to unpack .../python3-setuptools-whl_59.6.0-1.2ubuntu0.22.10.1_all.deb ...
Unpacking python3-setuptools-whl (59.6.0-1.2ubuntu0.22.10.1) ...
Selecting previously unselected package python3.10-venv.
Preparing to unpack .../python3.10-venv_3.10.7-1ubuntu0.3_amd64.deb ...
Unpacking python3.10-venv (3.10.7-1ubuntu0.3) ...
Selecting previously unselected package python3-venv.
Preparing to unpack .../python3-venv_3.10.6-1_amd64.deb ...
Unpacking python3-venv (3.10.6-1) ...
Setting up python3-setuptools-whl (59.6.0-1.2ubuntu0.22.10.1) ...
Setting up python3-pip-whl (22.2+dfsg-1ubuntu0.2) ...
Setting up linux-image-5.19.0-42-generic (5.19.0-42.43) ...
Setting up python3.10-venv (3.10.7-1ubuntu0.3) ...
Setting up python3-venv (3.10.6-1) ...
Processing triggers for linux-image-5.19.0-42-generic (5.19.0-42.43) ...
/etc/kernel/postinst.d/dkms:
 * dkms: running auto installation service for kernel 5.19.0-42-generic
   ...done.
/etc/kernel/postinst.d/initramfs-tools:
update-initramfs: Generating /boot/initrd.img-5.19.0-42-generic
/etc/kernel/postinst.d/vboxadd:
run-parts: failed to exec /etc/kernel/postinst.d/vboxadd: Exec format error
run-parts: /etc/kernel/postinst.d/vboxadd exited with return code 1
dpkg: error processing package linux-image-5.19.0-42-generic (--configure):
 installed linux-image-5.19.0-42-generic package post-installation script subprocess returned error exit
 status 1
Errors were encountered while processing:
 linux-image-5.19.0-42-generic
E: Sub-process /usr/bin/dpkg returned an error code (1)
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ pip install pylint
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: pylint in /home/gabriel/.local/lib/python3.10/site-packages (2.17.4)
Requirement already satisfied: platformdirs>=2.2.0 in /home/gabriel/.local/lib/python3.10/site-packages (from pylint) (3.5.1)
Requirement already satisfied: isort<6,>=4.2.5 in /home/gabriel/.local/lib/python3.10/site-packages (from pylint) (5.12.0)
Requirement already satisfied: dill>=0.2 in /home/gabriel/.local/lib/python3.10/site-packages (from pylint) (0.3.6)
Requirement already satisfied: tomli>=1.1.0 in /home/gabriel/.local/lib/python3.10/site-packages (from pylint) (2.0.1)
Requirement already satisfied: astroid<=2.17.0-dev0,>=2.15.4 in /home/gabriel/.local/lib/python3.10/site-packages (from pylint) (2.15.5)
Requirement already satisfied: tomlkit>=0.10.1 in /home/gabriel/.local/lib/python3.10/site-packages (from pylint) (0.11.8)
Requirement already satisfied: mccabe<0.8,>=0.6 in /home/gabriel/.local/lib/python3.10/site-packages (from pylint) (0.7.0)
Requirement already satisfied: wrapt<2,>=1.11 in /usr/lib/python3/dist-packages (from astroid<=2.17.0-dev0,>=2.15.4->pylint) (1.13.3)
Requirement already satisfied: lazy-object-proxy>=1.4.0 in /home/gabriel/.local/lib/python3.10/site-packages (from astroid<=2.17.0-dev0,>=2.15.4->pylint) (1.9.0)
Requirement already satisfied: typing-extensions>=4.0.0 in /home/gabriel/.local/lib/python3.10/site-packages (from astroid<=2.17.0-dev0,>=2.15.4->pylint) (4.5.0)
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ cd
gabriel@gabriel-VirtualBox:~$ sudo apt-get update
[sudo] password for gabriel: 
Get:1 http://security.ubuntu.com/ubuntu kinetic-security InRelease [109 kB]
Hit:2 http://ro.archive.ubuntu.com/ubuntu kinetic InRelease                                     
Ign:3 https://pkg.jenkins.io/debian-stable binary/ InRelease                                    
Hit:4 https://pkg.jenkins.io/debian-stable binary/ Release
Get:5 http://ro.archive.ubuntu.com/ubuntu kinetic-updates InRelease [118 kB]
Get:7 http://ro.archive.ubuntu.com/ubuntu kinetic-backports InRelease [99,9 kB]
Get:8 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/main i386 Packages [187 kB]
Get:9 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/main amd64 Packages [316 kB]
Fetched 830 kB in 2s (477 kB/s)                           
Reading package lists... Done
gabriel@gabriel-VirtualBox:~$ sudo apt-get install ca-certificates curl gnupg lsb-release
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
ca-certificates is already the newest version (20211016ubuntu0.22.10.1).
ca-certificates set to manually installed.
curl is already the newest version (7.85.0-1ubuntu0.5).
gnupg is already the newest version (2.2.35-3ubuntu1).
gnupg set to manually installed.
lsb-release is already the newest version (11.2ubuntu1).
lsb-release set to manually installed.
The following packages were automatically installed and are no longer required:
  linux-headers-5.19.0-21 linux-headers-5.19.0-21-generic linux-image-5.19.0-21-generic linux-modules-5.19.0-21-generic linux-modules-extra-5.19.0-21-generic
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 26 not upgraded.
1 not fully installed or removed.
After this operation, 0 B of additional disk space will be used.
Do you want to continue? [Y/n] y
Setting up linux-image-5.19.0-42-generic (5.19.0-42.43) ...
Processing triggers for linux-image-5.19.0-42-generic (5.19.0-42.43) ...
/etc/kernel/postinst.d/dkms:
 * dkms: running auto installation service for kernel 5.19.0-42-generic
   ...done.
/etc/kernel/postinst.d/initramfs-tools:
update-initramfs: Generating /boot/initrd.img-5.19.0-42-generic
/etc/kernel/postinst.d/vboxadd:
run-parts: failed to exec /etc/kernel/postinst.d/vboxadd: Exec format error
run-parts: /etc/kernel/postinst.d/vboxadd exited with return code 1
dpkg: error processing package linux-image-5.19.0-42-generic (--configure):
 installed linux-image-5.19.0-42-generic package post-installation script subprocess returned error exit status 1
Errors were encountered while processing:
 linux-image-5.19.0-42-generic
E: Sub-process /usr/bin/dpkg returned an error code (1)
gabriel@gabriel-VirtualBox:~$ sudo mkdir -p /etc/apt/keyrings
gabriel@gabriel-VirtualBox:~$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
gabriel@gabriel-VirtualBox:~$ echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
gabriel@gabriel-VirtualBox:~$ sudo apt-get update
Get:1 https://download.docker.com/linux/ubuntu kinetic InRelease [48,9 kB]
Get:2 https://download.docker.com/linux/ubuntu kinetic/stable amd64 Packages [11,9 kB]                                                                                                      
Ign:3 https://pkg.jenkins.io/debian-stable binary/ InRelease                                          
Hit:4 http://ro.archive.ubuntu.com/ubuntu kinetic InRelease         
Get:5 http://security.ubuntu.com/ubuntu kinetic-security InRelease [109 kB]
Hit:6 https://pkg.jenkins.io/debian-stable binary/ Release                    
Get:7 http://ro.archive.ubuntu.com/ubuntu kinetic-updates InRelease [118 kB]  
Get:9 http://ro.archive.ubuntu.com/ubuntu kinetic-backports InRelease [99,9 kB]
Get:10 http://security.ubuntu.com/ubuntu kinetic-security/main amd64 DEP-11 Metadata [30,1 kB]
Get:11 http://security.ubuntu.com/ubuntu kinetic-security/universe amd64 DEP-11 Metadata [7.860 B]
Get:12 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/main amd64 DEP-11 Metadata [86,0 kB]
Get:13 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/universe amd64 DEP-11 Metadata [41,3 kB]
Get:14 http://ro.archive.ubuntu.com/ubuntu kinetic-updates/multiverse amd64 DEP-11 Metadata [212 B]
Get:15 http://ro.archive.ubuntu.com/ubuntu kinetic-backports/universe amd64 DEP-11 Metadata [10,6 kB]
Fetched 563 kB in 1s (410 kB/s)              
Reading package lists... Done
gabriel@gabriel-VirtualBox:~$ sudo chmod 777 /etc/apt/keyrings/docker.gpg
gabriel@gabriel-VirtualBox:~$ sudo apt-get update
Hit:1 https://download.docker.com/linux/ubuntu kinetic InRelease
Ign:2 https://pkg.jenkins.io/debian-stable binary/ InRelease                                                                                             
Hit:3 https://pkg.jenkins.io/debian-stable binary/ Release                                       
Hit:4 http://ro.archive.ubuntu.com/ubuntu kinetic InRelease
Hit:6 http://security.ubuntu.com/ubuntu kinetic-security InRelease
Hit:7 http://ro.archive.ubuntu.com/ubuntu kinetic-updates InRelease
Hit:8 http://ro.archive.ubuntu.com/ubuntu kinetic-backports InRelease
Reading package lists... Done
gabriel@gabriel-VirtualBox:~$ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-compose –y
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package –y
gabriel@gabriel-VirtualBox:~$ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-compose
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  linux-headers-5.19.0-21 linux-headers-5.19.0-21-generic linux-image-5.19.0-21-generic linux-modules-5.19.0-21-generic linux-modules-extra-5.19.0-21-generic
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  docker-buildx-plugin docker-ce-rootless-extras libslirp0 pigz python3-docker python3-dockerpty python3-docopt python3-dotenv python3-jsonschema python3-pyrsistent python3-texttable python3-websocket
  slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite python-jsonschema-doc python3-json-pointer python3-rfc3987 python3-uritemplate python3-webcolors
Recommended packages:
  docker.io
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli docker-ce-rootless-extras docker-compose docker-compose-plugin libslirp0 pigz python3-docker python3-dockerpty python3-docopt python3-dotenv
  python3-jsonschema python3-pyrsistent python3-texttable python3-websocket slirp4netns
0 upgraded, 18 newly installed, 0 to remove and 26 not upgraded.
1 not fully installed or removed.
Need to get 111 MB of archives.
After this operation, 402 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://ro.archive.ubuntu.com/ubuntu kinetic/universe amd64 pigz amd64 2.6-1 [63,6 kB]
Get:2 https://download.docker.com/linux/ubuntu kinetic/stable amd64 containerd.io amd64 1.6.21-1 [28,3 MB]
Get:3 http://ro.archive.ubuntu.com/ubuntu kinetic/universe amd64 python3-websocket all 1.2.3-1 [34,7 kB]
Get:4 http://ro.archive.ubuntu.com/ubuntu kinetic/universe amd64 python3-docker all 5.0.3-1 [89,3 kB]
Get:5 http://ro.archive.ubuntu.com/ubuntu kinetic/universe amd64 python3-dockerpty all 0.4.1-4 [11,5 kB]
Get:6 http://ro.archive.ubuntu.com/ubuntu kinetic/universe amd64 python3-docopt all 0.6.2-4 [26,9 kB]
Get:7 http://ro.archive.ubuntu.com/ubuntu kinetic/universe amd64 python3-dotenv all 0.20.0-1 [20,3 kB]
Get:8 http://ro.archive.ubuntu.com/ubuntu kinetic/main amd64 python3-pyrsistent amd64 0.18.1-1build1 [55,5 kB]
Get:9 http://ro.archive.ubuntu.com/ubuntu kinetic/main amd64 python3-jsonschema all 4.6.0-3ubuntu1 [63,6 kB]
Get:10 http://ro.archive.ubuntu.com/ubuntu kinetic/universe amd64 python3-texttable all 1.6.4-1 [11,4 kB]
Get:11 http://ro.archive.ubuntu.com/ubuntu kinetic/universe amd64 docker-compose all 1.29.2-2 [95,6 kB]
Get:12 http://ro.archive.ubuntu.com/ubuntu kinetic/main amd64 libslirp0 amd64 4.7.0-1 [62,7 kB]
Get:13 http://ro.archive.ubuntu.com/ubuntu kinetic/universe amd64 slirp4netns amd64 1.2.0-1 [33,5 kB]
Get:14 https://download.docker.com/linux/ubuntu kinetic/stable amd64 docker-buildx-plugin amd64 0.10.4-1~ubuntu.22.10~kinetic [25,9 MB]                                                                    
Get:15 https://download.docker.com/linux/ubuntu kinetic/stable amd64 docker-ce-cli amd64 5:24.0.0-1~ubuntu.22.10~kinetic [13,3 MB]                                                                         
Get:16 https://download.docker.com/linux/ubuntu kinetic/stable amd64 docker-ce amd64 5:24.0.0-1~ubuntu.22.10~kinetic [22,9 MB]                                                                             
Get:17 https://download.docker.com/linux/ubuntu kinetic/stable amd64 docker-ce-rootless-extras amd64 5:24.0.0-1~ubuntu.22.10~kinetic [9.011 kB]                                                            
Get:18 https://download.docker.com/linux/ubuntu kinetic/stable amd64 docker-compose-plugin amd64 2.17.3-1~ubuntu.22.10~kinetic [10,9 MB]                                                                   
Fetched 111 MB in 21s (5.215 kB/s)                                                                                                                                                                         
Selecting previously unselected package pigz.
(Reading database ... 294863 files and directories currently installed.)
Preparing to unpack .../00-pigz_2.6-1_amd64.deb ...
Unpacking pigz (2.6-1) ...
Selecting previously unselected package containerd.io.
Preparing to unpack .../01-containerd.io_1.6.21-1_amd64.deb ...
Unpacking containerd.io (1.6.21-1) ...
Selecting previously unselected package docker-buildx-plugin.
Preparing to unpack .../02-docker-buildx-plugin_0.10.4-1~ubuntu.22.10~kinetic_amd64.deb ...
Unpacking docker-buildx-plugin (0.10.4-1~ubuntu.22.10~kinetic) ...
Selecting previously unselected package docker-ce-cli.
Preparing to unpack .../03-docker-ce-cli_5%3a24.0.0-1~ubuntu.22.10~kinetic_amd64.deb ...
Unpacking docker-ce-cli (5:24.0.0-1~ubuntu.22.10~kinetic) ...
Selecting previously unselected package docker-ce.
Preparing to unpack .../04-docker-ce_5%3a24.0.0-1~ubuntu.22.10~kinetic_amd64.deb ...
Unpacking docker-ce (5:24.0.0-1~ubuntu.22.10~kinetic) ...
Selecting previously unselected package docker-ce-rootless-extras.
Preparing to unpack .../05-docker-ce-rootless-extras_5%3a24.0.0-1~ubuntu.22.10~kinetic_amd64.deb ...
Unpacking docker-ce-rootless-extras (5:24.0.0-1~ubuntu.22.10~kinetic) ...
Selecting previously unselected package python3-websocket.
Preparing to unpack .../06-python3-websocket_1.2.3-1_all.deb ...
Unpacking python3-websocket (1.2.3-1) ...
Selecting previously unselected package python3-docker.
Preparing to unpack .../07-python3-docker_5.0.3-1_all.deb ...
Unpacking python3-docker (5.0.3-1) ...
Selecting previously unselected package python3-dockerpty.
Preparing to unpack .../08-python3-dockerpty_0.4.1-4_all.deb ...
Unpacking python3-dockerpty (0.4.1-4) ...
Selecting previously unselected package python3-docopt.
Preparing to unpack .../09-python3-docopt_0.6.2-4_all.deb ...
Unpacking python3-docopt (0.6.2-4) ...
Selecting previously unselected package python3-dotenv.
Preparing to unpack .../10-python3-dotenv_0.20.0-1_all.deb ...
Unpacking python3-dotenv (0.20.0-1) ...
Selecting previously unselected package python3-pyrsistent:amd64.
Preparing to unpack .../11-python3-pyrsistent_0.18.1-1build1_amd64.deb ...
Unpacking python3-pyrsistent:amd64 (0.18.1-1build1) ...
Selecting previously unselected package python3-jsonschema.
Preparing to unpack .../12-python3-jsonschema_4.6.0-3ubuntu1_all.deb ...
Unpacking python3-jsonschema (4.6.0-3ubuntu1) ...
Selecting previously unselected package python3-texttable.
Preparing to unpack .../13-python3-texttable_1.6.4-1_all.deb ...
Unpacking python3-texttable (1.6.4-1) ...
Selecting previously unselected package docker-compose.
Preparing to unpack .../14-docker-compose_1.29.2-2_all.deb ...
Unpacking docker-compose (1.29.2-2) ...
Selecting previously unselected package docker-compose-plugin.
Preparing to unpack .../15-docker-compose-plugin_2.17.3-1~ubuntu.22.10~kinetic_amd64.deb ...
Unpacking docker-compose-plugin (2.17.3-1~ubuntu.22.10~kinetic) ...
Selecting previously unselected package libslirp0:amd64.
Preparing to unpack .../16-libslirp0_4.7.0-1_amd64.deb ...
Unpacking libslirp0:amd64 (4.7.0-1) ...
Selecting previously unselected package slirp4netns.
Preparing to unpack .../17-slirp4netns_1.2.0-1_amd64.deb ...
Unpacking slirp4netns (1.2.0-1) ...
Setting up python3-dotenv (0.20.0-1) ...
Setting up python3-texttable (1.6.4-1) ...
Setting up python3-docopt (0.6.2-4) ...
Setting up linux-image-5.19.0-42-generic (5.19.0-42.43) ...
Setting up docker-buildx-plugin (0.10.4-1~ubuntu.22.10~kinetic) ...
Setting up containerd.io (1.6.21-1) ...
Created symlink /etc/systemd/system/multi-user.target.wants/containerd.service → /lib/systemd/system/containerd.service.
Setting up docker-compose-plugin (2.17.3-1~ubuntu.22.10~kinetic) ...
Setting up docker-ce-cli (5:24.0.0-1~ubuntu.22.10~kinetic) ...
Setting up python3-pyrsistent:amd64 (0.18.1-1build1) ...
Setting up libslirp0:amd64 (4.7.0-1) ...
Setting up pigz (2.6-1) ...
Setting up docker-ce-rootless-extras (5:24.0.0-1~ubuntu.22.10~kinetic) ...
Setting up python3-websocket (1.2.3-1) ...
Setting up python3-dockerpty (0.4.1-4) ...
Setting up slirp4netns (1.2.0-1) ...
Setting up python3-docker (5.0.3-1) ...
Setting up python3-jsonschema (4.6.0-3ubuntu1) ...
Setting up docker-ce (5:24.0.0-1~ubuntu.22.10~kinetic) ...
Created symlink /etc/systemd/system/multi-user.target.wants/docker.service → /lib/systemd/system/docker.service.
Created symlink /etc/systemd/system/sockets.target.wants/docker.socket → /lib/systemd/system/docker.socket.
Setting up docker-compose (1.29.2-2) ...
Processing triggers for man-db (2.10.2-2) ...
Processing triggers for libc-bin (2.36-0ubuntu4) ...
Processing triggers for linux-image-5.19.0-42-generic (5.19.0-42.43) ...
/etc/kernel/postinst.d/dkms:
 * dkms: running auto installation service for kernel 5.19.0-42-generic
   ...done.
/etc/kernel/postinst.d/initramfs-tools:
update-initramfs: Generating /boot/initrd.img-5.19.0-42-generic
/etc/kernel/postinst.d/vboxadd:
run-parts: failed to exec /etc/kernel/postinst.d/vboxadd: Exec format error
run-parts: /etc/kernel/postinst.d/vboxadd exited with return code 1
dpkg: error processing package linux-image-5.19.0-42-generic (--configure):
 installed linux-image-5.19.0-42-generic package post-installation script subprocess returned error exit status 1
Errors were encountered while processing:
 linux-image-5.19.0-42-generic
E: Sub-process /usr/bin/dpkg returned an error code (1)
gabriel@gabriel-VirtualBox:~$ ls -l
total 27792
drwxr-xr-x 2 gabriel gabriel     4096 apr 29 04:51 Desktop
drwxr-xr-x 2 gabriel gabriel     4096 apr 29 04:51 Documents
drwxr-xr-x 2 gabriel gabriel     4096 apr 29 04:51 Downloads
drwxrwxr-x 3 gabriel gabriel     4096 mai 19 15:19 git
drwxr-xr-x 2 gabriel gabriel     4096 apr 29 04:51 Music
drwxrwxr-x 7 gabriel gabriel     4096 apr 29 05:15 ns-allinone-3.33
-rw-rw-r-- 1 gabriel gabriel 28412785 apr 27  2022 ns-allinone-3.33.tar.bz2
drwxr-xr-x 2 gabriel gabriel     4096 apr 29 04:51 Pictures
drwxr-xr-x 2 gabriel gabriel     4096 apr 29 04:51 Public
drwx------ 4 gabriel gabriel     4096 apr 29 04:52 snap
drwxr-xr-x 2 gabriel gabriel     4096 apr 29 04:51 Templates
drwxr-xr-x 2 gabriel gabriel     4096 apr 29 04:51 Videos
gabriel@gabriel-VirtualBox:~$ cd git
gabriel@gabriel-VirtualBox:~/git$ cd curs_vcgj_444D_flori/
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ touch Dockerfile
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ gedit Docketfile
^C
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ touch Dockerfile
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ gedit Dockerfile
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ ls -l
total 20
drwxrwxr-x 5 gabriel gabriel 4096 mai 19 16:33 app
-rw-rw-r-- 1 gabriel gabriel  538 mai 19 18:57 Dockerfile
-rw-rw-r-- 1 gabriel gabriel  538 mai 19 18:56 Docketfile
-rw-rw-r-- 1 gabriel gabriel    0 mai 19 15:46 fisier.py
-rw-rw-r-- 1 gabriel gabriel 1539 mai 19 16:32 Jenkinsfile
-rw-rw-r-- 1 gabriel gabriel   28 mai 19 15:19 README.md
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ cd app
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ ls -l
total 24
-rw-rw-r-- 1 gabriel gabriel 2008 mai 19 15:30 444D_flori.py
-rw-rw-r-- 1 gabriel gabriel  360 mai 19 16:24 activeaza_venv
-rw-rw-r-- 1 gabriel gabriel  290 mai 19 16:25 activeaza_venv_jenkins
drwxrwxr-x 3 gabriel gabriel 4096 mai 19 15:42 lib
-rw-rw-r-- 1 gabriel gabriel  110 mai 19 16:27 ruleaza_aplicatia
drwxrwxr-x 3 gabriel gabriel 4096 mai 19 16:13 tests
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ touch quickrequirements.txt
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ gedit quickrequirements.txt 
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ touch dockerstart.sh
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ gedit dockerstart.sh 
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ ls -l
total 32
-rw-rw-r-- 1 gabriel gabriel 2008 mai 19 15:30 444D_flori.py
-rw-rw-r-- 1 gabriel gabriel  360 mai 19 16:24 activeaza_venv
-rw-rw-r-- 1 gabriel gabriel  290 mai 19 16:25 activeaza_venv_jenkins
-rw-rw-r-- 1 gabriel gabriel  302 mai 19 19:00 dockerstart.sh
drwxrwxr-x 3 gabriel gabriel 4096 mai 19 15:42 lib
-rw-rw-r-- 1 gabriel gabriel   81 mai 19 18:58 quickrequirements.txt
-rw-rw-r-- 1 gabriel gabriel  110 mai 19 16:27 ruleaza_aplicatia
drwxrwxr-x 3 gabriel gabriel 4096 mai 19 16:13 tests
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ cd ..
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ ls -l
total 20
drwxrwxr-x 5 gabriel gabriel 4096 mai 19 19:00 app
-rw-rw-r-- 1 gabriel gabriel  538 mai 19 18:57 Dockerfile
-rw-rw-r-- 1 gabriel gabriel  538 mai 19 18:56 Docketfile
-rw-rw-r-- 1 gabriel gabriel    0 mai 19 15:46 fisier.py
-rw-rw-r-- 1 gabriel gabriel 1539 mai 19 16:32 Jenkinsfile
-rw-rw-r-- 1 gabriel gabriel   28 mai 19 15:19 README.md
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ rm -rf Docketfile
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ ls -l
total 16
drwxrwxr-x 5 gabriel gabriel 4096 mai 19 19:00 app
-rw-rw-r-- 1 gabriel gabriel  538 mai 19 18:57 Dockerfile
-rw-rw-r-- 1 gabriel gabriel    0 mai 19 15:46 fisier.py
-rw-rw-r-- 1 gabriel gabriel 1539 mai 19 16:32 Jenkinsfile
-rw-rw-r-- 1 gabriel gabriel   28 mai 19 15:19 README.md
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ cd app
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ ls -l
total 32
-rw-rw-r-- 1 gabriel gabriel 2008 mai 19 15:30 444D_flori.py
-rw-rw-r-- 1 gabriel gabriel  360 mai 19 16:24 activeaza_venv
-rw-rw-r-- 1 gabriel gabriel  290 mai 19 16:25 activeaza_venv_jenkins
-rw-rw-r-- 1 gabriel gabriel  302 mai 19 19:00 dockerstart.sh
drwxrwxr-x 3 gabriel gabriel 4096 mai 19 15:42 lib
-rw-rw-r-- 1 gabriel gabriel   81 mai 19 18:58 quickrequirements.txt
-rw-rw-r-- 1 gabriel gabriel  110 mai 19 16:27 ruleaza_aplicatia
drwxrwxr-x 3 gabriel gabriel 4096 mai 19 16:13 tests
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ cd ..
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ sudo docker build -t 444d_flori:v01 .
[+] Building 5.9s (9/11)                                                                         
 => [internal] load .dockerignore                                                           0.0s
 => => transferring context: 2B                                                             0.0s
 => [internal] load build definition from Dockerfile                                        0.0s
 => => transferring dockerfile: 577B                                                        0.0s
 => [internal] load metadata for docker.io/library/python:3.8-alpine                        1.7s
 => [1/7] FROM docker.io/library/python:3.8-alpine@sha256:059b68e266d7a2843a91324ef7d4d786  3.7s
 => => resolve docker.io/library/python:3.8-alpine@sha256:059b68e266d7a2843a91324ef7d4d786  0.0s
 => => sha256:059b68e266d7a2843a91324ef7d4d7866498b87cd5ed0051d96df56c9c03 1.65kB / 1.65kB  0.0s
 => => sha256:4912e629ee15ae93787756afb2e02b040448a86eadcb00bb542a7e81cbb2 1.37kB / 1.37kB  0.0s
 => => sha256:26e212896cc3835989d7fd0477d9bc857067dc1cb5b5e5bebbf6055c965d 6.30kB / 6.30kB  0.0s
 => => sha256:8a49fdb3b6a5ff2bd8ec6a86c05b2922a0f7454579ecc07637e94dfd1d06 3.40MB / 3.40MB  0.9s
 => => sha256:0357922e53aa8671e175f58d46bfd245908047b81e66370f63486378 622.30kB / 622.30kB  0.5s
 => => sha256:75395374cb719bca03ff2e7886c5dd3c9cd370fe2d98a63698c2e1c5e2 11.25MB / 11.25MB  2.9s
 => => sha256:077a52cd34502845bf68dde76d2def8f197517f698cd29ebd1aa0fc5c1e37426 240B / 240B  0.7s
 => => sha256:31ede12613c20642c62f0f0fcadd31e5f12423d21a9131723b6b5825b724 2.91MB / 2.91MB  1.5s
 => => extracting sha256:8a49fdb3b6a5ff2bd8ec6a86c05b2922a0f7454579ecc07637e94dfd1d0639b6   0.1s
 => => extracting sha256:0357922e53aa8671e175f58d46bfd245908047b81e66370f634863785fe0c70e   0.2s
 => => extracting sha256:75395374cb719bca03ff2e7886c5dd3c9cd370fe2d98a63698c2e1c5e26c8568   0.4s
 => => extracting sha256:077a52cd34502845bf68dde76d2def8f197517f698cd29ebd1aa0fc5c1e37426   0.0s
 => => extracting sha256:31ede12613c20642c62f0f0fcadd31e5f12423d21a9131723b6b5825b7240e20   0.2s
 => [internal] load build context                                                           0.0s
 => => transferring context: 8.80kB                                                         0.0s
 => [2/7] RUN adduser -D 444D_flori                                                         0.3s
 => [3/7] WORKDIR /home/git/curs_vcgj_444D_flori                                            0.0s
 => [4/7] COPY app app                                                                      0.0s
 => ERROR [5/7] RUN python -m venv .venv                                                    0.1s
------
 > [5/7] RUN python -m venv .venv:
------
Dockerfile:19
--------------------
  17 |     #COPY dockerstart.sh dockerstart.sh
  18 |     
  19 | >>> RUN python -m venv .venv
  20 |     RUN .venv/bin/pip install -r app/quickrequirements.txt
  21 |     
--------------------
ERROR: failed to solve: process "/bin/sh -c python -m venv .venv" did not complete successfully: unable to find user sysinfo: no matching entries in passwd file
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ cd app
gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ source activeaza_venv
bash: ../.venv/bin/activate: No such file or directory
FAIL: cannot activate venv
Trying to create the venv in the folder: .venv
Activating virtual environment
Installing the dependencies
Collecting flask
  Downloading Flask-2.3.2-py3-none-any.whl (96 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.9/96.9 kB 1.3 MB/s eta 0:00:00
Collecting Jinja2>=3.1.2
  Downloading Jinja2-3.1.2-py3-none-any.whl (133 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.1/133.1 kB 2.7 MB/s eta 0:00:00
Collecting Werkzeug>=2.3.3
  Downloading Werkzeug-2.3.4-py3-none-any.whl (242 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 242.5/242.5 kB 3.4 MB/s eta 0:00:00
Collecting click>=8.1.3
  Downloading click-8.1.3-py3-none-any.whl (96 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.6/96.6 kB 4.1 MB/s eta 0:00:00
Collecting itsdangerous>=2.1.2
  Downloading itsdangerous-2.1.2-py3-none-any.whl (15 kB)
Collecting blinker>=1.6.2
  Downloading blinker-1.6.2-py3-none-any.whl (13 kB)
Collecting MarkupSafe>=2.0
  Downloading MarkupSafe-2.1.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (25 kB)
Installing collected packages: MarkupSafe, itsdangerous, click, blinker, Werkzeug, Jinja2, flask
Successfully installed Jinja2-3.1.2 MarkupSafe-2.1.2 Werkzeug-2.3.4 blinker-1.6.2 click-8.1.3 flask-2.3.2 itsdangerous-2.1.2
Collecting flask-bootstrap
  Using cached Flask_Bootstrap-3.3.7.1-py3-none-any.whl
Requirement already satisfied: Flask>=0.8 in /home/gabriel/git/curs_vcgj_444D_flori/.venv/lib/python3.10/site-packages (from flask-bootstrap) (2.3.2)
Collecting dominate
  Using cached dominate-2.7.0-py2.py3-none-any.whl (29 kB)
Collecting visitor
  Using cached visitor-0.1.3-py3-none-any.whl
Requirement already satisfied: itsdangerous>=2.1.2 in /home/gabriel/git/curs_vcgj_444D_flori/.venv/lib/python3.10/site-packages (from Flask>=0.8->flask-bootstrap) (2.1.2)
Requirement already satisfied: Werkzeug>=2.3.3 in /home/gabriel/git/curs_vcgj_444D_flori/.venv/lib/python3.10/site-packages (from Flask>=0.8->flask-bootstrap) (2.3.4)
Requirement already satisfied: click>=8.1.3 in /home/gabriel/git/curs_vcgj_444D_flori/.venv/lib/python3.10/site-packages (from Flask>=0.8->flask-bootstrap) (8.1.3)
Requirement already satisfied: blinker>=1.6.2 in /home/gabriel/git/curs_vcgj_444D_flori/.venv/lib/python3.10/site-packages (from Flask>=0.8->flask-bootstrap) (1.6.2)
Requirement already satisfied: Jinja2>=3.1.2 in /home/gabriel/git/curs_vcgj_444D_flori/.venv/lib/python3.10/site-packages (from Flask>=0.8->flask-bootstrap) (3.1.2)
Requirement already satisfied: MarkupSafe>=2.0 in /home/gabriel/git/curs_vcgj_444D_flori/.venv/lib/python3.10/site-packages (from Jinja2>=3.1.2->Flask>=0.8->flask-bootstrap) (2.1.2)
Installing collected packages: visitor, dominate, flask-bootstrap
Successfully installed dominate-2.7.0 flask-bootstrap-3.3.7.1 visitor-0.1.3
Collecting pytest
  Using cached pytest-7.3.1-py3-none-any.whl (320 kB)
Collecting iniconfig
  Using cached iniconfig-2.0.0-py3-none-any.whl (5.9 kB)
Collecting exceptiongroup>=1.0.0rc8
  Using cached exceptiongroup-1.1.1-py3-none-any.whl (14 kB)
Collecting tomli>=1.0.0
  Using cached tomli-2.0.1-py3-none-any.whl (12 kB)
Collecting packaging
  Downloading packaging-23.1-py3-none-any.whl (48 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 48.9/48.9 kB 816.2 kB/s eta 0:00:00
Collecting pluggy<2.0,>=0.12
  Using cached pluggy-1.0.0-py2.py3-none-any.whl (13 kB)
Installing collected packages: tomli, pluggy, packaging, iniconfig, exceptiongroup, pytest
Successfully installed exceptiongroup-1.1.1 iniconfig-2.0.0 packaging-23.1 pluggy-1.0.0 pytest-7.3.1 tomli-2.0.1
Collecting pylint
  Using cached pylint-2.17.4-py3-none-any.whl (536 kB)
Collecting isort<6,>=4.2.5
  Using cached isort-5.12.0-py3-none-any.whl (91 kB)
Collecting platformdirs>=2.2.0
  Using cached platformdirs-3.5.1-py3-none-any.whl (15 kB)
Collecting tomlkit>=0.10.1
  Using cached tomlkit-0.11.8-py3-none-any.whl (35 kB)
Collecting astroid<=2.17.0-dev0,>=2.15.4
  Using cached astroid-2.15.5-py3-none-any.whl (278 kB)
Collecting mccabe<0.8,>=0.6
  Using cached mccabe-0.7.0-py2.py3-none-any.whl (7.3 kB)
Collecting dill>=0.2
  Using cached dill-0.3.6-py3-none-any.whl (110 kB)
Requirement already satisfied: tomli>=1.1.0 in /home/gabriel/git/curs_vcgj_444D_flori/.venv/lib/python3.10/site-packages (from pylint) (2.0.1)
Collecting typing-extensions>=4.0.0
  Using cached typing_extensions-4.5.0-py3-none-any.whl (27 kB)
Collecting lazy-object-proxy>=1.4.0
  Using cached lazy_object_proxy-1.9.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (63 kB)
Collecting wrapt<2,>=1.11
  Downloading wrapt-1.15.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (78 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 78.4/78.4 kB 1.2 MB/s eta 0:00:00
Installing collected packages: wrapt, typing-extensions, tomlkit, platformdirs, mccabe, lazy-object-proxy, isort, dill, astroid, pylint
Successfully installed astroid-2.15.5 dill-0.3.6 isort-5.12.0 lazy-object-proxy-1.9.0 mccabe-0.7.0 platformdirs-3.5.1 pylint-2.17.4 tomlkit-0.11.8 typing-extensions-4.5.0 wrapt-1.15.0
(.venv) gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ cd ..
(.venv) gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ sudo docker build -t 444d_flori:v01 .
[+] Building 0.6s (9/11)                                                                         
 => [internal] load build definition from Dockerfile                                        0.0s
 => => transferring dockerfile: 577B                                                        0.0s
 => [internal] load .dockerignore                                                           0.0s
 => => transferring context: 2B                                                             0.0s
 => [internal] load metadata for docker.io/library/python:3.8-alpine                        0.5s
 => [1/7] FROM docker.io/library/python:3.8-alpine@sha256:059b68e266d7a2843a91324ef7d4d786  0.0s
 => [internal] load build context                                                           0.0s
 => => transferring context: 1.04kB                                                         0.0s
 => CACHED [2/7] RUN adduser -D 444D_flori                                                  0.0s
 => CACHED [3/7] WORKDIR /home/git/curs_vcgj_444D_flori                                     0.0s
 => CACHED [4/7] COPY app app                                                               0.0s
 => ERROR [5/7] RUN python -m venv .venv                                                    0.1s
------
 > [5/7] RUN python -m venv .venv:
------
Dockerfile:19
--------------------
  17 |     #COPY dockerstart.sh dockerstart.sh
  18 |     
  19 | >>> RUN python -m venv .venv
  20 |     RUN .venv/bin/pip install -r app/quickrequirements.txt
  21 |     
--------------------
ERROR: failed to solve: process "/bin/sh -c python -m venv .venv" did not complete successfully: unable to find user sysinfo: no matching entries in passwd file
(.venv) gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ python3 -m pip --upgrade pip

Usage:   
  /home/gabriel/git/curs_vcgj_444D_flori/.venv/bin/python3 -m pip <command> [options]

no such option: --upgrade
(.venv) gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ sudo docker build -t 444d_flori:v01 .
[+] Building 19.5s (12/12) FINISHED                                                              
 => [internal] load .dockerignore                                                           0.0s
 => => transferring context: 2B                                                             0.0s
 => [internal] load build definition from Dockerfile                                        0.0s
 => => transferring dockerfile: 580B                                                        0.0s
 => [internal] load metadata for docker.io/library/python:3.8-alpine                        0.6s
 => [1/7] FROM docker.io/library/python:3.8-alpine@sha256:059b68e266d7a2843a91324ef7d4d786  0.0s
 => [internal] load build context                                                           0.0s
 => => transferring context: 1.04kB                                                         0.0s
 => CACHED [2/7] RUN adduser -D 444D_flori                                                  0.0s
 => [3/7] WORKDIR /home/git/curs_vcgj_444D_flori                                            0.0s
 => [4/7] COPY app app                                                                      0.0s
 => [5/7] RUN python -m venv .venv                                                          4.1s
 => [6/7] RUN .venv/bin/pip install -r app/quickrequirements.txt                           14.2s
 => [7/7] WORKDIR /home/git/curs_vcgj_444D_flori/app                                        0.1s
 => exporting to image                                                                      0.4s 
 => => exporting layers                                                                     0.4s 
 => => writing image sha256:6feb074dd87c290afd550c85e5282f700fc7d112a2eb7f2a2e1fe03ebdd1c8  0.0s 
 => => naming to docker.io/library/444d_flori:v01                                           0.0s 
(.venv) gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ sudo docker images                
REPOSITORY   TAG       IMAGE ID       CREATED              SIZE
444d_flori   v01       6feb074dd87c   About a minute ago   105MB
(.venv) gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ sudo docker ps -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
(.venv) gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ sudo docker run --name 444d_flori -p 8020:5020 444d_flori:v01
docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: exec: "./dockerstart.sh": permission denied: unknown.
ERRO[0000] error waiting for container:                 
(.venv) gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ docker ps -a
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/json?all=1": dial unix /var/run/docker.sock: connect: permission denied
(.venv) gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ sudo docker ps -a
CONTAINER ID   IMAGE            COMMAND              CREATED          STATUS    PORTS                                                 NAMES
c6bce8cec793   444d_flori:v01   "./dockerstart.sh"   38 seconds ago   Created   5011/tcp, 0.0.0.0:8020->5020/tcp, :::8020->5020/tcp   444d_flori
(.venv) gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ sudo docker rm^C
(.venv) gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ sudo docker rm c6bce8cec793
c6bce8cec793
(.venv) gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ sudo docker images
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
444d_flori   v01       6feb074dd87c   5 minutes ago   105MB
(.venv) gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ sudo docker rmi 6feb074dd87c
Untagged: 444d_flori:v01
Deleted: sha256:6feb074dd87c290afd550c85e5282f700fc7d112a2eb7f2a2e1fe03ebdd1c8fb
(.venv) gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ cd app
(.venv) gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ sudo chmod 777 dockerstart.sh 
(.venv) gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori/app$ cd ..
(.venv) gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ sudo docker build -t 444d_flori:v01 .
[+] Building 18.5s (12/12) FINISHED                                                                             
 => [internal] load .dockerignore                                                                          0.0s
 => => transferring context: 2B                                                                            0.0s
 => [internal] load build definition from Dockerfile                                                       0.0s
 => => transferring dockerfile: 580B                                                                       0.0s
 => [internal] load metadata for docker.io/library/python:3.8-alpine                                       1.1s
 => [1/7] FROM docker.io/library/python:3.8-alpine@sha256:059b68e266d7a2843a91324ef7d4d7866498b87cd5ed005  0.0s
 => [internal] load build context                                                                          0.0s
 => => transferring context: 1.35kB                                                                        0.0s
 => CACHED [2/7] RUN adduser -D 444D_flori                                                                 0.0s
 => CACHED [3/7] WORKDIR /home/git/curs_vcgj_444D_flori                                                    0.0s
 => [4/7] COPY app app                                                                                     0.0s
 => [5/7] RUN python -m venv .venv                                                                         4.0s
 => [6/7] RUN .venv/bin/pip install -r app/quickrequirements.txt                                          13.0s
 => [7/7] WORKDIR /home/git/curs_vcgj_444D_flori/app                                                       0.0s 
 => exporting to image                                                                                     0.3s 
 => => exporting layers                                                                                    0.3s 
 => => writing image sha256:981b7dde2e8760af5f16e13db74b5358733072d6539801dae494ad2e386e56f6               0.0s 
 => => naming to docker.io/library/444d_flori:v01                                                          0.0s 
(.venv) gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ sudo docker run --name 444d_flori -p 8020:5020 444d_flori:v01
/home/git/curs_vcgj_444D_flori/app
Activare venv:
/home/git/curs_vcgj_444D_flori/app
Configurare variabila mediu FLASK_APP
Start server:
444D_flori
 * Ignoring a call to 'app.run()' that would block the current 'flask' CLI command.
   Only call 'app.run()' in an 'if __name__ == "__main__"' guard.
 * Serving Flask app '444D_flori'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5020
 * Running on http://172.17.0.2:5020
Press CTRL+C to quit
 * Restarting with stat
172.17.0.1 - - [19/May/2023 16:20:44] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [19/May/2023 16:20:44] "GET /favicon.ico HTTP/1.1" 404 -
172.17.0.1 - - [19/May/2023 16:21:20] "GET /liliac HTTP/1.1" 308 -
172.17.0.1 - - [19/May/2023 16:21:20] "GET /liliac/ HTTP/1.1" 200 -
172.17.0.1 - - [19/May/2023 16:21:31] "GET /liliac/culoare HTTP/1.1" 200 -
^C(.venv) gabriel@gabriel-VirtualBox:~/git/curs_vcgj_444D_flori$ 
