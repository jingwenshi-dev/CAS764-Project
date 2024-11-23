def generate_messages(sample_set, test_set, datasets):
    messages = [{
        "role": "system",
        "content": "You are an expert in identifying deceptive reviews. And given the following review, classify it as either 'truthful' or 'deceptive'."
    }]

    for dataset in datasets:
        if 'deceptive_negative' in dataset:
            messages.append({
                "role": "system",
                "content": "Deceptive review samples: "
            })
        elif 'truthful_negative' in dataset:
            messages.append({
                "role": "system",
                "content": "Truthful review samples: "
            })
        for index, row in sample_set[dataset].iterrows():
            messages.append({
                "role": "system",
                "content": row['text']
            })

    total_inputs = sum(len(test_set[dataset]) for dataset in test_set)
    messages.append({
        "role": "system",
        "content": (
            f"Now classify each of the following {total_inputs} reviews as either 'truthful' or 'deceptive'. "
            "Return your response as a JSON list of classifications paired with index, e.g. [{'0': 'truthful'}, {'1': 'deceptive'}, ...]. "
            f"The results should not contain more than {total_inputs} items."
        )
    })

    for dataset in test_set:
        for _, row in test_set[dataset].iterrows():
            messages.append({
                "role": "user",
                "content": f"{row['index']}: {row['text']}"
            })

    return messages