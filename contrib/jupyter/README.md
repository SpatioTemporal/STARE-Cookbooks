
# README contrib/jupyter

Jupyter Notebooks showing various STARE functions.

Please make requests for examples through the "Issues" mechanism.

## Examples

Examples require STARE version >= 0.14.2 and pystare version > 0.3.6.

### [00-HelloEarth.ipynb](00-HelloEarth.ipynb)

Import pystare and demonstrate STARE spatial index values by plotting
a few spatial elements (trixels) at the root resolution
(quadfurcation-level QL-0) and one step finer (QL-1).

### [01-GeoLocation.ipynb](01-GeoLocation.ipynb)

Show the basics of geolocation and neighborhoods using STARE by
encoding a longitude-latitude floating point location with
neighborhoods of various length scales. The difference between
geolocation bits vs. neighborhood resolution bits is introduced.

### [02-SpatialIntervals.ipynb](02-SpatialIntervals.ipynb)

Contiguous sequences of STARE indices may be replaced by intervals
denoted by their lower and upper bounds. STARE upper bounds are called
terminators and are greater than any possible index value within the
interval. Expanding intervals into and finding longitude-latitude
information from index values is introduced.

# Acknowledgments

2018-2020 Development supported by NASA/ACCESS-17 Grant 80NSSC18M0118.

Michael Rilee
mike@rilee.net


