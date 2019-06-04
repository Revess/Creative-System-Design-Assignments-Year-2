#pragma once
#include <math.h> 
using namespace std;

class AttackEnveloper
{
public:
	AttackEnveloper(double samplerate, double attackTime);
	~AttackEnveloper();
	
	double processSample(double sample);
	void reset();

private:
	double multiStack = 0.0; //The incrementel stepchange of the multiplier, the slope of the graph
	double multiplier = 1.0;
};

