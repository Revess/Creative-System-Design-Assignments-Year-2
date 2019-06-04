#include "voiceHandler.h"

VoiceHandler::VoiceHandler() {
}

VoiceHandler::~VoiceHandler() {
}

//==============================================================================
//Send the sample to the caller and apply the right calculation to the sample to be given
double VoiceHandler::readSample() {
	outputSample = 0;
	for (int i = 0; i < numVoices; i++) {
		outputSample += kpsVoices[i].readSample() / numActiveVoices;
	}
	return outputSample;
}

//==============================================================================
//Change the note of the corresponding string
void VoiceHandler::setNote(int midiNote) {
	if (midiNote >= ePitch && midiNote < ePitch + 12) {
		kpsVoices[0].setNote(midiNote + (ePitch-(int)ePitch));
	} else if (midiNote >= aPitch && midiNote < aPitch + 12) {
		kpsVoices[1].setNote(midiNote + (aPitch - (int)aPitch));
	} else if (midiNote >= dPitch && midiNote < dPitch + 12) {
		kpsVoices[2].setNote(midiNote + (dPitch - (int)dPitch));
	} else if (midiNote >= gPitch && midiNote <= gPitch + 12) {
		kpsVoices[3].setNote(midiNote + (gPitch - (int)gPitch));
	}
	updateActive();
}

//==============================================================================
//If the note has been released send an message to notice that the string is lose
//TODO: Implement this
void VoiceHandler::releaseNote(int midiNote) {
	if (midiNote >= ePitch && midiNote < ePitch+12) {
		eBusy = false;
	}
	else if (midiNote >= aPitch && midiNote < aPitch+12){
		aBusy = false;
	}
	else if (midiNote >= dPitch && midiNote < dPitch+12){
		dBusy = false;
	}
	else if (midiNote >= gPitch && midiNote <= gPitch+12) {
		gBusy = false;
	}
}

//==============================================================================
//Basically a second constructor that is called to prepare the syntheziser for playback, any time the samplerate changes etc.
void VoiceHandler::prepareToPlay(double samplerate, int samplesPerBlock, int numChannels, int filterCutoff){
	this->sampleRate = samplerate;
	this->samplesPerBlok = samplesPerBlock;
	this->numChannels = numChannels;
	this->filterCutoff = filterCutoff;

	for (int i = 0; i < numVoices; i++) {
		kpsVoices[i].prepareToPlay(sampleRate, samplesPerBlock, numChannels, this->filterCutoff+i*200);
	}
}

//==============================================================================
//Change the filter cutoff frequency for each seperate string
void VoiceHandler::updateFilterFreq(double frequency) {
	double offset = 0;
	for (int i = 0; i < numVoices; i++) {
		kpsVoices[i].updateFilterFreq(frequency + offset);
		offset + 100;
	}
}

//==============================================================================
//Change the Q factor of the filter for each sperate string
void VoiceHandler::updateFilterRes(double res) {
	for (int i = 0; i < numVoices; i++) {
		kpsVoices[i].updateFilterRes(res);
	}
}

//==============================================================================
//Update the number of active voices at one time, this to normalize the audio of the output
void VoiceHandler::updateActive() {
	numActiveVoices = 1.0;
	for (int i = 0; i < numVoices; i++) {
		if (kpsVoices[i].isActive()) {
			numActiveVoices += 1;
		}
	}
}

//==============================================================================
//Change the type of noise for each string
void VoiceHandler::updateNoiseType(int noise) {
	for (int i = 0; i < numVoices; i++) {
		kpsVoices[i].updateNoiseType(noise);
	}
}

//==============================================================================
//Change the pitchoffset for each string
void VoiceHandler::updatePitch(float pitch, int string) {
	if (string == 0) {
		ePitch = pitch;
	}
	else if (string == 1) {
		aPitch = pitch;
	}
	else if (string == 2) {
		dPitch = pitch;
	}
	else if (string == 3) {
		gPitch = pitch;
	}
}