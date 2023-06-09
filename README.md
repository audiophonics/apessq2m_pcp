# apessq2m_pcp
(Experimental) expose more ES90X8 DAC function in a friendly way within piCorePlayer webgui

![illustration_ap](https://github.com/audiophonics/apessq2m_pcp/assets/17196909/4ea62d0b-8519-4046-8aac-db150de9dbf4)

This is a tiny piCorePlayer extension that adds a configuration page in the WebGUI to expose additionnal hardware DAC functions (namely to allow toggling between the I2S and SPDIF inputs).
It does not override any pcp file and only executes a couple alsa functions so it should be safe to run on any hardware using Audiophonics I-Sabre Q2M Driver with SPDIF input.


## How to install 

Connect to piCorePlayer with SSH and execute the following : 

```shell
mkdir -p /tmp/install_apessq2m
cd /tmp/install_apessq2m
wget https://github.com/audiophonics/apessq2m_pcp/archive/main.tar.gz
tar -xvzf main.tar.gz
cd apessq2m_pcp-main
grep -qxF 'apessq2m_pcp.tcz' /etc/sysconfig/tcedir/onboot.lst || echo apessq2m_pcp.tcz >> /etc/sysconfig/tcedir/onboot.lst
mv -f apessq2m_pcp.tcz /etc/sysconfig/tcedir/optional
tce-load -li apessq2m_pcp.tcz
pcp bu 
cd ~
rm -rf /tmp/install_apessq2m

```

## How to use
Once installed, a new configuration page becomes available in http://pcp/cgi-bin/apessq2m.cgi (replace ```pcp``` with your local IP address if your client device does not support local DNS resolution)

If you did not configure the DAC output in http://pcp/cgi-bin/squeezelite.cgi so pcp will use the **Audiophonics ISabre Q2M**, you will get the following error : ```[ ERROR ] I-Sabre Q2M DAC not detected...```. Do this configuration, reboot and it should be working as expected.

## Tested on : 
picorePlayer 8.2.0
