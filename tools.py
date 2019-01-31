import os , sys
def pip():
    os.system('sudo apt update && sudo apt -y upgrade && sudo apt install -y python3-dev python3.6-dev python3-pip')
    os.system('sudo apt remove -y python3-pip')
    os.system('wget --no-check-certificate https://bootstrap.pypa.io/get-pip.py')
    os.system('sudo python3 get-pip.py')
    os.system('sudo rm get-pip.py')

def nginx():
    os.system('sudo apt update && sudo apt -y upgrade && sudo apt install -y nginx')

def unit():
    os.system('sudo apt update && sudo apt -y install unit')
    os.system('sudo apt-get install unit-python3.6 unit-dev')

def 数据库():
    os.system('wget --no-check-certificate https://repo.mysql.com/mysql-apt-config_0.8.12-1_all.deb')
    os.system('sudo dpkg -i *.deb')
    os.system('sudo apt update && sudo apt -y upgrade')
    os.system('sudo apt install -y mysql-community-server')
    os.system('sudo rm *.deb')

def 连接():
    os.system('sudo pip3 install mysql-connector-python')

def 注册():
    os.system('wget --no-check-certificate https://nginx.org/keys/nginx_signing.key')
    os.system('sudo apt-key add nginx_signing.key')
    os.system('sudo rm nginx_signing.key')
    f = open('/etc/apt/sources.list','a')
    f.write('\ndeb http://nginx.org/packages/mainline/ubuntu/ bionic nginx')
    f.write('\ndeb-src http://nginx.org/packages/mainline/ubuntu/ bionic nginx')
    f.close()  
    f = open('/etc/apt/sources.list.d/unit.list','a')
    f.write('\ndeb https://packages.nginx.org/unit/ubuntu/ bionic unit')
    f.write('\ndeb-src https://packages.nginx.org/unit/ubuntu/ bionic unit')
    f.close()

while True:
    print (' ')
    print (' ')
    print (' ')
    print ('****************************************')
    print ('*                                      *')
    print ('*               服务器安装             *')
    print ('*                                      *')
    print ('****************************************')
    print (' ')
    print (' ')
    print ('1. 安装pip')
    print ('2. 注入Nginx信息')
    print ('3. 安装MySQL')
    print ('4. 安装MySQL官方Python3库')
    print ('5. 安装Nginx')
    print ('6. 安装unit for Python3 ')
    print (' ')

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
        nginx()
    elif comm == "6":
        unit()
    elif comm == "Q" or comm == "q":
        break