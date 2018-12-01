#include "instrument.h"
#include <string>
#include <array>
using namespace std;

class Brass : public Instrument {
    public:
        array<string,4>types = {"trumpet","french horn","trombone","tuba"};
        array<string,4>sounds = {"Bwaap","BWuuuu","Preeeepp","PLPLPRPLPLRRRLRL"};
        Brass();
        ~Brass();
        void setType(string type);
        string getType();
};