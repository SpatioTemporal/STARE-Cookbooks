
# README contrib/jupyter

Jupyter Notebooks showing various STARE functions.

Please make requests for examples through the "Issues" mechanism.

## Examples

Examples require STARE version >= 0.14.2 and pystare version > 0.3.8.

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

### [03-SpatialRange.ipynb](03-SpatialRange.ipynb)

Nearly every analysis requires the ability to specify and work with
regions of interest. The notion of a *cover* is introduced, which is a
set of index values or intervals associated with an area covering a
region of interest. Covers may be stored in spatial ranges which are
sets of STARE spatial intervals stored as a skip-list for efficient
querying. A simple pair of covers is constructed and their
intersection is found using spatial ranges (srange).


### [04-Contains.ipynb](04-Contains.ipynb)

Examine pystare's cmp_spatial(a,b) which provides a *contains*
function. The function forms an exterior product a.contains.b. The
simplest usage is when either a or b is a single element array. Also
introduce the use of STARE index values as keys in a python
dictionary.

### [05-HullsAndGrids.ipynb](05-HullsAndGrids.ipynb)

Show an example of convex_hull via from_polygon to index regions marked by a coastline.


# Acknowledgments

2018-2020 Development supported by NASA/ACCESS-17 Grant 80NSSC18M0118.

Michael Rilee
mike@rilee.net


