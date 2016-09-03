from builtins import aliases, __xonsh_history__, evalx


def _new_command(args, stdin=None):
    last_command = __xonsh_history__.show("session")[-1][0]
    evalx('thefuck {}'.format(last_command))

aliases['fuck'] = _new_command
