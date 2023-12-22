# LocalMentor

<p align="center">
  <img src="https://github.com/remyxai/LocalMentor/blob/main/assets/dale_the_quail.png" height=400px>
  <br>

Trained on 1000+ hours of tech and startup podcast discussion, LocalMentor is a chatbot startup advisor that runs entirely on your local computer.

## Setup 

### Requirements
* Python 3 

PyPI:
```
pip install localmentor 
```

Or pip install from source:
```
git clone https://github.com/remyxai/LocalMentor.git
cd LocalMentor && pip install .
```

## Quickstart
Ask your startup question:

```bash
localmentor ask --prompt "What are three things to look for when hiring employees at an early stage startup?"
```

## Features

### Python Usage
Simply import the library and pass your command as a string to `mentor`

```python
from localmentor import mentor

mentor("What are three things to look for when hiring employees at an early stage startup?")
```
</p>
