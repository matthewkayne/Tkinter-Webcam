<h1 align="center">Tkinter-Webcam</h1>

<p align="center"><a href="https://www.codefactor.io/repository/github/matthewkayne/tkinter-webcam"><img src="https://www.codefactor.io/repository/github/matthewkayne/tkinter-webcam/badge" alt="CodeFactor" /></a> <a href="https://badge.fury.io/py/tkinter-webcam"><img src="https://badge.fury.io/py/tkinter-webcam.svg" alt="PyPI version" height="18"></a></p>

Easily display a webcam window in a Tkinter GUI

## ⚡️ Installation

To install the package use:

```bash
pip install tkinter-webcam
```

To use the package simply import it:

```python
from tkinter_webcam import webcam
```

Then create the `Box` object using any variable name and immediently run the show frames function:

```python
webcam_object = webcam.Box(window, width=450, height=450)
# Uses Box class from webcam to create video window
webcam_object.show_frames()
# Show the created Box
```

Checkout [`example.py`](https://github.com/matthewkayne/Tkinter-Webcam/blob/master/example.py) to see a full script using this object
