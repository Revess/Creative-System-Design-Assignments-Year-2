#include "boat.h"
#include <iostream>
#include <string>

using namespace std;

Boat::Boat(string type, string name) : Vehicle(130,8,"white/red"){
    this->type=type;
    this->boatName=name;
    cout<<"Construct a boat type: "<<this->type<<" and name: "<<this->boatName<<endl;
}

Boat::~Boat(){
    cout<<"Deconstructed Boat"<<endl;
}

void Boat::setType(string type){
    this->type=type;
}

string Boat::getType(){
    return type;
}

void Boat::setName(string name){
    this->boatName=name;
}

string Boat::getName(){
    return boatName;
}