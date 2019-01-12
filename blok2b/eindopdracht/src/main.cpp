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

//~~~~~~~~~~~~~Read the file; notes.txt first~~~~~~~~~~~~~//

//Auto_execute
//cd ..; make; cd bin; ./synthsong.exe

#define PI_2 6.28318530717959

using namespace std;                        //I like to use this so I don't constantly have to type std:: in front of everything. Nonetheless I know which pieces of code do need std:: for them to work.

int main(int argc,char **argv){
    //Variables
    int bpm = 120;
    string state;
    string layer;
    string waveform;
    string type;
    double timing;
    double endOfLoop = 0;
    double frequency;
    double ratio;
    double modulation;
    int measure;

    //Create a JackModule instance
    JackModule jack;

    //
    ifstream inFile;
    vector<vector<string> > notes;          //Initiate the 2D vector.
    vector<double> rhythm;
    vector<string> temporary;               //To store temporary data that will be read from the markov.txt file
    string note;

    //Reading the user input file
    inFile.open("../doc/markov.txt");
    if(!inFile){
        cout<<"Unable to open file"<<endl;  //If the file is not in the correct place display this error
        exit(1);
    }
    while(inFile >> note){
        if(note == "=="){                   //A small statemachine that will flip and switch when reading out the markov.txt file. This makes sure all the settings will be in the right place
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
        } else if(note == "melody:" || layer == "melody:"){     //Fill a vector with the input of the user, the vector is a 2d vector with the markovchain rules
            if(layer == "melody:"){
                if(note == "//"){                               //The check to see if the end of one layer of Markov is reached, if so then
                    notes.push_back(temporary);                 //Push the temporary array to the 2D array and clear it.
                    temporary.clear();
                } else if(note[0] == '`'){                      //Store the notelengths.
                    note.erase(note.begin());
                    if(stod(note) < 0.25 || stod(note) > 4){
                        cout<<"Note length too long, choose: 0.25 | 0.5 | 1 | 2 | 4 |"<<endl<<"Error at rhythm: "<<note<<endl;
                        exit(1);
                    }
                    rhythm.push_back(stod(note));
                } else if(note.size() <= 2) {                   //Check if the input is indeed a note and an octave next to eachother then push the notes to the 1D temporary array.
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
    frequency = melody.getNote(notes);      //Set the first frequency for the oscillator.
    timing = melody.getRhythm(rhythm);      //Set the first time of delay.

//~~~~~~~~~~~~~~~~~~~~~~~~~~
//~~~~~~~~~~~JACK~~~~~~~~~~~
//~~~~~~~~~~~~~~~~~~~~~~~~~~

    // init the jack, use program name as JACK client name
    jack.init("example.exe");
    double samplerate = jack.getSamplerate();

    //Make new simple and fm synth
    FmSynth fmsynth(samplerate,frequency,waveform, "sine",modulation,ratio);
    SimpleSynth simplesynth(samplerate,frequency,waveform);

    Synth *synthesizer;     //To easily pick a synthesizer use a pointer.

    if(type == "fm"){       //Type is written in the markov.txt file and is checked here, otherwise it defaults to a simple synth
        synthesizer = &fmsynth;
    } else{
        synthesizer = &simplesynth;
    }

    //assign a function to the JackModule::onProces
    //~~CC~~
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
    //||CC||

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//~~~~~~~~~~~MELODY~~~~~~~~~~~
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    //Start of notes loop
    while(true){
        frequency = melody.getNote(notes);      //Get the next frequency for the oscillator.
        synthesizer->setFrequency(frequency);   //Set the frequency of the synthesizer.
        timing = melody.getRhythm(rhythm);      //Set the timing of the sleeper function. The reason I used the sleeper function instead
                                                //of timestamps is becaus the compiler didn't completely get how to use timestamps.
        endOfLoop = endOfLoop + (timing/(60000/bpm));     //Add the timings to the loop value that determains if we are at the end of the song.
        Sleep(timing);
        if(endOfLoop >= measure){
            jack.end();                         //Disconnect Jack correctly
            break;                              //End loop
        }
    }
    
    return 0;
}