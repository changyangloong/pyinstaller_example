# pyinstaller_example
 Demonstration of pyinstaller usage

## Pre-requisite (tested version)
Make sure these 2 package are in system
Python >= 3.6.8 
Virtualenv >= 20.0.27

## Create a virtualenv
```bash
virtualenv path\to\desired\location\envname --python=python3.6
```

## Activate the env
```bash
path\to\desired\location\envname\Scripts\activate
```

You should able able to see 
```bash
(envname) C:\Users\username\some\directory\you\run\from
```

## Install packages for pyinstaller (and package for testing)
```bash
pip install pyinstaller
pip install numpy
```

## Generate/Convert main.py to executable
```bash
pyinstaller main.py --onefile
```
or
```bash
pyinstaller main.py --onedir
```

--onefile will generate a single exe contain all required package while --onedir will split them to files, the exe is locate in dist folder.

## Running the example
In the example, main.py (provided in the repo), no GUI is created, just simple bash program, so we had to run on cmd to observe the output, else, the program will not be visible.  
The program will work even outside of the virtualenv
Locate the exe,
```bash
## for --onedir example
dist\main\main.exe
```

Should output some default sorting operation. 
```
before:[4.0, 6.0, 2.0, 7.0]
after:[2. 4. 6. 7.]
```

In order to pass argument,
```bash
# for --onedir example
dist\main\main.exe --number_to_sort 100 20 101 3
```
Should output,
```
before:[100.0, 20.0, 101.0, 3.0]
after:[  3.  20. 100. 101.]
```

