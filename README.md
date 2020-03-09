Deauthenticator
------
  A tool to with in take two input as ip address of gateway and ip address of target device. Then it will block all the data of 
  target of victim computer making him think that the server is down.The code could also be modified such that you could 
  disconnect all the users from the specific network or leave someone behind.
  
        -h, --help            show this help message and exit
        -t TARGET, --target TARGET
                        IP address of Target computer
        -d SPOOF, -r SPOOF, -s SPOOF, --spoof SPOOF
                        IP address of Router/Gateway
   eg.
              
                python deauthenticator.py -t 192.168.137.54 -d 192.168.137.1
