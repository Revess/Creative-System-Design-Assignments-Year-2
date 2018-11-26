#include <iostream>
#include "Pet.h"
using namespace std;

Pet::Pet(string name){
    this->name=name;
    cout<<"Pet - constructor"<<endl;
    cout<<"Name of the pet is: "<<name<<endl;
}

Pet::~Pet(){
    cout<<"Pet - destructor"<<endl;
}

void Pet::eat(){
    cout<<"Pet - pet is eating"<<endl;
}

void Pet::sleep(){
    cout<<"Pet - pet is sleeping"<<endl;
}