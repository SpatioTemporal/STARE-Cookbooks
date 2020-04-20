
/**

   Make a circular region of interest and two points, one inside, and
   another out, and then use STARE SpatialRange to determine whether
   the region of interest contains each point.

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

  float64
    latDegrees      = 0.0
    ,lonDegrees     = 0.0
    ,radius_degrees = 0.5
    ;
  int force_resolution_level = 10; // 10km neighborhood
  
  STARE_SpatialIntervals
    circle_indices = stare.CoverCircleFromLatLonRadiusDegrees(latDegrees,lonDegrees,radius_degrees,force_resolution_level);

  SpatialRange
    circle_range = SpatialRange(circle_indices);

  STARE_ArrayIndexSpatialValue
    point_inside   = stare.ValueFromLatLonDegrees(latDegrees,lonDegrees) // default geolocation resolution is level 27.
    ,point_outside = stare.ValueFromLatLonDegrees(latDegrees,lonDegrees+2*radius_degrees) // default geolocation resolution is level 27.
    ;

  int
    n0  =  8
    ,n1 = 12;

  float64
    delta = 0.1,lons[n0][n1],lats[n0][n1];

  vector<STARE_ArrayIndexSpatialValues> index_rows(n0, STARE_ArrayIndexSpatialValues(n1));

  for( int i0 = 0; i0<n0; ++i0 ) {
    float64 lon = i0*delta;
    for( int i1 = 0; i1<n1; ++i1 ) {
      float64 lat = i1*delta;
      lons[i0][i1] = lon;
      lats[i0][i1] = lat;
      // indices[i0*n1+n1] = stare.ValueFromLatLonDegrees(lat,lon);
      index_rows[i0][i1]  = stare.ValueFromLatLonDegrees(lat,lon);
    }
    index_rows[i0] = stare.adaptSpatialResolutionEstimates(index_rows[i0]); // Improve for efficiency later.
  }

  STARE_SpatialIntervals intervals;
  intervals.push_back(point_inside); intervals.push_back(point_outside);

  cout << "Check points." << endl << flush;
  for( int i=0; i < intervals.size(); ++i ) {
    cout << i << " i,inside? " << circle_range.contains(intervals[i]) << endl << flush;
  }

  cout << endl << flush;
  cout << "Check our 2D array against the circular region of interest." << endl << flush;
  cout << "^" << endl << "|" << endl << "lat" << endl << flush;
  for( int i1 = n1; i1> -1; --i1 ) {
    // float64 lat = i1*delta;
    for( int i0 = 0; i0<n0; ++i0 ) {
      // float64 lon = i0*delta;
      if( circle_range.contains(index_rows[i0][i1]) ) {
	cout << "*" << flush;
      } else {
	cout << "." << flush;
      }
    }
    cout << endl << flush;
  }
  cout << "lon -->" << endl << flush;

  cout << "02-Subsetting-2DArray.cpp done" << endl << flush;

}
