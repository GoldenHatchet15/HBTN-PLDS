# Shell Basics & Permissions Lecture
**A Comprehensive Guide to Linux Command Line**

---

## Part 1: Shell Basics - Brief Review

### What is the Shell?

**Key Terminology:**
- **RTFM**: Read The Manual (tech slang for "consult the documentation")
- **Shell**: A command-line interpreter that processes commands and communicates with the operating system
- **Terminal**: The application window where you interact with the shell
- **Shell Prompt**: The text that appears waiting for your command (e.g., `$` for regular user, `#` for root)

**Popular Shells:**
- Bash (Bourne Again Shell) - most common
- Zsh (Z Shell)
- Fish (Friendly Interactive Shell)

---

### The Shebang (#!)

The shebang is the first line of a script that tells the system which interpreter to use.

**Format:**
```bash
#!/bin/bash
```

**Important Points:**
- Must be the very first line (no spaces before `#!`)
- Specifies the path to the interpreter
- Makes scripts executable as standalone programs
- Common shebangs: `#!/bin/bash`, `#!/bin/sh`, `#!/usr/bin/env python3`

**Example Script:**
```bash
#!/bin/bash
echo "Hello, World!"
```

---

### Navigation Commands

#### pwd - Print Working Directory
Shows your current location in the filesystem.

```bash
$ pwd
/home/user/documents
```

#### cd - Change Directory

```bash
cd /tmp              # Go to /tmp directory
cd ~                 # Go to home directory
cd                   # Also goes to home directory
cd -                 # Go to previous directory
cd ..                # Go up one directory level
cd /                 # Go to root directory
```

#### ls - List Directory Contents

```bash
ls                   # Basic list
ls -l                # Long format
ls -a                # Show hidden files
ls -la               # Long format with hidden files
ls -lan              # Long format with numeric IDs
```

---

### Understanding Directories

**Special Directories:**

| Symbol | Meaning | Example |
|--------|---------|---------|
| `.` | Current directory | `./script.sh` |
| `..` | Parent directory | `cd ..` |
| `~` | User's home directory | `/home/username` |
| `/` | Root directory | Top of filesystem |
| `/root` | Root user's home | Different from `/` |

**Hidden Files:**
- Files starting with `.` are hidden
- View with `ls -a` or `ls -la`
- Examples: `.bashrc`, `.profile`, `.gitignore`

---

### File and Directory Operations

#### Creating and Removing

```bash
# Create directory
mkdir my_directory
mkdir -p path/to/nested/directory    # Create nested directories

# Create empty file
touch filename.txt

# Remove file
rm filename.txt

# Remove directory
rmdir empty_directory               # Only works if empty
rm -r directory                     # Remove directory and contents
```

#### Copying and Moving

```bash
# Copy file
cp source.txt destination.txt
cp -r source_dir/ dest_dir/         # Copy directory recursively

# Move or rename
mv old_name.txt new_name.txt        # Rename
mv file.txt /tmp/                   # Move to different location
mv *.txt /backup/                   # Move all .txt files
```

---

### Examining Files

#### file - Determine File Type

```bash
$ file document.pdf
document.pdf: PDF document, version 1.4

$ file script.sh
script.sh: Bash shell script, ASCII text executable
```

#### less - View File Contents

```bash
less filename.txt
```

**Navigation in less:**
- `Space` or `Page Down` - Next page
- `b` or `Page Up` - Previous page
- `/pattern` - Search forward
- `?pattern` - Search backward
- `q` - Quit

---

### Links: Symbolic and Hard

#### Symbolic Links (Soft Links)
A pointer to another file (like a shortcut).

```bash
ln -s /path/to/original /path/to/link
ln -s /bin/ls __ls__
```

**Characteristics:**
- Points to a path (not the actual data)
- Breaks if the original file is deleted
- Can link to directories
- Can span different filesystems

#### Hard Links
Another name for the same file on disk.

```bash
ln /path/to/original /path/to/hardlink
```

**Characteristics:**
- Points to the same inode (actual data)
- Survives if the original name is deleted
- Cannot link directories
- Must be on the same filesystem

**Difference:**
- Symbolic link: "shortcut" that can break
- Hard link: duplicate name for same data

---

### Wildcards (Globbing)

Wildcards allow you to work with multiple files at once.

| Wildcard | Meaning | Example |
|----------|---------|---------|
| `*` | Matches any characters | `*.txt` (all .txt files) |
| `?` | Matches single character | `file?.txt` (file1.txt) |
| `[abc]` | Matches any character in brackets | `file[123].txt` |
| `[a-z]` | Matches range | `[A-Z]*` (starts with uppercase) |
| `[!abc]` | Matches any character NOT in brackets | `[!0-9]*` (no digits) |

**Examples:**

```bash
ls *.html                # All HTML files
rm file?.txt             # file1.txt, fileA.txt, etc.
cp [A-Z]* /tmp/u/        # Files starting with uppercase
rm *~                    # Delete backup files ending with ~
```

---

### Working with Commands

#### type - Identify Command Type

```bash
$ type cd
cd is a shell builtin

$ type ls
ls is aliased to `ls --color=auto'

$ type python3
python3 is /usr/bin/python3
```

#### which - Locate Executable

```bash
$ which python3
/usr/bin/python3
```

#### help - Built-in Help

```bash
help cd
help pwd
```

Use `help` for shell built-ins (cd, pwd, etc.).

#### man - Manual Pages

```bash
man ls
man chmod
man 5 passwd        # Section 5 (file formats) of passwd
```

---

### Man Page Sections

| Section | Contents |
|---------|----------|
| 1 | User commands |
| 2 | System calls |
| 3 | Library functions |
| 5 | File formats and conventions |
| 8 | System administration commands |

**Reading Man Pages:**
- Press `Space` for next page
- Press `q` to quit
- Press `/` to search
- Press `h` for help

---

### Command History and Shortcuts

#### History

```bash
history                 # Show command history
!123                    # Execute command 123 from history
!!                      # Execute last command
!ls                     # Execute last command starting with 'ls'
```

#### Bash Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl + A` | Move to beginning of line |
| `Ctrl + E` | Move to end of line |
| `Ctrl + U` | Delete from cursor to beginning |
| `Ctrl + K` | Delete from cursor to end |
| `Ctrl + L` | Clear screen |
| `Ctrl + R` | Search command history |
| `Tab` | Auto-complete |

---

### LTS (Long Term Support)

**What does LTS mean?**
- Stands for "Long Term Support"
- Version of software supported for extended period
- Ubuntu 22.04 LTS: Supported for 5 years
- Receives security updates and bug fixes
- Recommended for production systems requiring stability

---

### Script Requirements Recap

**All scripts must:**
1. Be exactly 2 lines long (`wc -l` should print 2)
2. Start with `#!/bin/bash`
3. End with a new line
4. Be executable (`chmod u+x script.sh`)
5. Not use backticks, `&&`, `||`, or `;`

**Example:**
```bash
#!/bin/bash
pwd
```

---

## Part 2: Shell Permissions - Full Lecture

### Introduction to Permissions

Linux is a multi-user system. Permissions control who can read, write, or execute files.

**Three Permission Groups:**
1. **Owner** (u) - The user who owns the file
2. **Group** (g) - Users in the file's group
3. **Others** (o) - Everyone else

**Three Permission Types:**
1. **Read** (r) - View file contents or list directory
2. **Write** (w) - Modify file or add/remove files in directory
3. **Execute** (x) - Run file as program or enter directory

---

### Understanding Permission Notation

#### Long Format Listing

```bash
$ ls -l
-rwxr-xr-- 1 julien staff 1234 Oct 10 12:00 script.sh
```

**Breaking it down:**
```
-rwxr-xr--  1  julien  staff  1234  Oct 10 12:00  script.sh
│││││││││  │    │       │      │       │          │
│││││││││  │    │       │      │       │          └─ filename
│││││││││  │    │       │      │       └─ modification time
│││││││││  │    │       │      └─ size in bytes
│││││││││  │    │       └─ group owner
│││││││││  │    └─ user owner
│││││││││  └─ number of hard links
│└┼┼└┼┼└┼┼─ permissions
│ ││ ││ ││
│ ││ ││ └┴─ others permissions (r--)
│ ││ └┴─── group permissions (r-x)
│ └┴───── owner permissions (rwx)
└──────── file type (- = regular file, d = directory, l = link)
```

---

### File Types

The first character indicates file type:

| Symbol | Type |
|--------|------|
| `-` | Regular file |
| `d` | Directory |
| `l` | Symbolic link |
| `c` | Character device |
| `b` | Block device |
| `p` | Named pipe |
| `s` | Socket |

---

### Numeric (Octal) Permissions

Each permission has a numeric value:
- **Read (r) = 4**
- **Write (w) = 2**
- **Execute (x) = 1**

**Calculate by adding values:**

| Permissions | Calculation | Value |
|-------------|-------------|-------|
| `rwx` | 4+2+1 | 7 |
| `rw-` | 4+2+0 | 6 |
| `r-x` | 4+0+1 | 5 |
| `r--` | 4+0+0 | 4 |
| `-wx` | 0+2+1 | 3 |
| `-w-` | 0+2+0 | 2 |
| `--x` | 0+0+1 | 1 |
| `---` | 0+0+0 | 0 |

**Example:**
- `755` = `rwxr-xr-x` (owner: rwx, group: r-x, others: r-x)
- `644` = `rw-r--r--` (owner: rw-, group: r--, others: r--)
- `600` = `rw-------` (owner: rw-, group: ---, others: ---)

---

### chmod - Change Mode (Permissions)

#### Symbolic Mode

**Format:** `chmod [who][operation][permissions] file`

**Who:**
- `u` - user (owner)
- `g` - group
- `o` - others
- `a` - all (same as ugo)

**Operations:**
- `+` - add permission
- `-` - remove permission
- `=` - set exact permission

**Examples:**

```bash
# Add execute for owner
chmod u+x script.sh

# Add execute for everyone
chmod a+x script.sh
chmod +x script.sh              # Same as above

# Add multiple permissions
chmod u+x,g+x,o+r file.txt

# Remove write for group and others
chmod go-w file.txt

# Set exact permissions
chmod u=rwx,g=rx,o=r file.txt
```

#### Numeric Mode

```bash
chmod 755 script.sh             # rwxr-xr-x
chmod 644 file.txt              # rw-r--r--
chmod 600 private.txt           # rw-------
chmod 007 file.txt              # -------rwx
chmod 753 file.txt              # rwxr-x-wx
```

**Common Permission Sets:**
- `777` - Everyone can do everything (dangerous!)
- `755` - Owner full, others read/execute (scripts, directories)
- `644` - Owner read/write, others read only (regular files)
- `600` - Owner read/write only (private files)
- `700` - Owner only (private directories)

---

### Practical chmod Examples

#### Task 5: Execute Permission
```bash
#!/bin/bash
chmod u+x hello
```

#### Task 6: Multiple Permissions
```bash
#!/bin/bash
chmod u+x,g+x,o+r hello
```
Or using numeric: `chmod 554 hello`

#### Task 7: Everybody Execute
```bash
#!/bin/bash
chmod a+x hello
```
Or: `chmod +x hello` or `chmod 111 hello` (adds execute only)

#### Task 8: James Bond (007)
```bash
#!/bin/bash
chmod 007 hello
```
Result: `-------rwx` (only others have full permissions)

#### Task 9: John Doe (753)
```bash
#!/bin/bash
chmod 753 hello
```
Result: `rwxr-x-wx`

---

### chmod on Directories

```bash
# Add execute permission to all subdirectories
chmod +X *                      # Capital X affects only directories

# Recursive permission change
chmod -R 755 directory/         # Changes directory and all contents
```

**Task 11: Execute on Subdirectories**
```bash
#!/bin/bash
chmod a+X *
```
The capital `X` adds execute only to directories, not regular files.

---

### chown - Change Owner

**Format:** `chown [owner][:group] file`

**Examples:**

```bash
# Change owner only
chown betty hello

# Change owner and group
chown betty:staff hello

# Change owner, keep group
chown betty: hello

# Recursive
chown -R betty directory/
```

**Task 3: New Owner**
```bash
#!/bin/bash
chown betty hello
```

**Task 14: Change Owner and Group**
```bash
#!/bin/bash
chown vincent:staff *
```

**Important:** Normal users cannot chown files to other users (only root can).

---

### chgrp - Change Group

**Format:** `chgrp group file`

**Examples:**

```bash
# Change group
chgrp school hello

# Recursive
chgrp -R staff directory/
```

**Task 13: Change Group**
```bash
#!/bin/bash
chgrp school hello
```

---

### Changing Ownership of Symbolic Links

Use the `-h` flag to change the link itself, not the target:

**Task 15: Symbolic Link Permissions**
```bash
#!/bin/bash
chown -h vincent:staff _hello
```

Without `-h`, it would change the target file instead of the link.

---

### Conditional Ownership Change

**Task 16: Change Owner Only If...**
```bash
#!/bin/bash
chown --from=guillaume vincent hello
```

This only changes ownership if the current owner is `guillaume`.

---

### su and sudo

#### su - Switch User

```bash
su betty                        # Switch to user betty (requires betty's password)
su                              # Switch to root (requires root password)
su -                            # Switch to root with root's environment
```

**Task 0: I am Betty**
```bash
#!/bin/bash
su betty
```

#### sudo - Execute as Superuser

```bash
sudo command                    # Run command as root
sudo -u betty command          # Run command as betty
sudo su                        # Become root (requires your password)
```

**Key Difference:**
- `su` - Switch to another user (need their password)
- `sudo` - Execute command with elevated privileges (need your password)

---

### User and Group Information

#### whoami - Print Current Username

```bash
$ whoami
julien
```

**Task 1: Who Am I**
```bash
#!/bin/bash
whoami
```

#### id - Print User and Group IDs

```bash
$ id
uid=1000(julien) gid=1000(julien) groups=1000(julien),27(sudo)

$ id -u                         # Just user ID
1000

$ id -g                         # Just group ID
1000
```

#### groups - Print Group Memberships

```bash
$ groups
julien adm cdrom sudo
```

**Task 2: Groups**
```bash
#!/bin/bash
groups
```

---

### Creating Users and Groups

#### adduser - Interactive User Creation

```bash
sudo adduser newuser
```

Prompts for password and user information.

#### useradd - Low-level User Creation

```bash
sudo useradd -m -s /bin/bash newuser
sudo passwd newuser
```

**Options:**
- `-m` - Create home directory
- `-s` - Set login shell
- `-G` - Add to additional groups

#### addgroup - Create Group

```bash
sudo addgroup newgroup
```

#### Adding User to Group

```bash
sudo usermod -aG groupname username
```

---

### mkdir with Permissions

You can set permissions when creating a directory:

**Task 12: Create Directory with Permissions**
```bash
#!/bin/bash
mkdir -m 751 my_dir
```

This creates `my_dir` with permissions `rwxr-x--x` (751).

---

### Permission Best Practices

**Security Guidelines:**

1. **Principle of Least Privilege**: Give minimum permissions necessary
2. **Avoid 777**: Never use unless absolutely necessary
3. **Private Files**: Use 600 for sensitive files
4. **Shared Files**: Use 644 for world-readable, 664 for group-writable
5. **Executables**: Use 755 for scripts/programs
6. **Directories**: Need execute permission to access contents

**Common Scenarios:**

| Use Case | Permission | Numeric |
|----------|-----------|---------|
| Private file | `rw-------` | 600 |
| Public file | `rw-r--r--` | 644 |
| Script | `rwxr-xr-x` | 755 |
| Private script | `rwx------` | 700 |
| Shared folder | `rwxrwxr-x` | 775 |
| Web files | `rw-r--r--` | 644 |
| Web directories | `rwxr-xr-x` | 755 |

---

### Quick Reference: Permission Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `chmod` | Change permissions | `chmod 755 file` |
| `chown` | Change owner | `chown user file` |
| `chgrp` | Change group | `chgrp group file` |
| `su` | Switch user | `su betty` |
| `sudo` | Execute as root | `sudo rm file` |
| `whoami` | Current username | `whoami` |
| `id` | User/group IDs | `id -u` |
| `groups` | List groups | `groups` |
| `umask` | Default permissions | `umask 022` |

---

### Testing Your Scripts

**Make script executable:**
```bash
chmod u+x script.sh
```

**Run script:**
```bash
./script.sh
```

**Check script format:**
```bash
wc -l script.sh                 # Should output 2
head -n 1 script.sh             # Should show #!/bin/bash
```

**Debug permissions:**
```bash
ls -l file                      # View current permissions
stat file                       # Detailed file information
```

---

### Common Mistakes to Avoid

1. **Forgetting the shebang**: Always start with `#!/bin/bash`
2. **Wrong line count**: Scripts must be exactly 2 lines
3. **Not making executable**: Use `chmod u+x` before running
4. **Using prohibited operators**: No backticks, `&&`, `||`, or `;`
5. **Wrong permission values**: Remember: r=4, w=2, x=1
6. **Forgetting sudo**: Many permission changes require root access
7. **Changing symlink target**: Use `-h` with chown to change the link itself

---

### Practice Exercise Solutions

**Create file and set permissions:**
```bash
#!/bin/bash
touch hello
```

**List with hidden files:**
```bash
#!/bin/bash
ls -la
```

**Create directory with specific permissions:**
```bash
#!/bin/bash
mkdir -m 751 my_dir
```

**Change owner and group:**
```bash
#!/bin/bash
chown vincent:staff *
```

**Add execute to all subdirectories:**
```bash
#!/bin/bash
chmod a+X *
```

---

## Summary

### Shell Basics Key Takeaways:
- The shell is your command-line interface to the operating system
- Navigation: `pwd`, `cd`, `ls`
- File operations: `cp`, `mv`, `rm`, `mkdir`
- Links: symbolic (shortcuts) vs hard (duplicate names)
- Wildcards: `*`, `?`, `[]` for pattern matching
- Get help: `man`, `help`, `type`, `which`

### Permissions Key Takeaways:
- Three groups: owner, group, others
- Three permissions: read (4), write (2), execute (1)
- Use `chmod` to change permissions
- Use `chown` to change owner
- Use `chgrp` to change group
- `sudo` for root privileges
- Always follow principle of least privilege

---

## Resources

**Read more:**
- The Linux Command Line by William Shotts
- man bash
- man chmod
- man chown
- https://linuxcommand.org/

**Practice:**
- Try commands in a safe environment
- Use `man` pages extensively
- Experiment with permissions on test files
- Create scripts and make them executable

---

**End of Lecture**

Questions? Remember: RTFM and practice, practice, practice!