#! /bin/bash
dpkg-query -l python3-tk || sudo apt-get install python3-tk
printf "#! /bin/bash\nsudo python3 `pwd`/toggle_hosts.py &\n" > toggle_hosts
chmod +x toggle_hosts
sudo cp toggle_hosts /usr/local/bin
toggle_hosts
