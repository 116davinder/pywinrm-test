#! /usr/bin/python

from winrm import Session, Protocol

print("Starting PyWinRM Script")
host = input("hostname of windows with port: ")
user = input("username of windows: ")
password = input("password of windows: ")

print("Running High Level API Test")
s = Session(host, auth=(user, password))
r = s.run_cmd('ipconfig', ['/all'])

print(r.std_out, r.std_err)

print("Running Low Level API Test")
p = Protocol(
    endpoint='http://' + host + '/wsman',
    transport='ntlm',
    username=user,
    password=password,
    server_cert_validation='ignore')
shell_id = p.open_shell()
command_id = p.run_command(shell_id, 'ipconfig', ['/all'])
std_out, std_err, status_code = p.get_command_output(shell_id, command_id)
p.cleanup_command(shell_id, command_id)
p.close_shell(shell_id)
print(std_out, std_err, status_code)

print("Stopping PyWinRM Script")
