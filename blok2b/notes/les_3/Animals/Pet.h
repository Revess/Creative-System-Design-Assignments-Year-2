#include <iostream>
#include <string>

class Pet {
    public:
    Pet(std::string name);
    ~Pet();

    void eat();
    void sleep();
    //With protected we can access the private variables from the subclass
    protected:
    std::string name;
};