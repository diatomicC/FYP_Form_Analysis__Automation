# FYP_Form_Analysis__Automation

## Overview

This code provides a way to visualize the relationship between two survey questions from a given dataset (CSV format). The relationship is demonstrated through histograms and normal distribution curves.

## Dependencies

- `pandas`
- `matplotlib`
- `numpy`
- `scipy`
- `openai`

You can install the required packages using pip:

```
pip install pandas matplotlib numpy scipy openai
```

## Usage

1. Ensure that you have the CSV file with your survey data.
2. Make sure to set your OpenAI API key at the `api_key` variable.
3. Run the script.
4. Enter the names of the two survey questions/columns you wish to compare.
5. The script will generate two side-by-side plots:
    - Histogram showcasing the responses distribution.
    - Normal distribution curves based on the mean and standard deviation of the two selected columns.

## Customizations

- The `maketitle` function utilizes the OpenAI GPT-3.5 model to generate short, English titles/labels for the plots. You can adjust the model or parameters if needed.
- Adjust the `max_tokens` parameter to control the length of the response from the model.
- The response scale in the x-axis of the plots is set from 1 to 5. Modify the `bins` parameter in the `plt.hist()` function if your data has a different scale.

## Output

- The script will show a visualization of the relationship between the two questions/columns in histogram and probability density plots.
- The titles and labels for the plots are generated using OpenAI's GPT-3.5 model for context relevance and conciseness.

## Notes

- The code assumes binary responses (Yes/No) for the comparison column and numerical responses for the question column.
- Ensure that you have appropriate rights to use the OpenAI API and incur any associated costs.

## Disclaimer

This script is for demonstration purposes. Before deploying or using it for professional tasks, you may want to conduct further validations or optimizations.
