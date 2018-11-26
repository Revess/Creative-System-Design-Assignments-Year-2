#include "Pet.h"

//The public is the inheritence of Pet. This means Dog copies parts of the baseclass Pet
class Dog : public Pet {
    public:
        Dog(std::string name);
        ~Dog();

        void bark();
};