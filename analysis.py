import pandas as pd
from datetime import datetime
from collections import Counter
import matplotlib.pyplot as plt
import re

def parse_log_line(line):
    # Extract timestamp and command from the log line
    match = re.match(r'(.*?) git (.+)', line)
    if match:
        timestamp_str, command = match.groups()
        timestamp = datetime.strptime(timestamp_str, '%a %b %d %H:%M:%S %Z %Y')
        return timestamp, command.split()[0]  # Return only the main command
    return None, None

def analyze_git_log(log_data):
    commands = []
    for line in log_data.split('\n'):
        _, command = parse_log_line(line.strip())
        if command:
            commands.append(command)
    
    # Create a dataframe with command counts
    df = pd.DataFrame({'command': commands})
    df = df['command'].value_counts().reset_index()
    df.columns = ['command', 'count']
    
    return df

def generateInsight(file):
    # Initialize a Counter to store command frequencies
    command_counter = Counter()

    # Regular expression pattern to match git commands
    command_pattern = r'git\s+([a-zA-Z\-]+)'

    # Read the log file
    with open(file, 'r') as f:
        for line in f:
            match = re.search(command_pattern, line)
            if match:
                command = match.group(1)
                command_counter[command] += 1

    # Extract the commands and their frequencies
    commands = list(command_counter.keys())
    frequencies = list(command_counter.values())

    # Generate the bar chart
    plt.figure(figsize=(10, 6))
    plt.barh(commands, frequencies, color='skyblue')
    plt.xlabel('Frequency')
    plt.ylabel('Git Command')
    plt.title('Frequency of Git Commands')
    plt.tight_layout()

    # Save the chart as insight.png
    plt.savefig('./output/insight.png')

# log_data = open('frequency.log', 'r').read()

# # Analyze the log data
# result_df = analyze_git_log(log_data)
# print(result_df)
generateInsight('./frequency.log')