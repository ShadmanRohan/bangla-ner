import json
import random
import os

def process_jsonl_file(filename):
    with open(filename, 'r') as f:
        data = [json.loads(line) for line in f]
    reformatted_data = [{"tokens": d[0].split(), "tags": d[1]} for d in data]
    return reformatted_data

def process_txt_file(filename):
    with open(filename, 'r') as f:
        lines = f.read().split('\n\n')
    data = []
    for l in lines:
        tokens = []
        tags = []
        for line in l.split('\n'):
            parts = line.split()
            if len(parts) == 2:  # If there are exactly 2 parts (token and tag)
                tokens.append(parts[0])
                tags.append(parts[1])
        if tokens and tags:  # If both lists are not empty
            data.append({"tokens": tokens, "tags": tags})
    return data

def split_data(data, proportions):
    train_cutoff = int(proportions[0] * len(data))
    val_cutoff = train_cutoff + int(proportions[1] * len(data))
    train_data = data[:train_cutoff]
    val_data = data[train_cutoff:val_cutoff]
    test_data = data[val_cutoff:]
    return train_data, val_data, test_data

def main():
    os.makedirs('processed_data', exist_ok=True)
    all_data = process_jsonl_file('data/main.jsonl') + process_txt_file('data/all_data.txt')
    random.shuffle(all_data) # Shuffle data before splitting

    # Split data into train, validation, and test sets (80%, 10%, 10% split)
    train_data, val_data, test_data = split_data(all_data, [0.8, 0.1, 0.1])

    # Write the reformatted data to new .jsonl files
    with open('processed_data/train.jsonl', 'w', encoding='utf8') as f:
        f.write('\n'.join(json.dumps(i, ensure_ascii=False) for i in train_data))
    with open('processed_data/val.jsonl', 'w', encoding='utf8') as f:
        f.write('\n'.join(json.dumps(i, ensure_ascii=False) for i in val_data))
    with open('processed_data/test.jsonl', 'w', encoding='utf8') as f:
        f.write('\n'.join(json.dumps(i, ensure_ascii=False) for i in test_data))

if __name__ == '__main__':
    main()
