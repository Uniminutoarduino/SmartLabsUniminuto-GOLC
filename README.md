# SmartLabsUniminuto-GOLC

This is the online repository for the GOLC_2022 international award. In this repository, you can find the main information concerning the laboratory (smartlabsuniminuto), e.g., structure, features, modes of programming, educational goals and outcomes, and presentation video. For more information about this award, please consult the link (http://online-engineering.org/GOLC_online-lab-award.php)

# 1. What is *Smartlabsuniminuto*?

*Smartlabsuniminuto*  is an initiative about low-cost remote laboratories for teaching and learning programming and control systems in academic programs of engineering and technology. The project was developed at the university Corporación Universitaria Minuto de Dios-UNIMINUTO ([https://www.uniminuto.edu/](https://www.uniminuto.edu/)) , Bogotá, Colombia, involving the programs of Technology in Electronics, Systems Engineering, and Industrial Engineering. *Smartlabsuniminuto* is available at https://www.smartlabsuniminuto.com/

The laboratory arose according to the educational problems regarding experimentation, hands-on activities, and learning by doing produced by the COVID-19 pandemic in 2020 from the second semester. The laboratory is focused on programming through Python Language and a beta version for control systems education with a level control plant. With the laboratory, the students can program in Python language and interact with hardware devices that have been interfaced with a Raspberry Pi in each node (Physical Computing). The remote laboratory is available in Spanish. Among the main features of *Smartlabsuniminuto*, we have:

<img src="https://user-images.githubusercontent.com/11606241/134404259-5af59424-fdb3-4c48-b344-de1bbe3d9db6.png" align="left" width="900">

###### Fig 1. Main feaures of smartlabsuniminuto.

If you want to more information about *smartlabsuniminuto*, please see these presentations (click on the image):

**(English Presentation):**

<a href="http://www.youtube.com/watch?feature=player_embedded&v=4iBcO_PigIo
" target="_blank"><img src="http://img.youtube.com/vi/4iBcO_PigIo/0.jpg" 
alt="Blocks-based programming" width="400" height="300" border="2" /></a>

**(Spanish Presentation):**

<a href="http://www.youtube.com/watch?feature=player_embedded&v=bnkgsYKd124
" target="_blank"><img src="http://img.youtube.com/vi/bnkgsYKd124/0.jpg" 
alt="Blocks-based programming" width="400" height="300" border="2" /></a>


## 1.1 Programming modes
Searching to expand the scope of students that could use our laboratory, we developed two programming modes (text-based, block-based). Please, click on the images to see the videos on YouTube.

### 1.1.1 Text-based programming
There, the students can program directly in Python Language. This mode could be used by students with experience in programming or who desire to know the statements and structure of Python.

<a href="http://www.youtube.com/watch?feature=player_embedded&v=1azGjeaalZ0
" target="_blank"><img src="http://img.youtube.com/vi/1azGjeaalZ0/0.jpg" 
alt="Text-based programming" width="500" height="350" border="2" /></a>

### 1.1.2 blocks-based programming
There, the students can program using graphical blocks (Blockly). This mode could be used by novice students. In any moment the students can see the Python code for their blocks.


<a href="http://www.youtube.com/watch?feature=player_embedded&v=TnZlTCT3V1w
" target="_blank"><img src="http://img.youtube.com/vi/TnZlTCT3V1w/0.jpg" 
alt="Blocks-based programming" width="500" height="350" border="2" /></a>

The help of these modes of programming with the educational materials is available at the following link: https://seconlearning.com/smartlabsuniminuto/doku.php

## 1.2 Hardware
We have developed a low-cost module in a 3D printer to ensemble the different hardware elements employed in each node. Also, each module (0-17) counts with a robotic arm with 2 Degree of Freedom (DOF) and several additional components as it will be described in table 1. With the elements elaborated in a 3D printer, we accelerated the process of construction of the remote laboratory. 

<img src="https://user-images.githubusercontent.com/11606241/134495226-8488ba42-5131-460d-9ac9-fa17a9a82497.jpeg" width="300"><img src="https://user-images.githubusercontent.com/11606241/134497125-bb9c9359-bc7d-4bb7-937f-ba6ceebc54ae.jpg" width="400"><img src="https://user-images.githubusercontent.com/11606241/134805857-c008500d-0838-44ef-bab6-17514d280919.jpg" width="400"><img src="https://user-images.githubusercontent.com/11606241/134805860-f1c307ab-2137-4fa2-bea5-ec5a15d11119.jpg" width="300"><img src="https://user-images.githubusercontent.com/11606241/137200799-abe28300-d6ff-41e0-bcac-bfb2a151c157.jpg" width="300"><img src="https://user-images.githubusercontent.com/11606241/134495354-20166d25-2311-4edf-8eae-a30adc68fc31.jpg" width="300">

###### Fig 2. Hardware components and materials. For the control plant (last picture), 1. Camera, 2. Raspberry module for sensor and motor pumps, 3. Tank control system. 

The nodes count with the following hardware devices and materials:

| Node | Description | Hardware components
| ------------- | ------------- | ------------- |
| 1-16 | Nodes for programming |Raspberry Pi V4 (2GB), protoboard (830 points), 4 leds, 1 display tm1637, 1 LCD (2x16), 1 robotic arm (2 DOF), 8Mpx Camera, 1 camera support.|
| 17  | Node for control systems. Control Plant (Tank system)  | Raspberry Pi V4 (2GB), motor pump (2), Ultrasonic sensor (US-016), Analog to Digital Converter (ADC) AD1115, 8Mpx Camera, 1 camera support. |
| 18  | Nodes for programming and sensing  |Raspberry Pi V4 (2GB), protoboard (830 points), 4 leds, 1 display tm1637, 1 LCD (2x16), 1 robotic arm (2 DOF), 1 temperature sensor TMP100, 1 lamp, 1 light-dimmer module, 8Mpx Camera, 1 camera support.|

###### Table 1. Description of hardware components used in the nodes.

# 2. Educational concepts and outcomes with the laboratory 
Our primary goal with *Smartlabsuniminuto* is to support the educational process of the students in programming, physical computing, and control systems from a constructivist point of view. At the start of the project (year 2020), we developed 15 nodes to support the teaching and learning of programming and physical computing. As part of different improvements, several students in their final year want to create additional modules for the Remote Laboratory (RL). Thus, a tank control system that can be programmed in Python language was created and interfaced with the RL.  

*Smartlabsuniminuto* have been tested by roughly *n=60* students from 2020 to 2021 (first semester). Currently, 40 additional students are using the laboratory for educational purposes. The test in a real educational setting was divided into the following stages:

- We tested the remote laboratory with n=30 students of Systems Engineering in 2020 (second semester). The average age of the students was 18.5 years with a students' distribution of 90% male and 10% female.
- We have tested the remote laboratory with n=30 students of Systems Engineering in 2021 (first semester). The average age of the students was 19.1 years with a students' distribution of 87.71% male and 12.29% female.

To collect the information and perceptions of the students about the remote laboratory in the courses, we developed two surveys (2020-2021) according to the Technology Acceptance Model (TAM). In general terms, the students have had a good acceptance of the laboratory which was manifested by the comments and the descriptive statistics in each category of the surveys. To know in-depth the results in (2020), please, consult the folder *Article (Paper IEEE Rita-preprint)* in this repository. This is a preprint article presented to the IEEE journal (Revista Iberoamericana de Tecnologias de Aprendizaje-RITA-http://rita.det.uvigo.es/IEEERITA2018/). The article was accepted with minor revisions and it could give an idea about the elements such as technical as educational taken into account in the remote laboratory. 

If you want to see the surveys with the responses of the students in Google Forms, please see the following links:
- 2020 (https://docs.google.com/spreadsheets/d/1C93m2tW9Stez-d2noz7AoC18rDQcv62aNwe2zUAkjZs/edit?usp=sharing)
- 2021 (https://docs.google.com/spreadsheets/d/17mQAp9Me4CKpd2XKMxwKP06FYitIavrlkD0VlvXsBKU/edit?usp=sharing)

The laboratory has been improved continuosly, and the students evaluated the laboratory in 2020 and 2021 with 4.25 and 4.61 in a scale from 0 to 5, respectively. In 2020, The students described some problems with the camera and video codecs that were solved for the year 2021, reducing, for instance, the video bandwidth in each node.

Some videos made by the students with the remote laboratory can be seen in the following link:

https://drive.google.com/drive/folders/1MCQRGiAie61a072QKWMHQRdbVi-zeKbw?usp=sharing

# 3. Description of files and folders in the repository

**Folders**
- Article with students: In this folder is located an article for the control system (tank plant) created with students. The article has been approved in the IEEE conference ICACIT (https://icacit.org.pe/simposio/)
- Base Article: Preprint article with the aspects technical and educational of the RL. The article has been approved with minor revisions in the SJR Q3-IEEE journal (Revista Iberoamericana de tecnologías de aprendizaje-RITA).
- Control Systems: This folder contains the different scripts for the control plant (Only NODE 17). In the scripts, you can find the controllers: Proportional (P), Proportional-Integral (PI), and Proportional-Integral-Derivative (PID).
- Programming: This folder contains the scripts and graphical algorithms for different functions of the RL, for instance: Handling GPIOs, LCD, 7-segment display, robotic arm, temperature sensor, among others in the two modes of programming (text-based) and (blocks-based).

# 4. Instructions for reviewers
Please, follow the instructions available at the videos:

Instructions for reviewers (English): https://youtu.be/neN03aYQ8tk

Instructions for reviewers (Spanish): https://youtu.be/g5oM3Qu31q0

Credentials to enter to our remote laboratory were provided in the document of the GOLC award.

# 5. Costs
The costs of the implementation and debugging of the RL in dollars (USD) are shown in the table. The purpose of this initiative is to offer a low-cost but efficient Remote Laboratory (RL) at the technical and educational levels.

| Description | Cost (USD)|
| ------------- | ------------- |
| Cost of each node (1-18)|  200-300 (depending on the hardware components used) |
| Cost of the control plant (Tank system) |  150   |
| Server Maintenance (by year)-VPS service|  1000  |
| **Total Costs**|  **1450**  |

###### Table 2. Costs of the RL. VPS (Virtual Private Server).

Regarding server maintenance, other cheaper options can be taken into account in order to reduce the costs. For instance, there are some Virtual Private Servers (VPS) with lower costs as USD 150 by six months. As for the cost of each node, it depends on the hardware devices available and the version of the Raspberry Pi (4 or 3).

# 6. Pending upgrades

- Python console to debug scripts (November 2021-February 2022).
- LoRa protocol and Programmable Logic Controller (PLC) support (November 2021-March 2022)
- Upgrade of sensors from HC1008 towards SHT30 in the nodes (September 2021-March 2022). **Nodes 5,9-18 already count with the sensor SHT30 :smile:**


# Credit
This study has been possible with the efforts of the following persons:

- Professors: Jonathan Álvarez Ariza: jalvarez@uniminuto.edu, Sergio Gónzalez Gil: segonzalez@uniminuto.edu
- Students: Hansel Neira, Christian Nomesqui, Harold Chavarro, Johan Cuesta

Program of Technology in Electronics and Systems Enginnering, Corporación Universitaria Minuto de Dios-UNIMINUTO

https://www.uniminuto.edu/

111021, Bogotá, Colombia

**Thank you for your interest in this research :wink:**
