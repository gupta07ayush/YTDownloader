## Describe the bug:
When trying to access the title of a specific video, the error "Exception while accessing title" raises up.
The error doesn't come every time I run the code. It comes 5 out of 10 times.
Otherwise I get the desired output.

## To Reproduce:

Use the url "https://youtube.com/shorts/pVMldM3PF-o?feature=share" for this test
Create a YouTube object with this url
Try to retrieve the title of the video

## Expected behavior:
Most Satisfying Funny Cat Video 😂😂😂  #shorts

## Output:
Traceback (most recent call last):
  File "C:\Users\gupta\AppData\Local\Programs\Python\Py    
  raise exceptions.PytubeError(pytube.exceptions.PytubeError: Exception while accessing title of https://youtube.com/watch?v=pVMldM3PF-o. 
  Please file a bug report at https://github.com/pytube/pytube

## System information:

Python version: 3.11.2
Pytube version: 12.1.3
IDE: Visual Studio Code 1.77.3
pip is used to install: pip install pytube