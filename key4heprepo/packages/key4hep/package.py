# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.package import PackageBase

class Key4hep(PackageBase):
    """The dummy package that installs the turnkey software stack, it relies on
    the packages.yaml distributed by LCG to concretise the packages
    correctly."""

    phases = ['build', 'install']
    build_system_class = 'BundlePackage'

    url = 'https://github.com/citibeth/dummy/tarball/v1.0'

    version('1.0', 'e2b724dfcc31d735897971db91be89ff')

    # Variants:

    # The software stack
    depends_on('root')
    depends_on('environment-modules')
    depends_on('dd4hep')
    depends_on('geant4')
    depends_on('gaudi')
    depends_on('pythia8')

    def build(self, spec, prefix):
        pass

    def install(self, spec, prefix):
        pass
