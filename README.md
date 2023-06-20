g# Twitter Actions Automation

Twitter Actions Automation is a tool built using Selenium WebDriver and OpenAI's GPT-3 model. It automates the process of searching and retrieving tweets from Twitter, and then it uses GPT-3 to analyze the sentiment of the tweet and generate a reply.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

What things you need to install the software and how to install them:

- Python 3.7 or later: See [here](https://www.python.org/downloads/) for installation details.
- Selenium WebDriver: Install with pip using `pip install selenium`
- OpenAI's Python package: Install with pip using `pip install openai`
- Google Chrome

### Installation

- Clone this repo to your local machine using `https://github.com/ikhana/Automation.git`
- Setup virtual environment.

### Setting up a Virtual Environment 

To isolate your project's dependencies, it is recommended to use a virtual environment. Follow the steps below to create a virtual environment using Python's `venv` module:

- Create virtual environment in windows by using `python -m venv venv`. 
- Activate virtual environment `venv\Scripts\Activate`
- Install dependency `pip install -r requirements.txt`
- When you're done working in the virtual environment, you can deactivate it by `deactivate`
- Note: Remember to update the `requirements.txt` file whenever you add or remove packages from your project. by using `pip freeze > requirements.txt`

### Setup Environment Variables

This project uses environment variables to protect sensitive information. Create a .env file in the project root and add your credentials:
```
TWITTER_USERNAME=your_twitter_username
TWITTER_PASSWORD=your_twitter_password
OPEN_AIAPI=your_openai_api_key
```

### Usage

After you have set up your environment variables, you can run the main script.

python main.py


## Built With

- [Python](https://www.python.org/) - Programming language used.
- [Selenium WebDriver](https://www.selenium.dev/) - Used to automate browser actions.
- [OpenAI GPT-3](https://www.openai.com/gpt-3/) - AI model used for text generation and sentiment analysis.

## Contributing

Please read [CONTRIBUTING.md](https://github.com/ikhana/Automation/blob/main/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

- **ikhana** - Initial work - [ikhana](https://github.com/ikhana)

See also the list of [contributors](https://github.com/ikhana/Automation/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/ikhana/Automation/blob/main/LICENSE.md) file for details.


