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
    2. - Sine wave generation at 1420 MHz offset => **In Part 4. it is changed to 0 due to a mistake by me**.
       - "Hydrogen Line" frequency at 10kHz.
    3. Throttle block.
    4. Simultaneous display of Time Sink and Frequency Sink.

**Comments on the plots**
    
   In the time domain we can see how the amplitude of the signal changes overtime. We can see a clean sine wave,that is periodic, smooth and has a    single-frequency tone. 
   It can be represented as: x(t) = Acos(2pift + Φ)
   
   Where:
      
   * A is the amplitude
   * f the frequency
   * t is the time in seconds
   * Φ is the phase angle of the signal
    
   In the frequency domain we can see the frequencies that are present in the signal. The frequency spike corresponds to the sine wave's frequency.
   It can be represented as: X(f) = Aδ(f - f0)
   
   Where:
   
   * A is the amplitude
   * δ is the Dirac delta function with its center on f0

   **Frequency Sink Spike explanation:** I is known from Fourier series theory, that a signal with a non-zero average value has a constant offset with zero frequency, that's why the spike is present at 0kHz.

**Information sources used for Part 2.:** personal knowledge and the official GNU Radio wiki.


# Part 3. | Adding Noise

Blocks Added for the new flowgraph:

   * Noise block
   * Add Block to add the Signal waveform and the Noise. The block was found under the **Math Operations** label.

### Answer for 4.: ### 

   **Noise Block Settings:** 
   
   - Noise Type: Gaussian
   - Amplitude for 1st run: 1
   - Amplitude for 2nd run: 5
   - Amplitude for 3rd run: 10
   - Test amplitude for fun: 10000
   - Seed: 0

   **Note:** The screeshots are from the 1st and 3rd runs to better demostrate the differences. A screenshot for *offset: 0* is placed in the foleder as well.

   **Report for amplitude changes**

   Starting with *amplitude: 1* we can still see the sine waveform in the time domain and can still see *spectral line* and the *energy spike* in the frequency domain pretty clearly. However, as the *amplitude of the noise increases gradually from 1 to 10,* and at around *amplitude: 3* the sine waveform becomes harder to distinguish due to the increase of the irregularities added, from the noise, to the signal.

   After testing with different amplitude values, the *spectral line* **DOES NOT** disapeer completely due to the offset not being 0.
   Even with *amplitude: 10000* the spike is still visible, although smaller due to the increase of the relative gain of the *spectral line* in general. If we set the *offset* from 1420e3 -> 0, then the spike at 0Hz disapeers completely.

   **About detecting weak astronomical signals:**

   After adding a single noise source to a simple sine waveform and seeing how distorted the signal is, it is clear that the detection of astronomical signals is difficult and requires complicated processing techniques.

**Information sources used for Part 3.:** personal knowledge, the official GNU Radio wiki, Stack Overflow and MathWorks site.


## Important Note:## due to a mistake from me, from **Part 4.** going forward, the offset changes from 1420e3 -> 0

## Changes in settings for Part 4. 
   
   - Noise amplitude back to initial value: 1


# Part 4. | Filtering

   **Low Pass Filter Settings:**
   
   - Decimation: 1
   - Gain: 1
   - Sample rate: 32k
   - Cutoff Freq. for 1st run: 10kHz
   - Transition Width for 1st run: 1kHz
   - Cutoff Freq. for 2nd run: 5kHz 
   - Transition Width for 2nd run: 1kHz
   - Window: Hamming
   - Beta: 6.76

   **Comments on the plots**

   * 




