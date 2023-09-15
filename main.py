import googletrans
import speech_recognition as sr
import gtts
import playsound

# Input Language
input_lang = str(input("Enter your input language key:"))
# Output Language
output_lang = str(input("Enter your input language key:"))
Recognize = sr.Recognizer()
# Record Audio
with sr.Microphone() as source:
    print("Listening...")
    voice = Recognize.listen(source)

    # Voice to Text
    text = Recognize.recognize_google(voice,language=input_lang)
    print(text)

#provides a simple API for translating text from one language to another.
translator = googletrans.Translator()
translation = translator.translate(text,dest=output_lang)
print(translation.text)

# Convert text to voice/speech
converted_voice = gtts.gTTS(translation.text, lang=output_lang)
# Save the Voice from Audio File
converted_voice.save("Audio.mp3")
# Play the voice
playsound.playsound("Audio.mp3")