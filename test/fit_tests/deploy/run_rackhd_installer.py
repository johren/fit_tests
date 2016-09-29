'''
Copyright 2015, EMC, Inc.

Author(s):
George Paulos

This wrapper script installs RackHD into the selected stack and runs the stack init routine, no tests
'''

import os
import sys
import subprocess
# set path to common libraries
sys.path.append(subprocess.check_output("git rev-parse --show-toplevel", shell=True).rstrip("\n") + "/test/fit_tests/common")
import fit_common

class rackhd_installer(fit_common.unittest.TestCase):
    def test01_install_os_ova(self):
        self.assertEqual(fit_common.run_nose(fit_common.TEST_PATH + '/deploy/os_ova_install.py'), 0, 'OS installer failed.')

    def test02_rackhd_installer(self):
        # sometimes it needs a retry
        for dummy in range(1,3):
            result = fit_common.run_nose(fit_common.TEST_PATH + '/deploy/rackhd_source_install.py')
            if result == 0:
                break
        self.assertEqual(result, 0, 'RackHD source installer failed.')

    def test03_initialize_stack(self):
        self.assertEqual(fit_common.run_nose(fit_common.TEST_PATH + '/deploy/rackhd_stack_init.py'), 0, 'RackHD stack init failed.')

if __name__ == '__main__':
    fit_common.unittest.main()
