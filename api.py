import assemblyai as aai

aai.settings.api_key = "6a0f67a7a0934dacaa68968e2d5c5c3a"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")
# transcript = transcriber.transcribe("./my-local-audio-file.wav")

print(transcript.text)
