Access: nc chal.ctf-league.osusec.org 1306

Download: http://chal.ctf-league.osusec.org/yoco/reuse.py

## Observations
We are given an encrypted flag and the opportunity to encrypt our own message using the same key. 

## Approach
In order to decrypt the encrypted flag, we need the key or so called one-time pad (OTP). Since we are given the chance to use the key twice, we can use a property of the XOR operation to figure out what the OTP is. XOR is a bitwise operator that returns 1 if the inputs are different and 0 if they are the same. Since we are given one input and the output, we can use the following theorem to find the other input.
```
Given xor(a,b) = c the following is true: xor(a,c) = b and xor(b,c) = a.
To prove this, let c = 0 then a = b = 0 or 1
xor(a,c) = b -> xor(a,0) = b, then a = b = 0 or 1
xor(b,c) = a ->  xor(b,0) = a, then a = b = 0 or 1
```
From this we can derive the following pseudocode.
```js
xor(user_input, otp) = encrypted_user_input
xor(user_input, encrypted_user_input) = otp
```

Now that we have the OTP, we can decrypt the flag.
```js
xor(otp, encrypted_flag)
```

