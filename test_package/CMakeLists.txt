project(tst_icu)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(tst_icu icu.cpp)
target_link_libraries(tst_icu ${CONAN_LIBS})

if (APPLE)
  add_custom_command(TARGET tst_icu POST_BUILD COMMAND install_name_tool -change libicuuc.57.dylib @executable_path/../lib/libicuuc.57.dylib ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/../lib/libicui18n.57.dylib)
  add_custom_command(TARGET tst_icu POST_BUILD COMMAND install_name_tool -change libicudata.57.dylib @executable_path/../lib/libicudata.57.dylib ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/../lib/libicui18n.57.dylib)
  add_custom_command(TARGET tst_icu POST_BUILD COMMAND install_name_tool -change libicudata.57.dylib @executable_path/../lib/libicudata.57.dylib ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/../lib/libicuuc.57.dylib)
  add_custom_command(TARGET tst_icu POST_BUILD COMMAND install_name_tool -change libicui18n.57.dylib @executable_path/../lib/libicui18n.57.dylib $<TARGET_FILE:tst_icu>)
  add_custom_command(TARGET tst_icu POST_BUILD COMMAND install_name_tool -change libicuuc.57.dylib @executable_path/../lib/libicuuc.57.dylib $<TARGET_FILE:tst_icu>)
  add_custom_command(TARGET tst_icu POST_BUILD COMMAND install_name_tool -change libicudata.57.dylib @executable_path/../lib/libicudata.57.dylib $<TARGET_FILE:tst_icu>)
endif ()