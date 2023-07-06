import socket

import IPy
import re

def tcp_Scan(ip,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    result = sock.connect_ex((ip, port))
    if result == 0:
        flag = True  # 服务的端口是通的
    else:
        flag = False  # 服务器端口不通
    return flag

def is_lived(ip):
    newIpList = list_ip(ip)
    ports = [21,22,23,25,53,80,110,143,443,445,1433,3389]
    for ip in newIpList:
        for port in ports:
            print("{}  端口:{}".format(ip,port))
            if tcp_Scan(ip,port):
                print("{}  端口:{}is lived".format(ip,port))
                break





def list_of_groups(init_list, childern_list_len):
    list_of_groups = zip(*(iter(init_list),) * childern_list_len)  # 使用zip函数将列表按照网段长度分成多个列表
    end_list = [list(i) for i in list_of_groups]  # 转换成列表
    count = len(init_list) % childern_list_len
    end_list.append(init_list[-count:]) if count != 0 else end_list
    return end_list

def list_ip(ip):
    newIplist = []
    if "/" in ip:
        if int(ip.split("/")[1]) >= 24:
            num = ip.split('/')[1]
            length = len(IPy.IP('127.0.0.0/{}'.format(num)))  # 计算网段的IP个数
            endiplists = list_of_groups(range(0, 256), length)  # 将整个C段按子网掩码划分成多个列表
            for endiplist in endiplists:  # 判断输入IP所在的子网
                if int(ip.split('/')[0].split('.')[-1].strip()) in endiplist:
                    for endip in endiplist:
                        newIplist.append(
                            '.'.join(ip.split('/')[0].split('.')[:-1]) + '.{}'.format(endip))  # 以.为连接符，组合IP。
                    break
        elif int(ip.split("/")[1]) >= 16:
            new_ip = ip.split(".")[0] + "." + ip.split(".")[1] + ".0.0/{}".format(ip.split("/")[1])
            ips = IPy.IP(new_ip)
            for i in ips:
                newIplist.append(str(i))
        else:
            new_ip = ip.split(".")[0] + ".0.0.0/{}".format(ip.split("/")[1])
            ips = IPy.IP(new_ip)
            for i in ips:
                newIplist.append(str(i))
    elif re.match(r'^\d{0,3}.\d{0,3}.\d{0,3}.\d{0,3}$', ip) != None:
        newIplist.append(ip)
    return newIplist


if __name__ == '__main__':
    ips = input("ip:")
    is_lived(ips)