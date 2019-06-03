#include "KPS.h"
using namespace std;

KPS::KPS() {
}

KPS::~KPS() {
	delete noiseptr;
	delete delayptr;
	delete filterptr;
	delete specptr;
	delete attackptr;
}

double KPS::readSample() {
	calculate();
	return outputSample;
}

void KPS::calculate() {
	outputSample = attackptr->processSample(outputSample);
	outputSample = filterptr->processSample(outputSample) * 0.99; //Feedback multiplication to ensure no floating numbers
	delayptr->writeSample(outputSample);
	outputSample = delayptr->readSample();
}

void KPS::setNote(float midiNote) {
	noteLength = round((1000.0 / (440 * pow(2.0, (midiNote - 69.0) / 12.0))) * (sampleRate / 1000.0)); //convert midi note to sample size

	delayptr->clear(noteLength);

	for (int i = 0; i < noteLength; i++) {
		outputSample = noiseptr->getSample();
		readSample();
	}
	filterptr->reset();
	attackptr->reset();
}

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

void KPS::updateFilterFreq(double frequency) {
	filterCutoff = frequency;
	filterptr->coefficients = coefficientsptr->makeLowPass(this->sampleRate, filterCutoff, resonance);
}

void KPS::updateFilterRes(double res) {
	resonance = res;
	filterptr->coefficients = coefficientsptr->makeLowPass(this->sampleRate, filterCutoff, resonance);
}

bool KPS::isActive() {
	if (outputSample < 0.001) {
		return false;
	}
	else {
		return true;
	}
}

void KPS::updateNoiseType(int noise) {
	noiseptr->setNoiseType(noise);
}