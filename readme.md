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