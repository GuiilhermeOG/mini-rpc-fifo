import os
import sys
import random
import argparse

SERVER_FIFO = "/tmp/rpc_req_fifo"
CLIENT_FIFO = f"tmp/rpc_resp_{os.getpid()}"

if os.path.exists(CLIENT_FIFO):
    os.remove(CLIENT_FIFO)
os.mkfifo(CLIENT_FIFO, mode=0o600)

parser = argparse.ArgumentParser()
parser.add_argument("operacao", choices=["soma", "sub", "mult", "div", "fat"])
args = parser.parse_args()

