# receive the flag via nc and crack it

import base64
import socket

CHARSET = base64._b85alphabet.decode()
N = len(CHARSET)

# receive the flag via nc
HOST = "instances.challenge-ecw.fr"
PORT = 41086
NB_GET_ENC = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.recv(1024)

# make a dict with all the CHARSET and their recurence

rec = []
for i in range(2198):
    rec.append(dict())
    for x in CHARSET:
        rec[i][x] = 0

s.send(b"1\n")
current_enc = s.recv(4096).decode().split("\n")[0]

# add the recurence of each char
for i in range(len(current_enc)):
    rec[i][current_enc[i]] += 1

for i in range(NB_GET_ENC):
    s.send(b"1\n")
    current_enc = ""
    while len(current_enc) != 2198:
        current_enc += s.recv(4096).decode().split("\n")[0]
    for j in range(len(current_enc)):
        rec[j][current_enc[j]] += 1
    if i % (NB_GET_ENC//10) == 0:
        print(i)

# get the most used char for each position
res = ""
for i in range(2198):
    res += max(rec[i], key=rec[i].get)

print(res)