# Network-Scanner
Scanning the ip and the open ports on a local network

It's necessary to modify the ping command depending on your operating system

| OS        | Ping command (line 20)  |  
|:---------:|:-----------------------:|
| Linux/OSX | ("ping -c 1 -t 0 " + _ip + str(hostbit), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) |
| Windows   | ("ping " + _ip + str(hostbit) + " -n 1", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) |

Enter at line 14 the ports you want to test the connection

⚠️ I'm not responsible of your actions ⚠️
