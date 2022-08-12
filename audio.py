from winsound import PlaySound, SND_FILENAME, SND_LOOP, SND_ASYNC

def start(): # 音を鳴らす。
    PlaySound("C:\Windows\Media\Alarm10.wav", SND_FILENAME|SND_LOOP|SND_ASYNC)

def stop(): # 音を終わらせる。
    PlaySound(None, SND_FILENAME)
