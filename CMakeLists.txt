cmake_minimum_required(VERSION 3.15)
project(udt)

set(CMAKE_CXX_STANDARD 14)

include_directories(src)

add_executable(udt
        src/api.cpp
        src/api.h
        src/buffer.cpp
        src/buffer.h
        src/cache.cpp
        src/cache.h
        src/ccc.cpp
        src/ccc.h
        src/channel.cpp
        src/channel.h
        src/common.cpp
        src/common.h
        src/core.cpp
        src/core.h
        src/epoll.cpp
        src/epoll.h
        src/list.cpp
        src/list.h
        src/md5.cpp
        src/md5.h
        src/packet.cpp
        src/packet.h
        src/queue.cpp
        src/queue.h
        src/udt.h
        src/window.cpp
        src/window.h)
