#include "vehicle.h"
#include <string>

using namespace std;

class Boat : public Vehicle {
    public:
        Boat(string type, string name);
        ~Boat();

        void setType(string type);
        string getType();
        void setName(string name);
        string getName();

    private:
        string type;
        string boatName;
};