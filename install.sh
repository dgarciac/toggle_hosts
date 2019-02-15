#! /bin/bash
dpkg -s python3-tk 2>/dev/null >/dev/null || sudo apt-get -y install python3-tk
printf "#! /bin/bash\nsudo python3 `pwd`/toggle_hosts.py &\n" > toggle_hosts
chmod +x toggle_hosts
sudo cp toggle_hosts /usr/local/bin
toggle_hosts
