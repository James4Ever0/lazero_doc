#!/bin/bash
while true
do
	pip3 install pytesseract
	if [ $? -eq 0 ]; then
                break
	fi
done
