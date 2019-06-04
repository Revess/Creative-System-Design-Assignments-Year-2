#pragma once
#include <random>
#include <iterator>
#include "../JuceLibraryCode/JuceHeader.h"

using namespace std;

//The different type of noise choises
enum noiseType { gaussian, white, pink, brown, blue, violet };

class Noise
{
public:
	Noise(noiseType noise_t);
	~Noise();

	double getSample();
	double generate();
	void setNoiseType(int noise);

private:
	//=====================================================================
	//Random functions
	noiseType noise_t = white;
	//Generator
	default_random_engine generator;
	//The Gaussian distribution
	normal_distribution<double> distribution{ 0.0, 0.3 };
	//The other noise types
	uniform_real_distribution<double> dist{ -1.0, 1.0 };
	
	//=====================================================================
	//Filters
	dsp::IIR::Coefficients<double>* coefficientsptr;
	struct dsp::IIR::Filter<double>* lpfptr;
	struct dsp::IIR::Filter<double>* hpfptr;
	struct dsp::IIR::Filter<double>* lpfptr2;
	struct dsp::IIR::Filter<double>* hpfptr2;
	dsp::ProcessSpec* specptr;
};

