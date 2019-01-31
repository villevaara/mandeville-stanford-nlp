# Stanford Core NLP for Mandeville's Fable of the Bees amnogs other texts

Check [The Core NLP demo](http://corenlp.run/) for reference on output.

## Installation

I'm using this wrapper: [https://github.com/Lynten/stanford-corenlp](https://github.com/Lynten/stanford-corenlp). Stanford CORE NLP needs to be installed and present. `nlp_path` -variable has to point to it in the .py file (see below).

Create a virtual environment, run with Python 3.6. 

Use pip to install the package:

```
pip install stanfordcorenlp
```

All the required (and then some) packages are listed in [requirements.txt](./requirements.txt). 

## Running

Run `main.sh`. To change the annotators used, adjust the 'annotators' key in `props` -variable.

## Input

Input is plain txt. Change the input path variable in `main.py`.

## Output

Output is JSON. Change the variable in the above .py file.
