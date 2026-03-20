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
    * **QT GUI Frequency Sink:** a block that displays multiple signals in frequency. Found under **GUI Widgets and then QT**.
    * **QT GUI Time Sink:** a block that displays multiple signals in time. Found under **GUI Widgets and then QT**.
    * **Throttle:** limiter of sample rate to a specified average rate using the system clock. Found under **Misc**.


**Issues with Part 1.:** no issues were encountered in Part 1. except the VM set-up problem that was resolved easily from the Oracle VM start screen.

**Information sources used for Part 1.:** previous knowledge and the official GNU Radio wiki were used to find the desscription of the blocks. Their locations in the GNU Radio companion application were found manually.






