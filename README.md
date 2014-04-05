shakeNbake
==========

Requirements
------------

    sudo apt-get install libusb-dev bluetooth blueman bluez-tools bluez-hcidump python-bluez bluez python-audioread

You will also need Qtsixa and the Soundcloud python API

* http://qtsixa.sourceforge.net/
* https://github.com/soundcloud/soundcloud-python

Get it!
-------

    git clone --recursive https://github.com/sovannara-hak/shakeNbake.git
    cd shakeNbake
    python setup.py [develop|install] --prefix=/valid/python/path

Setup bluetooth for Belkin F8T065BF dongle
------------------------------------------

    sudo modprobe btusb
    sudo -s
    sudo echo "050d 065a" >> /sys/bus/usb/drivers/btusb/new_id

You will need to replace the "050d 065a" by the value displayed in

    lsusb|grep Belkin

Pairing the sixaxis with the computer
-------------------------------------

Plug your sixaxis to your computer with the usb cable

    cd pair
    gcc -o sixpair sixpair.c -lusb
    sudo ./sixpair

Unplug the usb cable

Connect Sixaxis to the computer through bluetooth
-------------------------------------------------

    sixad -s

Press PS button to connect

shakeNbake
----------

In another terminal

    cd test
    python test_sixaxis.py
