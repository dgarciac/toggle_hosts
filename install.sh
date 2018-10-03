#! /bin/bash
dpkg-query -l python3-tk || sudo apt-get install python3-tk
sudo cp toggle_hosts /usr/local/bin
toggle_hosts
