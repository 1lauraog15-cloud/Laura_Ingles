# Cambridge C1/C2 English Trainer

A Streamlit app to practise advanced English for Cambridge C1 / C2 exams.

## Features

- Advanced vocabulary practice
- Phrasal verbs
- Verbs + prepositions
- Collocations
- Connectors
- Grammar exercises
- Use of English practice
- Optional AI feedback with Anthropic

## Project structure

```bash
english-app/
├── english_trainer.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository and enter the project folder:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git
cd YOUR-REPO
```

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

## Running the app

```bash
python3 -m streamlit run english_trainer.py
```

If port 8501 is busy, try another port:

```bash
python3 -m streamlit run english_trainer.py --server.port 8502
```

## Anthropic API key

This app imports `anthropic` for AI feedback in some grammar tasks.

Do **not** hardcode your API key in the source code or upload it to GitHub.

Set it as an environment variable in the terminal before running the app:

```bash
export ANTHROPIC_API_KEY="your_api_key_here"
```

Then run the app normally.

## requirements.txt

```txt
streamlit
anthropic
```

## Uploading to GitHub

Inside your project folder:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git
git push -u origin main
```

## Notes

- `random` is part of Python's standard library, so it does not go in `requirements.txt`.
- If VS Code says the file does not exist, make sure you are inside the correct folder before running Streamlit.
- If `anthropic` gives an error, check that the package is installed and your API key is set.

## Author

Laura Ortega
