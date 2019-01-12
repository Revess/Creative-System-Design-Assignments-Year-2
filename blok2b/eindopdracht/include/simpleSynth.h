#ifndef _SIMPLESYNTH_H_
#define _SIMPLESYNTH_H_
#include "synth.h"
using namespace std;

//See .cpp file for the explenation

class SimpleSynth : public Synth {
    public:
        SimpleSynth(double samplerate, double frequency, string waveform);
        ~SimpleSynth();
};

#endif