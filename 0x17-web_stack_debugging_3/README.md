## Using `strace`

For this project the hint was to use `strace` to debug an http request returning 500.  
The trick here is using `strace` on a already running process (Apache2). That means we want to use `strace -p` (man page: Attach to the process with the process ID pid, using strace \<EXECUTABLE\> would start and run the executable).   
### What worked
In the docker container:  
0- Use `ps -faux` to see the pids, and not apache2. We have to use apache2 slaves pid, the master process will not give anything in our case.  
1- Use `strace -p <pid>` . At this point the process is waiting.  
In another terminal:  
2- `curl -sI <IP>:<PORT>` I needed to do it twice.  
Go back to container  
3- see what happened `open("/var/www/html/wp-includes/class-wp-locale.phpp", O_RDONLY) = -1 ENOENT (No such file or directory)
`  
4- fix, however the error message is not super explicit.  

## Using log files
Swati oriented me to this page on [SO](http://stackoverflow.com/questions/4731364/internal-error-500-apache-but-nothing-in-the-logs). The idea is since nothing appears in apache2 error logs, look into php error logs.  
To do so:  
0- locate php conf file (eg `/etc/php5/apache2/php.ini`)  
1- in that file set to `Yes` or anything related to writing errors in logs in the Error part of the file (set all values to development values)  
2- in another terminal `curl` like before.  
3- open the error log (`/var/log/apache2/error.log`) and read `PHP Fatal error:  require_once(): Failed opening required '/var/www/html/wp-includes/class-wp-locale.phpp' (include_path='.:/usr/share/php:/usr/share/pear') in /var/www/html/wp-settings.php on line 137`. Note this operation and 2 may need to be repeated.  
4- fix, this time you know where to look.  

_________
**Notes**:   
About puppet, I tried first to change a line using puppet, but that failed as this was not in the container's puppet. Then I tried to first check if the file existed, but that failed as well. Look at Tim's answer where he does it running a command and checks the return value.  
Intro to strace [here](http://hokstad.com/5-simple-ways-to-troubleshoot-using-strace).