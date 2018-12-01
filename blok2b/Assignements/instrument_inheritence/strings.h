#include "instrument.h"
#include <string>
#include <array>
using namespace std;

class Strings : public Instrument {
    public:
        array<string,4>types = {"violin","viola","cello","contrbass"};
        array<string,4>sounds = {"Hnggg","Hunnggg","Hmmmm","Bwaaaa"};
        Strings();
        ~Strings();
        void setType(string type);
        string getType();
};