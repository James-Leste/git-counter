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
    hour_counter = Counter()

    # Regular expression pattern to match git commands
    command_pattern = r'git\s+([a-zA-Z\-]+)'
    timestamp_pattern = r'([A-Za-z]+\s+[A-Za-z]+\s+\d+\s+\d+:\d+:\d+\s+\w+)\s+\d+'


    # Read the log file
    with open(file, 'r') as f:
        for line in f:
            match = re.search(command_pattern, line)
            if match:
                command = match.group(1)
                command_counter[command] += 1
            timestamp_match = re.search(timestamp_pattern, line)
            if timestamp_match:
                timestamp_str = timestamp_match.group(1)
                timestamp = datetime.strptime(timestamp_str, '%a %b %d %H:%M:%S %Z')
                hour_counter[timestamp.hour] += 1

    # Extract the commands and their frequencies
    commands = list(command_counter.keys())
    frequencies = list(command_counter.values())

    hours = list(hour_counter.keys())
    hour_frequencies = list(hour_counter.values())
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    # Plot 1: Git command frequency (left)
    axs[0].barh(commands, frequencies, color='skyblue')
    axs[0].set_xlabel('Frequency')
    axs[0].set_ylabel('Git Command')
    axs[0].set_title('Frequency of Git Commands')

    # Plot 2: Command frequency by hour (right)
    axs[1].bar(hours, hour_frequencies, color='salmon', width=0.6)
    axs[1].set_xlabel('Hour of the Day')
    axs[1].set_ylabel('Frequency')
    axs[1].set_title('Git Commands Frequency by Hour of the Day')
    axs[1].set_xticks(range(24))  # Set x-axis to show all 24 hours

    # Adjust layout
    plt.tight_layout()

    # Save the chart as insight.png
    plt.savefig('./output/insight.png')

# log_data = open('frequency.log', 'r').read()

# # Analyze the log data
# result_df = analyze_git_log(log_data)
# print(result_df)
generateInsight('./frequency.log')