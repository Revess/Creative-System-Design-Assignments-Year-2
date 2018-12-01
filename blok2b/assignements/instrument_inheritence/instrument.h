#ifndef _INSTRUMENT_H_
#define _INSTRUMENT_H_
#include <string>
#include <array>
using namespace std;

class Instrument{
    public:
    //Constructor and deconstructor
        Instrument(string instrument,string sound,string type);
        ~Instrument();
    //Set the instrument (different from default)
        void setInstrument(string instrument,string sound);
        string getInstrument();
    //Set pitchrange
        void setPitchRange(int pitchMin, int pitchMax);
        string getPitchRange();
    //Play the sound
        void play();

    protected:
        string instrument;
        string sound;
        string type;
        array<int,2>pitchRange = {};
};

#endif