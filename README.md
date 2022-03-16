# Tkinter-Webcam

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

Checkout `example.py` to see a full script using this object
