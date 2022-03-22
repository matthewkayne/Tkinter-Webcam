# Tkinter-Webcam

[![CodeFactor](https://www.codefactor.io/repository/github/matthewkayne/tkinter-webcam/badge)](https://www.codefactor.io/repository/github/matthewkayne/tkinter-webcam) [![PyPI version](https://badge.fury.io/py/tkinter-webcam.svg)](https://badge.fury.io/py/tkinter-webcam)

Easily display a webcam window in a Tkinter GUI

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
