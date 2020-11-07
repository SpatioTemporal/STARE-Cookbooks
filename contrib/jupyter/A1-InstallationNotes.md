
# Notes to help installation

The following may help getting things running, at least before we get STARE tools into Conda Forge, etc.

## MacOS, homebrew, mini-conda installation (Thanks to M. Bauer.)

So I installed STARE, pystare on my mac (10.15.7) running the mini-conda version of anaconda (4.9.0, python 3.8.3). I had to do the following to get things up and running.

1) For some reason, my Homebrew setup didn't have cmake
<pre>
    brew install cmake
</pre>

2) In the STARE directory built by the github clone.

<pre>
conda activate base
mkdir build; cd build
cmake ..
make
make test
make install
</pre>

3) Modify my .bashrc

<pre>
export STARE_INCLUDE_DIR=/usr/local/include/STARE.h
export STARE_LIB_DIR=/usr/local/lib/libSTARE.a
</pre>


4) In the pystare directory built by the github clone.

<pre>
conda install -c anaconda swig  
python setup.py build_ext --inplace
python setup.py test
</pre>

5) Modify my .bashrc

<pre>
export PYTHONPATH=${PYTHONPATH}:/Users/mbauer/pystare/:/Users/mbauer/pystareplotlib/:/Users/mbauer/STARE-Cookbooks/contrib/jupyter/:
</pre>

## MacOS, Anaconda 3, Conda Forge. (Contact mike@rilee.net)


