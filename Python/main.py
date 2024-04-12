import serial

serialDevice = serial.Serial("COM3")

print("Zeskanuj kod kreskowy:")
while serialDevice.isOpen():

    scannedCode = serialDevice.readline()
    decodedCode = scannedCode.decode("utf-8")

    print(f"Zeskanowany kod: {decodedCode}")

serialDevice.close()
