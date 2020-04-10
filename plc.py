from snap7.util import *  # 对位操作的函数要导入该库
import snap7,time

mode=1

# 定义的函数可直接对QX.X一个位进行操作
def writeoutput(dev, byte, bit, cmd):
    data = dev.read_area(0x82, 0, byte, 1)  # 0x82表示输出Q，byte表示起始地址（Q0),1表示类型为byte，cmd位置的值（True或False）
    set_bool(data, byte, bit, cmd)  # 置Qbyte.bit(即Q0.4)为cmd(即True)
    dev.write_area(0x82, 0, byte, data)  # 同样，进行写数据操作

# 该函数只进行了读操作
def readoutput(dev, byte, bit):
    data = dev.read_area(0x82, 0, byte, 1)
    status = get_bool(data, byte, bit)  # 获取位状态
    return status

def readinput(dev, byte, bit):
    data = dev.read_area(0x81, 0, byte, 1)
    status = get_bool(data, byte, bit)  # 获取位状态
    return status

myplc=snap7.client.Client()
myplc.connect('192.168.0.1', rack=0,slot=1)     #建立连接（相关信息去TIA看，IP，机架和插槽）
print(myplc.get_connected())     # 测试是否通讯成功



while True:
    if mode==0:
        pass
    elif mode==1:
         for i in range(8):
             for j in range(8):
                 status=readinput(myplc,i,j)
                 writeoutput(myplc,i,j,status)
    elif mode==2:
        pass
    elif mode==3:
        pass
