CXX = g++
CXXFLAGS = -Ic:/Program\ Files\ \(x86\)/Jack/includes -Wall -std=c++1z
LDFLAGS= -Lc:/Program\ Files\ \(x86\)/Jack/lib -llibjack
SOURCE= main.o jack_module.o sine.o oscillator.o saw.o square.o triangle.o

example: $(SOURCE)
	$(CXX) -o $@ $(CXXFLAGS) $(SOURCE) $(LDFLAGS)

.cpp.o:
	$(CXX) -c $(CXXFLAGS) $<

clean:
	rm -f example *.o