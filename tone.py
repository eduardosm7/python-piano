"""
Tone class

This code was inspired by:
  https://mail.python.org/pipermail/tutor/2012-September/091476.html
It's a very interesting post, please check it out.
"""

import math
import struct
import pyaudio


class Tone:

    fs = 128000  # Sampling rate
    p = pyaudio.PyAudio()

    @staticmethod
    def play_tone(frequency, amplitude, duration):
        """
        Plays tone given the params

        :param frequency: Note frequency in Hz
        :type frequency: float
        :param amplitude: Amplitude
        :type amplitude: float
        :param duration: Duration of the note in seconds
        :type amplitude: float
        """
    
        # Opens stream
        stream = Tone.p.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=Tone.fs,
            output=True)

        N = int(Tone.fs / frequency)
        T = int(frequency * duration)  # repeat for T cycles
        dt = 1.0 / Tone.fs  # Sampling step size

        # Defines tone by sinusoid equation (sin wave)
        # Check it on https://en.wikipedia.org/wiki/Sine_wave
        tone = (amplitude * math.sin(2 * math.pi * frequency * n * dt)
                for n in range(N))

        # Joins bytes
        data = b''.join(struct.pack('f', samp) for samp in tone)

        # Writes bytes on the stream
        for n in range(T):
            stream.write(data)
    
        stream.close()
    