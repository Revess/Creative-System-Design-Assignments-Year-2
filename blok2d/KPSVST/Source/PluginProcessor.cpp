#include "PluginProcessor.h"
#include "PluginEditor.h"
#include <iostream>

//==============================================================================
KpsvstAudioProcessor::KpsvstAudioProcessor()
#ifndef JucePlugin_PreferredChannelConfigurations
     : AudioProcessor (BusesProperties()
                     #if ! JucePlugin_IsMidiEffect
                      #if ! JucePlugin_IsSynth
                       .withInput  ("Input",  AudioChannelSet::mono(), false)
                      #endif
                       .withOutput ("Output", AudioChannelSet::stereo(), true)
                     #endif
                       )
#endif
{
}

KpsvstAudioProcessor::~KpsvstAudioProcessor()
{
}

//==============================================================================
//Basic JUCE Settings, edit from the Projucer
const String KpsvstAudioProcessor::getName() const
{
    return JucePlugin_Name;
}

bool KpsvstAudioProcessor::acceptsMidi() const
{
   #if JucePlugin_WantsMidiInput
    return true;
   #else
    return false;
   #endif
}

bool KpsvstAudioProcessor::producesMidi() const
{
   #if JucePlugin_ProducesMidiOutput
    return true;
   #else
    return false;
   #endif
}

bool KpsvstAudioProcessor::isMidiEffect() const
{
   #if JucePlugin_IsMidiEffect
    return true;
   #else
    return false;
   #endif
}

double KpsvstAudioProcessor::getTailLengthSeconds() const
{
    return 0.0;
}

int KpsvstAudioProcessor::getNumPrograms()
{
    return 1;   // NB: some hosts don't cope very well if you tell them there are 0 programs,
                // so this should be at least 1, even if you're not really implementing programs.
}

int KpsvstAudioProcessor::getCurrentProgram()
{
    return 0;
}

void KpsvstAudioProcessor::setCurrentProgram (int index)
{
}

const String KpsvstAudioProcessor::getProgramName (int index)
{
    return {};
}

void KpsvstAudioProcessor::changeProgramName (int index, const String& newName)
{
}

//==============================================================================
void KpsvstAudioProcessor::prepareToPlay (double sampleRate, int samplesPerBlock)
{
	voiceHandler.prepareToPlay(sampleRate, samplesPerBlock, getNumOutputChannels(), 500); //Do this in Prepare to Play to make sure the class goes onto the stack
}

void KpsvstAudioProcessor::releaseResources()
{
    // When playback stops, you can use this as an opportunity to free up any
    // spare memory, etc.
}

#ifndef JucePlugin_PreferredChannelConfigurations
bool KpsvstAudioProcessor::isBusesLayoutSupported (const BusesLayout& layouts) const
{
  #if JucePlugin_IsMidiEffect
    ignoreUnused (layouts);
    return true;
  #else
    // This is the place where you check if the layout is supported.
    // In this template code we only support mono or stereo.
    if (layouts.getMainOutputChannelSet() != AudioChannelSet::mono()
     && layouts.getMainOutputChannelSet() != AudioChannelSet::stereo())
        return false;

    // This checks if the input layout matches the output layout
   #if ! JucePlugin_IsSynth
    if (layouts.getMainOutputChannelSet() != layouts.getMainInputChannelSet())
        return false;
   #endif

    return true;
  #endif
}
#endif

//==============================================================================
//The calculations, the processBlock
void KpsvstAudioProcessor::processBlock (AudioBuffer<float>& buffer, MidiBuffer& midiMessages)
{
    ScopedNoDenormals noDenormals;
    auto totalNumInputChannels  = getTotalNumInputChannels();
    auto totalNumOutputChannels = getTotalNumOutputChannels();

	for (auto i = totalNumInputChannels; i < totalNumOutputChannels; ++i) {
		buffer.clear(i, 0, buffer.getNumSamples());
	}

	//Handle midi messages
	int time;
	MidiMessage m;
	for (MidiBuffer::Iterator i(midiMessages); i.getNextEvent(m, time);)
	{
		if (m.isNoteOn()){
			voiceHandler.setNote(m.getNoteNumber());
		}
		else if (m.isNoteOff()){
			voiceHandler.releaseNote(m.getNoteNumber());
		}
	}

	//Get pointers for left and right channel data
	auto* channelData = buffer.getWritePointer (0);
	auto* channel2Data = buffer.getWritePointer(1);

	//Fill the audio buffer with samples from the KPS classes, and multiply the volumeOffset
	for (int sample = 0; sample < buffer.getNumSamples(); ++sample) {
		double outputSample = voiceHandler.readSample() * volumeOffset;
		channelData[sample] = outputSample;
		channel2Data[sample] = outputSample;
	}
}

//==============================================================================
bool KpsvstAudioProcessor::hasEditor() const
{
    return true;
}

AudioProcessorEditor* KpsvstAudioProcessor::createEditor()
{
    return new KpsvstAudioProcessorEditor (*this);
}

//==============================================================================
void KpsvstAudioProcessor::getStateInformation (MemoryBlock& destData)
{
    // You should use this method to store your parameters in the memory block.
    // You could do that either as raw data, or use the XML or ValueTree classes
    // as intermediaries to make it easy to save and load complex data.
}

void KpsvstAudioProcessor::setStateInformation (const void* data, int sizeInBytes)
{
    // You should use this method to restore your parameters from this memory block,
    // whose contents will have been created by the getStateInformation() call.
}

//==============================================================================
// This creates new instances of the plugin..
AudioProcessor* JUCE_CALLTYPE createPluginFilter()
{
    return new KpsvstAudioProcessor();
}

//==============================================================================
//CUSTOM FUNCTIONS
//Change the notevalue of the guitar string
void KpsvstAudioProcessor::setNote(MidiMessage& midiMessage) {
	if (midiMessage.isNoteOn())
	{
		voiceHandler.setNote(midiMessage.getNoteNumber());
	} else if (midiMessage.isNoteOff())
	{
		voiceHandler.releaseNote(midiMessage.getNoteNumber());
	}
}

//Change the cutoff frequency of the filter
void KpsvstAudioProcessor::updateFilterFreq(double frequency) {
	voiceHandler.updateFilterFreq(frequency);
}

//Change the Q factor of the Filter
void KpsvstAudioProcessor::updateFilterRes(double res) {
	voiceHandler.updateFilterRes(res);
}

//Change the type of Noise
void KpsvstAudioProcessor::updateNoiseType(int noise) {
	voiceHandler.updateNoiseType(noise);
}

//Change the pitchoffset of the string
void KpsvstAudioProcessor::updatePitch(float pitch, int string) {
	voiceHandler.updatePitch(pitch, string);
}