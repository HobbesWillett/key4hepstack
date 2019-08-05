# key4hepstack
The files required to setup my key4hep stack

To install into your Spack instance:
1. delete `apple-libunwind` from your repos/builtin (breaks geant4)
2. add the repo here as an external repo in spack so it knows what key4hep is.
3. run spack env creat [env name] [spack.lock/spack.yaml]

spack.lock will concretise exactly as the stack was constructed.
(currently spack.yaml will cause a recursion error during concretisation, an ongoing problem in spack)
