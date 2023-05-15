# apessq2m_pcp
(Experimental) expose more ES90X8 DAC function in a friendly way within picorePlayer webgui

This is a tiny picorePlayer extension that adds a configuration page in the WebGUI to expose additionnal hardware DAC functions (namely to allow toggling between the I2S and SPDIF inputs).
It does not override any pcp file and only executes a couple alsa functions so it should be safe to run on any hardware using Audiophonics I-Sabre Q2M Driver with SPDIF input.

## How to install 
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

