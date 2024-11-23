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

    messages.append({
        "role": "system",
        "content": (
            "Now classify each of the following reviews as either 'truthful' or 'deceptive'. "
            "Return your response as a JSON list of classifications, e.g., ['truthful', 'deceptive', ...]."
        )
    })

    for dataset in test_set:
        for index, row in test_set[dataset].iterrows():
            messages.append({
                "role": "user",
                "content": row['text']
            })

    return messages