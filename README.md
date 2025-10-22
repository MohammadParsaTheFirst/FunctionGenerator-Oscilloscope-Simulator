# Electrical Circuits Software Simulator

## Overview
This project is a Python-based simulation of essential electrical engineering lab tools: a Function Generator and an Oscilloscope. Developed as part of the Electrical Circuits course at Sharif University of Technology, it allows users to generate various waveforms (sine, square, triangular) and visualize them in real-time, mimicking hardware behavior. The application features an intuitive GUI built with PyQt5, enabling interactive control over frequency, amplitude, and waveform type.
The core goal is to design and test circuits virtually by generating test signals and analyzing outputs, bridging theoretical circuit design with practical signal processing.


## Key Concepts
- Function Generator: Produces repetitive or single-shot waveforms (e.g., sine, square, triangular, sawtooth) across a wide frequency range.
- Oscilloscope: Displays voltage signals as time-based graphs, measuring properties like amplitude, frequency, rise time, and distortion.


## Features
- Waveform Generation: Select and generate sine, square, or triangular waves.
- Frequency Control: Adjustable frequencies (1 Hz to 100 kHz) via buttons or dials.
- Amplitude Adjustment: Fine-tune signal amplitude.
- Real-Time Visualization: Oscilloscope view updates dynamically with generated signals.
- User-Friendly GUI: Welcome screen with project info, transitioning to a dual-panel interface for generator and scope controls.
- DC Offset Support: Add offsets to waveforms for advanced testing.

## Technologies Used
- Python 3.9: Core programming language.-
- PyQt5: For cross-platform GUI development (designed with Qt Designer).
- Libraries: QtCore, QtGui, QtWidgets for UI components; potential integration with NumPy/Matplotlib for signal processing (extendable).


## Usage
- Run the Application:
```
python main.py
```
This launches the welcome screen. Click Start to enter the main interface.

- Function Generator Controls:

Select waveform: Click sine, square, or triangular buttons.
Set frequency: Use buttons (1 Hz, 10 Hz, ..., 100 kHz) or dial.
Adjust amplitude: Rotate the amplitude dial.
Apply DC offset: Use the offset dial.


- Oscilloscope View:

Displays the generated waveform in real-time.
Channels: View Channel 1 (default) with vertical/horizontal positioning controls.
Trigger: Auto-trigger on waveform edges.


##Code Structure
- `welcome-page-gui.py`: Auto-generated UI for the splash screen.
- `App.py`: Main devices interface (generator + oscilloscope).
- `main.py`: Entry point to launch the app (integrates both UIs).
- UI files: Generated from .ui files via pyuic5 (do not edit manually).
