import ipaddress
import re

class My_Utils:
    @staticmethod
    def cidr_to_ips(cidr):
        ip_network = ipaddress.ip_network(cidr, strict=False)
        ips = []
        for ip in ip_network.hosts():
            ips.append(str(ip))
        return tuple(ips)

    @staticmethod
    def is_valid_cidr(cidr):
        ipv4_pattern = re.compile(
            r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])/(0|[1-9]|[12][0-9]|3[0-2])$"
        )

        if ipv4_pattern.match(cidr):
            return True
        else:
            return False

    @staticmethod
    def is_valid_ipv4(ipv4):
        pattern = re.compile(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")

        if pattern.match(ipv4):
            return True
        else:
            return False

