#pragma once
#include <vector>
#include "./noise.h"
#include "./delayLine.h"
#include "attackEnveloper.h"
#include "../JuceLibraryCode/JuceHeader.h"
using namespace std;

class KPS
{
public:
	KPS();
	~KPS();

	double readSample();
	void calculate();
	void setNote(float midiNote);
	void prepareToPlay(double samplerate, int samplesPerBlock, int numChannels, int filterCutoff);
	void updateFilterFreq(double frequency);
	void updateFilterRes(double res);
	void updateNoiseType(int noise);
	
	bool isActive();

private:
	Noise* noiseptr;
	DelayLine* delayptr;
	AttackEnveloper* attackptr;
	dsp::IIR::Coefficients<double>* coefficientsptr;
	struct dsp::IIR::Filter<double>* filterptr;
	dsp::ProcessSpec* specptr;

	bool prepared = false;
	double sampleRate = 44100;
	double filterCutoff = 500;
	double resonance = 0.5;
	int noteLength = 5;
	int samplesPerBlok = 128;
	int numChannels = 1;

	double outputSample = 0.0;
};

