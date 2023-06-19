import json
import re
from collections import Counter
import matplotlib.pyplot as plt

# Ask for input files
appjson_file = input("Please enter the name of the app json file: ")
session_dump_file = input("Please enter the name of the session dump file: ")

# Load the json file to a dict for easy lookup
with open(appjson_file, 'r') as f:
    apps_json = json.load(f)

# Create a dict to map app id to app name
app_dict = {}
for app in apps_json:
    try:
        # Skip apps with id "0"
        if app['id'] != "0":
            app_dict[app['id']] = app['app-name']
    except KeyError:
        continue

# Regex pattern to match app id in session info
pattern = re.compile(r'app=(\d+)')

# Counter to count occurrences of each app id
counter = Counter()

# Read the sessions file
with open(session_dump_file, 'r') as f:
    content = f.read()

# Find all app ids and update the counter
app_ids = pattern.findall(content)

# Exclude app id "0"
app_ids = [app_id for app_id in app_ids if app_id != "0"]

counter.update(app_ids)

# Ask for number of top apps to display
top_n = int(input("Please enter the number of top apps to display: "))

# Sort the counter by count and get the top N apps
top_n_apps = counter.most_common(top_n)

# Now we have the top N apps by id and count, let's replace the id with the name
top_n_apps_with_name = [(app_dict.get(id, id), count) for id, count in top_n_apps]

# Print the top N apps and their counts
for name, count in top_n_apps_with_name:
    print(f'App Name: {name}, Count: {count}')

# Ask if user wants to generate a bar graph
graph_choice = input("Do you want to generate a bar graph? (yes/no): ")

if graph_choice.lower() == "yes":
    # Create a bar graph
    names = [name for name, count in top_n_apps_with_name]
    counts = [count for name, count in top_n_apps_with_name]
    colors = plt.get_cmap('tab20').colors  # get 20 distinct colors

    plt.bar(names, counts, color=colors[:top_n])
    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability if needed
    plt.xlabel('App Name')
    plt.ylabel('Count')
    plt.title('Top N Apps')
    plt.show()
