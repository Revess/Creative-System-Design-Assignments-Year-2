#include "KPS.h"
using namespace std;

KPS::KPS() {
}

//==============================================================================
//Cleanup
KPS::~KPS() {
	delete noiseptr;
	delete delayptr;
	delete filterptr;
	delete specptr;
	delete attackptr;
}

//==============================================================================
//Return a generated sample to the caller
double KPS::readSample() {
	calculate();
	return outputSample;
}

//==============================================================================
//Push a sample through the attack enveloper, then filter the sample, then write a sample to the delayline, then get a sample from the delayline
void KPS::calculate() {
	outputSample = attackptr->processSample(outputSample);
	outputSample = filterptr->processSample(outputSample) * 0.99; //Feedback multiplication to ensure feedback protection
	delayptr->writeSample(outputSample);
	outputSample = delayptr->readSample();
}

//==============================================================================
//Change the pitch of the note to be returned.
void KPS::setNote(float midiNote) {
	//Notelength calculation
	noteLength = round((1000.0 / (440 * pow(2.0, (midiNote - 69.0) / 12.0))) * (sampleRate / 1000.0)); //convert midi note to sample size
	
	//Change the header of the delay pointer
	delayptr->clear(noteLength);

	//Prepare the delay by filling it up with samples so no delay in the playback
	for (int i = 0; i < noteLength; i++) {
		outputSample = noiseptr->getSample();
		readSample();
	}

	//Reset the filter and the attackenveloper
	filterptr->reset();
	attackptr->reset();
}

//==============================================================================
//Basically a second constructor that is called to prepare the syntheziser for playback, any time the samplerate changes etc.
void KPS::prepareToPlay(double samplerate, int samplesPerBlock, int numChannels, int filterCutoff) {
	this->sampleRate = samplerate;
	this->samplesPerBlok = samplesPerBlock;
	this->numChannels = numChannels;

	if (!prepared) {
		this->filterCutoff = filterCutoff;

		attackptr = new AttackEnveloper(this->sampleRate, 5);
		noiseptr = new Noise(white);
		delayptr = new DelayLine(noteLength);
		coefficientsptr = new dsp::IIR::Coefficients<double>;
		filterptr = new struct dsp::IIR::Filter<double>::Filter(coefficientsptr->makeLowPass(this->sampleRate, filterCutoff, resonance));
		specptr = new dsp::ProcessSpec();

		prepared = true;
	}

	specptr->sampleRate = 44100;
	specptr->maximumBlockSize = samplesPerBlock;
	specptr->numChannels = numChannels;
	filterptr->reset();
	filterptr->prepare(*specptr);
}

//==============================================================================
//Change the filter cutoff frequency
void KPS::updateFilterFreq(double frequency) {
	filterCutoff = frequency;
	filterptr->coefficients = coefficientsptr->makeLowPass(this->sampleRate, filterCutoff, resonance);
}

//==============================================================================
//Change the Q factor of the filter
void KPS::updateFilterRes(double res) {
	resonance = res;
	filterptr->coefficients = coefficientsptr->makeLowPass(this->sampleRate, filterCutoff, resonance);
}

//==============================================================================
//Return if the string is still active
bool KPS::isActive() {
	if (outputSample < 0.001) {
		return false;
	}
	else {
		return true;
	}
}

//==============================================================================
//Change the type of noise
void KPS::updateNoiseType(int noise) {
	noiseptr->setNoiseType(noise);
}