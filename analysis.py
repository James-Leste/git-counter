import pandas as pd
from datetime import datetime
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

log_data = open('frequency.log', 'r').read()

# Analyze the log data
result_df = analyze_git_log(log_data)
print(result_df)