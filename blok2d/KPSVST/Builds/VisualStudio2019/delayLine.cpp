#include "delayLine.h"
using namespace std;

DelayLine::DelayLine(int delayLength) {
	for (int i = 0; i < delayLength; i++) {
		delayLine[i] = 0;
	}
	this->delayLength = delayLength;
}

DelayLine::~DelayLine() {

}

double DelayLine::readSample() {
	double sample = delayLine[readHeader];
	delayLine[readHeader] = 0;
	return sample;
}

void DelayLine::writeSample(double sample) {
	delayLine[writeHeader] = sample;
	moveHeader();
}

void DelayLine::moveHeader() {
	readHeader++;
	readHeader = readHeader % delayLength;
	if (readHeader != 0) {
		writeHeader = readHeader - 1;
	}
	else {
		writeHeader = delayLength - 1;
	}
}

void DelayLine::clear(int length) {
	delayLength = length;
	for (int i = 0; i < delayLength; i++) {
		delayLine[i] = 0;
	}
	readHeader = -1;
	moveHeader();
}