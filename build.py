from conan.packager import ConanMultiPackager
import platform

if __name__ == "__main__":
  builder = ConanMultiPackager( username="shinichy", channel="testing" )
  builder.add_common_builds( pure_c=False )
  filtered_builds = []
  for settings, options in builder.builds:
    if platform.system() == "Darwin" and settings["arch"] in ["x86_64"]:
      filtered_builds.append([settings, options])
  builder.builds = filtered_builds
  builder.run()
