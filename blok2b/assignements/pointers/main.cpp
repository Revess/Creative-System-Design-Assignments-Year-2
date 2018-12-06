#include <iostream>
using namespace std;

int main()
{
char letter = 97;
char *letterpointer = &letter;
  std::cout << "Contents of the variable letter: "<<letter<<endl;
  std::cout << "Contents of letterpointer: "<<hex<<(unsigned long)letterpointer<<endl;
  std::cout << "Contents of what letterpointer points to: "<<*letterpointer<<endl;
  *letterpointer = 'b';
  std::cout << "The variabele letter has gotten a new value through letterpointer."<<endl;
  std::cout << "Contents of what letterpointer points to: "<<*letterpointer<<endl;
  std::cout << "Contents of the variable letter: "<<letter<<endl;

  /*
   * Create the necessary pointer(s) and use them
   */

  unsigned short year = 2018;
  unsigned short *yearpointer = &year;
  std::cout << "Contents of the variabele year: "<<dec<<year<<endl;
  std::cout << "Contents of yearpointer: "<<hex<<yearpointer<<endl;
  std::cout << "Contents of what yearpointer points to: "<<dec<<*yearpointer<<endl;
  *yearpointer = 2020;
  std::cout << "Contents of the variabele year: "<<year<<endl;
  unsigned short *anotheryearpointer = &year;
  std::cout << "Contents of anotheryearpointer: "<<hex<<anotheryearpointer<<endl;
  std::cout << "Contents of what anotheryearpointer points to: "<<dec<<*anotheryearpointer<<endl;
  *anotheryearpointer = 2005;
  std::cout << "Contents of year: "<<year<<endl;
  std::cout << "Contents of what anotheryearpointer points to: "<<*anotheryearpointer<<endl;
}

