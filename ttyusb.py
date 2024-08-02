!/opt/wmt/python-env/bin/python
import sys
import argparse
#import serial
import re
import subprocess

def extract_usb_numbers(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Regex para encontrar la línea que contiene "transport.deviceid usb" y extraer el número
    pattern = re.compile(r'transport\.deviceid usb:(\d+-\d+\.\d+)')
    usb_numbers = []

    for line in lines:
        match = pattern.search(line)
        if match:
            usb_number = match.group(1)
            usb_numbers.append(usb_number)

    return usb_numbers

def find_ttyUSB_in_dmesg(usb_numbers):
    dmesg_output = subprocess.check_output(['dmesg']).decode('utf-8')
    ttyUSB_lines = []

    for usb_number in usb_numbers:
        # Regex para buscar el usb_number en la salida de dmesg
        pattern = re.compile(rf'{usb_number}.*ttyUSB\d+')
        matches = pattern.findall(dmesg_output)
        ttyUSB_lines.extend(matches)

    return ttyUSB_lines

if __name__ == "__main__":
    file_path = "/home/mauricio/waldnet/python/pmsdump"
    usb_numbers = extract_usb_numbers(file_path)
    ttyUSB_lines = find_ttyUSB_in_dmesg(usb_numbers)

    for line in ttyUSB_lines:
        print(line)

