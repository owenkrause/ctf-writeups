from pwn import *
import itertools

io = remote("chal.ctf-league.osusec.org", 1308)

# useless info
io.recvline()
io.recvline()

# send user input of 48 bytes
# since the OTPs have length 48 bytes
user_input = b'\x00' * 48
io.sendline(user_input)
io.sendline(user_input)
io.sendline(user_input)

# receive the cyphertexts
cyphertext1 = io.recvline()[58:-1]
io.recvline()
cyphertext2 = io.recvline()[58:-1]
io.recvline()
cyphertext3 = io.recvline()[58:-1]
io.recvline()
io.recvline()

# get the encrypted flag
encrypted_flag = io.recvline()[:-1]

# function given in recycle.py 
def truncating_xor(a, b):
  return bytes(ai ^ bi for ai, bi in zip(a, b))

# function given in recycle.py 
# combines the otps into one 
# ['one', 'two', 'three'] -> b'ottnwheor'
def mix_otps(a, b, c):
  return bytes(itertools.chain.from_iterable(zip(a, b, c)))

# xor the cyphertext and user_input to get each otp
otp1 = truncating_xor(user_input, bytes.fromhex(cyphertext1.decode()))
otp2 = truncating_xor(user_input, bytes.fromhex(cyphertext2.decode()))
otp3 = truncating_xor(user_input, bytes.fromhex(cyphertext3.decode()))

# mix the otps together using the mix_otps function
# xor the mixed otps and the encrypted flag
# to get the decrypted flag
print(truncating_xor(mix_otps(otp1, otp2, otp3), bytes.fromhex(encrypted_flag.decode())).decode())
