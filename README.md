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

Troubleshouting
---------------

If pairing fails: Unable to retrieve local bd_addr from `hcitool dev`.

Is the USB interface up and running?

    sudo hciconfig hci0 
    hci0:	Type: BR/EDR  Bus: USB
	    BD Address: 00:02:72:CD:4E:2F  ACL MTU: 1021:8  SCO MTU: 64:1
	    DOWN 
	    RX bytes:547 acl:0 sco:0 events:27 errors:0
	    TX bytes:384 acl:0 sco:0 commands:27 errors:0

If Down:

    sudo hciconfig hci0 up
    sudo hciconfig hci0 
    hci0:	Type: BR/EDR  Bus: USB
	    BD Address: 00:02:72:CD:4E:2F  ACL MTU: 1021:8  SCO MTU: 64:1
	    UP RUNNING 
	    RX bytes:1094 acl:0 sco:0 events:54 errors:0
	    TX bytes:768 acl:0 sco:0 commands:54 errors:0
