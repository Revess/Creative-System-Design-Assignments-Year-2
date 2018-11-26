#ifndef _SINE_H_

#define PI_2 6.28318530717959

class Sine{
    public:
    Sine(double samplerate, double frequency);
    ~Sine();

    double getSample();

    void tick();

    void setFrequency(double frequency);
    double getFrequency();

    private:
    double samplerate;
    double amplitude;
    double frequency;
    double phase;
    double sample;
};

#endif