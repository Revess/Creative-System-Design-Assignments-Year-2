#ifndef _FMSYNTH_H_
#define _FMSYNTH_H_
#include "synth.h"
using namespace std;

class FmSynth : public Synth {
    public:
        FmSynth(double samplerate, double frequency, string waveform1, string waveform2, double modamount, double ratio);
        ~FmSynth();

        void setFrequency(double frequency);

        double getSample();

        void tick();

    private:
        double modamount;
        double ratio;
};

#endif