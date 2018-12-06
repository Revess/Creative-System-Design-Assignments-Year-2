#include <iostream>
#include <string>
#include "vehicle.h"
using namespace std;

Vehicle::Vehicle(int maxSpeed, int amount, string colour){
    this->maxSpeed = maxSpeed;
    this->numberOfSeats = amount;
    this->colour = colour;
    cout<<"Vehicle constructed with; "<<this->numberOfSeats<<" seats, "<<this->colour<<" colour and with a max speed of "<<this->maxSpeed<<"Km/h"<<endl;
}

Vehicle::~Vehicle(){
    cout<<"Vehicle deconstructed!"<<endl;
}

void Vehicle::setSpeed(int speed){
    this->maxSpeed = speed;
}

int Vehicle::getSpeed(){
    return maxSpeed;
}

void Vehicle::setSeats(int amount){
    this->numberOfSeats = amount;
}

int Vehicle::getSeats(){
    return numberOfSeats;
}

void Vehicle::setColour(string colour){
    this->colour = colour;
}

string Vehicle::getColour(){
    return colour;
}