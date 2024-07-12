import csv
import random
from datetime import datetime
from faker import Faker

fake = Faker()

# Function to generate random date
def generate_random_date():
    start_date = datetime(2000, 1, 1)
    end_date = datetime.now()
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date.isoformat()

# Sample data generator function
def generate_sample_data(num_records):
    data = []
    for i in range(num_records):
        post = {
            "_id": {"$oid": f"{i+1:0>24x}"},
            "author": fake.name(),
            "title": fake.sentence(nb_words=6),
            "tags": [fake.word()],
            "body": fake.paragraph(nb_sentences=5),
            "date": {"$date": generate_random_date()}
        }
        data.append(post)
    return data

# Function to write data to CSV
def write_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["_id", "author", "title", "tags", "body", "date"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for post in data:
            writer.writerow({
                "_id": post["_id"]["$oid"],
                "author": post["author"],
                "title": post["title"],
                "tags": ','.join(post["tags"]),
                "body": post["body"],
                "date": post["date"]["$date"]
            })

# Generate sample data
num_records = 10  # Adjust the number of records as needed
sample_data = generate_sample_data(num_records)

# Write data to CSV file
csv_filename = 'sample_posts.csv'
write_to_csv(sample_data, csv_filename)

print(f"Sample data generated and saved to '{csv_filename}'")