import re
import subprocess
import webbrowser


def obtain_commits():
    user = 'git config user.email'
    '--since=<date>, --after=<date>'
    command = 'git log --all  --author={user}'.format(user=user)
    commits = execute_command(command)
    return commits


def obtain_hashes(commits_log):
    pattern_string = r'^commit\s{1}[a-zA-Z0-9]{40}$'
    pattern = re.compile(pattern=pattern_string)

    _hashes = pattern.search(commits_log)
    return _hashes


def execute_command(command):
    return subprocess.run(command.split(' '), stdout=subprocess.PIPE).stdout.decode('utf-8').strip()


if __name__ == '__main__':
    commits_log = obtain_commits()
    hashes = obtain_hashes(commits_log=commits_log)

    base_url = 'https://github.com/gimi-org/gimi-server/commit/{hash}'

    for _hash in hashes:
        url = base_url.format(_hash)
        webbrowser.open(url=url)
