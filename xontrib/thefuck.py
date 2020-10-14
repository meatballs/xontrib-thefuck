import subprocess
def __fuckit(fuck_path, fuck_hist):
    """
    https://github.com/xonsh/xonsh/issues/928#issuecomment-611711887
    """
    p = subprocess.Popen([fuck_path, fuck_hist], stdout=subprocess.PIPE)
    out, _ = p.communicate()
    execx(out.decode('utf-8'))

aliases['fuck'] = "__fuckit($(which thefuck), $(history -1))"
