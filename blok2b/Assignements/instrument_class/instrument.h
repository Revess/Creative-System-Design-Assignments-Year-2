#include <string>
using namespace std;

class Instrument{
    public:
    Instrument(string newSound);
    void makeSound();
    string sound = "";
};