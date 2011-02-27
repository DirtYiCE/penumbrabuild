README
======

PenumbraOverture build script using [waf].

## Requirements
* [python] \(for waf)
* [OpenAL] with [freealut]
* [SDL] plus [SDL_image] and [SDL_ttf]
* [libvorbis] and [libtheora]
* OpenGL headers and libs
* [angelscript]-2.18
* [Newton]-2, from svn
* [NVIDIA Cg toolkit][Cg]

## Build
Configure with

    ./waf configure

If you have headers/libraries in non standard location, you have to specify them
here. For example on my Gentoo box I need this to find Cg:

    CXXFLAGS=-I/opt/nvidia-cg-toolkit/include \
      LDFLAGS=-L/opt/nvidia-cg-toolkit/lib    \
      ./waf configure

Build with

    ./waf

This will build PenumbraOverture and all tests and tools (except the C#
ones). To only build penumbra, use

    ./waf --targets=penumbraoverture

Please note that by default this build script build shared libraries. This means
that to run a compiled app, you need to specify `LD_LIBRARY_PATH` to point to
the build directory. Assuming `$PENUMBRABUILD` contains the location of the
repository, you can run penumbra like:

    $ cd /path/to/PenumbraOverture
    $ LD_LIBRARY_PATH=$PENUMBRABUILD/build $PENUMBRABUILD/build/penumbraoverture

(Similary for tools and test)

There is also a Doxyfile, if you want a nice Doxygen documentation (although,
the code is not really documented).

[waf]: http://waf.googlecode.com/
[python]: http://www.python.org/
[OpenAL]: http://kcat.strangesoft.net/openal.html
[freealut]: http://connect.creativelabs.com/openal/Downloads/Forms/AllItems.aspx?RootFolder=%2fopenal%2fDownloads%2fALUT&FolderCTID=&View={6A9700C6-7248-4CD2-83F5-268F2C176072}
[SDL]: http://www.libsdl.org/
[SDL_image]: http://www.libsdl.org/projects/SDL_image/
[SDL_ttf]: http://www.libsdl.org/projects/SDL_ttf/
[libvorbis]: http://xiph.org/vorbis/
[libtheora]: http://www.theora.org/downloads/
[angelscript]: http://www.angelcode.com/angelscript/
[Newton]: http://newton-dynamics.googlecode.com/
[Cg]: http://developer.nvidia.com/page/cg_main.html
