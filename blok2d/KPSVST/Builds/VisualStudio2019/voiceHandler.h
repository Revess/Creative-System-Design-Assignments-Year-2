#pragma once
#include "./KPS.h"
using namespace std;

class VoiceHandler
{
public:
	VoiceHandler();
	~VoiceHandler();

	double readSample();
	void setNote(int midiNote);
	void releaseNote(int midiNote);
	void prepareToPlay(double samplerate, int samplesPerBlock, int numChannels, int filterCutoff);

	void updateFilterFreq(double frequency);
	void updateFilterRes(double res);
	void updateNoiseType(int noise);

	void updateActive();
	void updatePitch(float pitch, int string);

private:
	KPS kpsVoices[4];

	int numVoices = 4;
	double outputSample = 0;
	double sampleRate;
	int samplesPerBlok;
	int numChannels;
	int filterCutoff;
	double numActiveVoices = 1;
	bool eBusy = false;
	bool aBusy = false;
	bool dBusy = false;
	bool gBusy = false;
	float ePitch = 28;
	float aPitch = 33;
	float dPitch = 38;
	float gPitch = 43;
};

