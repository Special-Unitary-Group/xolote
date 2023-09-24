# Smart Study

![](https://cdn-icons-png.flaticon.com/512/3743/3743319.png)

This repository is part of the competition HackMty, where the goal is to create a project to make an efficient and quick generstive AI result, being a search engine.

![HackMty](https://hackmty.com/img/Logo_2023.png)

![MLH](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fyt3.ggpht.com%2Fa%2FAATXAJymjH7ugfHm3TdKiYxMBIkSsDxbpne1eUjDOg%3Ds900-c-k-c0xffffffff-no-rj-mo&f=1&nofb=1&ipt=59abe5a367f59149c6bde832f84fc88b4a292e3eeed5b426ff18d9501b847908&ipo=images)

This project is done to resolve the issue of searching for an scientific paper, articule or report into a big pile with large amounts of documents. Where we only want to obtain information in a certain report that we are looking for.
To save up time and energy, this projects has as input one or several article files and a prompt for what is being looked for. Giving as an output the required file and section where the request is obtained from.

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

### Environmental variables

The `.env` file needs to have the following environmental variables for the script to work properly:
- `OPENAI_API_KEY`: API Key you use for OpenAI access
