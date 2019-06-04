#include "delayLine.h"
using namespace std;

//==============================================================================
//Set the max positon of the header of the delayline, also fill the entire array with 0's for safety
DelayLine::DelayLine(int delayLength) {
	for (int i = 0; i < delayLength; i++) {
		delayLine[i] = 0;
	}
	this->delayLength = delayLength;
}

DelayLine::~DelayLine() {

}

//==============================================================================
//Return a sample from the delay to the caller
double DelayLine::readSample() {
	double sample = delayLine[readHeader];
	delayLine[readHeader] = 0;
	return sample;
}

//==============================================================================
//Add a sample to the delay from the caller
void DelayLine::writeSample(double sample) {
	delayLine[writeHeader] = sample;
	moveHeader();
}

//==============================================================================
//Move the header of the delayline
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

//==============================================================================
//Empty all samples in the delayline
void DelayLine::clear(int length) {
	delayLength = length;
	for (int i = 0; i < delayLength; i++) {
		delayLine[i] = 0;
	}
	readHeader = -1;
	moveHeader();
}