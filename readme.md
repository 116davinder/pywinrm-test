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
```