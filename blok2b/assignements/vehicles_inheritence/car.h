#include "vehicle.h"
#include <string>

using namespace std;

class Car : public Vehicle {
    public:
        Car(string tires, string gear);
        ~Car();

        void setTires(string tires);
        string getTires();
        void setGear(string gear);
        string getGear();

    private:
        string tires;
        string gear;
};