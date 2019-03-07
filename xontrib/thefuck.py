from builtins import aliases, __xonsh__.history, evalx


def _new_command(args, stdin=None):
    last_command = __xonsh__.history[-1].cmd
    evalx('thefuck {}'.format(last_command))

aliases['fuck'] = _new_command
