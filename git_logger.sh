# if [[ "$1" == "add" || "$1" == "commit" || "$1" == "push" || "$1" == "status" ]]; then
#     # Do not log these commands, just pass them to git
#     git "$@"
# else
#     # Log the command (with date and time) and pass it to git
#     git "$@"
#     exit_status=$?

#     # If the exit status is 0 (success), log the command
#     #echo $exit_status
#     if [ $exit_status -eq 0 ]; then
#         echo "$(date) git $@" >> ~/gitcounter/frequency.log
#     else
#         echo "git-logger: The git command failed and will not be logged"
#     fi
#     #echo "$(date) git $@" >> ~/gitcounter/frequency.log
    

#     exit $exit_status
# fi

ignore_file="./.counterignore"

if [[ -f "$ignore_file" ]]; then
  # Read the ignored keywords into an array
  IFS=$'\n' read -d '' -r -a ignored_keywords < "$ignore_file"
# else
#   # If the file doesn't exist, exit with an error
#   echo "Error: .counterignore file not found at $ignore_file"
#   exit 1
fi

is_ignored_command() {
  for keyword in "${ignored_keywords[@]}"; do
    if [[ "$1" == "$keyword" ]]; then
      return 0  # Command is ignored
    fi
  done
  return 1  # Command is not ignored
}

if is_ignored_command "$1"; then
    # Do not log these commands, just pass them to git
    git "$@"
else
    # Log the command (with date and time) and pass it to git
    git "$@"
    exit_status=$?

    # If the exit status is 0 (success), log the command
    #echo $exit_status
    if [ $exit_status -eq 0 ]; then
        echo "$(date) git $@" >> /Users/jamesroot/gitcounter/frequency.log
    else
        echo "git-logger: The git command failed and will not be logged"
    fi
    
    

    exit $exit_status
fi