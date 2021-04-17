import numpy 
import pystare 
import unittest

intervals_src = [\
 0x2320000000000005,\
 0x2324000000000005,\
 0x2327ffffffffffff,\
 0x3aa0000000000005,\
 0x3aa7ffffffffffff,\
 0x3aa8000000000004,\
 0x3ab2000000000005,\
 0x3ac7ffffffffffff,\
 0x3ad0000000000005,\
 0x3ae7ffffffffffff,\
 0x3af2000000000005,\
 0x3afa000000000005,\
 0x3b40000000000004,\
 0x3b4c000000000005,\
 0x3b52000000000005,\
 0x3b5a000000000005,\
 0x3b5fffffffffffff,\
 0x3b80000000000004,\
 0x3b8a000000000005,\
 0x3b8fffffffffffff,\
 0x3b90000000000004,\
 0x3b9fffffffffffff,\
 0x3bc0000000000005,\
 0x3bc7ffffffffffff,\
 0x3bc8000000000004,\
 0x3bd0000000000005,\
 0x3bdfffffffffffff,\
 0x3be2000000000005,\
 0x3be8000000000004,\
 0x3bf4000000000005,\
 0x3bf8000000000005,\
 0x3bfc000000000005,\
 0x3bffffffffffffff,\
 0x3e40000000000005,\
 0x3e43ffffffffffff,\
 0x3e46000000000005,\
 0x3f20000000000005,\
 0x3f24000000000005,\
 0x3f27ffffffffffff,\
 0x3f32000000000005,\
 0x3f36000000000005,\
 0x3f3a000000000005,\
 0x3fa0000000000005\
]

intervals_expanded_src = [\
 0x2320000000000005 ,\
 0x2324000000000005 ,\
 0x2326000000000005 ,\
 0x3aa0000000000005 ,\
 0x3aa2000000000005 ,\
 0x3aa4000000000005 ,\
 0x3aa6000000000005 ,\
 0x3aa8000000000004 ,\
 0x3ab2000000000005 ,\
 0x3ab4000000000005 ,\
 0x3ab6000000000005 ,\
 0x3ab8000000000005 ,\
 0x3aba000000000005 ,\
 0x3abc000000000005 ,\
 0x3abe000000000005 ,\
 0x3ac0000000000005 ,\
 0x3ac2000000000005 ,\
 0x3ac4000000000005 ,\
 0x3ac6000000000005 ,\
 0x3ad0000000000005 ,\
 0x3ad2000000000005 ,\
 0x3ad4000000000005 ,\
 0x3ad6000000000005 ,\
 0x3ad8000000000005 ,\
 0x3ada000000000005 ,\
 0x3adc000000000005 ,\
 0x3ade000000000005 ,\
 0x3ae0000000000005 ,\
 0x3ae2000000000005 ,\
 0x3ae4000000000005 ,\
 0x3ae6000000000005 ,\
 0x3af2000000000005 ,\
 0x3afa000000000005 ,\
 0x3b40000000000004 ,\
 0x3b4c000000000005 ,\
 0x3b52000000000005 ,\
 0x3b5a000000000005 ,\
 0x3b5c000000000005 ,\
 0x3b5e000000000005 ,\
 0x3b80000000000004 ,\
 0x3b8a000000000005 ,\
 0x3b8c000000000005 ,\
 0x3b8e000000000005 ,\
 0x3b90000000000004 ,\
 0x3b98000000000004 ,\
 0x3bc0000000000005 ,\
 0x3bc2000000000005 ,\
 0x3bc4000000000005 ,\
 0x3bc6000000000005 ,\
 0x3bc8000000000004 ,\
 0x3bd0000000000005 ,\
 0x3bd2000000000005 ,\
 0x3bd4000000000005 ,\
 0x3bd6000000000005 ,\
 0x3bd8000000000005 ,\
 0x3bda000000000005 ,\
 0x3bdc000000000005 ,\
 0x3bde000000000005 ,\
 0x3be2000000000005 ,\
 0x3be8000000000004 ,\
 0x3bf4000000000005 ,\
 0x3bf8000000000005 ,\
 0x3bfc000000000005 ,\
 0x3bfe000000000005 ,\
 0x3e40000000000005 ,\
 0x3e42000000000005 ,\
 0x3e46000000000005 ,\
 0x3f20000000000005 ,\
 0x3f24000000000005 ,\
 0x3f26000000000005 ,\
 0x3f32000000000005 ,\
 0x3f36000000000005 ,\
 0x3f3a000000000005 ,\
 0x3fa0000000000005 \
]
 

class MainTest(unittest.TestCase):
    
    def test_fromlatlon(self):
        lat = numpy.array([30,45,60], dtype=numpy.double)
        lon = numpy.array([45,60,10], dtype=numpy.double)
        indices = pystare.from_latlon(lat, lon, 12)
        expected = numpy.array([4151504989081014892, 4161865161846704588, 3643626718498217164])
        numpy.testing.assert_array_equal(indices, expected)
        
    def test_intervals(self):
        a = numpy.array([0x0000000000000008, 0x000030000000000a, 0x000067ffffffffff, 0x000070000000000a, 0x0000907fffffffff], dtype=numpy.int64)
        starts, ends = pystare.from_intervals(a)
        self.assertEqual(starts[0], 8)
        self.assertEqual(ends[0], 8796093022207)

    def test_tolatlon(self):
        indices = numpy.array([4151504989081014892, 4161865161846704588, 3643626718498217164])
        lat, lon = pystare.to_latlon(indices)
        numpy.testing.assert_allclose(lat, numpy.array([30,45,60]), verbose=True)
        numpy.testing.assert_allclose(lon, numpy.array([45,60,10]), verbose=True)
        
    def test_tolatlonlevel(self):
        indices = numpy.array([4151504989081014892, 4161865161846704588, 3643626718498217164])
        lat, lon, level = pystare.to_latlonlevel(indices)
        numpy.testing.assert_allclose(lat, numpy.array([30,45,60]), verbose=True)
        numpy.testing.assert_allclose(lat, numpy.array([30,45,60]), verbose=True)
        numpy.testing.assert_allclose(level, numpy.array([12,12,12]), verbose=True)
        
    def test_latlonroundtrip(self):
        lat1 = numpy.array([30,45,60], dtype=numpy.double)
        lon1 = numpy.array([45,60,10], dtype=numpy.double)
        level1 = 12
        indices = pystare.from_latlon(lat1, lon1, level1)        
        lat2, lon2, level2 = pystare.to_latlonlevel(indices)
        numpy.testing.assert_allclose(lat1, lat2)
        numpy.testing.assert_allclose(lon1, lon2)
        self.assertEqual(level1, level2[0])
                
    def test_tolevel(self):
        indices = numpy.array([4151504989081014892, 4161865161846704588, 3643626718498217164])
        level = pystare.to_level(indices)
        numpy.testing.assert_array_equal(level, numpy.array([12,12,12]), verbose=True)

    def test_toarea(self):
        indices = numpy.array([4151504989081014892, 4161865161846704588, 3643626718498217164])
        area = pystare.to_area(indices)
        expected = numpy.array([8.66507750e-08, 8.74786654e-08, 7.97819113e-08])        
        numpy.testing.assert_allclose(area, expected)
    
    def test__tocompressedrange(self):
        indices = numpy.array([4151504989081014892, 4161865161846704588, 3643626718498217164])
        compressed = numpy.array([0, 0, 0], dtype=numpy.int64)
        pystare._to_compressed_range(indices, compressed)
        expected = numpy.array([3643626718498217164, 4151504989081014892, 4161865161846704588])
        numpy.testing.assert_array_equal(compressed, expected)
    
    def test_tocompressedrange(self):
        indices = numpy.array([4151504989081014892, 4161865161846704588, 3643626718498217164])
        compressed = pystare.to_compressed_range(indices)
        expected = numpy.array([3643626718498217164, 4151504989081014892, 4161865161846704588])
        numpy.testing.assert_array_equal(compressed, expected)

    def test__tohullrange(self):
        indices = numpy.array([4151504989081014892, 4161865161846704588, 3643626718498217164])
        result_size = numpy.zeros([1], dtype=numpy.int)
        result = pystare._to_hull_range(indices, 8)
        hull_indices = numpy.zeros([result.get_size_as_intervals()], dtype=numpy.int64)
        result.copy_as_intervals(hull_indices)
        self.assertEqual(hull_indices.size, 901)
        
    def test_tohullrange(self):
        indices = numpy.array([4151504989081014892, 4161865161846704588, 3643626718498217164])
        hull_indices = pystare.to_hull_range(indices, 8)
        self.assertEqual(hull_indices.size, 901)
    
    def test__cmpspatial(self):
        indices = numpy.array([4151504989081014892, 4161865161846704588, 3643626718498217164])
        compared = numpy.zeros([9], dtype=numpy.int64)
        pystare._cmp_spatial(indices, indices, compared)
        expected = numpy.array([1, 0, 0, 0, 1, 0, 0, 0, 1])
        numpy.testing.assert_array_equal(compared, expected)
        
    def test_cmpspatial(self):
        indices1 = numpy.array([4151504989081014892, 4161865161846704588, 3643626718498217164])
        indices2 = numpy.zeros([2],dtype=numpy.int64)
        indices2[0] = indices1[1]-2
        indices2[1] = indices1[1]
        compared = pystare.cmp_spatial(indices1 ,indices2)
        expected = numpy.array([ 0,  0, -1,  1,  0,  0])
        numpy.testing.assert_array_equal(compared, expected)
        
    def test__expand(self):
        src                = numpy.array(intervals_src,dtype=numpy.int64)
        expected_expanded  = numpy.array(intervals_expanded_src,dtype=numpy.int64)
        expanded           = numpy.zeros([len(expected_expanded)],dtype=numpy.int64)
        expanded_len       = numpy.zeros([1],dtype=numpy.int64)
        intervals_len = len(src)
        resolution = -1
        result = pystare._expand_intervals(src, resolution)
        expanded_len = result.get_size_as_values()
        result.copy_as_values(expanded)
        self.assertEqual(expanded_len, 74)
        error_found = False
        for i in range(len(expanded)):
            if(expanded[i] != expected_expanded[i]):
                error_found = True    
        self.assertFalse(error_found)
        
    def test_expand(self):
        src = numpy.array(intervals_src,dtype=numpy.int64)
        expected_expanded = numpy.array(intervals_expanded_src,dtype=numpy.int64)
        resolution = -1
        expanded = pystare.expand_intervals(src, resolution)        
        error_found = False
        for i in range(len(expanded)):
            if(expanded[i] != expected_expanded[i]):
                error_found = True
        self.assertFalse(error_found)
  
    def test_cover(self):
        expected = [(0,     4430603050402447369 ),
                    (295,   4430595237856935950 ),
                    (590,   4430626891765907470 ),
                    (885,   4430691958372958222 ),
                    (1180,  4430869121478950926 )]
        cover = pystare.to_circular_cover(1.5,0.5,0.25,14)
        for i in list(expected):
            self.assertEqual(i[1], cover[i[0]])

    def test_spatial_resolution_from_km(self):
        self.assertEqual(10,int(pystare.spatial_resolution_from_km(10)))

    def test_spatial_resolution(self):
        self.assertEqual(11,int(pystare.spatial_resolution(11)))
        self.assertEqual(15,int(pystare.spatial_resolution(15)))
        
