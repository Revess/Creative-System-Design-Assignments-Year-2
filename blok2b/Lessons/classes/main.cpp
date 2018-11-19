#include <iostream>
using namespace std;

class Bicycle {
public:
    //method = class function
    Bicycle(int dir);
    void pedal();
    int direction;
};

Bicycle::Bicycle(int dir){
    cout<<"Bicycle constructor - creating a Bicycle object"<<endl;
    cout<<"direction: "<<dir<<endl;
    direction = dir;
}

void Bicycle::pedal(){
    cout<<"pedal pedal pedal"<< direction <<endl;
}

int main(){
    cout<<"Creating a bicycle."<<endl;
    Bicycle bicycle1(4);
    bicycle1.pedal();
    return 0;
}

