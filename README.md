# ChemRxivFetch
<p><b>ChemRxivFetch - lightweight GUI and CLI tool for searching and downloading articles from ChemRxiv.org with filters</b></p>

<p>This project allows chemists and researchers to easily search and batch download preprints from <a href="https://chemrxiv.org">ChemRxiv.org</a> using simple filters like topics, date ranges, and the number of articles. It can significantly speed up literature collection for your research and lab needs, saving time when screening new preprints in your areas of interest.</p>

<h2>Key Features</h2>
<ul>
<li>Filter by topic and date range</li>
<li>Set the exact number of articles to download</li>
<li>Download PDFs automatically from ChemRxiv</li>
<li>Lightweight, no registration or API keys required</li>
<li>Both GUI and CLI usage available</li>
</ul>

<hr>

<h2>Installation and Usage</h2>

<p>Follow these clear step-by-step instructions, even if it is your first time working with GitHub or Python.</p>

<ol>
<li>
<b>Download the project:</b><br>
If you have Git installed, you can clone the repository using:
<pre><code>git clone https://github.com/meta6a6y/ChemRxivFetch_project
cd ChemRxivFetch_project
</code></pre>
If you do not have Git, you can download the ZIP archive:<br>
• Click the green <b>“Code”</b> button on this page, then click <b>“Download ZIP”</b>.<br>
• Extract the ZIP file and open the extracted folder.
</li>

<li>
<b>Install Python (if not installed):</b><br>
Make sure you have <b>Python 3.11 or newer</b> installed. You can download it from <a href="https://www.python.org/downloads/">python.org</a>.<br>
Note: <code>tkinter</code> (used for the graphical interface) is included by default with Python.
</li>

<li>
<b>(Optional but recommended) Create and activate a virtual environment:</b><br>
This helps to keep your Python environment clean and organized.
<pre><code>python -m venv venv
# Activate the environment:
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
</code></pre>
</li>

<li>
<b>Install required packages:</b><br>
Currently, the project uses only built-in modules. If future updates add dependencies, you can install them with:
<pre><code>pip install -r requirements.txt
</code></pre>
</li>

<li>
<b>Run the application:</b><br>
In the project folder, run:
<pre><code>python app.py
</code></pre>
The graphical interface will open, allowing you to select topics, set a date range, choose the number of articles, and download them easily from ChemRxiv.
</li>
</ol>

<h2>Where to run the commands?</h2>

<p>
Open your <b>terminal (Command Prompt, PowerShell, or Terminal)</b>, navigate to the project folder, and enter the commands there.
</p>

<ul>
<li><b>On Windows:</b>
  <ul>
    <li>Open the project folder.</li>
    <li>Shift + Right-click → “Open PowerShell window here”.</li>
    <li>Enter the commands.</li>
  </ul>
</li>

<li><b>On macOS/Linux:</b>
  <ul>
    <li>Open Terminal.</li>
    <li>Navigate to the folder with:</li>
    <pre><code>cd path/to/ChemRxivFetch_project</code></pre>
    <li>Enter the commands.</li>
  </ul>
</li>
</ul>

<p>If you encounter any issues or are new to Python, feel free to open an issue in this repository, and we will guide you.</p>
