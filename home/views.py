from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
#modbus
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.register_read_message import ReadHoldingRegistersResponse
from time import sleep
client = ModbusClient(method='rtu', port='/dev/ttyUSB0', stopbits=1, bytesize=8,paraty='N', baudrate=9600, timeout=1)
connection = client.connect()
print(connection)

context={0:0}
class IndexClass1(View):
    def get(self,request):
        for a in range(3,18):
            v1 = client.read_holding_registers(5784,6,unit=a)
            if not v1.isError():
                context['b'+str(a)]={v1.registers[0]/10,v1.registers[2]/10,v1.registers[4]/10}          
        return render(request,"home/para.U.html",context)   

context1={0:0}
class IndexClass2(View):
    def get(self,request):
        for c in range(3,18):
            v2 = client.read_holding_registers(5632,2,unit=c)
            if not v2.isError():
                context1['d'+str(c)]={round(v2.registers[0]/1000*65535+v2.registers[1]/1000,2)}          
        return render(request,"home/para.Ppd.html",context1)   

context2={0:0}
class IndexClass3(View):
    def get(self,request):
        for e in range(3,18):
            v3 = client.read_holding_registers(5796,2,unit=e)
            if not v3.isError():
                context2['f'+str(e)]={round(v3.registers[0]/1000*65535+v3.registers[1]/1000,2)}          
        return render(request,"home/para.Pout.html",context2) 

context3={0:0}
class IndexClass4(View):
    def get(self,request):
        for g in range(3,18):
            v4 = client.read_holding_registers(5654,2,unit=g)
            if not v4.isError():
                context3['h'+str(g)]={round(v4.registers[0]/100*65535+v4.registers[1]/100,2)}          
        return render(request,"home/para.Ed.html",context3)    

context4={0:0}
class IndexClass5(View):
    def get(self,request):
        for i in range(3,18):
            v5 = client.read_holding_registers(5694,2,unit=i)
            if not v5.isError():
                context4['k'+str(i)]={round(v5.registers[0]/100*65535+v5.registers[1]/100,2)}          
        return render(request,"home/para.Em.html",context4)  

context5={0:0}
class IndexClass6(View):
    def get(self,request):
        for l in range(3,18):
            v6 = client.read_holding_registers(5704,2,unit=l)
            if not v6.isError():
                context5['m'+str(l)]={round(v6.registers[0]/100*65535+v6.registers[1]/100,2)}          
        return render(request,"home/para.Ey.html",context5)  

context6={0:0}
class IndexClass7(View):
    def get(self,request):
        for n in range(3,18):
            v7 = client.read_holding_registers(5714,2,unit=n)
            if not v7.isError():
                context6['o'+str(n)]={round(v7.registers[0]/100*65535+v7.registers[1]/100,2)}          
        return render(request,"home/para.Et.html",context6) 

context7={0:0}
class IndexClass8(View):
    def get(self,request):
        for p in range(3,18):
            v8 = client.read_holding_registers(5640,2,unit=p)
            if not v8.isError():
                context7['q'+str(p)]={round(v8.registers[0]/1000*65535+v8.registers[1]/1000,2)}          
        return render(request,"home/para.Ppy.html",context7) 

context8={0:0}
class IndexClass9(View):
    def get(self,request):
        for r in range(3,18):
            v9 = client.read_holding_registers(5784,6,unit=r)
            if not v9.isError():
                context8['s'+str(r)]={v9.registers[1]/10,v9.registers[3]/10,v9.registers[5]/10}          
        return render(request,"home/para.I.html",context8)



