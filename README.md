# git-counter

## Intro

@git-counter is a self-used tool that records and analyzes all the Git commands you have run on your machine and generates data insight.

## Ask yourself before using git-counter

-   Have you ever encounter situations where you forget a Git command that you have used a lot but failed to recall its usage?
-   Have you ever wondered which are your most used Git commands?
-   Would you like an intuitive way to understand how you use Git in your developement?

If you answered 'yes' in one of the questions, git-counter is a good tool for you!

## Usage

Add the following alias to `.bashrc` or `.zshrc` and `source .zshrc`

```shell
alias git='/Location/Of/Script/git_logger.sh'
```

Give `git-logger.sh` executable permission

```shell
sudo chmod 765 git-logger.sh
```

Run `git-logger.sh`

```python
# Just type any git commands and they will be recorded
```

Run analysis

```python
python analysis.py
```

## Example output report

![alt](example/insight.png)
