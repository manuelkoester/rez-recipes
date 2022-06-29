name = "python"
version = "3.7.9"

variants = [["platform-linux", "arch-x86_64"]]


def commands():
    env.PATH.append("{root}")
    env.PYTHONHOME = "{root}"
    env.PYTHONPATH = "{root}"
    env.Python_ROOT = "{root}"
    env.PYTHONLOCATION = "{root}"
    env.Python_EXECUTABLE = "{root}/bin/python3"


build_command = f"""
wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz
tar xf Python-3.7.9.tgz --strip 1
./configure  --prefix=$REZ_BUILD_INSTALL_PATH \
    --enable-optimizations --enable-ipv6 --enable-shared \
    --with-dbmliborder=gdbm:ndbm:bdb --with-system-expat \
    --with-system-ffi --with-ensurepip --with-computed-gotos=yes
make install -j$REZ_BUILD_THREAD_COUNT
"""

def pre_build_commands():
    env.CFLAGS = " ".join(["-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2",
                            "-fexceptions -fstack-protector-strong",
                            "--param=ssp-buffer-size=4 -grecord-gcc-switches",
                            "-m64 -mtune=generic -D_GNU_SOURCE",
                            "-fPIC -fwrapv $CFLAGS"])
    env.LDFLAGS = "-Wl,-rpath,$REZ_BUILD_INSTALL_PATH/lib $LDFLAGS"