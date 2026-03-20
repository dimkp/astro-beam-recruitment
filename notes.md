# Part 1 | Installing GNU Radion and Getting Oriented

1. Installation and launch of **GNU Radio version 3.10.9.2**, via the terminal using the following set of instructions:
    * **Installation:**    
        - sudo update
        - sudo apt upgrade -y
        - sudo apt install gnuradio -y
    * **Launch:**
        - gnuradio-companion
**Source:** The instructions were found from the **GNU Radio wiki**.

2. Screenshot uploaded to GitHub via the host windows machine due to a configuration issue that has been solved.

3. Block descriptions and locations in the GNU Radio companion's **block library**: 
    * **Signal Source:** generates a waveform in a specified frequency, amplitude and sample rate. Found under **Waveform Generators**.
    * **Noise Source:** generates a random waveform to simulate real-world conditions. Found under **Waveform Generators**.
    * **Low Pass Filter:** a processing block that determines if a signal should pass while attenuating the higher frequencies. Found under **Filters**
    * **QT GUI Frequency Sink:** a block that displays multiple signals in frequency. Found under **Instrumentation and then QT**.
    * **QT GUI Time Sink:** a block that displays multiple signals in time. Found under **Instrumentation and then QT**.
    * **Throttle:** limiter of sample rate to a specified average rate using the system clock. Found under **Misc**.


**Issues with Part 1.:** no issues were encountered in Part 1. except the VM set-up problem that was resolved easily from the Oracle VM start screen.

**Information sources used for Part 1.:** previous knowledge and the official GNU Radio wiki were used to find the desscription of the blocks. Their locations in the GNU Radio companion application were found manually.


# Part 2. | Your First Flowgraph: A Clean Signal

Instructions: 
    1. Sample Rate of 100k points per second.
    2. - Sine wave generation at 1420 MHz offset.
       - "Hydrogen Line" frequency at 10kHz.
    3. Throttle block.
    4. Simultaneous display of Time Sink and Frequency Sink.

**Comments on the plots**
    In the time domain we can see how the amplitude of the signal changes overtime. We can see a clean sine wave,that is periodic, smooth and has a single-frequency tone. 
    It can be represented as: x(t) = A x cos(2 x pi x f x t + Φ)
        Where:
        - A is the amplitude
        - f the frequency
        - t is the time in seconds
        - Φ is the phase angle of the signal
    
    In the frequency domain we can see the frequencies that are present in the signal. The frequency spike corresponds to the sine wave's frequency.
    It can be represented as: X(f) = A x δ(f - f0)
        Where:
        - A is the amplitude
        - δ is the Dirac delta function with its center on f0

    **Frequency Sink Spike explanation:** I is known from Fourier series theory, that a signal with a non-zero average value has a constant offset with zero frequency, that's why the spike is present at 0kHz.

**Information sources used for Part 2.:** personal knowledge and the official GNU Radio wiki.

    

