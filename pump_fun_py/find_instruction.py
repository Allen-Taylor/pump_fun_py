import struct

# "Instruction Data Raw" taken from pump.fun transactions on solscan. 

# Buy Example: 66063d1201daebeac08049190403000080778e0600000000
# Sell Example: 33e685a4017f83ad5f5360df6d000000ae1f7e0100000000

hex_string = "66063d1201daebeac08049190403000080778e0600000000"

# Split the hexadecimal string into 8-byte segments
segments = [hex_string[i:i+16] for i in range(0, len(hex_string), 16)]

print("Segments:")

for segment in segments:
    print(segment)

# Convert each segment into a 64-bit integer in little-endian format
integers = [struct.unpack('<Q', bytes.fromhex(segment))[0] for segment in segments]

print("Integers:")

for integer in integers:
    print(integer)

print("Converted integers:", integers)

# buy instruction code - 16927863322537952870
# sell instruction code - 12502976635542562355
