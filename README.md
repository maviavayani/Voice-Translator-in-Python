<b>Voice-Translator-in-Python</b>
<br>
This Python code uses various libraries to perform the following tasks:

It takes input for the source language (input_lang) and the target language (output_lang) from the user.

It uses the Speech Recognition library (speech_recognition) to capture audio from the microphone and then transcribes the spoken words into text using Google's speech recognition service (recognize_google), with the input language specified.

The transcribed text is then translated from the source language to the target language using the Google Translate library (googletrans).

The translated text is converted into speech using the Google Text-to-Speech library (gtts).

The generated audio is saved as "Audio.mp3" and played using the playsound library.

In summary, this script records spoken words, transcribes them, translates them, converts the translation into speech, saves it as an audio file, and plays the audio. It can be used for language translation and text-to-speech tasks.
