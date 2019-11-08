from cpu.ProgramsContext import ProgramsContext


def get_next_pending_program(context: []):
    program: ProgramsContext = None
    tries = 0

    while program is None and tries < context.length:
        if not context[tries].taken:
            program = context[tries]
        tries += 1
    return program


def save_context(program_context: ProgramsContext, context: []):
    i = 0
    while i < context.length:
        if context[i].context_id == program_context.context_id:
            context[i] = program_context
            i = context.length
        i += 1
