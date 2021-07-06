import serial.tools.list_ports
import csv

print('Which port would you like to record data from?')


ports= serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
print(str(onePort))

val = input("select Port: COM ")

for x in range(0,len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portList[x])

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()


trash=1

while True:
   if serialInst.in_waiting:
        packet = serialInst.readline()
        print(packet.decode("utf"))


        with open('teledata.csv', 'w', newline='') as tele:
            thewriter = csv.writer(tele)

            thewriter.writerow(['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'PB1 ', 'PB2 ', 'PB3 ', 'PB4 ', 'PB5 ', 'PB6 ', 'PB7 ', 'PB8 ', 'PB9 ', 'PB10 ', 'PB11 ', 'PB12 ', 'PB13 ', 'PB14', 'PB15 ', 'PB16 '])

            for i in range(1,10000):
                packet = serialInst.readline()
                print(packet.decode("utf"))

                string = packet.decode('utf-8')
                thewriter.writerow([string])





            #fieldnames = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']
            #csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames, delimeter='\t')

            #csv_writer.writeheader()

            #for packet in csv_reader:
            #csv_writer.writerow(packet)


