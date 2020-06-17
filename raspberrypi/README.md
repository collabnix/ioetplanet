This is the complete guide starting from all the required installation to actual dockerizing and running of a node.js application.But first of all, why should we even dockerize our application?

1. You can launch an entire development environment on any computer supporting Docker which means you don’t have to install libraries, dependencies, download packages, etc.
2. Collaboration is really easy because of docker. The environment of the application remains compatible over the whole workflow. This implies that the app runs precisely the same way for developer, tester, and client, through development, staging, or production server.

Now that we have a reason, let’s start with docker!

1. Install Node.js & Npm on your Pi
Run the following command on a terminal to find out the version of node you require.

```
uname -m
```

My required version is ‘armv7’.

Next, to download node to your system,
go to https://nodejs.org/en/download/ and copy the link of your required version
Use wget on the terminal to download your version of the node.

```
wget https://nodejs.org/dist/v12.18.0/node-v12.18.0-linux-armv7l.tar.xz
```

Now, we need to extract the freshly downloaded archive. You will generally find your file in ‘Downloads’ folder under the name ‘node-v12.18.0-linux-armv7l.tar.xz’ (12.18.0 is the version of node I downloaded. Your version could differ)
Now to extract the files, use tar

```
tar -xf node-v12.18.0-linux-armv7l.tar.xz
```

Make sure you change the command according to your package’s version

now, go to the extracted folder.

``
cd node-v12.18.0-linux-armv7l/
```

Finally, check if node and npm has been properly installed

```
node -v
```

```
npm -v
```

If properly installed, these commands would return the versions of node and npm.

2. Create node app

To create the node.js app, first, we need a new directory where all our required files would reside.

```
mkdir docker-nodeapp
```

```
cd docker-nodeapp
```

now initialize your node project with a package.json which will hold the dependencies of the app. Use the following command and create a package.json by pressing enter to all the different prompts.

```
npm init
```

Let’s add the Express Framework as the first dependency:
now run

```
npm install express –save
```

This will create ‘app.js’ in the docker-nodeapp directory.

Now you will have these 3 files in docker-nodeapp directory


Open package.json, you will see that under dependencies express is specified with the version installed.


Let’s create our node application. Open app.js and copy the following code into the app.js file.

```
var express = require(‘express’) var app = express() app.get(‘/’, function (req, res) { res.send(‘Hello World!’) }) app.listen(8081, function () { console.log(‘app listening on port 8081!’) })
```

This is a simple node application with an HTTP server that will serve our Hello World website.

Now let’s run the app using node.

In a terminal, go in the directory docker-nodeapp and run app.js

```
node app.js
```

You will receive a log like this on your terminal

app listening on port 8081!

GREAT! You have deployed your node app.

you can view the app running in your browser at

http://localhost:8081/

You will see your Hello World website is deployed!


Hello World Website running on your local host

3. Install Docker on your Pi

For installing Docker on you Raspberry Pi, make sure that your SSH connection is enabled, your OS is updated and upgraded

Note: Opposed to most other Linux distributions, Raspberry Pi is based on ARM architecture. Hence, not all Docker images will work on your Raspberry Pi.

To install docker, run the following commands on the terminal`

```
curl -fsSL https://get.docker.com -o get-docker.sh
```
```
sudo sh get-docker.sh
```

once installed, check the version of docker to make sure everything is properly installed

```
docker -v
```

You will see the version of your docker displayed like this.


REBOOT AFTER CHECKING THE VERSION

Let’s run the Docker hello-world image provided by Docker.

```
docker run hello-world
```

You should see something like this.



Great!


You just created a Docker hello-world container. This is a simply ‘hello world’ program in Java running within a docker container

4. Create your Dockerfile

First of all, you will need to create an empty docker file in docker-nodeapp directory

```
touch Dockerfile
```

Open the newly created file in your code editor.

```
FROM node:12
WORKDIR /app
COPY package.json /app
RUN npm install
COPY . .
CMD node app.js
EXPOSE 8081
```

Create .dockerignore file in the same directory as your docker file and put the following lines of code in it.

```
node_modules npm-debug.log
```

This will prevent your local modules and debug logs from being copied onto your Docker image and possibly overwriting modules installed within your image.

5. Build your Docker image

To build your docker file using the command ‘docker build’.

```
docker build -t docker-nodeapp /full/path/to
```

or if you are in your project directory, you just need to use a dot

```
docker build -t docker-nodeapp .
```

The -t flag lets you tag your image so it’s easier to find later using the docker images command



Now to see your image listed by docker, run docker image in terminal

```
docker images
```


6. Run the Docker image

```
docker run -p 8080:8081 -d docker-nodeapp .
```


Running your image with -d runs the container in detached mode, leaving the container running in the background. The -p flag redirects a public port to a private port inside the container. Run the image you previously built.

Now you can go to http://localhost:8080/ and see your node app running within a docker container. you will notice that the port has changed from 8081 to 8080 as 8080 is our private port inside the container


There you go! you have successfully dockerized your application.
