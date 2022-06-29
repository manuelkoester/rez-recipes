name = "openjpeg"
version = "2.4.0"

build_requires = ["cmake"]

variants = [["platform-linux", "arch-x86_64"]]

def commands():
    env.PATH.prepend("{root}/bin")
    env.OpenJPEG_ROOT = "{root}"
    env.PKG_CONFIG_PATH.prepend("{root}/lib/pkgconfig")

    if building:
        env.LDFLAGS.prepend("-L{root}/lib -Wl,-rpath,{root}/lib")


def pre_build_commands():
    env.LDFLAGS.prepend("-Wl,-rpath,$REZ_BUILD_INSTALL_PATH/lib")



def pre_cook():
    import subprocess as sp
    archive = f"v{version}.tar.gz"
    sp.run(["wget", f"https://github.com/uclouvain/openjpeg/archive/refs/tags/{archive}"])
    sp.run(["tar", "xf", archive, "--strip", "1"])
    