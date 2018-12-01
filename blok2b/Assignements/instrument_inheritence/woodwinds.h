#include "instrument.h"
#include <string>
#include <array>
using namespace std;

class Woodwinds : public Instrument {
    public:
        array<string,5>types = {"clarinet","saxophone","piccolo","flute","fagot"};
        array<string,5>sounds = {"SquareSound","CarelessWhisper.mp3","Flulululuuu","FUUUU","BRWAAA"};
        Woodwinds();
        ~Woodwinds();
        void setType(string type);
        string getType();
};