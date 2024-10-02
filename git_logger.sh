if [[ "$1" == "add" || "$1" == "commit" || "$1" == "push" || "$1" == "status" ]]; then
    # Do not log these commands, just pass them to git
    git "$@"
else
    # Log the command (with date and time) and pass it to git
    git "$@"
    exit_status=$?

    # If the exit status is 0 (success), log the command
    #echo $exit_status
    if [ $exit_status -eq 0 ]; then
        echo "$(date) git $@" >> ~/gitcounter/frequency.log
    else
        echo "git-logger: The git command failed and will not be logged"
    fi
    #echo "$(date) git $@" >> ~/gitcounter/frequency.log
    

    exit $exit_status
fi


# # Check if the command is one of the ignored ones
# if [[ "$1" == "add" || "$1" == "commit" || "$1" == "push" ]]; then
#   # Directly execute the command without logging
#   git "$@"
# else
#   # Execute the git command and capture the exit status
#   git "$@"
#   exit_status=$?

#   # If the exit status is 0 (success), log the command
#   if [ $exit_status -eq 0 ]; then
#     echo "$(date) $@" >> ~/.git_command_log
#   fi

#   # Return the original exit status to the shell
#   exit $exit_status
# fi
