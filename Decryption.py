import wave

filename = input("File Name(only wav):\t")

song = wave.open(f"{filename}.wav", mode='rb')

frame_bytes = bytearray(list(song.readframes(song.getnframes())))


extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
decoded = string.split("###")[0]

#extracted = [frame_bytes[j] & 1 for i in range(len(frame_bytes))]
#string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
#decoded = string.split("###")[0]


#extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
#string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
#decoded = string.split("###")[]


#extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
#string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
#decoded = string("###")[0]



print("Sucessfully decoded: "+decoded)
song.close()
input("\n\nExit...")
