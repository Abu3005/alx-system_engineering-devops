## Webstack debugging 4
In this project we are given a container.  

0. Sky is the limit  
Logged in the container, testing the Nginx web server with this ApacheBench command ` ab -c 100 -n 2000 localhost/` returns that half the requests fail.  
To debug, look into /var/log/nginx/error.log. There we find a recurrent error: *nginx accept4() failed (24: Too many open files)*.  
Some googling leads to [this link](https://gist.github.com/joewiz/4c39c9d061cf608cb62b). I put it here, because it taught me a few things, but that did not work.  
A better googling (ubuntu change Max open files nginx) returned [this](https://stackoverflow.com/questions/27849331/how-to-set-nginx-max-open-files) and I had my solution.