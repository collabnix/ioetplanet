NVIDIA Jetson devices are powerful platforms designed for edge AI applications, offering excellent GPU acceleration capabilities to run compute-intensive tasks like language model inference. 

With official support for NVIDIA Jetson devices, Ollama brings the ability to manage and serve Large Language Models (LLMs) locally, ensuring privacy, performance, and offline operation. By integrating Open WebUI, you can enhance your workflow with an intuitive web interface for managing these models.

This guide will walk you through setting up Ollama on your Jetson device, integrating it with Open WebUI, and configuring the system for optimal GPU utilization. Whether you're a developer or an AI enthusiast, this setup allows you to harness the full potential of LLMs right on your Jetson device.

## Pre-requisite

1. [Jetson Nano](https://developer.nvidia.com/embedded/jetson-nano)
2. A 5V 4Ampere Charger
3. 64GB SD card
4. WiFi Adapter
5. Wireless Keyboard
6. Wireless mouse



![Image32](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cw8ms0ek90od5rrhd0uv.png)


## Software

- Download Jetson SD card image from [this link](https://developer.nvidia.com/embedded/downloads)
- Raspberry Pi Imager installed on your local system


## Preparing Your Jetson Nano

1. Unzip the SD card image
2. Insert SD card into your system.
3. Bring up Raspberry Pi Imager tool to flash image into the SD card


### Step 0. Verify the Jetson device


![Image1](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rar7xc470wz6m9wk6nu0.png)



Begin by verifying the L4T (Linux for Tegra) version on your Jetson device. Each Jetson platform runs a specific JetPack version tied to an L4T release. To check your configuration:

```
cat /etc/nv_tegra_release
# R32 (release), REVISION: 7.1, GCID: 29818004, BOARD: t210ref, EABI: aarch64, DATE: Sat Feb 19 17:05:08 UTC 2022
```

This output confirms the device is using L4T R32.7.1, compatible with JetPack 4.6.1. Ensure your Jetson device is updated to the latest supported L4T version to avoid compatibility issues.



### Step 1. Update the APT repository

Ensure your system is up to date to avoid errors during the installation of dependencies:

```
sudo apt update
```

### Step 2. Install the curl package

The Ollama installation script requires curl to fetch and execute:

```
sudo apt install curl
```

### Step 3. Install Ollama

Install Ollama using its official installation script, which automatically sets up the required services and permissions:

```
curl -fsSL https://ollama.com/install.sh | sh
```

```
>>> Adding ollama user to video group...
>>> Adding current user to ollama group...
>>> Creating ollama systemd service...
>>> Enabling and starting ollama service...
Created symlink /etc/systemd/system/default.target.wants/ollama.service → /etc/systemd/system/ollama.service.
>>> NVIDIA JetPack ready.
>>> The Ollama API is now available at 127.0.0.1:11434.
>>> Install complete. Run "ollama" from the command line.
```

Ollama is now ready to run locally, leveraging your Jetson’s GPU for efficient LLM inference.

### Step 4. Explore the  Ollama CLI

Ollama provides a CLI to manage and interact with models. To view available commands:

```
ollama
Usage:
  ollama [flags]
  ollama [command]

Available Commands:
  serve       Start ollama
  create      Create a model from a Modelfile
  show        Show information for a model
  run         Run a model
  stop        Stop a running model
  pull        Pull a model from a registry
  push        Push a model to a registry
  list        List models
  ps          List running models
  cp          Copy a model
  rm          Remove a model
  help        Help about any command

Flags:
  -h, --help      help for ollama
  -v, --version   Show version information

Use "ollama [command] --help" for more information about a command.
```

### Step 5. List Available Models

Check the preloaded models available in Ollama:

```
$ ollama list
NAME                     ID              SIZE      MODIFIED
llama3:latest            365c0bd3c000    4.7 GB    4 weeks ago
codellama:latest         8fdf8f752f6e    3.8 GB    4 months ago
codellama:7b-instruct    8fdf8f752f6e    3.8 GB    4 months ago
llama3:8b                365c0bd3c000    4.7 GB    4 months ago
mistral:latest           61e88e884507    4.1 GB    9 months ago
llama2:latest            78e26419b446    3.8 GB    10 months ago
```

### Step 6. Run a model

Run the llama3 model and perform tasks like generating Python code:

```
ollama run llama3
>>> > Can you write a Python script to calculate the factorial of a number?
Sure! Here’s the code:

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}")
```

## Integrating Open WebUI with Ollama

Open WebUI complements Ollama by providing an intuitive web-based interface to manage and interact with LLMs.

## Step 1: Stop the Ollama Service

Before proceeding, stop the system-wide Ollama service to avoid conflicts when running it in Docker:


```
sudo systemctl disable ollama
```

## Step 2. Run Ollama with Docker

Deploy Ollama as a Docker container with GPU support:

```
sudo docker run -d --gpus=all --runtime=nvidia -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

```

## Step 3. Run Open WebUI

Run Open WebUI with GPU acceleration in a separate Docker container:

```
sudo docker run -d -p 3000:8080 --gpus all --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:cuda
```

## Step 4. Verify Running Containers

Ensure both Ollama and Open WebUI containers are running correctly:


```
sudo docker ps
CONTAINER ID   IMAGE                                COMMAND               CREATED          STATUS                            PORTS                                           NAMES
dee2d1fbe4cf   ghcr.io/open-webui/open-webui:cuda   "bash start.sh"       10 seconds ago   Up 6 seconds (health: starting)   0.0.0.0:3000->8080/tcp, :::3000->8080/tcp       open-webui
9fd89a4fa908   ollama/ollama                        "/bin/ollama serve"   52 seconds ago   Up 48 seconds                     0.0.0.0:11434->11434/tcp, :::11434->11434/tcp   ollama
```

## Results:

```
cuda: Pulling from open-webui/open-webui
6d29a096dd42: Pull complete
6fab32a80202: Pull complete
610eb561c31b: Pull complete
50c0fb1f456e: Pull complete
ae5672aeb8ae: Pull complete
4f4fb700ef54: Pull complete
639718444375: Pull complete
5dcf97af08b1: Pull complete
ea9079f84622: Pull complete
e3fc97a4f07a: Pull complete
a538afa31f12: Pull complete
86ede3d9066a: Pull complete
a5aa461a25d1: Pull complete
6acc9cdc9b03: Pull complete
1920af2d5f9d: Pull complete
Digest: sha256:781acd8f2b45bdf45ac9a89fa80d52a6a966d9e1e7b55fbb5f0f1397ce5d9515
Status: Downloaded newer image for ghcr.io/open-webui/open-webui:cuda
843100c8d64d0ab9ea78fd64f4ffced0a62ce8783c850ce66d7ebb890f102e5a
```

```
ajeetraina@ajeetraina-desktop:~$ sudo docker ps
[sudo] password for ajeetraina:
CONTAINER ID   IMAGE                                COMMAND           CREATED         STATUS                     PORTS                                       NAMES
843100c8d64d   ghcr.io/open-webui/open-webui:cuda   "bash start.sh"   4 minutes ago   Up 4 minutes (unhealthy)   0.0.0.0:3000->8080/tcp, :::3000->8080/tcp   open-webui
```

## Bundled Installation of Open WebUI with Ollama

For a simplified setup, you can use a bundled Docker image that integrates both Open WebUI and Ollama.

### Using GPU

This installation method uses a single container image that bundles Open WebUI with Ollama, allowing for a streamlined setup via a single command. Choose the appropriate command based on your hardware setup:

```
sudo docker run -d -p 3000:8080 --gpus=all -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
```

### Using CPU only

For CPU Only: If you're not using a GPU, use this command instead:

```
sudo docker run -d -p 3000:8080 -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
```

Both commands facilitate a built-in, hassle-free installation of both Open WebUI and Ollama, ensuring that you can get everything up and running swiftly.

## Conclusion

Once configured, Open WebUI can be accessed at http://localhost:3000, while Ollama operates at http://localhost:11434. This setup provides a seamless and GPU-accelerated environment for running and managing LLMs locally on NVIDIA Jetson devices.

This guide showcases the power and versatility of NVIDIA Jetson devices when paired with Ollama and Open WebUI, enabling advanced AI workloads at the edge with ease and efficiency.


