#include <iostream>
#include "Dog.h"
using namespace std;

//Specify the constructor of the baseclass
Dog::Dog(string name) : Pet(name){
    cout<<"Dog - constructor"<<endl;
    cout<<"Dog name is: "<<name<<endl;
}

Dog::~Dog(){
    cout<<"Dog -destructor"<<endl;
}

void Dog::bark(){

}