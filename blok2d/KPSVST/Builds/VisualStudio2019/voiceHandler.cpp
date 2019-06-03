#include "voiceHandler.h"

VoiceHandler::VoiceHandler() {
}

VoiceHandler::~VoiceHandler() {
}

double VoiceHandler::readSample() {
	outputSample = 0;
	for (int i = 0; i < numVoices; i++) {
		outputSample += kpsVoices[i].readSample() / numActiveVoices;
	}
	return outputSample;
}

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

void VoiceHandler::prepareToPlay(double samplerate, int samplesPerBlock, int numChannels, int filterCutoff){
	this->sampleRate = samplerate;
	this->samplesPerBlok = samplesPerBlock;
	this->numChannels = numChannels;
	this->filterCutoff = filterCutoff;

	for (int i = 0; i < numVoices; i++) {
		kpsVoices[i].prepareToPlay(sampleRate, samplesPerBlock, numChannels, this->filterCutoff+i*200);
	}
}

void VoiceHandler::updateFilterFreq(double frequency) {
	double offset = 0;
	for (int i = 0; i < numVoices; i++) {
		kpsVoices[i].updateFilterFreq(frequency + offset);
		offset + 100;
	}
}

void VoiceHandler::updateFilterRes(double res) {
	for (int i = 0; i < numVoices; i++) {
		kpsVoices[i].updateFilterRes(res);
	}
}

void VoiceHandler::updateActive() {
	numActiveVoices = 1.0;
	for (int i = 0; i < numVoices; i++) {
		if (kpsVoices[i].isActive()) {
			numActiveVoices += 1;
		}
	}
}

void VoiceHandler::updateNoiseType(int noise) {
	for (int i = 0; i < numVoices; i++) {
		kpsVoices[i].updateNoiseType(noise);
	}
}

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