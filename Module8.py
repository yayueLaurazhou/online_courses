##Read the temperature and return the Centigrade value as an integer
import time
import os

def read_temp():
    f = open('/sys/bus/w1/devices/28-3c01d607cf74/w1_slave', 'r')
    lines = f.read()
    f.close()
    position = lines.find('t=')
    temperature = lines[position+2:]
    return(int(temperature))

temperature_file = open("temperature.txt","w")
dir_path = os.path.dirname(os.path.realpath("temperature.txt"))
print(dir_path)
tm_start = time.time()

while True:
    if time.time() > (tm_start + 1800) :
        break
    temperature = read_temp()
    temp = str(temperature / 1000.0)
    temperature_file = open("temperature.txt","a")
    temperature_file.write(time.strftime("            %a %d-%m-%Y @ %H:%M"))
    temperature_file.write("\n")
    temperature_file.write(str(temp) + "\n")
    
    temperature_file.close()
    #temperature_file = open("temperature.txt","w+")
    #print(temperature_file.read())
    time.sleep(300)

temperature_file.close()
