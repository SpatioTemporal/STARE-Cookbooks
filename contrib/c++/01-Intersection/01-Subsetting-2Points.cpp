
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

  STARE_SpatialIntervals intervals;
  intervals.push_back(point_inside); intervals.push_back(point_outside);

  for( int i=0; i < intervals.size(); ++i ) {
    cout << i << " i,inside? " << circle_range.contains(intervals[i]) << endl << flush;
  }
  
  cout << "01-Subsetting-2Points.cpp done" << endl << flush;

}
