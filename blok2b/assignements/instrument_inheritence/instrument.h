#include <string>
using namespace std;

class Instrument{
    public:
    //Constructor and deconstructor
        Instrument(string instrument,string sound);
        ~Instrument();
    //Set the instrument (different from default)
        void setInstrument(string instrument,string sound);
        string getInstrument();
    //Play the sound
        void play();

    private:
        string instrument;
        string sound;
};