from gtts import gTTS
import os

print("What do u want to say?")
language = "en"
speech = input()



#speech = "চিল করো আইসিটির পোলাপান"

output = gTTS(text=speech,lang=language , slow=True)
output.save("speech.mp3")

os.system("start speech.mp3")



