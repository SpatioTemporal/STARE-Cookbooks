
# README contrib/jupyter

Jupyter Notebooks showing various STARE functions.

Please make requests for examples through the "Issues" mechanism.

## Examples

Examples require STARE version >= 0.15.5 and pystare version >= 0.5.3

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

Show examples of convex_hull and non-convex hulls via from_polygon to
index regions marked by a coastline. The hulls bound covers which can
be used for intersections and search queries. Also show how readily
STARE works with Geopandas by showing the non-convex hull of Canada.

### [06-SanJoaquin.ipynb](06-SanJoaquin.ipynb)

Use Geopandas to input & output the San Joaquin watershed.

### [07-MODIS+Africa.ipynb](07-MODIS+Africa.ipynb)

Use Geopandas and pyhdf to load data from a MODIS swath and overlay
on Africa via STARE.

### [STARE-based Integrative Analysis Demonstration](2020-ACM-SIGSPATIAL20-STARE+Dask-Demo.ipynb)

The new STAREPandas interface is a central component of a fairly
complete example presenting the basics of how STARE spatial indexing
can be used to harmonize data for integrative analysis. Various
aspects of the common problem of searching for and subsetting Earth
Science data in a region of interest are discussed.

Of particular note is how little code an end-user must generate to
achieve very interesting search and subsetting capabilities. Also
demonstrated is one of the first uses of NASA's [Science Managed Cloud
Environment](https://www.nccs.nasa.gov/systems/SMCE) to perform this
processing in the cloud on Earth Science data (ESD) stored in the cloud,
pointing the way towards scaling up to support both the variety and
volume of ESD.

Supporting code for Michael Rilee, Niklas Griessbaum, Kwo-Sen Kuo, James Frew, and Robert Wolfe. 2020. _STARE-based Integrative Analysis of Diverse Data Using Dask Parallel Programming Demo Paper_. In Proceedings of ACM SIGSPATIAL conference (SIGSPATIAL’20). ACM, New York, NY, USA, 4 pages. https://doi.org/10.1145/3397536.3422346

# Acknowledgments

2018-2020 Development supported by NASA/ACCESS-17 Grant 80NSSC18M0118.

Michael Rilee
mike@rilee.net


