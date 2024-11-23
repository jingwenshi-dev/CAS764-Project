import json
import os

from openai import OpenAI
from pydantic import BaseModel

from experiment.extract_data import extract_data
from experiment.generate_msg import generate_messages

client = OpenAI()
api_key = os.getenv('OPENAI_API_KEY')

class Result(BaseModel):
    prediction: list[str]

folder = '../dataset/clean/deceptive-opinion-spam-corpus/'
datasets = ['deceptive_negative.csv', 'deceptive_positive.csv', 'truthful_negative.csv', 'truthful_positive.csv']

def api_call(folder: str, datasets: list, remove_cols: list, sample_num: int, sample_random_state: int, test_num: int, test_random_state):

    sample_set, test_set = extract_data(folder, datasets, remove_cols, sample_num, sample_random_state, test_num,
                                        test_random_state)

    messages = generate_messages(sample_set, test_set, datasets)

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=messages,
        response_format=Result,
        temperature=0,
    )

    result = json.loads(completion.choices[0].message.content)['prediction']

    for dataset in test_set:
        test_set[dataset]['prediction'] = result[:len(test_set[dataset])]
        result = result[len(test_set[dataset]):]
        test_set[dataset].to_csv('./results/' + dataset.replace('.csv', '_prediction.csv'), index=False)


# api_call(folder, datasets, [], 0, 42, 50, 42)
# api_call(folder, datasets, [], 5, 42, 50, 42)
# api_call(folder, datasets, [], 10, 42, 50, 42)
# api_call(folder, datasets, [], 15, 42, 50, 42)
# api_call(folder, datasets, [], 20, 42, 50, 42)

api_call(folder, datasets, [], 0, 42, 1, 42)