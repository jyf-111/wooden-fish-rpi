#!/bin/bash
hciconfig hci0 up
hciconfig hci0 name 'woodfish'
hciconfig hci0 class 0x000500
hciconfig hci0 piscan
hciconfig hci0 sspmode 1
hciconfig hci0 noauth
hciconfig hci0 noencrypt
sdptool add SP

python3 woodfish/main.py
