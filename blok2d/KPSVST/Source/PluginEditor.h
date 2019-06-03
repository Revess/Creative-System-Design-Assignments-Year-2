/*
  ==============================================================================

    This file was auto-generated!

    It contains the basic framework code for a JUCE plugin editor.

  ==============================================================================
*/

#pragma once

#include "../JuceLibraryCode/JuceHeader.h"
#include "PluginProcessor.h"

//==============================================================================
/**
*/
class KpsvstAudioProcessorEditor : 
	public AudioProcessorEditor,
	private MidiInputCallback,
	private MidiKeyboardStateListener,
	public Slider::Listener,
	public ComboBox::Listener
{
public:
    KpsvstAudioProcessorEditor (KpsvstAudioProcessor&);
    ~KpsvstAudioProcessorEditor();

    //==============================================================================
    void paint (Graphics&) override;
    void resized() override;
	void sliderValueChanged (Slider* slider) override;
	void comboBoxChanged(ComboBox* comboBox) override;

	//==============================================================================
	MidiKeyboardState kSliderState;
	MidiKeyboardComponent kSlider;

private:
    // This reference is provided as a quick way for your editor to
    // access the processor object that created it.
    KpsvstAudioProcessor& processor;
	Rectangle<int> windowSize = Desktop::getInstance().getDisplays().getMainDisplay().userArea;
	Slider pitchDialE;
	Slider pitchDialA;
	Slider pitchDialD;
	Slider pitchDialG;
	Slider gainDial;
	Slider freqDial;
	Slider resDial;
	Label freqLabel;
	Label resLabel;
	Label gainLabel;
	Label eLabel;
	Label aLabel;
	Label dLabel;
	Label gLabel;
	Label controlText;
	ComboBox noise;

	const int numNoiseTypes = 4;
	string noiseTypes[4] = {"white","pink","brown","gaussian"};
	bool isAddingFromMidiInput = false;

	void handleIncomingMidiMessage(MidiInput* source, const MidiMessage& message) override;
	void handleNoteOn(MidiKeyboardState*, int midiChannel, int midiNoteNumber, float velocity) override;
	void handleNoteOff(MidiKeyboardState*, int midiChannel, int midiNoteNumber, float /*velocity*/) override;

    JUCE_DECLARE_NON_COPYABLE_WITH_LEAK_DETECTOR (KpsvstAudioProcessorEditor)
};
