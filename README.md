<h1 align="center">Self hosted IoT Temperature and Light level monitor</h1>

<p align="center">
  <img src="Images/DALLE_illustration_of_IoT.webp" alt="DALLE genererad bild" width="500">
  
  Image is generated with DALL*E
</p>

<p align="center">
  By: <a href="https://github.com/dwov">David Permlid.</a> - Student ID: dp222nr
</p>

## Overview
This is an IoT project for the course *Introduction to Applied IoT* at *Linneus University*.  

The purpose of this project is to monitor temperature, humidity, and light levels in a room, with the potential future goal of automating existing smart home appliances. The project utilizes a Raspberry Pi Pico and sensors to read and send data to a **MQTT** Broker hosted locally on computer of choice, where the data then will be displayed in **Node-RED**.

Q: **How much time will this take to make?**  
A: Approximately 5-6 hours

## Objective
The Goal: Monitor and Automate My Apartment  

I aim to monitor the environment in my one-room apartment and eventually automate my existing smart home setup, which includes some lights and a fan. I went for a locally self-hosted solution to increase security and remove limitations of free version of ex. *Adafruit*. This project provided an opportunity to delve into IoT technologies and hands-on DIY projects.

Exploring IoT basics, communications, and home automation has always intrigued me, but I never had the push to start. This course kickstarted my journey, sparking various ideas for future projects. 

*Stay tuned for updates on GitHub!*

### Project insights
This project and course have provided me with new knowledge about IoT concepts and IoT connectivity. But it has also come with some challenges, particularly in server-side setup, but it has been a rewarding experience nonetheless.

## Materials
### List of Material Needed, Including Description, Price, and Where to Buy

**Disclaimer:** The materials used in this project were purchased as part of the [Start Kit - Applied IoT at Linnaeus University](https://www.electrokit.com/lnu-starter). Not all components are used, so here are the components used.

| Image | Description | Where | Price |
| ------------- | ------------- | ------------- | ------------- |
| <img src="Images/piPicoWH.jpg" width="150"> | Raspberry Pi Pico WH | [electrokit](https://www.electrokit.com/raspberry-pi-pico-wh) | 109 SEK |
| <img src="Images/kopplingsBrada.jpg" width="150"> | Breadboard | [electrokit](https://www.electrokit.com/kopplingsdack-840-anslutningar) | 69 SEK |
| <img src="Images/jumperWire.jpg" width="150"> | Jumper wire M/M | [electrokit](https://www.electrokit.com/labbsladd-20-pin-15cm-hane/hane) | 29 SEK |
| <img src="Images/photoresistor.jpg" width="150"> | Photoresistor | [electrokit](https://www.electrokit.com/fotomotstand-cds-4-7-kohm) | 8 SEK |
| <img src="Images/mcp9700.jpg" width="150"> | MCP9700 | [electrokit](https://www.electrokit.com/mcp9700-to-92-temperaturgivare) | 12 SEK |
| <img src="Images/dht11.jpg" width="150"> | DHT11 | [electrokit](https://www.electrokit.com/digital-temperatur-och-fuktsensor-dht11) | 49 SEK |
| 10kΩ Resistor |  | Electronics store |  |
| Micro-USB | Cable | Anywhere |  |

\* All prices adjusted as of 2024-06-30 

- **Raspberry Pi Pico WH:** A microcontroller board based on Raspberry Pi's RP2040 chip, providing a cost-effective solution for DIY IoT projects.
- **Breadboard:** A reusable solderless prototyping board that allows for easy circuit experimentation and component connections.
- **Jumper wire M/M:** Male-to-male jumper wires for connecting components on a breadboard.
- **Photoresistor:** A light-sensitive resistor that changes its resistance based on the intensity of light.
- **MCP9700:** A temperature sensor that provides analog output proportional to the temperature.
- **DHT11:** A temperature and humidity sensor that provides digital output.

## Computer setup
How is the device programmed. Which IDE are you using. Describe all steps from flashing the firmware, installing plugins in your favorite editor. How flashing is done on MicroPython. The aim is that a beginner should be able to understand.

- Chosen IDE
- How the code is uploaded
- Steps that you needed to do for your computer. Installation of Node.js, extra drivers, etc.
#

https://hackmd.io/@lnu-iot/rkiTJj8O9

### Getting Started and Programming the Raspberry Pi Pico WH
To develop and run the code on the Raspberry Pi Pico on a Windows computer using Visual Studio Code, you will need to:
1. **Download and Install [Node.js LTS](https://Nodejs.org/en/)**
2. **Download and Install [Visual Studio Code](https://code.visualstudio.com/Download)**
3. **Download and Install Pymakr**

![bild](Images/pymakr_install.png)

4. **Flash MicroPython firmware onto Raspberry Pi Pico WH**
- Download the latest MicroPython firmware [here](https://micropython.org/download/rp2-pico-w).
- While holding the **BOOTSEL** button, connect your Raspberry Pi Pico WH to the computer. When plugged in, button can be released.
- A new drive should pop-up in file manager called **RPI-RP2**, copy and paste the firmware-file there.
- The device should now automatically disconnect from your computer.
- Replug the USB cable (without holding the BOOTSEL button). And voila!

If you have trouble setting things up or dont know how to start a project, I advice you to check the course's guides for [Installing VS Code and Pymakr](https://hackmd.io/@lnu-iot/rkiTJj8O9) and [Updating firmware of Pi Pico W + Test run code](https://hackmd.io/@lnu-iot/rkFw7gao_#Visual-Studio-Code) and also [Basic code structure](https://hackmd.io/@lnu-iot/B1T1_KM83)  

### Ubuntu Server and Mosquitto MQTT Setup
I did not have access to a seperate computer and do not want to install Linux as the main operating system at the time of doing this project so I had to improvise. I knew that Windows 11 could run virtual Linux with [WSL](https://learn.microsoft.com/en-us/windows/wsl/). So with that in mind I set it up on my laptop in a virutal Linux environment. (Which was a fight). This choice was made because I could not get Mosquitto MQTT to work directly on windows.

*If you want to run it natively on a seperate computer follow these steps from a previous student of the course. [HERE](https://github.com/Aleij/Smart_Horticulture/blob/main/README.md#ubuntu-server-setup)*  
*Another side-note: If you want to use Adafruit IO, you can skip this setup part and check out [this tutorial](https://hackmd.io/@lnu-iot/r1yEtcs55) on how to connect to Adafruit*

#
1. **Getting Setup with Ubuntu WSL**
    - Install WSL by following Microsofts guide linked above. Then Install Ubuntu from [Microsoft Store](https://www.microsoft.com/store/productId/9PDXGNCFSCZV?ocid=pdpshare).
    - Launch Ubuntu and a Termial window should pop-up, promting you to create an admin user. When successfull, make sure to update the software package.
    ```shell
    $ sudo apt update -y
    $ sudo apt upgrade -y
    ```
2. **Installing Mosquitto MQTT Broker**
    - In the Ubuntu termial window type:
    ```shell
    $ sudo apt install -y mosquitto mosquitto-clients
    ```
    - Enable autostart at boot.
    ```shell
    $ sudo systemctl enable mosquitto
    ```
    - Check Mosquitto version and support
    ```shell
    $ sudo mosquitto -h
    ```
    - You can start mosquitto with either
    ```shell
    $ sudo systemctl start mosquitto
    "or"
    $ sudo mosquitto
    ```
    We will use the latter one with some flags to specify a config file and run it in verbose mode (basically a debug mode where it prints more information).
    - To do this we will need a configuration file. I had trouble modifiying the default configuration so I created a new one in the conf.d file in the Mosquitto folder.  
    Lets create the file with,
    ```shell
    $ sudo touch /etc/mosquitto/conf.d/custom.conf
    "then type,"
    $ sudo nano /etc/mosquitto/conf.d/custom.conf
    "to edit the file."
    ```
    - In this file we want to add these lines
    ```shell
    listener 1883
    allow_anonymous true
    # The path to the usernames and passwords file
    password_file /etc/mosquitto/passwd
    # Give authorization access to specific topic to each user
    acl_file /etc/mosquitto/aclfile
    ```
    - Press ctrl + X, then ctrl + Y and then ENTER to save and exit.

    - Now create some users and give them a password,
    ```shell
    $ sudo mosquitto_passwd  -c /etc/mosquitto/passwd admin
    $ sudo mosquitto_passwd  /etc/mosquitto/passwd myUser
    "give mosquitto ownership"
    $ sudo chown mosquitto:mosquitto /etc/mosquitto/passwd
    ```
    - Now we need to edit/create a ACL file, create the file like above and place it ```/etc/mosquitto/aclfile```.
    - Sudo nano into file and add the following lines,
    ```shell
    user admin
    topic read $SYS/#
    topic readwrite devices/#

    user myUser
    topic readwrite devices/#
    ```
    - Restart mosquitto with
    ```shell
    $ sudo systemctl restart mosquitto
    ```

    If I was inclear in these steps (which are bascially a straight copy of the provided tutorial) check the [LNU tutorial](https://hackmd.io/@lnu-iot/rJr_nGyq5).

3. **Install Node-RED**
    - Follow Node-RED's tutorial on how to install it on Windows [HERE](https://Nodered.org/docs/getting-started/windows).
    - Run Node-RED in a normal terminal window in Windows with ```node-red```

4. **Connect Node-RED to Mosquitto MQTT**  
    When starting Node-RED it should give you the address and port to use for configuration, and since we are running this on one machine we can use ```localhost``` as our address which simplifies things alot (This is not the case later for Pi Pico).
    - The default port if ```1880```, use this to open up Node-RED's configuration page by typing ```localhost:1880``` in to your favorite browsers addressbar.
    - Add an ``"mqtt-in"`` and a ``"Debug"`` node to your flow.
    - Follow [this guide](https://hackmd.io/@lnu-iot/rJr_nGyq5#Connecting-Node-Red-to-Mosquitto-MQTT-Broker) until you've finished step 5.

5. **Now to the fun part of making this work for the Pi Pico**

## Putting everything together
How is all the electronics connected? Describe all the wiring, good if you can show a circuit diagram. Be specific on how to connect everything, and what to think of in terms of resistors, current and voltage. Is this only for a development setup or could it be used in production?

- Circuit diagram (can be hand drawn)
- *Electrical calculations
#
![bild](Images/Kopplingar_Visuellt.png)

## Chosen platform
Describe your choice of platform. If you have tried different platforms it can be good to provide a comparison.
Comment

Is your platform based on a local installation or a cloud? Do you plan to use a paid subscription or a free? Describe the different alternatives on going forward if you want to scale your idea.

- Describe platform in terms of functionality
- *Explain and elaborate what made you choose this platform

## The code
Import core functions of your code here, and don't forget to explain what you have done! Do not put too much code here, focus on the core functionalities. Have you done a specific function that does a calculation, or are you using clever function for sending data on two networks? Or, are you checking if the value is reasonable etc. Explain what you have done, including the setup of the network, wireless, libraries and all that is needed to understand.

## Data transmission and connectivity
How is the data transmitted to the internet or local server? Describe the package format. All the different steps that are needed in getting the data to your end-point. Explain both the code and choice of wireless protocols.

- How often is the data sent?
- Which wireless protocols did you use (WiFi, LoRa, etc …)?
- Which transport protocols were used (MQTT, webhook, etc …)
- *Elaborate on the design choices regarding data transmission and wireless protocols. That is how your choices affect the device range and battery consumption.

## Data presentation
Describe the presentation part. How is the dashboard built? How long is the data preserved in the database?

- Provide visual examples on how the dashboard looks. Pictures needed.
- How often is data saved in the database.
- *Explain your choice of database.
- *Automation/triggers of the data.

## Finalizing the design
Show the final results of your project. Give your final thoughts on how you think the project went. What could have been done in an other way, or even better? Pictures are nice!

- Show final results of the project
- Pictures
- *Video presentation
