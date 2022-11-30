#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import paramiko
import time

def get_parameters(config):
  with open(config) as json_file:
    data = json.load(json_file)
  return data

def create_ssh_connection(p):
  #--- Create a new Paramiko SSH connection object
  conn = paramiko.SSHClient()
  #--- 新規ホスト鍵に関しては警告を出しつつ受け入れる
  """
  C:\Python310\lib\site-packages\paramiko\client.py:852: UserWarning:
  Unknown ssh-ed25519 host key for [192.168.30.33]:22: b'<finger print>'
  """
  conn.set_missing_host_key_policy(paramiko.WarningPolicy())
  #--- extract ED25519 key from specified private_key file
  ed25519_key = paramiko.Ed25519Key.from_private_key_file(p['PRIVATE_KEY'])

  conn.connect(p['HOST'], p['PORT'], p['USERNAME'], pkey=ed25519_key)
  return conn

def decode_utf8(str):
  return str.decode('utf-8', 'strict')

def main(config):
  params = get_parameters(config)
  conn = create_ssh_connection(params)
  buffer = b''

  #--- create a shell session for multiple commands
  remote_shell = conn.invoke_shell()

  #--- receive remote host shell output
  time.sleep(2)
  buffer += remote_shell.recv(65535)

  #--- send the command
  remote_shell.send("ls -l\n")
  time.sleep(1)
  buffer += remote_shell.recv(65535)

  #--- display the output
  print( decode_utf8(buffer) )

  #--- disconnect
  conn.close()

if __name__ == '__main__':
  args = sys.argv
  main(args[1])

sys.exit()

#--- example
# ./test_paramiko.py ssh_config.json
