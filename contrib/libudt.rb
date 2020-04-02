class Libudt < Formula
  desc "UDT is a reliable UDP based application level data transport protocol for distributed data intensive applications over wide area high-speed networks"
  homepage "http://udt.sf.net"
  url "https://github.com/asenci/udt/archive/v4.11.tar.gz"
  version "4.11"
  revision 2
  sha256 "af5ffc8d8d968e4d9e431f46cbd80b791cebc9c5e6e1bc67f6accb8ce71e5c5c"

  def install
    Dir.chdir('src')
    system "make -e os=OSX arch=AMD64"
    lib.install "libudt.a"
    lib.install "libudt.dylib"
    include.install "udt.h"
    (include/"udt").install Dir["*.h"]
  end
end
