#ifndef _VEHICLE_H_
#define _VEHICLE_H_
#include <string>
using namespace std;

class Vehicle {
    public:
        Vehicle(int maxSpeed, int amount, string colour);
        ~Vehicle();

        void setSpeed(int speed);
        int getSpeed();
        void setSeats(int numberOfSeats);
        int getSeats();
        void setColour(string colour);
        string getColour();
    
    protected:
        int maxSpeed;
        int numberOfSeats;
        string colour;
};

#endif