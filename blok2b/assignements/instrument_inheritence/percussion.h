#include "instrument.h"
#include <string>
#include <array>
using namespace std;

class Percussion8 {
    public:
        array<string,5>types = {"drums","timbale","marimba","conga","bongo"};
        array<string,5>sounds = {"Ba Dum Tss","Dum","Plom","Tuk","Tak"};
        Percussion();
        ~Percussion();
        void setType(string type);
        string getType();
    private:
        string type;
        string sound;
        Instrument percussion(string type, string sound);
};