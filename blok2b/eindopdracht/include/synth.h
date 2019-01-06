#ifndef _SYNTH_
#define _SYNTH_
#include "oscillator.h"
#include <vector>
#include <string>
using namespace std;

class Synth{
    public:

        Synth(double samplerate, double frequency, string waveform, int amount);
        virtual ~Synth();

        virtual void setFrequency(double frequency);
        void addOscillator(string waveform, int amount, double frequency);
        virtual double getSample();
        virtual void tick();

    protected:
        double frequency;
        double samplerate;
        Oscillator *oscillator;
        vector<Oscillator*> oscillatorVector;
        string waveform;
};

#endif