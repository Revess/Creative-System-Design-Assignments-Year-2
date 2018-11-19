CXX=g++
CXXFLAGS=Wall -std=c++14 
SOURCE=instrument.o main.o

instrument_maker: $(SOURCE)
	$(CXX) -o $@ $(SOURCE)

,cpp.o:
	$(CXX) -c $(CXXFLAGS) $<

clean:
	/bin/rm -f instrument_maker *.o