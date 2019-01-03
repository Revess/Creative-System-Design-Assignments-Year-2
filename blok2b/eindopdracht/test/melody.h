#include <vector>
#include <string>
#include <array>
using namespace std;

class Melody{
    public:
        Melody(vector<vector<string> > &notes);
        ~Melody();

        double getNote(vector<vector<string> > &notes);

    private:
        //TODO: Add sharps and flats, only white keys rn
        int midiNotes[7][2]={{97,9},{98,11},{99,0},{100,2},{101,4},{102,5},{103,7}};
        string newNote;
        string prevNote;
        double frequency;
};