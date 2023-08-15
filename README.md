# kill_process_with_python

# Language used:
- Python 3.9.7 and its libraries: time and psuti

# A respeito do programa:

Terminates all processes running on the following ports: 80, 443, 3306, 21, 14147
If there is any process running on these ports, it will display a message in the CLI that will last for 10 seconds.

# Observations:
  
This program was designed to prepare the local environment for hosting a web server and exchanging files via FTP. In some cases simply shutting down the server does not stop service on the ports.
If you want to use it for another purpose, you can modify the list of ports. 

# Pontos a ser melhorados:

- Have a testing program;
- Be object-oriented;
- Allow manual input of ports to terminate processes.

# Execution image:

![image](https://user-images.githubusercontent.com/95552879/222029849-35a99ef9-089e-4b2a-b874-a160beb8af44.png)

