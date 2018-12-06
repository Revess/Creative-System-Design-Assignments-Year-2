#include "plane.h"
#include <iostream>
#include <string>

using namespace std;

Plane::Plane(string engine, string type) : Vehicle(400,400,"White/Blue"){
    this->engine=engine;
    this->type=type;
    cout<<"Construct a plane type: "<<this->type<<" and engine type: "<<this->engine<<endl;
}

Plane::~Plane(){
    cout<<"Deconstructed Plane"<<endl;
}

void Plane::setEngine(string wings){
    this->engine=engine;   
}

string Plane::getEngine(){
    return engine;
}

void Plane::setType(string type){
    this->type=type;
}

string Plane::getType(){
    return type;
}