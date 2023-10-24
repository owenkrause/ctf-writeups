from pwn import *
io = remote('chal.ctf-league.osusec.org', 1307)
io.recvline()

# get encrypted flag
encrypted_flag = bytes.fromhex(io.recvline()[:-1].decode())

# get otp by performing XOR operation on first four characters of encrypted flag
# and b'osu{ since all flags start with that
otp = xor(encrypted_flag[0:4], b'osu{')

# decrypt flag by performing XOR operation on otp and encrypted flag
print(xor(otp, encrypted_flag).decode())
