# nsf-grants-dei-2023
Using OpenAI ChatGPT 4o to analyze NSF Grants made in 2023 for DEI.

The data were obtained from the National Science Foundation's website on or around October 27, 2024.

## Running the analysis

### Setup

You will need a recent Python version (3.10+) and an OpenAI API key. Use a virtual environment and install the necessary packages using pip:

```
pip install -r requirements.txt
```

Next steps:

1. Preprocess the NSF Data: unzip `2023.zip` and run `python preprocess.py`.

2. Run ChatGPT 4o -- this can take a while and will cost roughly $20. Run `analyze_openai.py`.

3. Run the summary analysis in `analyze_final.py`



