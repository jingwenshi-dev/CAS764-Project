import pandas as pd

path = './results/baseline/0/'

for i in range(3):
    # if i == 0:
    #     files = ['deceptive_negative_prediction_0.csv', 'deceptive_positive_prediction_0.csv',
    #              'truthful_negative_prediction_0.csv', 'truthful_positive_prediction_0.csv']
    # elif i == 1:
    #     files = ['deceptive_negative_prediction_5.csv', 'deceptive_positive_prediction_5.csv',
    #              'truthful_negative_prediction_5.csv', 'truthful_positive_prediction_5.csv']
    # else:
    #     files = ['deceptive_negative_prediction_10.csv', 'deceptive_positive_prediction_10.csv',
    #              'truthful_negative_prediction_10.csv', 'truthful_positive_prediction_10.csv']

    # if i == 0:
    #     files = ['deceptive_positive_prediction_0.csv', 'truthful_positive_prediction_0.csv']
    # elif i == 1:
    #     files = ['deceptive_positive_prediction_5.csv', 'truthful_positive_prediction_5.csv']
    # else:
    #     files = ['deceptive_positive_prediction_10.csv', 'truthful_positive_prediction_10.csv']

    if i == 0:
        files = ['deceptive_negative_prediction_0.csv', 'truthful_negative_prediction_0.csv']
    elif i == 1:
        files = ['deceptive_negative_prediction_5.csv', 'truthful_negative_prediction_5.csv']
    else:
        files = ['deceptive_negative_prediction_10.csv', 'truthful_negative_prediction_10.csv']

    # if i == 0:
    #     files = ['deceptive_prediction_0.csv', 'truthful_prediction_0.csv']
    # elif i == 1:
    #     files = ['deceptive_prediction_5.csv', 'truthful_prediction_5.csv']
    # else:
    #     files = ['deceptive_prediction_10.csv', 'truthful_prediction_10.csv']

    dfs = []
    for file in files:
        df = pd.read_csv(f'{path}/{file}')
        dfs.append(df)

    # Calculate the total accuracy, precision, and recall
    total_correct = 0
    total_predictions = 0
    true_positives = 0
    false_positives = 0
    false_negatives = 0

    for df in dfs:
        total_correct += (df['class'] == df['prediction']).sum()
        total_predictions += len(df)
        true_positives += ((df['class'] == 'deceptive') & (df['prediction'] == 'deceptive')).sum()
        false_positives += ((df['class'] == 'truthful') & (df['prediction'] == 'deceptive')).sum()
        false_negatives += ((df['class'] == 'deceptive') & (df['prediction'] == 'truthful')).sum()

    accuracy = total_correct / total_predictions
    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
    recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0

    print(f'Total Accuracy: {accuracy:.2f}')
    print(f'Precision: {precision:.2f}')
    print(f'Recall: {recall:.2f}')