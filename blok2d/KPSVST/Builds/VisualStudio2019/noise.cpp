#include "noise.h"
using namespace std;

Noise::Noise(noiseType noise_t){
	this->noise_t = noise_t;

	coefficientsptr = new dsp::IIR::Coefficients<double>;
	lpfptr = new struct dsp::IIR::Filter<double>::Filter(coefficientsptr->makeFirstOrderLowPass(44100, 100));
	lpfptr2 = new struct dsp::IIR::Filter<double>::Filter(coefficientsptr->makeFirstOrderLowPass(44100, 100));
	hpfptr = new struct dsp::IIR::Filter<double>::Filter(coefficientsptr->makeFirstOrderHighPass(44100, 100));
	hpfptr2 = new struct dsp::IIR::Filter<double>::Filter(coefficientsptr->makeFirstOrderHighPass(44100, 100));
	specptr = new dsp::ProcessSpec();

	specptr->sampleRate = 44100;
	specptr->maximumBlockSize = 256;
	specptr->numChannels = 1;

	lpfptr->reset();
	lpfptr->prepare(*specptr); //prepare for the samplerate
	hpfptr->reset();
	hpfptr->prepare(*specptr); //prepare for the samplerate
	lpfptr2->reset();
	lpfptr2->prepare(*specptr); //prepare for the samplerate
	hpfptr2->reset();
	hpfptr2->prepare(*specptr); //prepare for the samplerate

}

Noise::~Noise() {}

double Noise::getSample() {
	if (noise_t == white) {
		return generate();
	} else if (noise_t == pink) {
		return  lpfptr->processSample(generate());
	} else if (noise_t == gaussian) {
		return distribution(generator);
	} else if (noise_t == brown) {
		return lpfptr->processSample(lpfptr2->processSample(generate()));
	} else if (noise_t == blue) {
		return hpfptr->processSample(generate());
	} else if (noise_t == violet) {
		return hpfptr->processSample(hpfptr2->processSample(generate()));
	}
}

double Noise::generate() {
	double samlr = dist(generator);
	return samlr;
}

void Noise::setNoiseType(int noise) {
	if (noise == 0) {
		noise_t = white;
	} else if (noise == 1) {
		noise_t = pink;
		lpfptr->reset();
		lpfptr2->reset();
	} else if (noise == 2) {
		noise_t = brown;
		lpfptr->reset();
		lpfptr2->reset();
	} else if (noise == 3) {
		noise_t = gaussian;
	} else if (noise == 4) {
		noise_t = blue;
		hpfptr->reset();
		hpfptr2->reset();
	} else if (noise == 5) {
		noise_t = violet;
		hpfptr->reset();
		hpfptr2->reset();
	}
}