speakly
=====================

Just a fun project that uses a large number of technologies to achieve simple things.



Install
=====================

Don't forget to download the submodules to get the whole project. You have two options for doing that:

```
$ git clone https://github.com/amateescu/speakly.git speakly
$ cd speakly
$ git submodule update --init
```

Or

```
$ git clone https://github.com/amateescu/speakly.git speakly --recursive
```

Packages needed
=====================

PHP
sudo apt-get install libzmq-dev php-pear php5-dev
sudo pear channel-discover pear.zero.mq
sudo pecl install pear.zero.mq/zmq-beta

Python
sudo apt-get install libzmq-dev python-zmq
