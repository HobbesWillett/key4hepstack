# key4hepstack
The files required to setup my key4hep stack

To install into your Spack isntance:
1. delete `apple-libunwind` from your repos/builtin
2. add the repo here as an external repo in spack so it knows what key4hep is.
3. run spack env create [env name] [spack.lock/spack.yaml]
