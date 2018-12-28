#ifndef _SYNTH_H_
#define _SYNTH_H_
#include "sine.h"
#include "saw.h"
#include "square.h"
#include "triangle.h"
#include <string>
using namespace std;

class Synth {
    public:
    Synth(string type, double frequency, string waveform, float amplitude, double samplerate);
    virtual ~Synth();

    //Getters en Setters
    void setEnvelope(float attack, float decay, float sustain, float release);
    //int getEnvelope(int *array);
    
    void setType(string type);
    string getType();

    void setFrequency(double frequency);
    double getFrequency();

    void setAmplitude(double amplitude);
    double getAmplitude();
    
    void setWaveform(string waveform);
    string getWaveform();

    double getSample();
    void tick();

    protected:
        virtual void calculate();
        Oscillator *oscillator;
        string type;
        string waveform;
        double frequency;
        double amplitude;

};

#endif