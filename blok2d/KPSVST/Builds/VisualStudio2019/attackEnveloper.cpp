#include "attackEnveloper.h"
using namespace std;

//Set the envelope curve (lineair factor) and reset the multiplier to zero
AttackEnveloper::AttackEnveloper(double samplerate, double attackTime) {
	multiStack = multiplier / round(((samplerate / 1000.0) * attackTime));
	multiplier = 0.0;
}

AttackEnveloper::~AttackEnveloper() {

}

//Process and return a sample to the caller
double AttackEnveloper::processSample(double sample) {
	if (multiplier < 1.0) {
		multiplier += multiStack;
	}
	else {
		multiplier = 1.0;
	}
	return sample * multiplier;
}

//Reset the Enveloper
void AttackEnveloper::reset() {
	multiplier = 0.0;
}