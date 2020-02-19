# PythonUtility

## Setup

Install project dependencies:

```sh
script/setup.sh
```

Install pip package from GitHub:

```sh
pip3 install git+https://git@github.com/FunTimeCoding/python-utility.git#egg=python-utility
```

Install pip package from DevPi:

```sh
pip3 install -i https://testpypi.python.org/pypi python-utility
```

Uninstall package:

```sh
pip3 uninstall python-utility
```


## Usage

Run the main program:

```sh
bin/pu
```

Run the main program inside the container:

```sh
docker run -it --rm funtimecoding/python-utility
```


## Development

Configure Git on Windows before cloning:

```sh
git config --global core.autocrlf input
```

Install NFS plugin for Vagrant on Windows:

```bat
vagrant plugin install vagrant-winnfsd
```

Create the development virtual machine on Linux and Darwin:

```sh
script/vagrant/create.sh
```

Create the development virtual machine on Windows:

```bat
script\vagrant\create.bat
```

Run tests, style check and metrics:

```sh
script/test.sh [--help]
script/check.sh [--help]
script/measure.sh [--help]
```

Build project:

```sh
script/build.sh
```

Install Debian package:

```sh
sudo dpkg --install build/python3-python-utility_0.1.0-1_all.deb
```

Show files the package installed:

```sh
dpkg-query --listfiles python-utility
```
