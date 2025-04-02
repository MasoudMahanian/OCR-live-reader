<!DOCTYPE html>
<html lang="en">
<body>

  <h1> OCR Live Reader</h1>
  <p><strong>Description:</strong> Real-time OCR and text-to-speech using webcam, EasyOCR, and OpenCV.</p>

  <h2> Features</h2>
  <ul>
    <li>Live webcam feed with a selected region for OCR</li>
    <li>Adjustable region for fine-tuned OCR results</li>
    <li>Text detection using EasyOCR</li>
    <li>Optional saving of the current frame and OCR image</li>
    <li>Text-to-speech support using pyttsx3</li>
    <li>Keyboard shortcuts for full control</li>
  </ul>

  <h2> Dependencies</h2>
  <p>Install required packages using pip:</p>
  <pre><code>pip install opencv-python easyocr numpy pyttsx3</code></pre>

  <h2> How to Run</h2>
  <p>Run the script using the command:</p>
  <pre><code>python main.py</code></pre>

  <h2> Keyboard Controls</h2>
  <ul>
    <li><code>o</code>: Run OCR on the selected region</li>
    <li><code>p</code>: Read the detected text aloud</li>
    <li><code>c</code>: Clear detected text and results</li>
    <li><code>s</code>: Save the current camera and OCR frame</li>
    <li><code>h</code> / <code>H</code>: Decrease/Increase ROI height</li>
    <li><code>j</code> / <code>J</code>: Decrease/Increase ROI width</li>
    <li><code>q</code>: Quit the application</li>
  </ul>

  <h2> OCR Region</h2>
  <p>The OCR is run on a central rectangular region of the webcam feed, which can be resized using keyboard controls.</p>

  <h2> Text-to-Speech</h2>
  <p>After performing OCR, press <code>p</code> to use <code>pyttsx3</code> to read the detected text aloud.</p>

  <p><strong>Note:</strong> GPU acceleration is enabled for EasyOCR by default. You can change <code>gpu=True</code> to <code>gpu=False</code> in the script if needed.</p>

<h1> OCR on Single Captured Frame (Notebook)</h1>
<p>
  This script captures a single frame from the webcam and applies multiple preprocessing techniques to enhance OCR results using EasyOCR.
</p>

<h3> What It Does:</h3>
<ol>
  <li>Captures one image from the webcam.</li>
  <li>Saves the image as <code>captured_image.jpg</code>.</li>
  <li>Displays the original image using <code>matplotlib</code>.</li>
  <li>Applies three preprocessing methods:
    <ul>
      <li><strong>Brightness/Contrast adjustment</strong></li>
      <li><strong>Histogram Equalization</strong></li>
      <li><strong>Gamma Correction</strong></li>
    </ul>
  </li>
  <li>Runs OCR on:
    <ul>
      <li>The original image</li>
      <li>The histogram-equalized image</li>
      <li>The gamma-corrected image</li>
    </ul>
  </li>
  <li>Draws detected text regions and overlays recognized text on each version.</li>
</ol>

<h3> Purpose:</h3>
<p>
  This script is designed to compare how different image preprocessing methods affect OCR accuracy. It helps determine which technique gives the best recognition results depending on the input lighting or quality.
</p>

<h3> Additional Dependencies:</h3>
<p>
  Besides the core libraries, this script uses <code>matplotlib</code> for image visualization. Install it with:
</p>
<pre><code>pip install matplotlib</code></pre>

</body>
</html>
