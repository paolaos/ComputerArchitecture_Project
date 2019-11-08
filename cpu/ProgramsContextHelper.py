from cpu.ProgramsContext import ProgramsContext


def get_next_pending_program(context: []):
    program: ProgramsContext = None
    tries = 0

    while program is None and tries < context.length:
        if not context[tries].taken:
            program = context[tries]
        tries += 1
    return program
