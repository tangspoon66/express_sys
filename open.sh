#!/bin/bash
echo -n -e "\xA0\x01\x01\xA2" >/dev/ttyUSB0
sleep 0.5s
echo -n -e "\xA0\x01\x00\xA1" >/dev/ttyUSB0