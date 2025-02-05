
# HTTP Image Viewer

A simple python http server for images


## Installation

Install using git (without virtualenv)

```bash
  git clone https://github.com/8harifi/http_image_viewer
  cd http_image_viewer
  pip install -r requirements.txt
```
    
Install using git (with virtualenv)

```bash
  git clone https://github.com/8harifi/http_image_viewer
  cd http_image_viewer
  pip install virtualenv
  virtualenv venv
  source venv/bin/activate
  pip install -r requirements.txt
```

## Usage/Examples

Run Locally:

```bash
uvicorn main:app --reload
```


## Optimizations

On-the-fly Image Resizing: Instead of storing multiple versions of the same image, the server generates resized images dynamically based on request parameters, reducing storage usage and download time.

## Image Resizing

One of the key features of this server is the ability to resize images dynamically by specifying the desired dimensions in the URL.

Example usage:
```bash
http://localhost:8000/images/test_1.png?width=300&height=200
```

## License

MIT License

Copyright (c) 2025 m sharifi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

