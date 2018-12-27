# python-piano
A simple piano made with python and love. It has no GUI.

## Getting Started

### Prerequisites

What things you need to install the software and how to install them

* [Python3](https://www.python.org/)
* [PortAudio](http://www.portaudio.com/)
* [Pynput](https://pypi.org/project/pynput/)
* [PyAudio](https://pypi.org/project/PyAudio/)

### Installing

- On Windows  
[Download](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) the proper PyAudio whl file

```
pip install <downloaded_file>.whl
```

- On Ubuntu 

1. Uninstall python-pyaudio with sudo ```apt-get purge --remove python-pyaudio``` if you have it (This is version 0.2.8)
2. [Download](http://www.portaudio.com/download.html) the latest version (19) of PortAudio.
3. Untar(```tar -xzvf <downloaded_file>.tgz```) and install PortAudio
    ```
    ./configure
    make
    make install
    ```
4. Get the dependencies for pyaudio (can be via apt-get)
    portaudio19-dev
    python-all-dev (python3-all-dev for Python 3)
5. ```sudo pip install pyaudio```

[Source](https://stackoverflow.com/questions/36681836/pyaudio-could-not-import-portaudio)

## Running

```python main.py```

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Eduardo Moura** - *Initial work* - [eduardosm7](https://github.com/eduardosm7)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [eyksun](https://mail.python.org/pipermail/tutor/2012-September/091476.html)

