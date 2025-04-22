import os

SERVER_FIFO = "/tmp/rpc_req_fifo"
CLIENT_FIFO = f"tmp/rpc_resp_{os.getpid()}"

if os.path.exists(SERVER_FIFO):
    os.remove(SERVER_FIFO)
os.mkfifo(SERVER_FIFO, mode=0o600)

if os.path.exists(CLIENT_FIFO):
    os.remove(CLIENT_FIFO)
os.mkfifo(CLIENT_FIFO, mode=0o600)
