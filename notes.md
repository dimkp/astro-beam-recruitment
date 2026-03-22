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
    
   In the time domain we can see how the amplitude of the signal changes overtime. We can see a clean sine wave,that is periodic, smooth and has a single-frequency tone. 
   It can be represented as: x(t) = Asin(2pift + Φ)
   
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


## Important Note: due to a mistake from me, from **Part 4.** going forward, the offset changes from 1420e3 -> 0

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

   **Answer for 1.**

   *Cutoff frequency* is firstly set to 10kHz and the *Transition Width* is set to 1kHz and then the *Cutoff frquency* is decreased to 5kHz while the *Transition Width* stays the same.

   **Answer for 2.**

   - Cutoff frequency: 5kHz
   - Transition Width: 1kHz

   Between the **filtered** and the **unfiltered** signals we can see that, in the filtered signal, the amplitude variations are gratly reduced and that indicates that a big part of the noise has been removed. However, as we can see the sine waveform, is still not clearly visible which proves that filtering helps improve the quality of the signal but does not complytely eliminate the noise.

   **Comments on the plots for 3.**

   * Setting the *Cutoff frequency* value close to the signal value of 10kHz, we can see, the spike in the frequency domain belongs in the *passband* (almost straight line from around -10kHz -> 10kHz), that the signal passes through the filter and some of the noise is removed.
   * Changing the *Cutoff frequency* value from 10kHz to 5kHz, we can see that the spike at 10kHz, **IS NOT** part of the passband, so the signal does not pass through the filter.

   **Additional questions for Part 4.**

   - Filtering does not recover the signal from noise, but it helps make it a little bit more distinguisable by removing some of the noise.
   - By making the filter very narrow, we remove more noise but also lose some potentially usefull frequencies that were higher than the filters cutoff.
   - Answered in *Comments on the plots for 3.*.

**Information sources used for Part 4.:** personal knowledge, the official GNU Radio wiki, Scribd.com "Disadvantages of a Low Pass Filter", MathWorks site and CHatGPT for explanation of how the filter parameters work because the documentaion was a bit chaotic.


# Part 5. | Simulating an Observation

Blocks added for the new flowgraph:   
   
   - 2 Signal Sources, one with frequency 10kHz and Amplitude 1 and the other with the same frequency and Amplitude 0.
   - A **Selector Block** with 2 inputs and 2 outputs. The **Selector Block** can be found under the label **Misc**
   - 2 QT Frequency Sinks, one for plotting the OFF state and one for the ON state.

   By observing the **Off position** astronomers can calculate the noise produced by the atmosphere, the environment or other sources and then subtract it from the *weaker* signal of the object they want to observe in the **On position**. 

   The mathematical representation is: Reduced_spectrum = (ON - OFF) / OFF

**Information sources used for Part 5.:** GNU Radio wiki for how the Selector Block works, aanda.org, astro.cornell.edu, Springer Nature website.


# Part 5.5 | Analyzing Your Signal in Python

**Comments for every code instruction is present in the .py file for convenience, as the file is pretty small**

   **Comments for the results of Parts 5.5.1 and 5.5.2**
   
   We can se the sine signal clearly because of the *two spikes* at ~-1000 and ~1000 Hz. We can see both the negative and the positive values becuse the FFT computes both so i chose to not remove them for the first two parts but i will remove them for the rest for convenience and clarity.

   **Comments for the results of Part 5.5.3 and Part 5.5.4**
   
   I chose to implement my own Smoothing function because i wanted to experiment with Python a bit more, no other reason.

   We can see both signals (Raw = Blue and Smoothed = Red) on the same plot and we can see that the smoothing loop worked correctly. The noise is reduced as it's evident from the smoother waveform and the smaller spikes, while the signal still passes through as we can see from the, smaller and smoother but stil evident, peak at 1000 Hz.

   **Comments for the results of Part 5.5.5**

   Again, i chose to implement my own linear search algorithm just to experiment with Python.

   The *frequency index* where the singal peaks changes depending on the size of the sample_rate. That happens mainly because of the FFT. The FFT doesn't see every frequency on it;s own but as bins with a distance between then that is calculated: distance = sample_rate / array_size. So the peak **value** goes no to the true value but to the nearest bin, but the peak **index** i believe it is calculated correctly. I searched the Python documentation and couldn't anything on how to resolve this issue so i report it here. 
   
   Test results: 

   - For N = 1000 and sample_rate = 10000, the peak value is 1050.0 Hz and the peak index is 105
   - For N = 5000 and sample_rate = 10000, the peak value is 1006.0 Hz and the peak index is 503
   - For N = 10000 and sample_rate = 10000, the peak value is 997.0 Hz and the peak index is 997

   As we can see, the bigger the size of the samples (N) => the bigger the accuracy of the result. If the sample size (N) is small enough, the peak frequency value can be calculated as bigger than the signals frequency.

   **Note for push**

   The code will get pushed with N = 1000, sample_rate = 10000 because i can't see the plots clearly, due to my VMs low resolution. 

   **GRC vs Python**

   Coding in **Python** gives more control and flexibility over every step of the signal analysis, while **GNU Radio companion** is easier for seeing how the date flows from one step to the next and it's faster for prototyping.  

**Information sources and help for Part 5.:** Python documentation, ChatGPT for information regarding some of the code.

   
# Part 6. | Your Turn

   **Option B:** Use a **QT GUI Range** widget to make the noise amplitude adjustable with a slider while the flowgraph is running. Observe and screenshot the effect in real time.



   **Option C:** Research what the **FFT Size** parameter in the Frequency Sink does and experiment with several values. Describe the tradeoff between frequency resolution and time resolution.


**Information sources for Part 6.:**


# Part 7. | The Real Thing

### First: 

   
   
### Second:






