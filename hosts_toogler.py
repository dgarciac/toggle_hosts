#!/usr/env/bin python3

import subprocess
from tkinter import *


def get_etc_hosts():
    return subprocess.check_output(['cat', '/etc/hosts']).decode().split('\n')

def get_hosts():
    l = get_etc_hosts()
    d = {}
    count = 0
    for i in l:
        if '127.0.0.1' not in i:
            count +=1
            continue
        d[count] = {}
        if i.strip()[0] == '#':
            d[count]['commented'] = 1
            d[count]['line'] = i.strip().split()[-1]
        else:
            d[count]['commented'] = 0
            d[count]['line'] = i.strip().split()[-1]
        count += 1
    return d


class HostsWidget:
    def __init__(self, master):
        self.hosts = get_hosts()
        self.vars = []
        for i in self.hosts.keys():
            var = IntVar()
            c = Checkbutton(master, variable=var, text=self.hosts[i]['line'], command=self.get_checkbutton_changes)
            if self.hosts[i]['commented'] == 1:
                c.select()
            c.pack(anchor=W, ipadx=50)
            self.vars.append(var)
        b = Button(master, text='Save changes', command=self.change_states)
        b.pack()

    def get_checkbutton_changes(self):
        self.hosts = get_hosts()        
        return [i.get() for i in self.vars]

    def change_states(self):
        etc_hosts = get_etc_hosts()
        for i, b in zip(self.get_checkbutton_changes(), self.hosts):
            if i != self.hosts[b]['commented']:
                if self.hosts[b]['commented'] == 1:
                    etc_hosts[b] = etc_hosts[b].strip("# ")
                else:
                    etc_hosts[b] = '#' + etc_hosts[b]
        with open('/etc/hosts', 'w') as output:
            try:
                for line in etc_hosts[:-1]:
                    output.write(line + '\n')
                output.write(etc_hosts[-1])
            except KeyError:
                pass
        
root = Tk()
my_gui = HostsWidget(root)
root.title("HOSTS TOOGLER")
root.mainloop()