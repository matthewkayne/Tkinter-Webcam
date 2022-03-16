# Tkinter-Webcam

[![PyPI version](https://badge.fury.io/py/tkinter-webcam.svg)](https://badge.fury.io/py/tkinter-webcam)

Easily display a webcam window in a Tkinter GUI

To use the package simply import it:

```python
from tkinter_webcam import webcam
```

Then create the `Box` object using any variable name and immediently run the show frames function:

```python
webcamObject = webcam.Box(window, 450, 450)
# Uses Box class from webcam to create video window
webcamObject.show_frames()
# Show the created Box
```

Checkout [`example.py`](https://github.com/matthewkayne/Tkinter-Webcam/blob/master/example.py) to see a full script using this object
