CXX=g++
SOURCE=Pet.o Dog.o main.o

animals: $(SOURCE)
	$(CXX) -o $@ $(SOURCE)

,cpp.o:
	$(CXX) -c $(CXXFLAGS) $<

clean:
	/bin/rm -f animals *.o