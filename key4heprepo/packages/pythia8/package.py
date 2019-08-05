# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os

class Pythia8(AutotoolsPackage):
    """PYTHIA is a high-energy physics event generator"""

    homepage = "http://home.thep.lu.se/~torbjorn/Pythia.html"
    url      = "http://home.thep.lu.se/~torbjorn/pythia8/pythia8243.tgz"

    version('8243',
    sha256='f8ec27437d9c75302e192ab68929131a6fd642966fe66178dbe87da6da2b1c79')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def install(self, spec, prefix):
        configure("--prefix=%s" % prefix)
        make()
        make("install")

    def setup_dependent_environment(self, spack_env, run_env, dspec):
        spack_env.set('PYTHIA8_DIR', self.prefix)
        spack_env.set('PYTHIA8_XML', os.path.join(self.prefix, "share", "Pythia8", "xmldoc"))
        spack_env.set('PYTHIA8DATA', os.path.join(self.prefix, "share", "Pythia8", "xmldoc"))
