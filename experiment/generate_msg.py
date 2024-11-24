import random


def generate_messages(sample_set, test_set, datasets):
    messages = [{
        "role": "system",
        "content": ("You are an expert in identifying deceptive reviews. \n")
    }]

    for dataset in datasets:
        if not sample_set[dataset].empty:

            if 'deceptive_negative' in dataset:
                messages.append({
                    "role": "system",
                    "content": "Deceptive negative review samples: "
                })
            elif 'deceptive_positive' in dataset:
                messages.append({
                    "role": "system",
                    "content": "Deceptive positive review samples: "
                })
            elif 'truthful_negative' in dataset:
                messages.append({
                    "role": "system",
                    "content": "Truthful negative review samples: "
                })
            elif 'truthful_positive' in dataset:
                messages.append({
                    "role": "system",
                    "content": "Truthful positive review samples: "
                })

            # if 'deceptive' in dataset:
            #     messages.append({
            #         "role": "system",
            #         "content": "Deceptive review samples: "
            #     })
            # elif 'truthful' in dataset:
            #     messages.append({
            #         "role": "system",
            #         "content": "Truthful review samples: "
            #     })

        for index, row in sample_set[dataset].iterrows():
            messages.append({
                "role": "system",
                "content": row['text']
            })

    # for dataset in datasets:
    #     if not sample_set[dataset].empty:
    #         if 'deceptive_negative' in dataset:
    #             messages[0]['content'] += "Deceptive review samples: \n"
    #         elif 'truthful_negative' in dataset:
    #             messages[0]['content'] += "Truthful review samples: \n"
    #     for index, row in sample_set[dataset].iterrows():
    #         messages[0]['content'] += row['text']

    total_inputs = sum(len(test_set[dataset]) for dataset in test_set)
    messages.append({
        "role": "user",
        "content": (
            f"Now classify each of the following {total_inputs} reviews as either 'truthful' or 'deceptive'. "
            "The reviews are given with an id and the text, e.g. 1234: This is a review. "
            "Return your response as a JSON list of classifications paired with an id, e.g. [{'1234': 'truthful'}, {'5678': 'deceptive'}, ...]."
            f"The results should not contain more than {total_inputs} items."
        )
    })

    # messages[0]['content'] += (
    #     f"Now classify each of the following {total_inputs} reviews as either 'truthful' or 'deceptive'. "
    #     "The reviews are given with an id and the text, e.g. 1234: This is a review. "
    #     "Return your response as a JSON list of classifications paired with an id, e.g. [{'1234': 'truthful'}, {'5678': 'deceptive'}, ...]."
    #     f"The results should not contain more than {total_inputs} items."
    # )

    # messages.append({
    #     "role": "user",
    #     "content": ""
    # })

    # for dataset in test_set:
    #     for _, row in test_set[dataset].iterrows():
    #         messages[-1]['content'] += f"{row['index']}: {row['text']}"

    for dataset in test_set:
        for _, row in test_set[dataset].iterrows():
            messages.append({
                "role": "user",
                "content": f"{row['index']}: {row['text']}"
            })

    return messages