#include <vector>
#include <string>
#include <array>
using namespace std;

//See .cpp file for the explenation

class Melody{
    public:
        Melody(vector<vector<string> > &notes, vector<double> &rhythm, int bpm);
        ~Melody();

        double getNote(vector<vector<string> > &notes);
        double getRhythm(vector<double> &rhythm);

    private:
        //TODO: Add sharps and flats, only white keys rn
        int midiNotes[7][2]={{97,9},{98,11},{99,0},{100,2},{101,4},{102,5},{103,7}};
        int bpm;
        string newNote;
        string prevNote;
        double newRhythm;
        double prevRhythm;
        int position;
        double frequency;
};