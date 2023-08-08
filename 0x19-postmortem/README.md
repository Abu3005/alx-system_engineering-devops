## Post Mortem for [webstack_debugging_2](../0x11-web_stack_debugging_2/)  

### Issue Summary  

At 9:15AM PT on 03-10-2017 it was found a security breach in one of the containers. 
Web server Nginx was run as root, listening on port 80. Service had to be interrupted on that port.
Service was completely down on that container for 15 minutes around 11:45AM.
Security breach was solved immediately and container resumed normal course of operations by 12:15PM PT. 

### Timeline

- 9:15AM engineer noticed problem during daily routine. Shut down Nginx.  
- 9:30AM list all users on container. Examine commands history.  
- 9:45AM examine configuration files.
- 11:00AM start fixing configuration files. 
- 11:45AM stop Apache2. Container is now out.  
- 12:00PM restart Nginx as another user. Check all is running smoothly.  

### Root Cause  

Earlier that day a new container was configured improperly due to lack of order and information in deployment/image files and directories.
After a routine check after its deployment, an engineer found the issue. It was found that the wrong configuration files were used.
The configuration created the user that was supposed to run Nginx, but the Nginx configuration files did not take that user into 
consideration. As Nginx starts automatically after install, we had to stop it first. 
As Nginx should not have been run as root then it should not have been listening on port 80. It was then found another bug,
as Apache was already running on this container on port 8080 instead of Nginx.  
Thankfully this was a single error, and no other containers were touched.

### Resolution and Recovery

It was decided to stop Nginx immediately because of security, and to keep using Apache as long as Nginx was not ready.
Then the set-up and configuration of the container were thoroughly examined to see what had been done. The Nginx user was there.
However Nginx configuration file was set up to be run as root. The file had to be changed to listen to port 8080 on IPv4 and IPv6.
Then it was decided to let the error logs, website root folders, configuration files as they were in the file system, and so they needed to be
tracked down to change their owner and their permission. Eventually Apache was stopped and Nginx started as the user.  

### Corrective and Preventative Measures

It was decided an overhaul of all the deployment/images directories and files to reorganize them. As it was difficult to identify
fast and clearly what needed to be done and where.  
Further along, all those files need to be better automated as to limit human involvement in the process and to make the whole procedure more transparent.
Those files will need to be thoroughly documented as it was found that neglect in the documentation was a triggering factor in that error.