#!/usr/bin/env python

import unittest
import os
import glob

class Tests(unittest.TestCase):
    def test_run(self):
        """Test full run"""
        os.chdir(os.path.join(os.path.dirname(sys.argv[0]), '..'))
        # Test modeling script
        p = subprocess.check_call(['./ms_cg.py'])
        # Make sure models were produced
        num = len(glob.glob('conf_eif3.*.pym'))
        self.assert_(num > 9900, "Only %d models were produced" % num)
        # Make mfj files
        p = subprocess.check_call(['./pym2tcl.py'])
        p = subprocess.check_call(['./tcl2mfj.py'])

if __name__ == '__main__':
    unittest.main()
