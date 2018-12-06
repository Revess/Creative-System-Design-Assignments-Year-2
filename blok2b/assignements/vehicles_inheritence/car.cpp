#include "car.h"
#include <iostream>
#include <string>

using namespace std;

Car::Car(string tires, string gear) : Vehicle(200,4,"red"){
    this->tires=tires;
    this->gear=gear;
    cout<<"Construct a car with tires: "<<this->tires<<" and gear type: "<<this->gear<<endl;
}

Car::~Car(){
    cout<<"Deconstructed Car"<<endl;
}

void Car::setTires(string tires){
    this->tires=tires;
}

string Car::getTires(){
    return tires;
}

void Car::setGear(string gear){
    this->gear=gear;
}

string Car::getGear(){
    return gear;
}