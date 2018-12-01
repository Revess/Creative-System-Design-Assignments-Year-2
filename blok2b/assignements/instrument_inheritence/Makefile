CXX=g++
SOURCE=instrument.o main.o percussion.o strings.o brass.o woodwinds.o

instrument_maker: $(SOURCE)
	$(CXX) -o $@ $(SOURCE)

,cpp.o:
	$(CXX) -c $(CXXFLAGS) $<

clean:
	/bin/rm -f instrument_maker *.o