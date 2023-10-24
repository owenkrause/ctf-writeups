Access: nc chal.ctf-league.osusec.org 1307

Download: http://chal.ctf-league.osusec.org/yoco/reduce.py

## Observations
We are given an encrypted flag but no opportunity to encrypt something with the same key like in flag 1.

The OTP is a random bytestring of length four. There is a wrapping XOR function that first turns the OTP into a repeated sequence that is the length of the flag using.
```python
def wrapping_xor(a, b):
  # flag is not shorter than otp so this is redundant
  if len(a) <= len(b):
    a_iter = itertools.cycle(a)
    return bytes(ai ^ bi for ai, bi in zip(a_iter, b))
  else:
    # turns the otp into an infinitely repeating sequence
    b_iter = itertools.cycle(b)

    # zip(a, b_iter) maps each part of the flag to part of the otp cycle.
    # (b'o', \x00), (b's', \x00), (b'u', \x00)...
    # finally, for each ai and bi in each pair, perform the XOR operation.
    return bytes(ai ^ bi for ai, bi in zip(a, b_iter))

otp = os.urandom(4)
encrypted_flag = wrapping_xor(FLAG, otp)
```
## Approach
Since we know the OTP is only four bytes long and gets repeated for the length of the flag, it is true that if we can decode the first four bytes of the flag correctly then we can decode the rest. Since the first four bytes of the flag is always ``osu{`` we can perform an XOR operation with the bytestring ``osu{`` and the first four bytes of the encrypted flag. 
```python
xor(encrypted_flag[0:4], b'osu{')
```
This gives us the OTP and now we can simply perform an XOR operation with the OTP and the encrypted flag to decrypt it. 
```python
xor(otp, encrypted_flag)
```
