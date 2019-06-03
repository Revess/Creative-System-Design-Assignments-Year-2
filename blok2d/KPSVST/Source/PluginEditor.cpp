/*
  ==============================================================================

    This file was auto-generated!

    It contains the basic framework code for a JUCE plugin editor.

  ==============================================================================
*/

#include "PluginProcessor.h"
#include "PluginEditor.h"

//==============================================================================
KpsvstAudioProcessorEditor::KpsvstAudioProcessorEditor(KpsvstAudioProcessor& p)
	: AudioProcessorEditor(&p), processor(p),
	kSlider(kSliderState, MidiKeyboardComponent::horizontalKeyboard)
{
    // Make sure that before the constructor has finished, you've set the
    // editor's size to whatever you need it to be.
    setSize (584, 380);
	addAndMakeVisible(kSlider);

	addAndMakeVisible(pitchDialA);
	addAndMakeVisible(pitchDialE);
	addAndMakeVisible(pitchDialD);
	addAndMakeVisible(pitchDialG);
	addAndMakeVisible(gainDial);
	addAndMakeVisible(freqDial);
	addAndMakeVisible(resDial);

	addAndMakeVisible(gainLabel);
	addAndMakeVisible(resLabel);
	addAndMakeVisible(freqLabel);
	addAndMakeVisible(eLabel);
	addAndMakeVisible(aLabel);
	addAndMakeVisible(dLabel);
	addAndMakeVisible(gLabel);

	addAndMakeVisible(noise);
	addAndMakeVisible(controlText);

	for (int i = 1; i <= numNoiseTypes; i++) {
		noise.addItem(noiseTypes[i-1], i);
	}

	gainLabel.setText("Gain", dontSendNotification);
	resLabel.setText("Muteness", dontSendNotification);
	freqLabel.setText("String Type", dontSendNotification);
	controlText.setText("String Control", dontSendNotification);
	eLabel.setText("E String", dontSendNotification);
	aLabel.setText("A String", dontSendNotification);
	dLabel.setText("D String", dontSendNotification);
	gLabel.setText("G String", dontSendNotification);

	gainLabel.attachToComponent(&gainDial, false);
	resLabel.attachToComponent(&resDial, false);
	freqLabel.attachToComponent(&freqDial, false);
	eLabel.attachToComponent(&pitchDialE, false);
	aLabel.attachToComponent(&pitchDialA, false);
	dLabel.attachToComponent(&pitchDialD, false);
	gLabel.attachToComponent(&pitchDialG, false);

	gainDial.setSliderStyle(Slider::SliderStyle::Rotary);
	resDial.setSliderStyle(Slider::SliderStyle::Rotary);
	freqDial.setSliderStyle(Slider::SliderStyle::Rotary);
	pitchDialE.setSliderStyle(Slider::SliderStyle::Rotary);
	pitchDialA.setSliderStyle(Slider::SliderStyle::Rotary);
	pitchDialD.setSliderStyle(Slider::SliderStyle::Rotary);
	pitchDialG.setSliderStyle(Slider::SliderStyle::Rotary);

	//gainDial.setTextValueSuffix(" dB");

	gainDial.setTextBoxStyle(Slider::TextBoxBelow, true, 90, 15);
	resDial.setTextBoxStyle(Slider::NoTextBox, true, 90, 15);
	freqDial.setTextBoxStyle(Slider::NoTextBox, true, 90, 15);
	pitchDialE.setTextBoxStyle(Slider::TextBoxBelow, true, 50, 15);
	pitchDialA.setTextBoxStyle(Slider::TextBoxBelow, true, 50, 15);
	pitchDialD.setTextBoxStyle(Slider::TextBoxBelow, true, 50, 15);
	pitchDialG.setTextBoxStyle(Slider::TextBoxBelow, true, 50, 15);

	gainDial.setRange(0.0f,1.0f,0.01);
	resDial.setRange(0.01f,0.8f,0.01);
	freqDial.setRange(150,6000,1);
	pitchDialE.setRange(23,40,0.01);
	pitchDialA.setRange(28,45,0.01);
	pitchDialD.setRange(33,50,0.01);
	pitchDialG.setRange(38,55,0.01);

	gainDial.setValue(1.0);
	resDial.setValue(0.5);
	freqDial.setValue(500);
	pitchDialE.setValue(28);
	pitchDialA.setValue(33);
	pitchDialD.setValue(38);
	pitchDialG.setValue(43);

	gainLabel.setJustificationType(Justification::centred);
	resLabel.setJustificationType(Justification::centred);
	freqLabel.setJustificationType(Justification::centred);
	controlText.setJustificationType(Justification::centred);
	eLabel.setJustificationType(Justification::centred);
	aLabel.setJustificationType(Justification::centred);
	dLabel.setJustificationType(Justification::centred);
	gLabel.setJustificationType(Justification::centred);

	freqDial.setSkewFactorFromMidPoint(1000);
	gainDial.setSkewFactorFromMidPoint(0.5);

	kSliderState.addListener(this);

	noise.setText("white");

	freqDial.addListener(this);
	gainDial.addListener(this);
	resDial.addListener(this);
	pitchDialE.addListener(this);
	pitchDialA.addListener(this);
	pitchDialD.addListener(this);
	pitchDialG.addListener(this);

	noise.addListener(this);
}

KpsvstAudioProcessorEditor::~KpsvstAudioProcessorEditor()
{
	kSliderState.removeListener(this);
}

//==============================================================================
void KpsvstAudioProcessorEditor::paint (Graphics& g)
{
    // (Our component is opaque, so we must completely fill the background with a solid colour)
    g.fillAll (getLookAndFeel().findColour (ResizableWindow::backgroundColourId));
	Line<float> bottomLine(Point<float>(8, 150), Point<float>(576, 150));
	Line<float> Vert1(Point<float>(440, 158), Point<float>(440, 280));
	Line<float> Vert2(Point<float>(376, 8), Point<float>(376, 142));

	g.setColour(Colours::ghostwhite);
	g.drawLine(bottomLine, 2.0f);
	g.drawLine(Vert1, 2.0f);
	g.drawLine(Vert2, 2.0f);
}

void KpsvstAudioProcessorEditor::resized()
{
	const int pitchDialWidth = 90;
	const int dialWidth = 100;
	auto area = getLocalBounds();
	area.reduce(8, 0);

	controlText.setBounds(114, 50, 140, 25);

	noise.setBounds(392, 50, 168, 25);

	kSlider.setBounds(area.removeFromBottom(80).reduced(8));
	kSlider.setAvailableRange(24, 70);
	kSlider.setKeyWidth(area.getWidth() / 28);

	gainDial.setBounds(456, 175, dialWidth, dialWidth);
	resDial.setBounds(260, 28, dialWidth, dialWidth);
	freqDial.setBounds(8, 28, dialWidth, dialWidth);

	pitchDialE.setBounds(8, 175, dialWidth, dialWidth);
	pitchDialA.setBounds(116, 175, dialWidth, dialWidth);
	pitchDialD.setBounds(224, 175, dialWidth, dialWidth);
	pitchDialG.setBounds(332, 175, dialWidth, dialWidth);
}



void KpsvstAudioProcessorEditor::handleIncomingMidiMessage(MidiInput* source, const MidiMessage& message)
{
	const ScopedValueSetter<bool> scopedInputFlag(isAddingFromMidiInput, true);
	kSliderState.processNextMidiEvent(message);
}

void KpsvstAudioProcessorEditor::handleNoteOn(MidiKeyboardState*, int midiChannel, int midiNoteNumber, float velocity)
{
	if (!isAddingFromMidiInput)
	{
		auto m = MidiMessage::noteOn(midiChannel, midiNoteNumber, velocity);
		m.setTimeStamp(Time::getMillisecondCounterHiRes() * 0.001);
		processor.setNote(m);
	}
}

void KpsvstAudioProcessorEditor::handleNoteOff(MidiKeyboardState*, int midiChannel, int midiNoteNumber, float /*velocity*/)
{
	if (!isAddingFromMidiInput)
	{
		auto m = MidiMessage::noteOff(midiChannel, midiNoteNumber);
		m.setTimeStamp(Time::getMillisecondCounterHiRes() * 0.001);
	}
}

void KpsvstAudioProcessorEditor::sliderValueChanged(Slider* slider) {
	if (slider == &freqDial) {
		processor.updateFilterFreq(freqDial.getValue());
	} else if (slider == &resDial) {
		processor.updateFilterRes(slider->getValue());
	} else if (slider == &gainDial) {
		processor.volumeOffset = gainDial.getValue();
	} else if (slider == &pitchDialE) {
		processor.updatePitch(pitchDialE.getValue(), 0);
	} else if (slider == &pitchDialA) {
		processor.updatePitch(pitchDialA.getValue(), 1);
	} else if (slider == &pitchDialD) {
		processor.updatePitch(pitchDialD.getValue(), 2);
	} else if (slider == &pitchDialG) {
		processor.updatePitch(pitchDialG.getValue(), 3);
	}
}

void KpsvstAudioProcessorEditor::comboBoxChanged(ComboBox* comboBox) {
	processor.updateNoiseType(noise.getSelectedItemIndex());
}