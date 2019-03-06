#!/bin/bash

#工具安装
yum install epel-release python-setuptools m2crypto

#安装supervisor，再设置开机自启
yum install supervisor
systemctl enable supervisord.service

#安装shadowsocks
easy_install pip
pip install shadowsocks


#配置账号密码
IPADDR=$(/sbin/ifconfig -a|grep inet|grep -v 127.0.0.1|grep -v inet6|awk '{print $2}'|tr -d "addr:")
echo "{
   "server":"$IPADDR",
   "port_password":{
   "8381":"myss",
   "8382":"myss",
   "8383":"myss",
   "8384":"myss",
   "8385":"myss",
   "8386":"myss",
   "8387":"myss",
   "8388":"myss",
   "8389":"myss"
   },
 "timeout":300,
 "method":"aes-256-cfb"
}" > /etc/shadowsocks.json

#配置日志文件
echo "
[program:shadowsocks]
command=ssserver -c /etc/shadowsocks.json
autostart=true
autorestart=true
user=root
log_stderr=true
logfile=/var/log/shadowsocks.log" >>/etc/supervisord.conf

#设置端口
firewall-cmd --zone=public --add-port=8381-8389/tcp --permanent
firewall-cmd --zone=public --add-port=8381-8389/udp --permanent
systemctl restart firewalld.service


#安装锐速
wget -N --no-check-certificate https://github.com/91yun/serverspeeder/raw/master/serverspeeder.sh && bash serverspeeder.sh
#设置锐速开机自启
systemctl enable serverSpeeder.service
