from pwn import * 

io = remote("chal.ctf-league.osusec.org", 1306)

# recieve encrypted flag
encrypted_flag = io.recvline()[22:98]
io.recvline()

# send input with length of 38 bits
user_input = b'\x00' * 38
io.sendline(user_input)

# recieve encrypted message
encrypted_message = io.recvline()[58:-1]

# get otp by performing XOR operation on user input and encrypted message
otp = xor(user_input, bytes.fromhex(encrypted_message.decode()))

# decrypt flag by performing XOR operation on otp and encrypted flag
print(xor(otp, bytes.fromhex(encrypted_flag.decode())).decode())
