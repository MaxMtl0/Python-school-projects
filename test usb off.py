import serial
#ser = serial.Serial('COM14', 19200)
def get_port():
  port = serial.Serial('COM14', 9600)
  #port.port = port_name
  #port.baud_rate = 19200
  return port
 
def switch_on():
  port = get_port()
  port.open()
  port.write('H')	
  port.close()

def switch_off():
  port = get_port()
  port.open()
  port.write('L')	
  port.close()
 
while 1:
    a= int(input("position 1 ou 0 ?"))
    if a==0:
        #ser.setDTR(1)
        switch_off()
        print ("le relais est off")
    else:
        #ser.setDTR(0)
        switch_on()
        print ("le relais est on")





#port_name = 'COM14'
 



import os
import sys
import serial
import argparse
 
port_name = 'COM14'
 
def get_port():
  port = serial.Serial()
  port.port = port_name
  port.baud_rate = 19200
  return port
 
def switch_on():
  port = get_port()
  port.open()
  port.write('H')	
 
def switch_off():
  port = get_port()
  port.open()
  port.write('L')	
 
def main():
  parser = argparse.ArgumentParser(description = 'Switch on/off the LED of an Arduino board with the PhysicalPixel sketch loaded')
  subparsers = parser.add_subparsers(title = 'subcommands',description = 'valid subcommands', help = 'additional help')
 
  cmd_parser = subparsers.add_parser('on', description = 'Switch the LED on')
  cmd_parser.set_defaults(func = switch_on)
 
  cmd_parser = subparsers.add_parser('off', description = 'Switch the LED off')
  cmd_parser.set_defaults(func = switch_off)
  
  args = parser.parse_args()
  
  args.func()
  
 
if __name__ == '__main__':
  main()