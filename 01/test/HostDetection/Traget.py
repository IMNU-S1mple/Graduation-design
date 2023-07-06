class Target:
    def __init__(self,ip,*ports,**kwargs):

        self.ip = ip
        self.ports = ports
        self.kwargs = kwargs


    @property
    def show(self):
        return self.ip,self.ports,self.kwargs
        # for port in self.ports:
        #     print(self.ip+":"+str(port))
        # print(type(self.ports))
        # for k,v in self.kwargs.items():
        #     print(f"{k}:{v}")



if __name__ == "__main__":
    target = Target("192.168.3.1/24",1,2,3,4,5,asd=123,zxc="456")
    print(target.show)