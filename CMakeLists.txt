
cmake_minimum_required(VERSION 3.9)

project(pybind11_generics_tests)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# set(CMAKE_VERBOSE_MAKEFILE ON)

# set compile options
add_compile_options(
  "-fmax-errors=2" "-Wall" "-pedantic"
  "$<$<CONFIG:DEBUG>:-fno-omit-frame-pointer>"
)

# set optimzation level for release
set(CMAKE_CXX_FLAGS_RELEASE "-O3")
# generate compilation commands file for emacs
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
# prefer pthreads
set(THREADS_PREFER_PTHREAD_FLAG ON)

# make sure linker raise errors if shared library has undefined symbols
# this makes it a lot easier to debug
set(CMAKE_SHARED_LINKER_FLAGS "-Wl,--no-undefined")
# add rpaths to the final install executable
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)

# Include pybind11
add_subdirectory(pybind11_generics)

set(SRC_FILES_TEST
  ${CMAKE_CURRENT_SOURCE_DIR}/src/pybind11_generics_tests/src_cpp/main.cpp
  ${CMAKE_CURRENT_SOURCE_DIR}/src/pybind11_generics_tests/src_cpp/move_cast.cpp
  ${CMAKE_CURRENT_SOURCE_DIR}/src/pybind11_generics_tests/src_cpp/test_any.cpp
  ${CMAKE_CURRENT_SOURCE_DIR}/src/pybind11_generics_tests/src_cpp/test_dict.cpp
  ${CMAKE_CURRENT_SOURCE_DIR}/src/pybind11_generics_tests/src_cpp/test_iter.cpp
  ${CMAKE_CURRENT_SOURCE_DIR}/src/pybind11_generics_tests/src_cpp/test_iterable.cpp
  ${CMAKE_CURRENT_SOURCE_DIR}/src/pybind11_generics_tests/src_cpp/test_list.cpp
  ${CMAKE_CURRENT_SOURCE_DIR}/src/pybind11_generics_tests/src_cpp/test_sequence.cpp
  ${CMAKE_CURRENT_SOURCE_DIR}/src/pybind11_generics_tests/src_cpp/test_optional.cpp
  ${CMAKE_CURRENT_SOURCE_DIR}/src/pybind11_generics_tests/src_cpp/test_tuple.cpp
  ${CMAKE_CURRENT_SOURCE_DIR}/src/pybind11_generics_tests/src_cpp/test_union.cpp
  )

pybind11_add_module(cpp ${SRC_FILES_TEST})

target_include_directories(cpp
  PRIVATE
  ${CMAKE_CURRENT_SOURCE_DIR}/src/pybind11_generics_tests/src_cpp
  )

target_link_libraries(cpp
  PRIVATE
  pybind11_generics
  )

if (NOT DEFINED CMAKE_LIBRARY_OUTPUT_DIRECTORY)
  # default location
  set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/lib/${PROJECT_NAME})
endif()

set_target_properties(cpp
  PROPERTIES
  LIBRARY_OUTPUT_DIRECTORY ${CMAKE_LIBRARY_OUTPUT_DIRECTORY}
)
