# Basic commands
Every day basic commands

[command] "ls" list files
[short_info] lists the files in the current directory (or optionaly also in all subdirectories)
[example_1] "ls"
[exampel_2] "ls -la" list all files (including hidden files)
[example_3] "ls -laR | grep -i readme"   
list all files (option la), including subdirectories (option R), pipe result to 'grep' command and then only show files that contain 'readme' (option -i, case insensitiv)

[command] "dir"
[short_info] lists the files in a directory

[command] "cp" copy files
[short_info] Copies files or directories.
[example_1] "cp file1.txt file2.txt" makes a copy form file1.txt to file2.txt


# Networking
Check and troubleshoot network settings.

[command] "ip" Show IP address
[example_1] "ip a" Displays network interfaces.

[command] "ping" Ping host
[short_info] Tests network connectivity.
[example_1] "ping google.com"
[example_2] "ping 8.8.8.8"
