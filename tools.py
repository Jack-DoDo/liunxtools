import os
import sys

os.system('sudo apt update && sudo apt -y upgrade')

def pip():
    os.system('sudo apt install -y python3-dev python3.6-dev python3-pip')
    os.system('sudo apt remove -y python3-pip')
    os.system('wget --no-check-certificate https://bootstrap.pypa.io/get-pip.py')
    os.system('sudo python3 get-pip.py')
    os.system('sudo rm get-pip.py')
    

def nginx():
    os.system('sudo apt install -y nginx')

def 数据库():
    os.system('wget --no-check-certificate https://repo.mysql.com/mysql-apt-config_0.8.12-1_all.deb')
    os.system('sudo dpkg -i *.deb')
    os.system('sudo apt update')
    os.system('sudo apt install -y mysql-server')
    os.system('sudo rm *.deb')

def 连接():
    os.system('sudo pip3 install mysql-connector-python')

def MySqlclient():
    os.system('sudo apt install python-dev default-libmysqlclient-dev')
    os.system('sudo pip3 install mysqlclient')

def 注册():
    os.system('sudo apt-get -y install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common')
    os.system('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -')
    os.system('wget --no-check-certificate https://nginx.org/keys/nginx_signing.key')
    os.system('sudo apt-key add nginx_signing.key')
    os.system('sudo rm nginx_signing.key')
    f = open('/etc/apt/sources.list','a')
    f.write('\ndeb http://nginx.org/packages/mainline/ubuntu/ bionic nginx')
    f.write('\ndeb-src http://nginx.org/packages/mainline/ubuntu/ bionic nginx')
    f.close()  
    print('\n/etc/apt/sources.list 成功写入\n')
    f = open('/etc/apt/sources.list.d/unit.list','a')
    f.write('\ndeb https://packages.nginx.org/unit/ubuntu/ bionic unit')
    f.write('\ndeb-src https://packages.nginx.org/unit/ubuntu/ bionic unit')
    f.close()
    print('\n/etc/apt/sources.list.d/unit.list 成功写入\n')
    os.system('sudo apt update && sudo apt -y upgrade')

def docker():
    os.system('sudo apt-get -y install docker-ce docker-ce-cli containerd.io')

while True:
    print ('''
    ****************************************
    *                                      *
    *               服务器安装             *
    *                                      *
    ****************************************

    1. 安装并更新Pip
    2. 注入Nginx和Docker的APT信息
    3. 安装MySQL')
    4. 安装MySQL官方Python3库
    5. 安装MySqlclient for Python3库')
    6. 安装Nginx')
    7. 安装Docker')
    8. 用户时区设置
    
    ''')
    
    comm = input(" 回复数字或 Q 退出:")
    if comm == "1":
        pip()
    elif comm == "2":
        注册()
    elif comm == "3":
        数据库()
    elif comm == "4":
        连接()
    elif comm == "5":
        MySqlclient()
    elif comm == "6":
        nginx()
    elif comm == "7":
        docker()
    elif comm == "8":
        os.system('tzselect')
    elif comm == "Q" or comm == "q":
        os.system('sudo apt -y autoremove')
        break
