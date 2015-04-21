# encoding: utf-8
# module posix
# from (built-in)
# by generator 1.136
"""
This module provides access to operating system functionality that is
standardized by the C Standard and the POSIX standard (a thinly
disguised Unix interface).  Refer to the library manual and
corresponding Unix manual entries for more information on calls.
"""

# imports
from exceptions import error


# Variables with simple values

EX_CANTCREAT = 73
EX_CONFIG = 78
EX_DATAERR = 65
EX_IOERR = 74
EX_NOHOST = 68
EX_NOINPUT = 66
EX_NOPERM = 77
EX_NOUSER = 67
EX_OK = 0
EX_OSERR = 71
EX_OSFILE = 72
EX_PROTOCOL = 76
EX_SOFTWARE = 70
EX_TEMPFAIL = 75
EX_UNAVAILABLE = 69
EX_USAGE = 64

F_OK = 0

NGROUPS_MAX = 16

O_APPEND = 8
O_ASYNC = 64
O_CREAT = 512
O_DIRECTORY = 1048576
O_DSYNC = 4194304
O_EXCL = 2048
O_EXLOCK = 32
O_NDELAY = 4
O_NOCTTY = 131072
O_NOFOLLOW = 256
O_NONBLOCK = 4
O_RDONLY = 0
O_RDWR = 2
O_SHLOCK = 16
O_SYNC = 128
O_TRUNC = 1024
O_WRONLY = 1

R_OK = 4

TMP_MAX = 308915776

WCONTINUED = 16

WNOHANG = 1

WUNTRACED = 2

W_OK = 2

X_OK = 1

# functions

def abort(): # real signature unknown; restored from __doc__
    """
    abort() -> does not return!
    
    Abort the interpreter immediately.  This 'dumps core' or otherwise fails
    in the hardest way possible on the hosting operating system.
    """
    pass

def access(path, mode): # real signature unknown; restored from __doc__
    """
    access(path, mode) -> True if granted, False otherwise
    
    Use the real uid/gid to test for access to a path.  Note that most
    operations will use the effective uid/gid, therefore this routine can
    be used in a suid/sgid environment to test if the invoking user has the
    specified access to the path.  The mode argument can be F_OK to test
    existence, or the inclusive-OR of R_OK, W_OK, and X_OK.
    """
    return False

def chdir(path): # real signature unknown; restored from __doc__
    """
    chdir(path)
    
    Change the current working directory to the specified path.
    """
    pass

def chflags(path, flags): # real signature unknown; restored from __doc__
    """
    chflags(path, flags)
    
    Set file flags.
    """
    pass

def chmod(path, mode): # real signature unknown; restored from __doc__
    """
    chmod(path, mode)
    
    Change the access permissions of a file.
    """
    pass

def chown(path, uid, gid): # real signature unknown; restored from __doc__
    """
    chown(path, uid, gid)
    
    Change the owner and group id of path to the numeric uid and gid.
    """
    pass

def chroot(path): # real signature unknown; restored from __doc__
    """
    chroot(path)
    
    Change root directory to path.
    """
    pass

def close(fd): # real signature unknown; restored from __doc__
    """
    close(fd)
    
    Close a file descriptor (for low level IO).
    """
    pass

def closerange(fd_low, fd_high): # real signature unknown; restored from __doc__
    """
    closerange(fd_low, fd_high)
    
    Closes all file descriptors in [fd_low, fd_high), ignoring errors.
    """
    pass

def confstr(name): # real signature unknown; restored from __doc__
    """
    confstr(name) -> string
    
    Return a string-valued system configuration variable.
    """
    return ""

def ctermid(): # real signature unknown; restored from __doc__
    """
    ctermid() -> string
    
    Return the name of the controlling terminal for this process.
    """
    return ""

def dup(fd): # real signature unknown; restored from __doc__
    """
    dup(fd) -> fd2
    
    Return a duplicate of a file descriptor.
    """
    pass

def dup2(old_fd, new_fd): # real signature unknown; restored from __doc__
    """
    dup2(old_fd, new_fd)
    
    Duplicate file descriptor.
    """
    pass

def execv(path, args): # real signature unknown; restored from __doc__
    """
    execv(path, args)
    
    Execute an executable path with arguments, replacing current process.
    
        path: path of executable file
        args: tuple or list of strings
    """
    pass

def execve(path, args, env): # real signature unknown; restored from __doc__
    """
    execve(path, args, env)
    
    Execute a path with arguments and environment, replacing current process.
    
        path: path of executable file
        args: tuple or list of arguments
        env: dictionary of strings mapping to strings
    """
    pass

def fchdir(fildes): # real signature unknown; restored from __doc__
    """
    fchdir(fildes)
    
    Change to the directory of the given file descriptor.  fildes must be
    opened on a directory, not a file.
    """
    pass

def fchmod(fd, mode): # real signature unknown; restored from __doc__
    """
    fchmod(fd, mode)
    
    Change the access permissions of the file given by file
    descriptor fd.
    """
    pass

def fchown(fd, uid, gid): # real signature unknown; restored from __doc__
    """
    fchown(fd, uid, gid)
    
    Change the owner and group id of the file given by file descriptor
    fd to the numeric uid and gid.
    """
    pass

def fdopen(fd, mode='r', bufsize=None): # real signature unknown; restored from __doc__
    """
    fdopen(fd [, mode='r' [, bufsize]]) -> file_object
    
    Return an open file object connected to a file descriptor.
    """
    pass

def fork(): # real signature unknown; restored from __doc__
    """
    fork() -> pid
    
    Fork a child process.
    Return 0 to child process and PID of child to parent process.
    """
    pass

def forkpty(): # real signature unknown; restored from __doc__
    """
    forkpty() -> (pid, master_fd)
    
    Fork a new process with a new pseudo-terminal as controlling tty.
    
    Like fork(), return 0 as pid to child process, and PID of child to parent.
    To both, return fd of newly opened pseudo-terminal.
    """
    pass

def fpathconf(fd, name): # real signature unknown; restored from __doc__
    """
    fpathconf(fd, name) -> integer
    
    Return the configuration limit name for the file descriptor fd.
    If there is no limit, return -1.
    """
    return 0

def fstat(fd): # real signature unknown; restored from __doc__
    """
    fstat(fd) -> stat result
    
    Like stat(), but for an open file descriptor.
    """
    pass

def fstatvfs(fd): # real signature unknown; restored from __doc__
    """
    fstatvfs(fd) -> statvfs result
    
    Perform an fstatvfs system call on the given fd.
    """
    pass

def fsync(fildes): # real signature unknown; restored from __doc__
    """
    fsync(fildes)
    
    force write of file with filedescriptor to disk.
    """
    pass

def ftruncate(fd, length): # real signature unknown; restored from __doc__
    """
    ftruncate(fd, length)
    
    Truncate a file to a specified length.
    """
    pass

def getcwd(): # real signature unknown; restored from __doc__
    """
    getcwd() -> path
    
    Return a string representing the current working directory.
    """
    pass

def getcwdu(): # real signature unknown; restored from __doc__
    """
    getcwdu() -> path
    
    Return a unicode string representing the current working directory.
    """
    pass

def getegid(): # real signature unknown; restored from __doc__
    """
    getegid() -> egid
    
    Return the current process's effective group id.
    """
    pass

def geteuid(): # real signature unknown; restored from __doc__
    """
    geteuid() -> euid
    
    Return the current process's effective user id.
    """
    pass

def getgid(): # real signature unknown; restored from __doc__
    """
    getgid() -> gid
    
    Return the current process's group id.
    """
    pass

def getgroups(): # real signature unknown; restored from __doc__
    """
    getgroups() -> list of group IDs
    
    Return list of supplemental group IDs for the process.
    """
    return []

def getloadavg(): # real signature unknown; restored from __doc__
    """
    getloadavg() -> (float, float, float)
    
    Return the number of processes in the system run queue averaged over
    the last 1, 5, and 15 minutes or raises OSError if the load average
    was unobtainable
    """
    pass

def getlogin(): # real signature unknown; restored from __doc__
    """
    getlogin() -> string
    
    Return the actual login name.
    """
    return ""

def getpgid(pid): # real signature unknown; restored from __doc__
    """
    getpgid(pid) -> pgid
    
    Call the system call getpgid().
    """
    pass

def getpgrp(): # real signature unknown; restored from __doc__
    """
    getpgrp() -> pgrp
    
    Return the current process group id.
    """
    pass

def getpid(): # real signature unknown; restored from __doc__
    """
    getpid() -> pid
    
    Return the current process id
    """
    pass

def getppid(): # real signature unknown; restored from __doc__
    """
    getppid() -> ppid
    
    Return the parent's process id.
    """
    pass

def getsid(pid): # real signature unknown; restored from __doc__
    """
    getsid(pid) -> sid
    
    Call the system call getsid().
    """
    pass

def getuid(): # real signature unknown; restored from __doc__
    """
    getuid() -> uid
    
    Return the current process's user id.
    """
    pass

def initgroups(username, gid): # real signature unknown; restored from __doc__
    """
    initgroups(username, gid) -> None
    
    Call the system initgroups() to initialize the group access list with all of
    the groups of which the specified username is a member, plus the specified
    group id.
    """
    pass

def isatty(fd): # real signature unknown; restored from __doc__
    """
    isatty(fd) -> bool
    
    Return True if the file descriptor 'fd' is an open file descriptor
    connected to the slave end of a terminal.
    """
    return False

def kill(pid, sig): # real signature unknown; restored from __doc__
    """
    kill(pid, sig)
    
    Kill a process with a signal.
    """
    pass

def killpg(pgid, sig): # real signature unknown; restored from __doc__
    """
    killpg(pgid, sig)
    
    Kill a process group with a signal.
    """
    pass

def lchflags(path, flags): # real signature unknown; restored from __doc__
    """
    lchflags(path, flags)
    
    Set file flags.
    This function will not follow symbolic links.
    """
    pass

def lchmod(path, mode): # real signature unknown; restored from __doc__
    """
    lchmod(path, mode)
    
    Change the access permissions of a file. If path is a symlink, this
    affects the link itself rather than the target.
    """
    pass

def lchown(path, uid, gid): # real signature unknown; restored from __doc__
    """
    lchown(path, uid, gid)
    
    Change the owner and group id of path to the numeric uid and gid.
    This function will not follow symbolic links.
    """
    pass

def link(src, dst): # real signature unknown; restored from __doc__
    """
    link(src, dst)
    
    Create a hard link to a file.
    """
    pass

def listdir(path): # real signature unknown; restored from __doc__
    """
    listdir(path) -> list_of_strings
    
    Return a list containing the names of the entries in the directory.
    
        path: path of directory to list
    
    The list is in arbitrary order.  It does not include the special
    entries '.' and '..' even if they are present in the directory.
    """
    pass

def lseek(fd, pos, how): # real signature unknown; restored from __doc__
    """
    lseek(fd, pos, how) -> newpos
    
    Set the current position of a file descriptor.
    """
    pass

def lstat(path): # real signature unknown; restored from __doc__
    """
    lstat(path) -> stat result
    
    Like stat(path), but do not follow symbolic links.
    """
    pass

def major(device): # real signature unknown; restored from __doc__
    """
    major(device) -> major number
    Extracts a device major number from a raw device number.
    """
    pass

def makedev(major, minor): # real signature unknown; restored from __doc__
    """
    makedev(major, minor) -> device number
    Composes a raw device number from the major and minor device numbers.
    """
    pass

def minor(device): # real signature unknown; restored from __doc__
    """
    minor(device) -> minor number
    Extracts a device minor number from a raw device number.
    """
    pass

def mkdir(path, mode=0777): # real signature unknown; restored from __doc__
    """
    mkdir(path [, mode=0777])
    
    Create a directory.
    """
    pass

def mkfifo(filename, mode=0666): # real signature unknown; restored from __doc__
    """
    mkfifo(filename [, mode=0666])
    
    Create a FIFO (a POSIX named pipe).
    """
    pass

def mknod(filename, mode=0600, device=None): # real signature unknown; restored from __doc__
    """
    mknod(filename [, mode=0600, device])
    
    Create a filesystem node (file, device special file or named pipe)
    named filename. mode specifies both the permissions to use and the
    type of node to be created, being combined (bitwise OR) with one of
    S_IFREG, S_IFCHR, S_IFBLK, and S_IFIFO. For S_IFCHR and S_IFBLK,
    device defines the newly created device special file (probably using
    os.makedev()), otherwise it is ignored.
    """
    pass

def nice(inc): # real signature unknown; restored from __doc__
    """
    nice(inc) -> new_priority
    
    Decrease the priority of process by inc and return the new priority.
    """
    pass

def open(filename, flag, mode=0777): # real signature unknown; restored from __doc__
    """
    open(filename, flag [, mode=0777]) -> fd
    
    Open a file (for low level IO).
    """
    pass

def openpty(): # real signature unknown; restored from __doc__
    """
    openpty() -> (master_fd, slave_fd)
    
    Open a pseudo-terminal, returning open fd's for both master and slave end.
    """
    pass

def pathconf(path, name): # real signature unknown; restored from __doc__
    """
    pathconf(path, name) -> integer
    
    Return the configuration limit name for the file or directory path.
    If there is no limit, return -1.
    """
    return 0

def pipe(): # real signature unknown; restored from __doc__
    """
    pipe() -> (read_end, write_end)
    
    Create a pipe.
    """
    pass

def popen(command, mode='r', bufsize=None): # real signature unknown; restored from __doc__
    """
    popen(command [, mode='r' [, bufsize]]) -> pipe
    
    Open a pipe to/from a command returning a file object.
    """
    pass

def putenv(key, value): # real signature unknown; restored from __doc__
    """
    putenv(key, value)
    
    Change or add an environment variable.
    """
    pass

def read(fd, buffersize): # real signature unknown; restored from __doc__
    """
    read(fd, buffersize) -> string
    
    Read a file descriptor.
    """
    return ""

def readlink(path): # real signature unknown; restored from __doc__
    """
    readlink(path) -> path
    
    Return a string representing the path to which the symbolic link points.
    """
    pass

def remove(path): # real signature unknown; restored from __doc__
    """
    remove(path)
    
    Remove a file (same as unlink(path)).
    """
    pass

def rename(old, new): # real signature unknown; restored from __doc__
    """
    rename(old, new)
    
    Rename a file or directory.
    """
    pass

def rmdir(path): # real signature unknown; restored from __doc__
    """
    rmdir(path)
    
    Remove a directory.
    """
    pass

def setegid(gid): # real signature unknown; restored from __doc__
    """
    setegid(gid)
    
    Set the current process's effective group id.
    """
    pass

def seteuid(uid): # real signature unknown; restored from __doc__
    """
    seteuid(uid)
    
    Set the current process's effective user id.
    """
    pass

def setgid(gid): # real signature unknown; restored from __doc__
    """
    setgid(gid)
    
    Set the current process's group id.
    """
    pass

def setgroups(p_list): # real signature unknown; restored from __doc__
    """
    setgroups(list)
    
    Set the groups of the current process to list.
    """
    pass

def setpgid(pid, pgrp): # real signature unknown; restored from __doc__
    """
    setpgid(pid, pgrp)
    
    Call the system call setpgid().
    """
    pass

def setpgrp(): # real signature unknown; restored from __doc__
    """
    setpgrp()
    
    Make this process the process group leader.
    """
    pass

def setregid(rgid, egid): # real signature unknown; restored from __doc__
    """
    setregid(rgid, egid)
    
    Set the current process's real and effective group ids.
    """
    pass

def setreuid(ruid, euid): # real signature unknown; restored from __doc__
    """
    setreuid(ruid, euid)
    
    Set the current process's real and effective user ids.
    """
    pass

def setsid(): # real signature unknown; restored from __doc__
    """
    setsid()
    
    Call the system call setsid().
    """
    pass

def setuid(uid): # real signature unknown; restored from __doc__
    """
    setuid(uid)
    
    Set the current process's user id.
    """
    pass

def stat(path): # real signature unknown; restored from __doc__
    """
    stat(path) -> stat result
    
    Perform a stat system call on the given path.
    """
    pass

def statvfs(path): # real signature unknown; restored from __doc__
    """
    statvfs(path) -> statvfs result
    
    Perform a statvfs system call on the given path.
    """
    pass

def stat_float_times(newval=None): # real signature unknown; restored from __doc__
    """
    stat_float_times([newval]) -> oldval
    
    Determine whether os.[lf]stat represents time stamps as float objects.
    If newval is True, future calls to stat() return floats, if it is False,
    future calls return ints. 
    If newval is omitted, return the current setting.
    """
    pass

def strerror(code): # real signature unknown; restored from __doc__
    """
    strerror(code) -> string
    
    Translate an error code to a message string.
    """
    return ""

def symlink(src, dst): # real signature unknown; restored from __doc__
    """
    symlink(src, dst)
    
    Create a symbolic link pointing to src named dst.
    """
    pass

def sysconf(name): # real signature unknown; restored from __doc__
    """
    sysconf(name) -> integer
    
    Return an integer-valued system configuration variable.
    """
    return 0

def system(command): # real signature unknown; restored from __doc__
    """
    system(command) -> exit_status
    
    Execute the command (a string) in a subshell.
    """
    pass

def tcgetpgrp(fd): # real signature unknown; restored from __doc__
    """
    tcgetpgrp(fd) -> pgid
    
    Return the process group associated with the terminal given by a fd.
    """
    pass

def tcsetpgrp(fd, pgid): # real signature unknown; restored from __doc__
    """
    tcsetpgrp(fd, pgid)
    
    Set the process group associated with the terminal given by a fd.
    """
    pass

def tempnam(dir=None, prefix=None): # real signature unknown; restored from __doc__
    """
    tempnam([dir[, prefix]]) -> string
    
    Return a unique name for a temporary file.
    The directory and a prefix may be specified as strings; they may be omitted
    or None if not needed.
    """
    return ""

def times(): # real signature unknown; restored from __doc__
    """
    times() -> (utime, stime, cutime, cstime, elapsed_time)
    
    Return a tuple of floating point numbers indicating process times.
    """
    pass

def tmpfile(): # real signature unknown; restored from __doc__
    """
    tmpfile() -> file object
    
    Create a temporary file with no directory entries.
    """
    return file('/dev/null')

def tmpnam(): # real signature unknown; restored from __doc__
    """
    tmpnam() -> string
    
    Return a unique name for a temporary file.
    """
    return ""

def ttyname(fd): # real signature unknown; restored from __doc__
    """
    ttyname(fd) -> string
    
    Return the name of the terminal device connected to 'fd'.
    """
    return ""

def umask(new_mask): # real signature unknown; restored from __doc__
    """
    umask(new_mask) -> old_mask
    
    Set the current numeric umask and return the previous umask.
    """
    pass

def uname(): # real signature unknown; restored from __doc__
    """
    uname() -> (sysname, nodename, release, version, machine)
    
    Return a tuple identifying the current operating system.
    """
    pass

def unlink(path): # real signature unknown; restored from __doc__
    """
    unlink(path)
    
    Remove a file (same as remove(path)).
    """
    pass

def unsetenv(key): # real signature unknown; restored from __doc__
    """
    unsetenv(key)
    
    Delete an environment variable.
    """
    pass

def urandom(n): # real signature unknown; restored from __doc__
    """
    urandom(n) -> str
    
    Return n random bytes suitable for cryptographic use.
    """
    return ""

def utime(path, (atime, mtime)): # real signature unknown; restored from __doc__
    """
    utime(path, (atime, mtime))
    utime(path, None)
    
    Set the access and modified time of the file to the given values.  If the
    second form is used, set the access and modified times to the current time.
    """
    pass

def wait(): # real signature unknown; restored from __doc__
    """
    wait() -> (pid, status)
    
    Wait for completion of a child process.
    """
    pass

def wait3(options): # real signature unknown; restored from __doc__
    """
    wait3(options) -> (pid, status, rusage)
    
    Wait for completion of a child process.
    """
    pass

def wait4(pid, options): # real signature unknown; restored from __doc__
    """
    wait4(pid, options) -> (pid, status, rusage)
    
    Wait for completion of a given child process.
    """
    pass

def waitpid(pid, options): # real signature unknown; restored from __doc__
    """
    waitpid(pid, options) -> (pid, status)
    
    Wait for completion of a given child process.
    """
    pass

def WCOREDUMP(status): # real signature unknown; restored from __doc__
    """
    WCOREDUMP(status) -> bool
    
    Return True if the process returning 'status' was dumped to a core file.
    """
    return False

def WEXITSTATUS(status): # real signature unknown; restored from __doc__
    """
    WEXITSTATUS(status) -> integer
    
    Return the process return code from 'status'.
    """
    return 0

def WIFCONTINUED(status): # real signature unknown; restored from __doc__
    """
    WIFCONTINUED(status) -> bool
    
    Return True if the process returning 'status' was continued from a
    job control stop.
    """
    return False

def WIFEXITED(status): # real signature unknown; restored from __doc__
    """
    WIFEXITED(status) -> bool
    
    Return true if the process returning 'status' exited using the exit()
    system call.
    """
    return False

def WIFSIGNALED(status): # real signature unknown; restored from __doc__
    """
    WIFSIGNALED(status) -> bool
    
    Return True if the process returning 'status' was terminated by a signal.
    """
    return False

def WIFSTOPPED(status): # real signature unknown; restored from __doc__
    """
    WIFSTOPPED(status) -> bool
    
    Return True if the process returning 'status' was stopped.
    """
    return False

def write(fd, string): # real signature unknown; restored from __doc__
    """
    write(fd, string) -> byteswritten
    
    Write a string to a file descriptor.
    """
    pass

def WSTOPSIG(status): # real signature unknown; restored from __doc__
    """
    WSTOPSIG(status) -> integer
    
    Return the signal that stopped the process that provided
    the 'status' value.
    """
    return 0

def WTERMSIG(status): # real signature unknown; restored from __doc__
    """
    WTERMSIG(status) -> integer
    
    Return the signal that terminated the process that provided the 'status'
    value.
    """
    return 0

def _exit(status): # real signature unknown; restored from __doc__
    """
    _exit(status)
    
    Exit to the system with specified status, without normal exit processing.
    """
    pass

# classes

class statvfs_result(object):
    """
    statvfs_result: Result from statvfs or fstatvfs.
    
    This object may be accessed either as a tuple of
      (bsize, frsize, blocks, bfree, bavail, files, ffree, favail, flag, namemax),
    or via the attributes f_bsize, f_frsize, f_blocks, f_bfree, and so on.
    
    See os.statvfs for more information.
    """
    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __getslice__(self, i, j): # real signature unknown; restored from __doc__
        """
        x.__getslice__(i, j) <==> x[i:j]
                   
                   Use of negative indices is not supported.
        """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __mul__(self, n): # real signature unknown; restored from __doc__
        """ x.__mul__(n) <==> x*n """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __rmul__(self, n): # real signature unknown; restored from __doc__
        """ x.__rmul__(n) <==> n*x """
        pass

    f_bavail = property(lambda self: 0)
    """:type: int"""

    f_bfree = property(lambda self: 0)
    """:type: int"""

    f_blocks = property(lambda self: 0)
    """:type: int"""

    f_bsize = property(lambda self: 0)
    """:type: int"""

    f_favail = property(lambda self: 0)
    """:type: int"""

    f_ffree = property(lambda self: 0)
    """:type: int"""

    f_files = property(lambda self: 0)
    """:type: int"""

    f_flag = property(lambda self: 0)
    """:type: int"""

    f_frsize = property(lambda self: 0)
    """:type: int"""

    f_namemax = property(lambda self: 0)
    """:type: int"""


    n_fields = 10
    n_sequence_fields = 10
    n_unnamed_fields = 0


class stat_result(object):
    """
    stat_result: Result from stat or lstat.
    
    This object may be accessed either as a tuple of
      (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
    or via the attributes st_mode, st_ino, st_dev, st_nlink, st_uid, and so on.
    
    Posix/windows: If your platform supports st_blksize, st_blocks, st_rdev,
    or st_flags, they are available as attributes only.
    
    See os.stat for more information.
    """
    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __getslice__(self, i, j): # real signature unknown; restored from __doc__
        """
        x.__getslice__(i, j) <==> x[i:j]
                   
                   Use of negative indices is not supported.
        """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __mul__(self, n): # real signature unknown; restored from __doc__
        """ x.__mul__(n) <==> x*n """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __rmul__(self, n): # real signature unknown; restored from __doc__
        """ x.__rmul__(n) <==> n*x """
        pass

    st_atime = property(lambda self: 0)
    """time of last access

    :type: int
    """

    st_birthtime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """time of creation"""

    st_blksize = property(lambda self: 0)
    """blocksize for filesystem I/O

    :type: int
    """

    st_blocks = property(lambda self: 0)
    """number of blocks allocated

    :type: int
    """

    st_ctime = property(lambda self: 0)
    """time of last change

    :type: int
    """

    st_dev = property(lambda self: 0)
    """device

    :type: int
    """

    st_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """user defined flags for file"""

    st_gen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """generation number"""

    st_gid = property(lambda self: 0)
    """group ID of owner

    :type: int
    """

    st_ino = property(lambda self: 0)
    """inode

    :type: int
    """

    st_mode = property(lambda self: 0)
    """protection bits

    :type: int
    """

    st_mtime = property(lambda self: 0)
    """time of last modification

    :type: int
    """

    st_nlink = property(lambda self: 0)
    """number of hard links

    :type: int
    """

    st_rdev = property(lambda self: 0)
    """device type (if inode device)

    :type: int
    """

    st_size = property(lambda self: 0)
    """total size, in bytes

    :type: int
    """

    st_uid = property(lambda self: 0)
    """user ID of owner

    :type: int
    """


    n_fields = 19
    n_sequence_fields = 10
    n_unnamed_fields = 3


# variables with complex values

confstr_names = {
    'CS_DARWIN_USER_CACHE_DIR': 65538,
    'CS_DARWIN_USER_DIR': 65536,
    'CS_DARWIN_USER_TEMP_DIR': 65537,
    'CS_PATH': 1,
    'CS_XBS5_ILP32_OFF32_CFLAGS': 20,
    'CS_XBS5_ILP32_OFF32_LDFLAGS': 21,
    'CS_XBS5_ILP32_OFF32_LIBS': 22,
    'CS_XBS5_ILP32_OFF32_LINTFLAGS': 23,
    'CS_XBS5_ILP32_OFFBIG_CFLAGS': 24,
    'CS_XBS5_ILP32_OFFBIG_LDFLAGS': 25,
    'CS_XBS5_ILP32_OFFBIG_LIBS': 26,
    'CS_XBS5_ILP32_OFFBIG_LINTFLAGS': 27,
    'CS_XBS5_LP64_OFF64_CFLAGS': 28,
    'CS_XBS5_LP64_OFF64_LDFLAGS': 29,
    'CS_XBS5_LP64_OFF64_LIBS': 30,
    'CS_XBS5_LP64_OFF64_LINTFLAGS': 31,
    'CS_XBS5_LPBIG_OFFBIG_CFLAGS': 32,
    'CS_XBS5_LPBIG_OFFBIG_LDFLAGS': 33,
    'CS_XBS5_LPBIG_OFFBIG_LIBS': 34,
    'CS_XBS5_LPBIG_OFFBIG_LINTFLAGS': 35,
}

environ = {} # real value of type <type 'dict'> skipped

pathconf_names = {
    'PC_ASYNC_IO': 17,
    'PC_CHOWN_RESTRICTED': 7,
    'PC_FILESIZEBITS': 18,
    'PC_LINK_MAX': 1,
    'PC_MAX_CANON': 2,
    'PC_MAX_INPUT': 3,
    'PC_NAME_MAX': 4,
    'PC_NO_TRUNC': 8,
    'PC_PATH_MAX': 5,
    'PC_PIPE_BUF': 6,
    'PC_PRIO_IO': 19,
    'PC_SYNC_IO': 25,
    'PC_VDISABLE': 9,
}

sysconf_names = {
    'SC_2_CHAR_TERM': 20,
    'SC_2_C_BIND': 18,
    'SC_2_C_DEV': 19,
    'SC_2_FORT_DEV': 21,
    'SC_2_FORT_RUN': 22,
    'SC_2_LOCALEDEF': 23,
    'SC_2_SW_DEV': 24,
    'SC_2_UPE': 25,
    'SC_2_VERSION': 17,
    'SC_AIO_LISTIO_MAX': 42,
    'SC_AIO_MAX': 43,
    'SC_AIO_PRIO_DELTA_MAX': 44,
    'SC_ARG_MAX': 1,
    'SC_ASYNCHRONOUS_IO': 28,
    'SC_ATEXIT_MAX': 107,
    'SC_BC_BASE_MAX': 9,
    'SC_BC_DIM_MAX': 10,
    'SC_BC_SCALE_MAX': 11,
    'SC_BC_STRING_MAX': 12,
    'SC_CHILD_MAX': 2,
    'SC_CLK_TCK': 3,
    'SC_COLL_WEIGHTS_MAX': 13,
    'SC_DELAYTIMER_MAX': 45,
    'SC_EXPR_NEST_MAX': 14,
    'SC_FSYNC': 38,
    'SC_GETGR_R_SIZE_MAX': 70,
    'SC_GETPW_R_SIZE_MAX': 71,
    'SC_IOV_MAX': 56,
    'SC_JOB_CONTROL': 6,
    'SC_LINE_MAX': 15,
    'SC_LOGIN_NAME_MAX': 73,
    'SC_MAPPED_FILES': 47,
    'SC_MEMLOCK': 30,
    'SC_MEMLOCK_RANGE': 31,
    'SC_MEMORY_PROTECTION': 32,
    'SC_MESSAGE_PASSING': 33,
    'SC_MQ_OPEN_MAX': 46,
    'SC_MQ_PRIO_MAX': 75,
    'SC_NGROUPS_MAX': 4,
    'SC_NPROCESSORS_CONF': 57,
    'SC_NPROCESSORS_ONLN': 58,
    'SC_OPEN_MAX': 5,
    'SC_PAGESIZE': 29,
    'SC_PAGE_SIZE': 29,
    'SC_PASS_MAX': 131,
    'SC_PRIORITIZED_IO': 34,
    'SC_PRIORITY_SCHEDULING': 35,
    'SC_REALTIME_SIGNALS': 36,
    'SC_RE_DUP_MAX': 16,
    'SC_RTSIG_MAX': 48,
    'SC_SAVED_IDS': 7,
    'SC_SEMAPHORES': 37,
    'SC_SEM_NSEMS_MAX': 49,
    'SC_SEM_VALUE_MAX': 50,
    'SC_SHARED_MEMORY_OBJECTS': 39,
    'SC_SIGQUEUE_MAX': 51,
    'SC_STREAM_MAX': 26,
    'SC_SYNCHRONIZED_IO': 40,
    'SC_THREADS': 96,
    'SC_THREAD_ATTR_STACKADDR': 82,
    'SC_THREAD_ATTR_STACKSIZE': 83,
    'SC_THREAD_DESTRUCTOR_ITERATIONS': 85,
    'SC_THREAD_KEYS_MAX': 86,
    'SC_THREAD_PRIORITY_SCHEDULING': 89,
    'SC_THREAD_PRIO_INHERIT': 87,
    'SC_THREAD_PRIO_PROTECT': 88,
    'SC_THREAD_PROCESS_SHARED': 90,
    'SC_THREAD_SAFE_FUNCTIONS': 91,
    'SC_THREAD_STACK_MIN': 93,
    'SC_THREAD_THREADS_MAX': 94,
    'SC_TIMERS': 41,
    'SC_TIMER_MAX': 52,
    'SC_TTY_NAME_MAX': 101,
    'SC_TZNAME_MAX': 27,
    'SC_VERSION': 8,
    'SC_XBS5_ILP32_OFF32': 122,
    'SC_XBS5_ILP32_OFFBIG': 123,
    'SC_XBS5_LP64_OFF64': 124,
    'SC_XBS5_LPBIG_OFFBIG': 125,
    'SC_XOPEN_CRYPT': 108,
    'SC_XOPEN_ENH_I18N': 109,
    'SC_XOPEN_LEGACY': 110,
    'SC_XOPEN_REALTIME': 111,
    'SC_XOPEN_REALTIME_THREADS': 112,
    'SC_XOPEN_SHM': 113,
    'SC_XOPEN_UNIX': 115,
    'SC_XOPEN_VERSION': 116,
    'SC_XOPEN_XCU_VERSION': 121,
}

