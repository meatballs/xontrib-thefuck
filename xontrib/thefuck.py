from builtins import aliases, __xonsh__, evalx


def _new_command(args, stdin=None):
    try:
        last_command = __xonsh__.history[-1].cmd.strip()
    except IndexError:
        return

    execx('thefuck {}'.format(last_command))

aliases['fuck'] = _new_command
