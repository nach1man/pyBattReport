# pyBattReport
A GUI script to get battery report for work since many batteries from laptop serials ending in H2 were faulty.

Though this script can be ran from the CLI, I packaged it up as a .EXE for easier use in our Windows environment. The EXE was hosted on our Google Drive and the link was sent to the users with faulty serials. They then ran the EXE and it would send out IT Director an email with the battery report and showed who it came from.

To create an exe, I used py2exe since it was quick and painless and packages everything up including the icon we used for the GUI presentation.
