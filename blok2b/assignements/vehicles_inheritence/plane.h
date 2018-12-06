#include "vehicle.h"
#include <string>

using namespace std;

class Plane : public Vehicle {
    public:
        Plane(string engine, string type);
        ~Plane();

        void setEngine(string engine);
        string getEngine();
        void setType(string type);
        string getType();

    private:
        string engine;
        string type;
};