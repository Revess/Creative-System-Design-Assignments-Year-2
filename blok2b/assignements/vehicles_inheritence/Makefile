CXX=g++
SOURCE=main.o car.o vehicle.o boat.o plane.o

vehicles: $(SOURCE)
	$(CXX) -o $@ $(SOURCE)

,cpp.o:
	$(CXX) -c $(CXXFLAGS) $<

clean:
	/bin/rm -f vehicles *.o