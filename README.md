# backend-dirwatcher

### Objectives

* Create a long running program
* Demonstrate signal handling
* Demonstrate program logging
* Use exception handling to keep the program running
* Create and structure your own code repository using best practices
* Show that you know how to read a set of requirements and deliver on them, asking for clarification if anything is unclear.

### Description
For this assessment you will create your own small long-running program named `dirwatcher.py`.  This will give you experience in structuring a long-running program, which will help you with the SlackTweet project later on. The `dirwatcher.py` program should accept some command line arguments that will instruct it to monitor a given directory for text files that are created within the monitored directory.  Your `dirwatcher.py` program will continually search within all files in the directory for a 'magic' string which is provided as a command line argument.  This can be implemented with a timed polling loop.  If the magic string is found in a file, your program should log a message indicating which file and line number the magic text was found.  Once a magic text occurrence has been logged, it should not be logged again unless it appears in the file as another subsequent line entry later on.

Files in the monitored directory may be added or deleted or appended at any time by other processes.  Your program should log a message when new files appear or other previously watched files disappear.  Assume that files will only be changed by appending to them.  That is, anything that has previously been written to the file will not change.  Only new content will be added to the end of the file.  You don't have to continually re-check sections of a file that you have already checked.

Your program should terminate itself by catching SIGTERM or SIGINT (be sure to log a termination message).  The OS will send a signal event to processes that it wants to terminate from the outside.  Think about when a sys admin wants to shutdown the entire computer for maintenance with a `sudo shutdown` command.  If your process has open file handles, or is writing to disk, or is managing other resources, this is the OS way of telling your program that you need to cleanup, finish any writes in progress, and release resources before shutting down.

NOTE that handling OS signals and polling the directory that is being watched are two separate functions of your program.  You won't be getting an OS signal when files are created or deleted.

### Criteria

| Criteria | Ratings |
| --- | --- |
| Cmd Line Arguments | Program should accept cmd line arguments for directory to watch (dir), file extension to filter on (ext), polling interval (int) and magic text (magic). Polling interval defaults to 1.0 seconds. If the target watch directory does not exist, program should log an appropriate event message for each interval, e.g. "directory XXXXX does not exist" |
| Magic text detection | Magic text sequences are detected within files. Detection events are logged, with file line numbers. If a line contains multiple magic strings, only one message is logged. Any previously detected magic text should not be logged again. |
| OS Signal Handler | Program should respond to SIGINT and SIGTERM signals from the OS. signal events should be logged so that a human can determine what the signal was. Program should terminate upon either signal. |
| Exception handler | The program should have one or more exception (try/except) handlers. Program should stay running even if the entire watched directory is suddenly deleted. Also Stay running if a watched file is deleted. Log an appropriate event message in these cases. |
| Logging | All log messages should contain timestamps. Events to log are startup BANNER, shutdown BANNER, exceptions, magic text found events, files added or removed from watched dir, and OS signal events. There should be ONLY ONE termination (exit) point for the program. |
| Repo | Use previously cloned repos as examples: Your Repo must have a .gitignore file. Repo shall not contain any log files, or test directories or test files. Repo shall not contain a virtual environment. Repo MUST have a descriptive README.md that explains what the program does, and and its configuration and runtime options. Source code should have docstrings, __author__ header and pass all PEP8 (flake8) tests. Any meaningless commit messages such as "Done", "Finished", "Completed", "Debugged Code" and the like, shall be awarded negative points. |