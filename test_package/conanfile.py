from conans import ConanFile, CMake
import os

channel = os.getenv("CONAN_CHANNEL", "testing")
username = os.getenv("CONAN_USERNAME", "demo")

class IcuConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "icu/57.1@%s/%s" % (username, channel)
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)
        
    def imports( self ):
        self.copy( '*.dll', 'bin', 'bin' )
        self.copy( '*.dylib', 'lib', 'lib' )

    def test(self):
        self.run(os.sep.join([".","bin", "tst_icu"]))
