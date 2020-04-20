
/**

  Make a circular region of interest and a 2D geolocated array, then
  use STARE SpatialRange to determine what points of the array are in
  the ROI.

   Subsetting: Given a 2D data array, where the level 27 sindex is
   known for each element and a set of sindices that define a ROI,
   return the list of indices in the array that fall within the ROI
   (effectively, this is region intersection). What qualifications
   should be placed on the two sets of indices to improve performance?

 */
#include <iostream>
#include <STARE.h>
#include <SpatialRange.h>

using namespace std;

int main(int argc, char *argv[]) {

  STARE stare;

  // Make a region of interest. At thiks writing, a 0.5 degree circle centered at the origin.
  float64
    latDegrees      = 0.0
    ,lonDegrees     = 0.0
    ,radius_degrees = 0.5
    ;
  int force_resolution_level = 10; // 10km neighborhood
  STARE_SpatialIntervals
    circle_indices = stare.CoverCircleFromLatLonRadiusDegrees(latDegrees,lonDegrees,radius_degrees,force_resolution_level);

  // Make a SpatialRange from the ROI. SpatialRange is based on skip-lists.
  SpatialRange
    circle_range = SpatialRange(circle_indices);

  // Make a couple of points for testing.
  STARE_ArrayIndexSpatialValue
    point_inside   = stare.ValueFromLatLonDegrees(latDegrees,lonDegrees) // default geolocation resolution is level 27.
    ,point_outside = stare.ValueFromLatLonDegrees(latDegrees,lonDegrees+2*radius_degrees) // default geolocation resolution is level 27.
    ;


  // Be a little silly -- just realized we don't have a contains(vector) method in SpatialRange.
  STARE_SpatialIntervals intervals;
  intervals.push_back(point_inside); intervals.push_back(point_outside);

  // Check
  cout << "Check points." << endl << flush;
  for( int i=0; i < intervals.size(); ++i ) {
    cout << i << " i,inside? " << circle_range.contains(intervals[i]) << endl << flush;
  }

  // Now set up a geolocated data array. Data array not shown as not needed here.
  int
    n0  =  8
    ,n1 = 12;

  vector<STARE_ArrayIndexSpatialValues> index_rows(n0, STARE_ArrayIndexSpatialValues(n1));

  float64
    delta = 0.1,lons[n0][n1],lats[n0][n1];

  // Initialize geolocated arrays. This is an 8x12 set of points with spacings of 0.1 degrees, left corner at origin.
  for( int i0 = 0; i0<n0; ++i0 ) {
    float64 lon = i0*delta;
    for( int i1 = 0; i1<n1; ++i1 ) {
      float64 lat = i1*delta;
      lons[i0][i1] = lon;
      lats[i0][i1] = lat;
      // indices[i0*n1+n1] = stare.ValueFromLatLonDegrees(lat,lon);
      index_rows[i0][i1]  = stare.ValueFromLatLonDegrees(lat,lon); // Geolocations are known to level 27 by default.
    }
    index_rows[i0] = stare.adaptSpatialResolutionEstimates(index_rows[i0]); // Improve for efficiency later. Potentially use pass-by-reference to avoid copy.
  }

  // Figure out what parts of geolocated array are in ROI. Determining index values follows from the following.
  cout << endl << flush;
  cout << "Check our 2D array against the circular region of interest." << endl << flush;
  cout << "^" << endl << "|" << endl << "lat" << endl << flush;
  for( int i1 = n1; i1> -1; --i1 ) {
    // float64 lat = i1*delta;
    for( int i0 = 0; i0<n0; ++i0 ) {
      // float64 lon = i0*delta;
      if( circle_range.contains(index_rows[i0][i1]) ) {  // Note: at this writing we don't have a vector<bool> = SpatialRange.contains(indicies) functions.
	cout << "*" << flush;
      } else {
	cout << "." << flush;
      }
    }
    cout << endl << flush;
  }
  cout << "lon -->" << endl << flush;
  cout << endl << flush;

  cout << "02-Subsetting-2DArray.cpp done" << endl << flush;

}
