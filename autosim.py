import argparse
import serial

parser = argparse.ArgumentParser()
parser.add_argument ('port', help="The serial port")

args = parser.parse_args()

commands = [ 'at!impref="AUTO-SIM"' ]

with serial.Serial (args.port, 19200, timeout=2) as ser:
    for cmd in commands:
        ser.write((cmd + '\r\n').encode())
        while True:
            line = ser.readline().decode().strip()
            if not line:
                continue
            print(line)
            if 'OK' in line:
                break
            if 'ERROR' in line:
                break


