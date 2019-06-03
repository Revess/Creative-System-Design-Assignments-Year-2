#include "attackEnveloper.h"
using namespace std;

AttackEnveloper::AttackEnveloper(double samplerate, double attackTime) {
	multiStack = multiplier / round(((samplerate / 1000.0) * attackTime));
	multiplier = 0.0;
}

AttackEnveloper::~AttackEnveloper() {

}

double AttackEnveloper::processSample(double sample) {
	if (multiplier < 1.0) {
		multiplier += multiStack;
	}
	else {
		multiplier = 1.0;
	}
	return sample * multiplier;
}

void AttackEnveloper::reset() {
	multiplier = 0.0;
}