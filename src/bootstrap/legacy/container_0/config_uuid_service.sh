#!/bin/bash
sudo chmod +x uuid_server.js
sudo cp uuid_server.js /usr/bin/
sudo cp uuid_service.service /etc/systemd/system/uuid_service.service
sudo chmod 644 /etc/systemd/system/uuid_service.service
sudo systemctl enable uuid_service
sudo systemctl start uuid_service
# consider using chromium on windows to test the fucking plugin. able to install it outside the shit.
# also consider something like that on Android. Consider finding some prankable system.
# in general, prankable. WINDOWS-HACKED. MACOS-HACKED. LINUX-HACKED.