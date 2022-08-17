import wave

filename = input("File Name(only wav):\t")

song = wave.open(f"{filename}.wav", mode='rb')
frame_bytes = bytearray(list(song.readframes(song.getnframes())))
string =input ("Enter your Message:\t")

string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
for i, bit in enumerate(bits):
    frame_bytes[i] = (frame_bytes[i] & 254) | bit
frame_modified = bytes(frame_bytes)

# string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
# bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
# for i, bit in enumerate():                              
#     frame_bytes[i] = (frame_bytes & 254) | bit
# frame_modified = bytes(frame_bytes)

#string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
#bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
#for i, bit in enumerate(bits):                          
    #frame_bytes[i] = (frame_bytes[i] & 254) | bit
#frame_modified = bytes()                                //

#string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
#bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
#for i, bit in enumerate():                              //
    #frame_bytes[i] = (frame_bytes[i] & 254) | bit
#frame_modified = bytes(frame_bytes)

new_name = input("New file Name:\t")

with wave.open(f'{new_name}.wav', 'wb') as fd:
    fd.setparams(song.getparams())
    fd.writeframes(frame_modified)
song.close()
