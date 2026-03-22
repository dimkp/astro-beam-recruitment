#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Hydrogen_Flowgraph
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from datetime import datetime
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
import numpy as np
import pmt
import sip



class Hydrogen_Flowgraph(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Hydrogen_Flowgraph", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Hydrogen_Flowgraph")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "Hydrogen_Flowgraph")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.vec_length = vec_length = 1024
        self.sinc_sample_locations = sinc_sample_locations = np.arange(-np.pi*4/2.0, np.pi*4/2.0, np.pi/vec_length)
        self.sinc = sinc = np.sinc(sinc_sample_locations/np.pi)
        self.samp_rate = samp_rate = 10e6
        self.rfgain = rfgain = 30
        self.ifgain = ifgain = 0
        self.bbgain = bbgain = 0
        self.timenow = timenow = datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
        self.restFreq = restFreq = 9.75e9
        self.receiver = receiver = "80cm Sun"
        self.output_filename = output_filename = "observation.dat"
        self.observationType = observationType = 'Sun3/'
        self.observationRA = observationRA = 42.5
        self.observationObject = observationObject = "M82"
        self.observationDec = observationDec = 130.2
        self.intermediate_rate = intermediate_rate = 1e3
        self.integrationTimeShort = integrationTimeShort = .5
        self.integrationTimeLong = integrationTimeLong = 5
        self.freq = freq = 1.45e9
        self.file_rate = file_rate = 1
        self.file = file = str(rfgain)+'_'+str(ifgain)+'_'+str(bbgain)+'G'+str(samp_rate/10e5)+'MHz.dat'
        self.dire = dire = '/home/georkeso/observations/Radiometer/'
        self.dc_gain = dc_gain = 1e5
        self.date = date = 'Sun300625/'
        self.custom_window = custom_window = sinc*np.hamming(4*vec_length)
        self.center_freq = center_freq = 1.45e9
        self.T_hot = T_hot = 300
        self.T_cold = T_cold = 10
        self.P_hot = P_hot = 64
        self.P_cold = P_cold = 33

        ##################################################
        # Blocks
        ##################################################

        self.Flowgraph_Tabs = Qt.QTabWidget()
        self.Flowgraph_Tabs_widget_0 = Qt.QWidget()
        self.Flowgraph_Tabs_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Flowgraph_Tabs_widget_0)
        self.Flowgraph_Tabs_grid_layout_0 = Qt.QGridLayout()
        self.Flowgraph_Tabs_layout_0.addLayout(self.Flowgraph_Tabs_grid_layout_0)
        self.Flowgraph_Tabs.addTab(self.Flowgraph_Tabs_widget_0, 'Sun_Flowgraph')
        self.Flowgraph_Tabs_widget_1 = Qt.QWidget()
        self.Flowgraph_Tabs_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Flowgraph_Tabs_widget_1)
        self.Flowgraph_Tabs_grid_layout_1 = Qt.QGridLayout()
        self.Flowgraph_Tabs_layout_1.addLayout(self.Flowgraph_Tabs_grid_layout_1)
        self.Flowgraph_Tabs.addTab(self.Flowgraph_Tabs_widget_1, 'Hydrogen_Flowgraph')
        self.top_layout.addWidget(self.Flowgraph_Tabs)
        self._center_freq_range = qtgui.Range(900e6, 3e9, 4e6, 1.45e9, 200)
        self._center_freq_win = qtgui.RangeWidget(self._center_freq_range, self.set_center_freq, "'center_freq'", "slider", float, QtCore.Qt.Horizontal)
        self.Flowgraph_Tabs_layout_1.addWidget(self._center_freq_win)
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            vec_length,
            ((center_freq-(samp_rate/2))/1e6),
            ((samp_rate/vec_length)/1e6),
            "Frequency (MHz)",
            "Signal",
            "",
            1, # Number of inputs
            None # parent
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis((-140), 10)
        self.qtgui_vector_sink_f_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0.enable_grid(False)
        self.qtgui_vector_sink_f_0.set_x_axis_units("MHz")
        self.qtgui_vector_sink_f_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0.set_ref_level(0)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0.qwidget(), Qt.QWidget)
        self.Flowgraph_Tabs_grid_layout_1.addWidget(self._qtgui_vector_sink_f_0_win, 4, 0, 20, 10)
        for r in range(4, 24):
            self.Flowgraph_Tabs_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 10):
            self.Flowgraph_Tabs_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_histogram_sink_x_0_0 = qtgui.histogram_sink_f(
            1024,
            100,
            (-1),
            1,
            "System Heartbeat",
            1,
            None # parent
        )

        self.qtgui_histogram_sink_x_0_0.set_update_time(0.10)
        self.qtgui_histogram_sink_x_0_0.enable_autoscale(True)
        self.qtgui_histogram_sink_x_0_0.enable_accumulate(False)
        self.qtgui_histogram_sink_x_0_0.enable_grid(False)
        self.qtgui_histogram_sink_x_0_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers= [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_histogram_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_histogram_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_histogram_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_histogram_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_histogram_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_histogram_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_histogram_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_histogram_sink_x_0_0_win = sip.wrapinstance(self.qtgui_histogram_sink_x_0_0.qwidget(), Qt.QWidget)
        self.Flowgraph_Tabs_grid_layout_1.addWidget(self._qtgui_histogram_sink_x_0_0_win, 0, 8, 3, 1)
        for r in range(0, 3):
            self.Flowgraph_Tabs_grid_layout_1.setRowStretch(r, 1)
        for c in range(8, 9):
            self.Flowgraph_Tabs_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            center_freq, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.fft_vxx_0 = fft.fft_vcc(vec_length, True, window.rectangular(vec_length), True, 1)
        self._dc_gain_tool_bar = Qt.QToolBar(self)
        self._dc_gain_tool_bar.addWidget(Qt.QLabel("DC Gain" + ": "))
        self._dc_gain_line_edit = Qt.QLineEdit(str(self.dc_gain))
        self._dc_gain_tool_bar.addWidget(self._dc_gain_line_edit)
        self._dc_gain_line_edit.editingFinished.connect(
            lambda: self.set_dc_gain(eng_notation.str_to_num(str(self._dc_gain_line_edit.text()))))
        self.top_layout.addWidget(self._dc_gain_tool_bar)
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_gr_complex*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_stream_to_vector_0_5_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, vec_length)
        self.blocks_stream_to_vector_0_5 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, vec_length)
        self.blocks_stream_to_vector_0_3 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, vec_length)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, vec_length)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, vec_length, 0)
        self.blocks_multiply_const_vxx_0_2_0_0 = blocks.multiply_const_vcc(custom_window[0:vec_length])
        self.blocks_multiply_const_vxx_0_2_0 = blocks.multiply_const_vcc(custom_window[0:vec_length])
        self.blocks_multiply_const_vxx_0_2 = blocks.multiply_const_vcc(custom_window[-vec_length:])
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_vcc(custom_window[2*vec_length:3*vec_length])
        self.blocks_integrate_xx_0 = blocks.integrate_ff((int(samp_rate/vec_length)), vec_length)
        self.blocks_file_sink_1 = blocks.file_sink(gr.sizeof_float*vec_length, '/home/dim/astro-beam-recruitment/flowgraphs/Part_7/obs2.dat', True)
        self.blocks_file_sink_1.set_unbuffered(False)
        self.blocks_delay_0_1 = blocks.delay(gr.sizeof_gr_complex*1, (2*vec_length))
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_gr_complex*1, vec_length)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, (3*vec_length))
        self.blocks_complex_to_real_0_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_mag_squared_0_0 = blocks.complex_to_mag_squared(vec_length)
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(vec_length)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 10e3, 1, 0, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 1, 0)
        self._P_hot_tool_bar = Qt.QToolBar(self)
        self._P_hot_tool_bar.addWidget(Qt.QLabel("Hot Pw" + ": "))
        self._P_hot_line_edit = Qt.QLineEdit(str(self.P_hot))
        self._P_hot_tool_bar.addWidget(self._P_hot_line_edit)
        self._P_hot_line_edit.editingFinished.connect(
            lambda: self.set_P_hot(int(str(self._P_hot_line_edit.text()))))
        self.Flowgraph_Tabs_layout_0.addWidget(self._P_hot_tool_bar)
        self._P_cold_tool_bar = Qt.QToolBar(self)
        self._P_cold_tool_bar.addWidget(Qt.QLabel("Cold Pw" + ": "))
        self._P_cold_line_edit = Qt.QLineEdit(str(self.P_cold))
        self._P_cold_tool_bar.addWidget(self._P_cold_line_edit)
        self._P_cold_line_edit.editingFinished.connect(
            lambda: self.set_P_cold(int(str(self._P_cold_line_edit.text()))))
        self.Flowgraph_Tabs_layout_0.addWidget(self._P_cold_tool_bar)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_complex_to_real_0_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_delay_0_1, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.blocks_integrate_xx_0, 0))
        self.connect((self.blocks_complex_to_real_0_0, 0), (self.qtgui_histogram_sink_x_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_stream_to_vector_0_3, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_stream_to_vector_0_5, 0))
        self.connect((self.blocks_delay_0_1, 0), (self.blocks_stream_to_vector_0_5_0, 0))
        self.connect((self.blocks_integrate_xx_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0_2, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_2_0, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_multiply_const_vxx_0_2_0_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_file_sink_1, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.qtgui_vector_sink_f_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.blocks_multiply_const_vxx_0_2, 0))
        self.connect((self.blocks_stream_to_vector_0_3, 0), (self.blocks_multiply_const_vxx_0_2_0, 0))
        self.connect((self.blocks_stream_to_vector_0_5, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))
        self.connect((self.blocks_stream_to_vector_0_5_0, 0), (self.blocks_multiply_const_vxx_0_2_0_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_complex_to_mag_squared_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Hydrogen_Flowgraph")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_vec_length(self):
        return self.vec_length

    def set_vec_length(self, vec_length):
        self.vec_length = vec_length
        self.set_custom_window(self.sinc*np.hamming(4*self.vec_length))
        self.set_sinc_sample_locations(np.arange(-np.pi*4/2.0, np.pi*4/2.0, np.pi/self.vec_length))
        self.blocks_delay_0.set_dly(int((3*self.vec_length)))
        self.blocks_delay_0_0.set_dly(int(self.vec_length))
        self.blocks_delay_0_1.set_dly(int((2*self.vec_length)))
        self.blocks_multiply_const_vxx_0_0_0.set_k(self.custom_window[2*self.vec_length:3*self.vec_length])
        self.blocks_multiply_const_vxx_0_2.set_k(self.custom_window[-self.vec_length:])
        self.blocks_multiply_const_vxx_0_2_0.set_k(self.custom_window[0:self.vec_length])
        self.blocks_multiply_const_vxx_0_2_0_0.set_k(self.custom_window[0:self.vec_length])
        self.qtgui_vector_sink_f_0.set_x_axis(((self.center_freq-(self.samp_rate/2))/1e6), ((self.samp_rate/self.vec_length)/1e6))

    def get_sinc_sample_locations(self):
        return self.sinc_sample_locations

    def set_sinc_sample_locations(self, sinc_sample_locations):
        self.sinc_sample_locations = sinc_sample_locations
        self.set_sinc(np.sinc(self.sinc_sample_locations/np.pi))

    def get_sinc(self):
        return self.sinc

    def set_sinc(self, sinc):
        self.sinc = sinc
        self.set_custom_window(self.sinc*np.hamming(4*self.vec_length))
        self.set_sinc(np.sinc(self.sinc_sample_locations/np.pi))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_file(str(self.rfgain)+'_'+str(self.ifgain)+'_'+str(self.bbgain)+'G'+str(self.samp_rate/10e5)+'MHz.dat')
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate)
        self.qtgui_vector_sink_f_0.set_x_axis(((self.center_freq-(self.samp_rate/2))/1e6), ((self.samp_rate/self.vec_length)/1e6))

    def get_rfgain(self):
        return self.rfgain

    def set_rfgain(self, rfgain):
        self.rfgain = rfgain
        self.set_file(str(self.rfgain)+'_'+str(self.ifgain)+'_'+str(self.bbgain)+'G'+str(self.samp_rate/10e5)+'MHz.dat')

    def get_ifgain(self):
        return self.ifgain

    def set_ifgain(self, ifgain):
        self.ifgain = ifgain
        self.set_file(str(self.rfgain)+'_'+str(self.ifgain)+'_'+str(self.bbgain)+'G'+str(self.samp_rate/10e5)+'MHz.dat')

    def get_bbgain(self):
        return self.bbgain

    def set_bbgain(self, bbgain):
        self.bbgain = bbgain
        self.set_file(str(self.rfgain)+'_'+str(self.ifgain)+'_'+str(self.bbgain)+'G'+str(self.samp_rate/10e5)+'MHz.dat')

    def get_timenow(self):
        return self.timenow

    def set_timenow(self, timenow):
        self.timenow = timenow

    def get_restFreq(self):
        return self.restFreq

    def set_restFreq(self, restFreq):
        self.restFreq = restFreq

    def get_receiver(self):
        return self.receiver

    def set_receiver(self, receiver):
        self.receiver = receiver

    def get_output_filename(self):
        return self.output_filename

    def set_output_filename(self, output_filename):
        self.output_filename = output_filename

    def get_observationType(self):
        return self.observationType

    def set_observationType(self, observationType):
        self.observationType = observationType

    def get_observationRA(self):
        return self.observationRA

    def set_observationRA(self, observationRA):
        self.observationRA = observationRA

    def get_observationObject(self):
        return self.observationObject

    def set_observationObject(self, observationObject):
        self.observationObject = observationObject

    def get_observationDec(self):
        return self.observationDec

    def set_observationDec(self, observationDec):
        self.observationDec = observationDec

    def get_intermediate_rate(self):
        return self.intermediate_rate

    def set_intermediate_rate(self, intermediate_rate):
        self.intermediate_rate = intermediate_rate

    def get_integrationTimeShort(self):
        return self.integrationTimeShort

    def set_integrationTimeShort(self, integrationTimeShort):
        self.integrationTimeShort = integrationTimeShort

    def get_integrationTimeLong(self):
        return self.integrationTimeLong

    def set_integrationTimeLong(self, integrationTimeLong):
        self.integrationTimeLong = integrationTimeLong

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq

    def get_file_rate(self):
        return self.file_rate

    def set_file_rate(self, file_rate):
        self.file_rate = file_rate

    def get_file(self):
        return self.file

    def set_file(self, file):
        self.file = file

    def get_dire(self):
        return self.dire

    def set_dire(self, dire):
        self.dire = dire

    def get_dc_gain(self):
        return self.dc_gain

    def set_dc_gain(self, dc_gain):
        self.dc_gain = dc_gain
        Qt.QMetaObject.invokeMethod(self._dc_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.dc_gain)))

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_custom_window(self):
        return self.custom_window

    def set_custom_window(self, custom_window):
        self.custom_window = custom_window
        self.blocks_multiply_const_vxx_0_0_0.set_k(self.custom_window[2*self.vec_length:3*self.vec_length])
        self.blocks_multiply_const_vxx_0_2.set_k(self.custom_window[-self.vec_length:])
        self.blocks_multiply_const_vxx_0_2_0.set_k(self.custom_window[0:self.vec_length])
        self.blocks_multiply_const_vxx_0_2_0_0.set_k(self.custom_window[0:self.vec_length])

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.qtgui_freq_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate)
        self.qtgui_vector_sink_f_0.set_x_axis(((self.center_freq-(self.samp_rate/2))/1e6), ((self.samp_rate/self.vec_length)/1e6))

    def get_T_hot(self):
        return self.T_hot

    def set_T_hot(self, T_hot):
        self.T_hot = T_hot

    def get_T_cold(self):
        return self.T_cold

    def set_T_cold(self, T_cold):
        self.T_cold = T_cold

    def get_P_hot(self):
        return self.P_hot

    def set_P_hot(self, P_hot):
        self.P_hot = P_hot
        Qt.QMetaObject.invokeMethod(self._P_hot_line_edit, "setText", Qt.Q_ARG("QString", str(self.P_hot)))

    def get_P_cold(self):
        return self.P_cold

    def set_P_cold(self, P_cold):
        self.P_cold = P_cold
        Qt.QMetaObject.invokeMethod(self._P_cold_line_edit, "setText", Qt.Q_ARG("QString", str(self.P_cold)))




def main(top_block_cls=Hydrogen_Flowgraph, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
