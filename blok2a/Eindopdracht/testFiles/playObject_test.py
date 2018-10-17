import simpleaudio as sa

samples = [sa.WaveObject.from_wave_file("../audioFiles/CowBell.wav")]
x = 0
while True:    
    playObject = samples[0].play()
    if x > 5:
        playObject.stop()
    x +=1