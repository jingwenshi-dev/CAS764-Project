import json
import os

from openai import OpenAI
from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray
from pydantic import BaseModel, Field

from experiment.extract_data import extract_data
from experiment.generate_msg import generate_messages

client = OpenAI()
api_key = os.getenv('OPENAI_API_KEY')


class PredictionItem(BaseModel):
    index: int
    prediction: str

class Result(BaseModel):
    results: list[PredictionItem]

folder = '../dataset/clean/fake-reviews-of-apps/'
datasets = ['deceptive.csv', 'truthful.csv']

def api_call(folder: str, datasets: list, remove_cols: list, sample_num: int, sample_random_state: int, test_num: int, test_random_state, i):

    sample_set, _ = extract_data(folder, datasets, remove_cols, sample_num, sample_random_state, test_num,
                                 test_random_state)

    _, test_set = extract_data('../dataset/clean/afrd-arabic-fake-reviews-detection/',
                               ['deceptive_negative.csv', 'deceptive_positive.csv', 'truthful_negative.csv',
                                'truthful_positive.csv'], remove_cols,
                               sample_num, sample_random_state, test_num,
                               test_random_state)

    messages = generate_messages(sample_set, test_set, datasets)

    # print(messages)

    completion = client.beta.chat.completions.parse(
        model="gpt-4o",
        messages=messages,
        response_format=Result,
    )

    result = json.loads(completion.choices[0].message.content)['results']
    print(result)

    predictions = [item['prediction'] for item in result]
    for dataset in test_set:
        test_set[dataset]['prediction'] = predictions[:len(test_set[dataset])]
        predictions = predictions[len(test_set[dataset]):]

        output_path = f'./results/app-language/{i}/'
        os.makedirs(output_path, exist_ok=True)
        test_set[dataset].to_csv(os.path.join(output_path, dataset.replace('.csv', f'_prediction_{sample_num}.csv')),
                                 index=False)

for i in range(1):
    api_call(folder, datasets, [], 0, 1, 20, 2, i)
    api_call(folder, datasets, [], 5, 3, 20, 4, i)
    api_call(folder, datasets, [], 10, 5, 20, 6, i)