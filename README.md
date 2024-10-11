<h1>Project Employee Ratings</h1>

<img src="docs/readme.images/Capture.PNG" alt="A screen shot of a google spreadsheet on employee ratings">
<br>
<br>

<p>Project Employee Ratings is a Python backend data automation project that calculates a company's average ratings on three job contentment subjects namely; Environment Satisfaction, Job Satisfaction and Work-Life Balance. The program utilizes a google survey spreadsheet to obtain ratings data on these topics from users atop the spreadsheet, and then use the sum of each of the collated ratings data, to calculate and present the average rating of each subject at the bottom of the spreadsheet. The intent and essence of this project is to give the company a way to know at all times, which area(s) she lags behind and improve on it/them.</p>
<h3>User</h3>
<ul>
<li>As a user, i want to be able to participate in the survey and also glean insights from the survey results.</li>
</ul>
<h3>Site Owner</h3>
<ul>
<li>As a site owner, i want to be able to give external users the opportunity to provide data for the survey.</li>
<li>As a site owner, i want to be able to pinpoint at all times, area(s) for improvement for purposes of building a work environment where employees feel fulfilled.</li>
</ul>
<br>

<h2>Features</h2>
<p>In achieving the aforementioned project goals, i incorporated the underlisted features.</p>

<h3>Import Structured Data File</h3>
<ul>
<li>I utilized a csv data set imported from https://www.kaggle.com/ .</li>
<li>To interface with these imported csv data file, I activated firstly, my API Credentials and installed afterwards, two additional dependencies namely; gspread and google-auth.</li>
</ul>
<br>

<h3>Parse and Analyse the Data</h3>
<ul>
<li>I utilized four (4) functions to achieve this goal. The first collect data from users, the second validates the collected data, the third extracts/gets inputted data from each subject column and the last function calculates and updates the columns with the calculated averages.</li>
</ul>
<br>

<h3>Export Results to Appropriate file</h3>
<ul>
<li>The update_worksheet_with_employee_ratings function specifically achieves this goal. It exports and updates relevant columns of the spreadsheet with the calculated averages.</li>
</ul>
<br>

<h2>Technology Used</h2>
<P><strong>Python</strong></P>
<ul>
<li>The project is a entirely backend in nature hence my use of Python technology in writing the program.</li>
</ul>
<br>

<h3>Testing</h3>
<p>I manually tested this project to determine site usability, responsiveness and intuitivity to new users, by self and with the help of a few friends.</p>
<br>

<h4>Testing phase</h4>
<br>
<h5>Testing for links and form</h5>
<table>
<tr>
    <th>Test</th>
    <th>Outcome</th>
  </tr>
   <tr>
    <td>All links on Navigation lead to their correct pages</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Reserve button lead to contact form on contact us page</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Footer social media links all lead to their respective social media sites</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Contact form submits when all criteria is filled correctly</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>User prevented from submitting form without correct elements</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Form validation presents when incorrect input type is entered</td>
    <td>Pass</td>
  </tr>
</table>
<br>

<h5>Testing for responsiveness</h5>
<table>
<tr>
    <th>Test</th>
    <th>Outcome</th>
  </tr>
   <tr>
    <td>Home page, about us, portfolio, contact us display correctly on screens larger than 950px</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Home page, about us, portfolio, contact us display correctly on screens smaller than 950px</td>
    <td>Pass</td>
  </tr>
</table>
<br>

<h4>User testing</h4>
<br>
<h5>User testing challenge</h5>
<p>5 users were tasked prior to visiting the web page to conduct under-stated basic testing and report on success or otherwise.</p>
<br>
<table>
<tr>
    <th>Test</th>
    <th>Result</th>
  </tr>
   <tr>
    <td>Upon arrival to website please navigate to where you would expect to find a contact form</td>
    <td>100%</td>
  </tr>
  <tr>
    <td>Please navigate to the social media links of this business</td>
    <td>100%</td>
  </tr>
  <tr>
    <td>Please fill in contact form with your information and car category preference throught the reserve button</td>
    <td>100%</td>
  </tr>
  <tr>
    <td>Please navigate to the Portfolio page and count how many images there are</td>
    <td>100%</td>
  </tr>
</table>
<br>

<h5>User responsive testing</h5>
<p>5 users were asked to view the website on their mobile devices and/or tablets to provide any feedback on errors or page overlapping issues.</p>
<br>
<table>
<tr>
    <th>Test</th>
    <th>Result</th>
  </tr>
   <tr>
    <td>Issues reported</td>
    <td>None</td>
  </tr>
</table>
<br>

<h3>Bugs</h3>
<p>Solved bugs</p>
<ul>
<li>After deployment, my logo won't stop wrapping on mobile screens of width of 315px and below. I created a new media query for screens of max-width 315px and below to debug the problem</li>
<li>Navbar items kept wrapping on tablet screens even after i reduced it's font size. I debuged it using the code - whitespace : nowrap; - on the media query of tablets</li>
<li>Reserve forms could be submitted with no values using the space key. I debuged the issue using the code - pattern="[A-Za-z0-9]{1,20}"</li>
</ul>
<br>

<h3>Validator Testing</h3>
<ul>
<li><p>HTML</p>
<ul>
<li>The W3C validator-detected errors were corrected.</li>
<li>No errors were returned when re-ran on W3C validator after correction was effected.</li>
</ul>
</li>

<li><p>CSS</p>
<ul>
<li>No errors were returned when css style sheet was run on the official (Jigsaw) validator.</li>
</ul>
</li>

<li><p>Accessibility</p>
<ul>
<li>I confirmed that the colors and fonts chosen are easy to read and accessible by running it through lighhouse in devtools.</li>
<img src="docs/readme.images/testing.images/jpeg-optimizer_Lighthouse.PNG" alt="Screen shot of 'lighthouse accessibility diagnosis' of Sirjays Car Rental project">
</ul>
</li>

</ul>
<br>

<h3>Unfixed Bugs</h3>
<p>No unfixed bugs</p>
<br>

<h3>Deployment</h3>
<p>The site was deployed to GitHub pages using the following steps:</p>
<ul>
<li>Go to the settings tab of GitHub repository page</li>
<li>On the left-hand sidebar in the code and automation section, select pages</li>
<li>Set 'Source' to 'Deploy from Branch', select 'Main branch', set 'Folder' to 'Root', then click save</li>
<li>Click the 'Code<>' tab and wait a few minutes and then refresh repository</li>
<li>Go to the 'Environments' section on the right-hand side and click on 'github-pages'</li>
<li>Click on the URL displayed to see the live deployed site</li>
</ul>
<p>The live link can be found here - https://sirjay009.github.io/Sirjays-Car-Rentals/index.html</p>
<br>
<h3>Credits</h3>
<p>Credit</p>
<ul>
<li>The favicon link code was taken from https://www.w3schools.com</li>
<li>The navbar link code was taken from the CI love Running Project - https://sirjay009.github.io/love-running/</li>
<li>The code to debug navbar items that kept wrapping on tablet screen was taken from https://css-tricks.com</li>
<li>The code to debug contact/reserve form from accepting empty values was taken from https://stackoverflow.com</li>
<li>The code to make the reserve button in hero's overlay was taken from Alan Bushell's Belfast Auto Repairs project - https://alan-bushell.github.io/belfast-auto-repairs/index.html</li>
<li>The code to create space between text and font icons and debug footer was taken from https://wwwshecodes.io</li>
<li>The code to make the social media links was taken from both the CI Love Running Project and Alan Bushell's Belfast Auto Repairs project</li>
<li>Pieces of code for the general styling of the project was also taken from https://www.w3schools.com , https://www.codedamn.com , https://www.keentodesign.com and https://www.youtube.com/channel/UCvCyHScz5b1atuGYOQG_W8g</li>
</ul>
<br>
<h3>Acknowledgments</h3>
<h4>Alan Bushell</h4>
<p>My mentor under whose tutelage i was able to overcome my anxiety and conclude this project. I also appreciate his immense assistance in pointing me to most materials i utilized for this project.</p>
