# SmartLabsUniminuto-GOLC

This is the online repository for the GOLC_2022 international award. In this repository, you can find the main information concerning the laboratory (smartlabsuniminuto), e.g., structure, features, modes of programming, educational goals and outcomes, and presentation video. For more information about this award, please consult the link (http://online-engineering.org/GOLC_online-lab-award.php)

# 1. What is *Smartlabsuniminuto*?

*Smartlabsuniminuto*  is an initiative about remote laboratories for teaching and learning programming and control systems in academic programs of engineering and technology. The project was developed at the university Corporación Universitaria Minuto de Dios-UNIMINUTO ([https://www.uniminuto.edu/](https://www.uniminuto.edu/)) , Bogotá, Colombia, involving the programs of Technology in Electronics, Systems Engineering, and Industrial Engineering. *Smartlabsuniminuto* is available at https://www.smartlabsuniminuto.com/

The laboratory arose according to the educational problems regarding experimentation, hands-on activities, and learning by doing produced by the COVID-19 pandemic in 2020 from the second semester. The laboratory is focused on programming through Python Language and a beta version for control systems education with a level control plant. With the laboratory, the students can program in Python language and interact with hardware devices which have been interfaced with a Raspberry Pi in each node (Physical Computing). The remote laboratory is available in Spanish. Among the main features of *Smartlabsuniminuto*, we have:

![Imag1](https://user-images.githubusercontent.com/11606241/134404259-5af59424-fdb3-4c48-b344-de1bbe3d9db6.png)
###### Fig 1. Main feaures of smartlabsuniminuto.



## 1.1 Programming modes
Searching to expand the scope of students that could use our laboratory, we developed two programming modes (text-based, block-based). Please, click on the images to see the videos in YouTube.

### 1.1.1 Text-based programming
There, the students can program directly in Python Language. This mode could be used by students with experience in programming or who desire to know the statements and structure of Python.

<a href="http://www.youtube.com/watch?feature=player_embedded&v=1azGjeaalZ0
" target="_blank"><img src="http://img.youtube.com/vi/1azGjeaalZ0/0.jpg" 
alt="Text-based programming" width="400" height="300" border="2" /></a>

### 1.1.2 blocks-based programming
There, the students can program using graphical blocks (Blockly). This mode could be used by novice students.


<a href="http://www.youtube.com/watch?feature=player_embedded&v=TnZlTCT3V1w
" target="_blank"><img src="http://img.youtube.com/vi/TnZlTCT3V1w/0.jpg" 
alt="Blocks-based programming" width="400" height="300" border="2" /></a>

## 1.2 Hardware
We have developed a low-cost module in a 3D printer to emsamble the different hardware elements employed in each node. Also, each module (0-17) counts with a robotic arm with 2 Degree of Freedom (DOF) and several additional components as it will be described in table 1. With the elements elaborated in a 3D printer, we accelerated the process of construction of the remote laboratory. 

<img src="https://user-images.githubusercontent.com/11606241/134495226-8488ba42-5131-460d-9ac9-fa17a9a82497.jpeg" width="300"><img src="https://user-images.githubusercontent.com/11606241/134497125-bb9c9359-bc7d-4bb7-937f-ba6ceebc54ae.jpg" width="400"><img src="https://user-images.githubusercontent.com/11606241/134495354-20166d25-2311-4edf-8eae-a30adc68fc31.jpg" width="300">

###### Fig 2. Hardware components and materials. For the control plant (last picture), 1. Camera, 2. Raspberry module for sensor and motor pumps, 3. Tank control system. 

The nodes count with the following hardware devices and materials:

| Node | Description | Hardware components
| ------------- | ------------- | ------------- |
| 1-16 | Nodes for programming |Raspberry Pi V4 (2GB), protoboard (830 points), 4 leds, 1 display tm1637, 1 LCD (2x16), 1 robotic arm (2 DOF), 8Mpx Camera, 1 camera support.|
| 17  | Node for control systems. Control Plant (Tank system)  | Raspberry Pi V4 (2GB), motor pump (2), Ultrasonic sensor (US-016), Analog to Digital Converter (ADC) AD1115, 8Mpx Camera, 1 camera support. |
| 18  | Nodes for programming and sensing  |Raspberry Pi V4 (2GB), protoboard (830 points), 4 leds, 1 display tm1637, 1 LCD (2x16), 1 robotic arm (2 DOF), 1 temperature sensor TMP100, 1 lamp, 1 light-dimmer module, 8Mpx Camera, 1 camera support.|

###### Table 1. Description of hardware components used in the nodes.

# 2. Educational concepts and outcomes with the laboratory 
Our primary goal with *Smartlabsuniminuto* is to support the educational process of the students in programming, physical computing, and control systems from a constructivist point of view. At the start of the project (year 2020), we developed 15 nodes to support teaching and learning of programming and physical computing. As part of different improvements, several students in their final year want to create additional modules for the Remote Laboratory (RL). Thus, a tank control system that can be programmed in Python language was created and interfaced with the RL.  

*Smartlabsuniminuto* have been tested by roughly *n=60* students from 2020 to 2021 (first semester). The test in a real educational setting was divided in the following stages:

- We tested the remote laboratory with n=30 students of Systems Engineering in 2020 (second semester). The average age of the students was 18.5 years with a students' distribution of 90% male and 10% female.
- We have tested the remote laboratory with n=30 students of Systems Engineering in 2021 (first semester). The average age of the students was 19.1 years with a students' distribution of 87.71% male and 12.29% female.

To collect the information and perceptions of the students about the remote laboratory in the courses, we developed two surveys (2020-2021) according to the Technology Acceptance Model (TAM). In general terms, the students have had a good acceptance of the laboratory which was manifested by the comments and the descriptive statistics in each category of the surveys. To know in-depth the results in (2020), please, consult the folder *Article (Paper IEEE Rita-preprint)* in this repository. This is a preprint article presented to the IEEE journal (Revista Iberoamericana de Tecnologias de Aprendizaje-RITA). The article was accepted with minor revisions and it could give an idea about the elements such technical as educational taken into account in the remote laboratory. 

If you want to see the surveys with their responses in Google Forms, please see the following links:
- 2020 (https://docs.google.com/spreadsheets/d/1C93m2tW9Stez-d2noz7AoC18rDQcv62aNwe2zUAkjZs/edit?usp=sharing)
- 2021 (https://docs.google.com/spreadsheets/d/17mQAp9Me4CKpd2XKMxwKP06FYitIavrlkD0VlvXsBKU/edit?usp=sharing)

The laboratory has been improved continuosly, and the students evaluated the laboratory in 2020 and 2021 with 4.25 and 4.61 in a scale from 0 to 5, respectively. In 2020, The students described some problems with the camera and video codecs that were solved for the year 2021, reducing, for instance, the video bandwidth in each node.

# 3. Description of files and folders in the repository

# 4. Instructions for reviewers

# Credit
This study has been possible with the efforts of the following persons:

- MEd. Jonathan Álvarez Ariza: jalvarez@uniminuto.edu
- MSc. Sergio Gónzalez Gil: segonzalez@uniminuto.edu

Engineering Professors

Program of Technology in Electronics and Systems Enginnering, Corporación Universitaria Minuto de Dios-UNIMINUTO

111021, Bogotá, Colombia

**Thank you for your interest in this research :wink:**
