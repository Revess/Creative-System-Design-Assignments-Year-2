from midiutil import MIDIFile

track    = 0
channel  = 9
time     = 0
duration = 1
bpm    = 200
velocity   = 100

MyMIDI = MIDIFile(2)
MyMIDI.addTempo(track, time, bpm)

MyMIDI.addTimeSignature(track, 0, 7, 2, 24)


MyMIDI.addNote(track, channel, 35, 0, duration, velocity)
MyMIDI.addNote(track, channel, 38, 3 * duration, duration, velocity)
MyMIDI.addNote(track, channel, 38, 5 * duration, duration, velocity)
for i in range(7):
    MyMIDI.addNote( track, channel, 42, (time + i) * duration, duration,
                    velocity)

with open("beat.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)