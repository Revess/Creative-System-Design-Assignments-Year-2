#include <string>
using namespace std;

class Instrument{
    public:
    Instrument(string newSound);
    ~Instrument();
    void makeSound();
    string sound = "";
};