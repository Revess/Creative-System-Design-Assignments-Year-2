#include <iostream>
#include <string>
#include <conio.h>
#include <windows.h>
#include <vector>
#include <fstream>
#include <thread>
#include "../include/jack_module.h"
#include "../include/simpleSynth.h"
#include "../include/fmSynth.h"
#include "../include/melody.h"

//Auto_execute
//cd ..; make; cd bin; ./synthsong.exe

#define PI_2 6.28318530717959

using namespace std;

int main(int argc,char **argv){
    //Variables
    int bpm = 120;
    double timing;
    string state;
    string layer;
    string waveform;
    double test = 0;
    double frequency;
    double ratio;
    double modulation;
    string type;
    int measure;

    //Create a JackModule instance
    JackModule jack;

    ifstream inFile;
    vector<vector<string> > notes;
    vector<double> rhythm;
    vector<string> temporary;
    string note;

    //Reading the user input file
    inFile.open("../doc/markov.txt");
    if(!inFile){
        cout<<"Unable to open file"<<endl;
        exit(1);
    }
    //Fill a vector with the input of the user, the vector is a 2d vector with the markovchain rules
    while(inFile >> note){
        if(note == "=="){
            layer = "";
        } else if(note == "settings:" || layer == "settings:"){
            if(layer == "settings:"){
                if(note == "waveform:" || state == "waveform:"){
                    if(state == "waveform:"){
                        state = "";
                        waveform = note;
                    } else {
                        state = note;
                    }
                } else if(note == "type:" || state == "type:"){
                    if(state == "type:"){
                        state = "";
                        type = note;
                    } else{
                        state = note;
                    }
                }else if(note == "mod:" || state == "mod:"){
                    if(state == "mod:"){
                        state = "";
                        modulation = stod(note);
                    } else {
                        state = note;
                    }
                } else if(note == "ratio:" || state == "ratio:"){
                    if(state == "ratio:"){
                        state = "";
                        ratio = stod(note);
                    } else {
                        state = note;
                    }
                } else if(note == "measure:" || state == "measure:"){
                    if(state == "measure:"){
                        state = "";
                        measure = stoi(note)*4;
                    } else {
                        state = note;
                    }
                } else if(note == "bpm:" || state == "bpm:"){
                    if(state == "bpm:"){
                        state = "";
                        bpm = stoi(note);
                    } else {
                        state = note;
                    }
                }
            } else {
                layer = note;
            }
        } else if(note == "melody:" || layer == "melody:"){
            if(layer == "melody:"){
                if(note == "//"){
                    notes.push_back(temporary);
                    temporary.clear();
                } else if(note[0] == '`'){
                    note.erase(note.begin());
                    if(stod(note) < 0.25 || stod(note) > 4){
                        cout<<"Note length too long, choose: 0.25 | 0.5 | 1 | 2 | 4 |"<<endl<<"Error at rhythm: "<<note<<endl;
                        exit(1);
                    }
                    rhythm.push_back(stod(note));
                } else if(note.size() <= 2) {
                    temporary.push_back(note);
                }
            } else {
                layer = note;
            }
        }
    }
    inFile.close();

    //Initiate the melody calculator
    Melody melody(notes,rhythm,bpm);
    frequency = melody.getNote(notes);
    timing = melody.getRhythm(rhythm);

//~~~~~~~~~~~~~~~~~~~~~~~~~~
//~~~~~~~~~~~JACK~~~~~~~~~~~
//~~~~~~~~~~~~~~~~~~~~~~~~~~

    // init the jack, use program name as JACK client name
    jack.init("example.exe");
    double samplerate = jack.getSamplerate();

    //Make new synth
        FmSynth fmsynth(samplerate,frequency,waveform, "sine",modulation,ratio);
        SimpleSynth simplesynth(samplerate,frequency,waveform);

    Synth *synthesizer;

    if(type == "fm"){
        synthesizer = &fmsynth;
    } else{
        synthesizer = &simplesynth;
    }

    //assign a function to the JackModule::onProces
    jack.onProcess = [&synthesizer](jack_default_audio_sample_t *inBuf,
        jack_default_audio_sample_t *outBuf, jack_nframes_t nframes) {
            static double amplitude = 0.5;
            for(unsigned int i = 0; i < nframes; i++) {
                // write sine output * amplitude --> to output buffer
                outBuf[i] = amplitude * synthesizer->getSample();
                // calculate next sample
                synthesizer->tick();
            }
        return 0;
    };

    jack.autoConnect();

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//~~~~~~~~~~~MELODY~~~~~~~~~~~
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    //Start of notes loop
    while(true){
        frequency = melody.getNote(notes);
        synthesizer->setFrequency(frequency);
        timing = melody.getRhythm(rhythm);
        test = test + (timing/(60000/bpm));
        cout<<test<<endl;
        Sleep(timing);
        if(test >= measure){
            jack.end();
            break;
        }
    }
    
    return 0;
}