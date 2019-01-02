#include <vector>
#include <string>
using namespace std;

class Melody{
    public:
        Melody(vector<vector<string> > &notes);
        ~Melody();

        string getNote(vector<vector<string> > &notes);

    private:
        string newNote;
        string prevNote;
        double frequency;
        double startTimestamp;
        double currentTimestamp;
};