# -*- mode: python -*-

top = '.'
out = 'build'

def options(opt):
    opt.load('compiler_cxx')

def configure(cfg):
    cfg.load('compiler_cxx nasm')
    cfg.check_library()
    cfg.check_cfg(package='openal', args='--cflags --libs')
    cfg.check_cfg(package='freealut', args='--cflags --libs')

    cfg.check_cfg(path='sdl-config', args='--cflags --libs', package='',
                  msg='Checking for SDL', uselib_store='SDL')
    cfg.check_cfg(package='SDL_ttf', args='--cflags --libs')
    cfg.check_cfg(package='SDL_image', args='--cflags --libs')
    cfg.check_cfg(package='vorbis', args='--cflags --libs')
    cfg.check_cfg(package='vorbisfile', args='--cflags --libs')
    cfg.check_cfg(package='theora', args='--cflags --libs')

    cfg.check(header_name='GL/gl.h', uselib_store='GL')
    cfg.check(header_name='GL/glu.h', uselib_store='GLU')
    cfg.check(lib='GL')
    cfg.check(lib='GLU')

    cfg.check(header_name='angelscript.h', uselib_store='ANGELSCRIPT')
    cfg.check(lib='angelscript')

    cfg.check(lib='pthread')
    cfg.check(header_name='Newton.h', uselib_store='NEWTON')
    cfg.check(lib='Newton', uselib='PTHREAD')

    cfg.check(header_name='Cg/cg.h', uselib_store='CG')
    cfg.check(lib='Cg', uselib='PTHREAD')
    cfg.check(header_name='Cg/cgGL.h', uselib_store='CGGL')
    cfg.check(lib='CgGL', uselib='PTHREAD GL')

def build(bld):
    bld.shlib(source=bld.path.ant_glob('OALWrapper/sources/*.cpp'),
              includes='OALWrapper/include',
              uselib='OPENAL FREEALUT SDL VORBIS VORBISFILE',
              target='oalwrapper')
    ps = bld.path.ant_glob('HPL1Engine/sources/**/*.cpp')
    def f(x): return str(x) != 'win32.cpp'
    bld.shlib(source=filter(f, ps) +
              ['HPL1Engine/sources/impl/GLee.c'],
              includes='OALWrapper/include HPL1Engine/include',
              uselib='OPENAL FREEALUT SDL SDL_TTF SDL_IMAGE GL GLU NEWTON CG CGGL THEORA',
              use='oalwrapper',
              target='hpl1engine')

    bld.program(source=bld.path.ant_glob('PenumbraOverture/*.cpp'),
                includes='PenumbraOverture HPL1Engine/include OALWrapper/include',
                use='hpl1engine',
                uselib='ANGELSCRIPT',
                target='penumbraoverture')

    #tests
    bld.stlib(source='HPL1Engine/tests/Common/SimpleCamera.cpp',
              includes='OALWrapper/include HPL1Engine/include',
              target='testcommon',
              use='hpl1engine')

    bld.program(source='HPL1Engine/tests/PhysicsTest/PhysicsTest.cpp',
                includes='OALWrapper/include HPL1Engine/include',
                target='physicstest',
                use='testcommon',
                uselib='ANGELSCRIPT')

    bld.program(source='HPL1Engine/tests/GuiTest/GuiTest.cpp',
                includes='OALWrapper/include HPL1Engine/include',
                target='guitest',
                use='testcommon',
                uselib='ANGELSCRIPT')

    bld.program(source='HPL1Engine/tests/RenderTest/RenderTest.cpp',
                includes='OALWrapper/include HPL1Engine/include',
                target='rendertest',
                use='testcommon',
                uselib='ANGELSCRIPT')

    bld.program(source=['HPL1Engine/tests/SceneTest/SceneTest.cpp',
                        'HPL1Engine/tests/SceneTest/SceneCamera.cpp'],
                includes='OALWrapper/include HPL1Engine/include',
                target='scenetest',
                use='hpl1engine',
                uselib='ANGELSCRIPT')

    bld.program(source='HPL1Engine/tests/SerializeTest/SerializeTest.cpp',
                includes='OALWrapper/include HPL1Engine/include',
                target='serializetest',
                use='testcommon',
                uselib='ANGELSCRIPT')

    bld.program(source='HPL1Engine/tests/SpotLightTest/SpotLightTest.cpp',
                includes='OALWrapper/include HPL1Engine/include',
                target='spotlighttest',
                use='testcommon',
                uselib='ANGELSCRIPT')

    bld.program(source='HPL1Engine/tests/VideoTest/VideoTest.cpp',
                includes='OALWrapper/include HPL1Engine/include',
                target='videotest',
                use='testcommon',
                uselib='ANGELSCRIPT')

    # tools
    bld.program(source=['HPL1Engine/tools/HudObjectEditor/HudObjectEditor.cpp',
                        'HPL1Engine/tools/HudObjectEditor/HOECamera.cpp',],
                includes='OALWrapper/include HPL1Engine/include',
                target='hoe',
                use='hpl1engine',
                uselib='ANGELSCRIPT')

    bld.program(source=['HPL1Engine/tools/ModelViewer/ModelViewer.cpp',
                        'HPL1Engine/tools/ModelViewer/MVCamera.cpp'],
                includes='OALWrapper/include HPL1Engine/include',
                target='mv',
                use='hpl1engine',
                uselib='ANGELSCRIPT')

    bld.program(source=['HPL1Engine/tools/ParticleViewer/ParticleViewer.cpp',
                        'HPL1Engine/tools/ParticleViewer/PVCamera.cpp'],
                includes='OALWrapper/include HPL1Engine/include',
                target='pv',
                use='hpl1engine',
                uselib='ANGELSCRIPT')

    bld.program(source=['HPL1Engine/tools/SceneViewer/SceneViewer.cpp',
                        'HPL1Engine/tools/SceneViewer/SceneCamera.cpp'],
                includes='OALWrapper/include HPL1Engine/include',
                target='sv',
                use='hpl1engine',
                uselib='ANGELSCRIPT')
