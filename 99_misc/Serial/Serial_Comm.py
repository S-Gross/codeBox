__author__ = 'sgr'

import serial
import sys
import time
import datetime
import binascii
import csv


"""
Init. the pyserial
look in EMU documentation
todo finde sinnvoll timeout zeit
"""
def InitPySerial():
    ser = serial.Serial()
    ser.port = 7 # TODO set correct COM port
    ser.baudrate = 2400
    ser.bytesize = serial.EIGHTBITS
    ser.parity = serial.PARITY_EVEN
    ser.stopbits = serial.STOPBITS_ONE

    # Wichtig
    ser.timeout = 4

    return ser

"""
@todo unfinished function main problem is the calculation of the cs (checksum) byte
"""
def ReadOutMeter(ser, meter):
    """
    Reads out a meter
    todo:   string sollte so aussehen
            Problem bei der Bildung der Checksumme

    f if fix    ff ff ff ff ff ff ff xx xx xx xx ff ff ff ff xx ff
    example:    68 0B 0B 68 73 FD 52 35 26 69 03 FF FF FF FF 85 16
    >  68 0B 0B 68 73 FD 52 35 26 69 03 FF FF FF FF 85 16
    >  68 0B 0B 68 73 FD 52 25 26 69 03 FF FF FF 1FF 75 16
    >  68 0B 0B 68 73 FD 52 43 26 69 03 FF FF FF FF 93 16

    """
    soll_hexstring = "68 0B 0B 68 73 FD 52 35 26 69 03 FF FF FF FF 85 16"
    hexstring = "68 0B 0B 68 73 FD 52"

    # plits the meter string into a list with 2 chars per entry
    meter = [meter[i:i+2] for i in range(0, len(meter), 2)]

    # Extends the hexstring with the secondary address
    for i in range(len(meter)):
        #print(meter[len(meter)-1-i])
        hexstring += " "
        hexstring += meter[len(meter)-1-i]

    # Extends the telegram with Manufacturer Code 2 byte, Version Number 1 byte, Medium 1 Byte
    for i in range(4):
        hexstring += " FF"

    # Calculation of the checksum which is the last byte before the stop byte
    # from byte 5-15
    list_hexstring = hexstring.split(" ")
    list_hexstring = list_hexstring[5:15]
    tobeSummed = ' '.join(item for item in list_hexstring if item)
    tobytes = bytes.fromhex(tobeSummed)
    listbytes = list(tobytes)



    checksum3 = sum(bytearray(listbytes)) % 254
    checksum1 = sum(bytearray(listbytes)) % 255
    checksum2 = sum(bytearray(listbytes)) % 256

    #checksum2 = hex(checksum1)
    print(meter)
    print(hexstring)
    print(soll_hexstring)
    return meter


"""
Reads out all meter which belong to the UV2.2
Meter ids:
    P01 03692635    68 0B 0B 68 73 FD 52 35 26 69 03 FF FF FF FF 85 16
    P02 03692625    68 0B 0B 68 73 FD 52 25 26 69 03 FF FF FF FF 75 16
    P03 03692643    68 0B 0B 68 73 FD 52 43 26 69 03 FF FF FF FF 93 16
"""
def ReadOut_UV22_P01(ser):
    #Request telegram for PO1
    Meter_UV22 = "68 0B 0B 68 73 FD 52 35 26 69 03 FF FF FF FF 85 16"

    # Converts the string hex telegram to a bytes object
    Meter_UV22 = bytes.fromhex(Meter_UV22)

    # Sends selction of MBUS ELM by sec. address
    ser.write(Meter_UV22)

    # Reads response byte ACK = "E5"
    read = ser.read(1)

    # Sends the request
    ser.write(bytes.fromhex("10 7B FD 78 16"))

    # Resv. the response
    read = ser.read(211)

    listbytes = list(read)
    print("Response: PO1")
    print(listbytes)

    data = DataInterpreter(listbytes)
    with open("D:\\04_Python\\UV22_P01.csv", 'a') as csv_file:
        my_csv_writer = csv.writer(csv_file, delimiter=",", lineterminator="\n")
        my_csv_writer.writerow(data)

    return ""


def ReadOut_UV22_P02(ser):
    #Request telegram for PO1
    Meter_UV22 = "68 0B 0B 68 73 FD 52 25 26 69 03 FF FF FF FF 75 16"

    # Converts the string hex telegram to a bytes object
    Meter_UV22 = bytes.fromhex(Meter_UV22)

    # Sends selction of MBUS ELM by sec. address
    ser.write(Meter_UV22)

    # Reads response byte ACK = "E5"
    read = ser.read(1)

    # Sends the request
    ser.write(bytes.fromhex("10 7B FD 78 16"))

    # Resv. the response
    read = ser.read(211)

    listbytes = list(read)

    print("Response: PO2")
    print(listbytes)
    data = DataInterpreter(listbytes)
    with open("D:\\04_Python\\UV22_P02.csv", 'a') as csv_file:
        my_csv_writer = csv.writer(csv_file, delimiter=",", lineterminator="\n")
        my_csv_writer.writerow(data)

    return ""

def ReadOut_UV22_P03(ser):
    #Request telegram for PO1
    Meter_UV22 = "68 0B 0B 68 73 FD 52 43 26 69 03 FF FF FF FF 93 16"

    # Converts the string hex telegram to a bytes object
    Meter_UV22 = bytes.fromhex(Meter_UV22)

    # Sends selction of MBUS ELM by sec. address
    ser.write(Meter_UV22)

    # Reads response byte ACK = "E5"
    read = ser.read(1)

    # Sends the request
    ser.write(bytes.fromhex("10 7B FD 78 16"))

    # Resv. the response
    read = ser.read(211)

    listbytes = list(read)
    print("Response: PO3")
    print(listbytes)
    data = DataInterpreter(listbytes)
    with open("D:\\04_Python\\UV22_P03.csv", 'a') as csv_file:
        my_csv_writer = csv.writer(csv_file, delimiter=",", lineterminator="\n")
        my_csv_writer.writerow(data)

    return ""

"""
todo fix bytes verwenden. das sollte mit abstand das schnellste sein
"""
def DataInterpreter(data):
    #data = [104, 205, 205, 104, 8, 1, 114, 53, 38, 105, 3, 181, 21, 1, 2, 0, 0, 0, 0, 134, 16, 131, 0, 64, 69, 46, 1, 0, 0, 2, 253, 224, 0, 16, 0, 2, 253, 201, 255, 129, 0, 233, 0, 2, 253, 201, 255, 130, 0, 233, 0, 2, 253, 201, 255, 131, 0, 234, 0, 3, 253, 217, 255, 129, 0, 161, 4, 0, 3, 253, 217, 255, 130, 0, 145, 14, 0, 3, 253, 217, 255, 131, 0, 13, 2, 0, 3, 253, 217, 0, 57, 21, 0, 4, 171, 255, 129, 0, 234, 0, 0, 0, 4, 171, 255, 130, 0, 62, 3, 0, 0, 4, 171, 255, 131, 0, 59, 0, 0, 0, 4, 171, 0, 99, 4, 0, 0, 1, 255, 225, 255, 129, 0, 85, 1, 255, 225, 255, 130, 0, 95, 1, 255, 225, 255, 131, 0, 48, 19, 253, 217, 255, 129, 0, 250, 95, 0, 19, 253, 217, 255, 130, 0, 193, 94, 0, 19, 253, 217, 255, 131, 0, 8, 95, 0, 20, 171, 255, 129, 0, 220, 18, 0, 0, 20, 171, 255, 130, 0, 157, 18, 0, 0, 20, 171, 255, 131, 0, 165, 18, 0, 0, 3, 255, 145, 0, 232, 3, 0, 175, 22]

    Active_Energy_Import = ParseData(data[23:29])
    Voltage_Phase_One = ParseData(data[41:43])
    Voltage_Phase_Two = ParseData(data[49:51])
    Voltage_Phase_Three = ParseData(data[57:59])
    Current_Phase_One = ParseData(data[65:68])
    Current_Phase_Two = ParseData(data[74:77])
    Current_Phase_Three = ParseData(data[83:86])
    Current_Total = ParseData(data[90:93])
    Active_Power_Phase_One = ParseData(data[98:102])
    Active_Power_Phase_Two = ParseData(data[107:111])
    Active_Power_Phase_Three = ParseData(data[116:120])
    Active_Power_Total = ParseData(data[123:127])
    #Power_Factor_Phase_One = ParseData(list([data[133:133]]))
    Power_Factor_Phase_One = ""
    #Power_Factor_Phase_Two = ParseData(list([data[140:140]]))
    Power_Factor_Phase_Two = ""
    #Power_Factor_Phase_Three = ParseData(list([data[147:147]]))
    Power_Factor_Phase_Three = ""

    # Create time to log
    timestamp = time.time()
    log_date = datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
    log_clock = datetime.datetime.fromtimestamp(timestamp).strftime("%H:%M:%S")


    Alldata = [str(timestamp), log_date, log_clock, Active_Energy_Import, Voltage_Phase_One, Voltage_Phase_Two, Voltage_Phase_Three, Current_Phase_One, Current_Phase_Two, Current_Phase_Three, Current_Total]
    Alldata.extend([Active_Power_Phase_One, Active_Power_Phase_Two, Active_Power_Phase_Three, Active_Power_Total, Power_Factor_Phase_One, Power_Factor_Phase_Two, Power_Factor_Phase_Three])
#    csv_row = ",".join(str(ele) for ele in Alldata)

    return Alldata


# Dreht bytes
def ParseData(data):
    #print(datetime)
    data_rev = []
    # Dreht die
    for ele in reversed(data):
        data_rev.append(ele)

    for idx, val in enumerate(data_rev):
        if(val != 0):
            data_rev = data_rev[idx:]
            break

    #print(data_rev)
    res = "".join(str(ele) for ele in data_rev)

    return res

def Create_New_Logging_Files():
    now = time.time()
    log_date = datetime.datetime.fromtimestamp(now).strftime("%Y_%m_%d_%H_%M")


    file_root = "D:\\04_Python\\"
    header = ["Timestamp", "Date", "Time", \
              "Active_Energy_Import", \
              "Voltage_Phase_One", "Voltage_Phase_Two", "Voltage_Phase_Three", \
              "Current_Phase_One", "Current_Phase_Two", "Current_Phase_Three", "Current_Total",\
              "Active_Power_Phase_One", "Active_Power_Phase_Two", "Active_Power_Phase_Three" , "Active_Power_Total",\
              "Power_Factor_Phase_One", "Power_Factor_Phase_Two", "Power_Factor_Phase_Three"]

    # P01
    file_url = file_root + "UV22_P01.csv"
    with open(file_url, 'w') as csv_file:
        my_csv_writer = csv.writer(csv_file, delimiter=",", lineterminator="\n")
        my_csv_writer.writerow(header)

    #P02
    file_url = file_root  + "UV22_P02.csv"
    with open(file_url, 'w') as csv_file:
        my_csv_writer = csv.writer(csv_file, delimiter=",", lineterminator="\n")
        my_csv_writer.writerow(header)

    #P03
    file_url = file_root + "UV22_P03.csv"
    with open(file_url, 'w') as csv_file:
        my_csv_writer = csv.writer(csv_file, delimiter=",", lineterminator="\n")
        my_csv_writer.writerow(header)



"""
Main function
"""
if __name__ == "__main__":
    Create_New_Logging_Files()

    # Starts the connection to the serial port
    ser = InitPySerial()
    ser.open()
    res = ser.isOpen()
    if(res != True):
        print("There seems to be a problem with the connection to the virtual com port.")
        sys.exit(-1)
    print("Connected = " + str(res) + " to Com Port = " + ser.name)


    for i in range(0, 720):
        print("Loop counter = " + str(i))
        ReadOut_UV22_P01(ser)
        ReadOut_UV22_P02(ser)
        ReadOut_UV22_P03(ser)
        time.sleep(60)

    ser.close()
    sys.exit(0)


    #input2 = 680B0B6873FD5225266903FFFFFFFF7516
    #input3 = bytes(input2, "hex")

    #hexstring = "68 0B 0B 68 73 FD 52 25 26 69 03 FF FF FF FF 75 16"
    hexstring = "680B0B6873FD5225266903FFFFFFFF7516"

    # write
    intput_bytes = bytes.fromhex(hexstring)



    ser.write(intput_bytes)
    time.sleep(1)

    #read
    read = ser.read(1)
    time.sleep(1)

    # Write
    input2 = bytes.fromhex("10 7B FD 78 16")
    ser.write(input2)
    #read

    read = ser.read(211)

    listbytes = list(read)
    hexlist = []
    for element in listbytes:
        hexlist.append(hex(element))


    ser.close()


    """
    hexstring = "680B0B6873FD5225266903FFFFFFFF7516"

    tobytes = bytes.fromhex(hexstring)
    print(tobytes)
    listbytes = list(tobytes)
    hexlist = []
    for element in listbytes:
    hexlist.append(hex(element))
    sys.exit(0)





    # 134 16 131 0
    # 6 data bytes
    active_Energy_Import = []
    key_active_Energy_Import = [134, 16, 131]

    Voltage_p1 = []
    key_Voltage_p1 = [2, 253, 201, 255, 129]

    Voltage_p2 = []
    key_Voltage_p2 = [2, 253, 201, 255, 130]

    Voltage_p3 = []
    key_Voltage_p3 = [2, 253, 201, 255, 131]

    Current_p1 = []
    key_Current_p1 = [3, 253, 217, 255, 129]
    Current_p2 = []
    key_Current_p2 = [3, 253, 217, 255, 130]
    Current_p3 = []
    key_Current_p3 = [3, 253, 217, 255, 131]
    Current_t = []
    key_Current_t = [3, 253, 217]

    active_Power_p1 = []
    key_active_Power_p1 = [4, 171, 255, 129]
    active_Power_p2 = []
    key_active_Power_p2 = [4, 171, 255, 130]
    active_Power_p3 = []
    key_active_Power_p3 = [4, 171, 255, 131]
    active_Power_t = []
    key_active_Power_t = [4, 171]

    power_factor_p1 = []
    key_power_factor_p1 = [1, 255, 225, 255, 129]
    power_factor_p2 = []
    key_power_factor_p2 = [1, 255, 225, 255, 130]
    power_factor_p3 = []
    key_power_factor_p3 = [1, 255, 225, 255, 131]



    """
