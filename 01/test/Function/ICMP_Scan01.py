import platform
import subprocess
import IPy
import re


def ping_func(ip):
    if (platform.system() == 'Windows') :
        ping = subprocess.Popen(
            'ping -n 1 {}'.format(ip), 
            shell=False, #如果该参数为 True，将通过操作系统的 shell 执行指定的命令。
            close_fds=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
            )
    else:
        ping = subprocess.Popen(
            'ping -c 1 {}'.format(ip), 
            shell=False, 
            close_fds=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
            )
    try:
        out, err = ping.communicate(timeout=8)
        if 'ttl' in out.decode('GBK').lower():
            print("ip {} is alive".format(ip))
    except:
        pass
    ping.kill()
    
def list_of_groups(init_list, childern_list_len):
    list_of_groups = zip(*(iter(init_list),) * childern_list_len)   # 使用zip函数将列表按照网段长度分成多个列表
    end_list = [list(i) for i in list_of_groups]    # 转换成列表
    count = len(init_list) % childern_list_len
    end_list.append(init_list[-count:]) if count != 0 else end_list
    return end_list

def list_ip(ip):
    newIplist = []
    if "/" in ip:
        if int(ip.split("/")[1]) >= 24:
            num = ip.split('/')[1]
            length = len(IPy.IP('127.0.0.0/{}'.format(num)))    # 计算网段的IP个数
            endiplists = list_of_groups(range(0, 256), length)  # 将整个C段按子网掩码划分成多个列表
            for endiplist in endiplists:    # 判断输入IP所在的子网
                if int(ip.split('/')[0].split('.')[-1].strip()) in endiplist:
                    for endip in endiplist:
                        newIplist.append('.'.join(ip.split('/')[0].split('.')[:-1]) + '.{}'.format(endip))    # 以.为连接符，组合IP。
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


def main(ip):

    newIplist = list_ip(ip)
    for perip in newIplist :
        print('{}'.format(perip))
        ping_func(perip)


if __name__ == "__main__":
    ip = '192.168.31.30/30'
    main(ip)
