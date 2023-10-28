import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import openai

api_key = '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'

# Initialize the OpenAI API client
openai.api_key = api_key

def maketitle(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # GPT-3.5 model
        prompt=prompt,
        max_tokens=50  # Adjust this to control response length
    )
    return response.choices[0].text.strip()


# Load the CSV file
file_path = 'fyp.csv'
df = pd.read_csv(file_path, encoding='utf-8')

# Get input from user for comparison and question columns
comparison_column = input("Please enter the column name for comparison (e.g. '대학에서 ChatGPT 사용이 금지되었나요?'): ")
question_column = input("Please enter the column name for the question (e.g. 'ChatGPT의 문제점들을 이해하고 있나요?'): ")

# Filter for 'Yes' and 'No' responses in the selected column
yes_responses = df[df[comparison_column] == 'Yes']
no_responses = df[df[comparison_column] == 'No']

# Generate data for normal distribution curves
x = np.linspace(1, 5, 100)
mu_yes, std_dev_yes = yes_responses[question_column].mean(), yes_responses[question_column].std()
mu_no, std_dev_no = no_responses[question_column].mean(), no_responses[question_column].std()

#summary
title = maketitle(f"make a very short ENGLISH title about the relationship between {comparison_column} and {question_column}")
print(title)
label = maketitle(f"make a very short ENGLISH label about {comparison_column}")


# Plotting the histogram and normal distribution curves
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist([yes_responses[question_column], no_responses[question_column]],
         bins=[1, 2, 3, 4, 5, 6],
         alpha=0.5, label=['Yes', 'No'], density=True)
plt.xlabel('Response Scale (1: Not at all, 5: Very well)')
plt.ylabel('Normalized Frequency')
plt.title(f'{title}')

plt.subplot(1, 2, 2)
plt.plot(x, norm.pdf(x, mu_yes, std_dev_yes), 'b-', label=f'Yes to {label}', color='blue')
plt.plot(x, norm.pdf(x, mu_no, std_dev_no), 'r-', label=f'No to {label}', color='red')
plt.xlabel('Response Scale (1: Not at all, 5: Very well)')
plt.ylabel('Probability Density')
plt.title(f'{title}')
plt.legend()

plt.tight_layout()
plt.show()

