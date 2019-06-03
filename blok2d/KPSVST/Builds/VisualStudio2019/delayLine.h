#pragma once
#include <vector>
using namespace std;

class DelayLine
{
public:
	DelayLine(int delayLength);
	~DelayLine();

	double readSample();
	void writeSample(double sample);
	void clear(int length);

private:
	vector<double> circularBuffer;
	double delayLine[9800];
	int readHeader = 1;
	int writeHeader = 0;
	int delayLength = 1;

	void moveHeader();
};

