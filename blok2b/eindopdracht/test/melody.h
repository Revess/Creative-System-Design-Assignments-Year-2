using namespace std;

class Melody{
    public:
        Melody(int (&notes)[4][3]);
        ~Melody();

        int getNote(int (&notes)[4][3]);

    private:
        int choises;
        int newNote;
        int prevNote;
        double frequency;
        double startTimestamp;
        double currentTimestamp;
};