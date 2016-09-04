from builtins import aliases, __xonsh_history__, evalx


def _new_command(args, stdin=None):
    last_command = __xonsh_history__.__getitem__(-1)
    evalx('thefuck {}'.format(last_command))

aliases['fuck'] = _new_command
