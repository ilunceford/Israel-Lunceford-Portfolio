# Israel Lunceford Django Portfolio Website

This project is a Django web app for my personal software and computer engineering portfolio. It demonstrates my previous CSE 310 projects, includes project cards with GitHub repository links and YouTube demo links, and features my ECEN 240 4-bit CPU circuit. The site also provides a contact page, validates user input, and dynamically changes generated HTML based on form submissions.

## Instructions for Build and Use

Steps to build and/or run the software:

1. Download or clone the project folder.
2. Install Django if needed with `python -m pip install django`.
3. Run the app with `python manage.py runserver`.
4. Open `http://127.0.0.1:8000/` in a web browser.

Instructions for using the software:

1. Use the navigation bar to move between the project section, skills section, contact page, and report page.
2. Click `View Repository` on any project card to open the GitHub repository.
3. Click `Watch Demo` on any project card to open the YouTube demo video.
4. Fill out the recommendation form on the home page to receive a project recommendation.
5. Open the contact page to view my contact information or submit a message preview.
6. Open the report page to review the completed assignment requirements.
7. Open the 4-bit CPU section to inspect the architecture overview and download `ECEN240_Final_Project_4bit_CPU.circ`.
8. Download `Final_Proj_All_code.txt` to inspect or reload the CPU's instruction ROM program.

## 4-bit CPU Circuit

The CPU circuit was built for Logisim-evolution 4.0.0. The project contains six circuits, including the top-level CPU, a three-port register file, four-bit registers, an add/subtract ALU, and a full adder.

Steps to open and run the circuit:

1. Install Logisim-evolution 4.0.0 or newer from the [official releases page](https://github.com/logisim-evolution/logisim-evolution/releases).
2. Open Logisim-evolution and choose `File`, then `Open`.
3. Select `ECEN240_Final_Project_4bit_CPU.circ`.
4. Open the `Final_Project` circuit and select the Poke tool.
5. Pulse the `CLR` input to reset the circuit.
6. Enable simulation ticks or click the clock manually, then watch the probes and TTY output.

### Programming the Instruction ROM

The instruction ROM program is embedded in the circuit. `Final_Proj_All_code.txt` contains the same program as a Logisim `v3.0 hex words addressed` memory image for the 256-word, 16-bit instruction ROM.

Steps to reload the ROM from the text file:

1. Open the `Final_Project` circuit and locate the large instruction ROM connected to the program counter.
2. Open the ROM's `Edit Contents` hex editor.
3. Use the editor's open/load command and select `Final_Proj_All_code.txt`.
4. Confirm that address `00` begins with `1003 2700 1004 1109`.
5. Close the editor and save the circuit.
6. Pulse `CLR`, enable simulation ticks, and watch the probes and TTY as the program executes.

The original project also references helper circuit libraries from its development folder, so keep those libraries available if Logisim-evolution prompts for them after the file is moved to another computer.

## Development Environment

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Visual Studio Code or another code editor
* Python 3.12
* Django 6.0.6
* HTML5
* CSS3
* JavaScript
* Modern web browser such as Chrome, Edge, or Firefox

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [MDN HTML Documentation](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [MDN CSS Documentation](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [MDN JavaScript Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
* [GitHub Docs](https://docs.github.com/)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Add a full Logisim circuit screenshot or recorded CPU walkthrough.
* [ ] Add a backend or form service so contact messages can be submitted directly.
* [ ] Add more project details, including technologies used and lessons learned.
* [ ] Improve accessibility testing and keyboard navigation.

## Requirement Report

The requirements I completed and how I completed them:

* Generated at least one HTML page from the app: Django renders the home page, contact page, and report page from templates in `showcase/templates/showcase/`.
* Included CSS stored with the app code: the app serves `styles/styles.css` through Django static files.
* Accepted input from the user: the home page includes a project recommendation form, and the contact page includes a contact form.
* Performed error checking on user input: Django forms validate required fields, minimum text lengths, selected options, and email format.
* Modified generated HTML based on user input: valid recommendation form input displays a matching project recommendation, and valid contact form input displays a message preview.
* Completed a stretch challenge: I added a third dynamically generated page at `/report/`.

The requirements I did not complete and why:

* Database integration was not completed because I selected the third dynamically generated page as the stretch challenge.
