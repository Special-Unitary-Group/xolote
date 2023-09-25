# Kaban

<p align="center">
<img src="img/kaban-logo.png" width="300">
</p>

This repository is part of the competition HackMty, where the goal is to create a project to make an efficient and quick generstive AI result, being a search engine.

<p align="center">
<img src="https://hackmty.com/img/Logo_2023.png" width="200">
</p>

This project is done to resolve the issue of searching for an scientific paper, articule or report into a big pile with large amounts of documents. Where we only want to obtain information in a certain report that we are looking for.
To save up time and energy, this projects has as input one or several article files and a prompt for what is being looked for. Giving as an output the required file and section where the request is obtained from.

Our project went to top 10 finalist teams in the Hackathon!

<p align="center">
<img src="img/su-group.jpg" width="800">
</p>

## Previous configurations

### Installing the libraries

The script works with the following versions:
- python `3.11.5`

To install the necessary libraries, run the following code in a Python executer
``` CMD Commands
pip install -r requirements.txt
```

To view the version of your libraries, run the following:
``` CMD Commands
pip show python-dotenv
```

## Frontend

This repo uses a frontend UI to make the LLM dynamic to a user. To avoid bad practices, this was forked into another repository and developed there, separately from the model and analysis.

- [Front End Repo](https://github.com/David-Lazaro-Fernandez/smart-study)

### Environmental variables

The `.env` file needs to have the following environmental variables for the script to work properly:
- `OPENAI_API_KEY`: API Key you use for OpenAI access
