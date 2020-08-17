import random

lower = "abcdefghijklmñnopqrstuvwxyz"
upper = lower.upper()
numbers = "1234567890"
symbols = "[]{0*}:/.;,-"

all = lower + upper + numbers + symbols
lenght = 16

print (''.join(random.sample(all,lenght)))