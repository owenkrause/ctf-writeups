Access: nc chal.ctf-league.osusec.org 1308

Download: http://chal.ctf-league.osusec.org/yoco/recycle.py

## Observations
Three random OTPs are generated and mixed to create one OTP that is used to encrypt the flag. We are given an opportunity to encrypt a message using each OTP. The mixing function is described below.
```python
def mix_otps(a, b, c):
    # zip(a, b, c) maps each byte at index i of the bytestrings to eachother
    # zip(b'one', b'two', b'three') -> (o,t,t), (n,w,h), (e,o,r)
    # itertools.chain.from_iterable joins them together -> 'ottnwheor'
    return bytes(itertools.chain.from_iterable(zip(a, b, c)))

otps = [os.urandom(48) for _ in range(3)]
flag_otp = mix_otps(*otps)
```
## Approach
In order to decrypt the flag, we must get the final OTP. The final OTP is the three OTPs passed through the ``mix_otps`` function. So our starting point is finding all three of the OTPs. Since we are given the chance to encrypt our own message using each of the OTPs, we can get the OTPs by performing an XOR operation on the message and the encrypted messaged.
```python
# do this three times for each input and encrypted message
xor(user_input, encrypted_message)
```
Now that we have the three OTPs, we can use the ``mix_otps`` function to get the final OTP.
```python
mixed_otps = mix_otps(otp1, otp2, otp3)
```
Finally, we can perform an XOR operation on the final OTP and the encrypted flag to decrypt it.
```python
xor(mixed_otps, encrypted_flag)
```

