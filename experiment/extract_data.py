import pandas as pd

def extract_data(folder: str, datasets: list, remove_cols: list, sample_num: int, sample_random_state: int, test_num: int, test_random_state: int):

    sample_set, test_set = {}, {}

    for dataset in datasets:
        df = pd.read_csv(folder + dataset)

        if remove_cols:
            df = df.drop(columns=remove_cols)

        samples = df.sample(n=sample_num, random_state=sample_random_state)
        remaining = df.drop(samples.index)
        tests = remaining.sample(n=test_num, random_state=test_random_state)

        sample_set[dataset] = samples
        test_set[dataset] = tests

    return sample_set, test_set