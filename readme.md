# how to run test cases?

### Run Docker Container
```bash
docker run -it -v "$PWD":"/test" ubuntu:18.04 bash
```

### Prepare
```bash
cd /test
apt update && apt install python3 python3-pip
pip3 install -r requirements.txt
```

### Run Scripts
```bash
python3 raw-winrm-test.py
python3 winrm-lib-test.py
bash curl-test.sh http://<windows ip>:5985 <username> <password>
```

### what is happening behind the scene?
* **winrm-lib-test.py**

It uses `pywinrm` library to make connection to windows hosts
and run test command to check the connection.

* **raw-winrm-test.py**

It uses `requests-ntlm` library to make connection to windows hosts
and run test command to check the connection.

* **curl-test.sh**

It uses `curl / libcurl` to make connection to windows hosts
and run test command to check the connection.

**Above mentioned cases will help you to identify if there is any issue with library or
connection itself.**


### Sample Outputs with hardcoded values
```bash
$ python3 raw-winrm-test.py 
Starting NTLM Script
415 b'' <Response [415]>
```

```bash
$ python3 winrm-lib-test.py 
Starting PyWinRM Script
Running High Level API Test
b'\r\nWindows IP Configuration\r\n\r\n   Host Name . . . . . . . . . . . . : WIN-06GI2II5U5U\r\n   Primary Dns Suffix  . . . . . . . : \r\n   Node Type . . . . . . . . . . . . : Hybrid\r\n   IP Routing Enabled. . . . . . . . : No\r\n   WINS Proxy Enabled. . . . . . . . : No\r\n   DNS Suffix Search List. . . . . . : us-east-1.ec2-utilities.amazonaws.com\r\n                                       ec2.internal\r\n\r\nEthernet adapter Ethernet 3:\r\n\r\n   Connection-specific DNS Suffix  . : ec2.internal\r\n   Description . . . . . . . . . . . : Amazon Elastic Network Adapter\r\n   Physical Address. . . . . . . . . : 0A-7B-98-F0-09-5D\r\n   DHCP Enabled. . . . . . . . . . . : Yes\r\n   Autoconfiguration Enabled . . . . : Yes\r\n   Link-local IPv6 Address . . . . . : fe80::388c:83c6:195f:c4cc%21(Preferred) \r\n   IPv4 Address. . . . . . . . . . . : 10.72.12.116(Preferred) \r\n   Subnet Mask . . . . . . . . . . . : 255.255.255.0\r\n   Lease Obtained. . . . . . . . . . : Friday, January 22, 2021 8:58:40 AM\r\n   Lease Expires . . . . . . . . . . : Friday, January 22, 2021 11:28:41 AM\r\n   Default Gateway . . . . . . . . . : 10.72.12.1\r\n   DHCP Server . . . . . . . . . . . : 10.72.12.1\r\n   DHCPv6 IAID . . . . . . . . . . . : 353008536\r\n   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-27-9C-3C-65-0A-86-3B-5E-2B-79\r\n   DNS Servers . . . . . . . . . . . : 10.72.0.2\r\n   NetBIOS over Tcpip. . . . . . . . : Enabled\r\n\r\nTunnel adapter isatap.ec2.internal:\r\n\r\n   Media State . . . . . . . . . . . : Media disconnected\r\n   Connection-specific DNS Suffix  . : ec2.internal\r\n   Description . . . . . . . . . . . : Microsoft ISATAP Adapter\r\n   Physical Address. . . . . . . . . : 00-00-00-00-00-00-00-E0\r\n   DHCP Enabled. . . . . . . . . . . : No\r\n   Autoconfiguration Enabled . . . . : Yes\r\n' b''
Running Low Level API Test
b'\r\nWindows IP Configuration\r\n\r\n   Host Name . . . . . . . . . . . . : WIN-06GI2II5U5U\r\n   Primary Dns Suffix  . . . . . . . : \r\n   Node Type . . . . . . . . . . . . : Hybrid\r\n   IP Routing Enabled. . . . . . . . : No\r\n   WINS Proxy Enabled. . . . . . . . : No\r\n   DNS Suffix Search List. . . . . . : us-east-1.ec2-utilities.amazonaws.com\r\n                                       ec2.internal\r\n\r\nEthernet adapter Ethernet 3:\r\n\r\n   Connection-specific DNS Suffix  . : ec2.internal\r\n   Description . . . . . . . . . . . : Amazon Elastic Network Adapter\r\n   Physical Address. . . . . . . . . : 0A-7B-98-F0-09-5D\r\n   DHCP Enabled. . . . . . . . . . . : Yes\r\n   Autoconfiguration Enabled . . . . : Yes\r\n   Link-local IPv6 Address . . . . . : fe80::388c:83c6:195f:c4cc%21(Preferred) \r\n   IPv4 Address. . . . . . . . . . . : 10.72.12.116(Preferred) \r\n   Subnet Mask . . . . . . . . . . . : 255.255.255.0\r\n   Lease Obtained. . . . . . . . . . : Friday, January 22, 2021 8:58:40 AM\r\n   Lease Expires . . . . . . . . . . : Friday, January 22, 2021 11:28:40 AM\r\n   Default Gateway . . . . . . . . . : 10.72.12.1\r\n   DHCP Server . . . . . . . . . . . : 10.72.12.1\r\n   DHCPv6 IAID . . . . . . . . . . . : 353008536\r\n   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-27-9C-3C-65-0A-86-3B-5E-2B-79\r\n   DNS Servers . . . . . . . . . . . : 10.72.0.2\r\n   NetBIOS over Tcpip. . . . . . . . : Enabled\r\n\r\nTunnel adapter isatap.ec2.internal:\r\n\r\n   Media State . . . . . . . . . . . : Media disconnected\r\n   Connection-specific DNS Suffix  . : ec2.internal\r\n   Description . . . . . . . . . . . : Microsoft ISATAP Adapter\r\n   Physical Address. . . . . . . . . : 00-00-00-00-00-00-00-E0\r\n   DHCP Enabled. . . . . . . . . . . : No\r\n   Autoconfiguration Enabled . . . . : Yes\r\n' b'' 0
Stopping PyWinRM Script
```

```bash
$ ./curl-test.sh http://xxxxxxxxxxxx:5985 test-user test-password 
*   Trying xxxxxxxxxxxx:5985...
* TCP_NODELAY set
* Connected to xxxxxxxxxxxx (xxxxxxxxxxxx) port 5985 (#0)
> GET /wsman HTTP/1.1
> Host: xxxxxxxxxxxx:5985
> User-Agent: curl/7.68.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 405 
< Allow: POST
< Server: Microsoft-HTTPAPI/2.0
< Date: Fri, 22 Jan 2021 10:31:16 GMT
< Connection: close
< Content-Length: 0
< 
* Closing connection 0
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying xxxxxxxxxxxx:5985...
* TCP_NODELAY set
* Connected to xxxxxxxxxxxx(xxxxxxxxxxxx) port 5985 (#0)
* Server auth using NTLM with user 'molecule'
> POST /wsman HTTP/1.1
> Host: xxxxxxxxxxxx:5985
> Authorization: NTLM xxxxxxxxxxxxxxxxxxx=
> User-Agent: curl/7.68.0
> Accept: */*
> Content-Length: 0
> Content-Type: application/x-www-form-urlencoded
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 401 
< Server: Microsoft-HTTPAPI/2.0
< WWW-Authenticate: Negotiate
< WWW-Authenticate: Basic realm="WSMAN"
< Date: Fri, 22 Jan 2021 10:31:16 GMT
< Connection: close
< Content-Length: 0
< 
* Closing connection 0
```

