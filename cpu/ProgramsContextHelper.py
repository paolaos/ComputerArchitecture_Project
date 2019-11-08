from cpu.ProgramsContext import ProgramsContext


def get_next_pending_program(context: []):
    program = ProgramsContext()
    tries = 0

    while program.context_id == -1 and tries < len(context):
        if not context[tries].taken:
            program = context[tries]
        tries += 1
    return program


def save_context(program_context: ProgramsContext, context: []):
    i = 0
    while i < len(context):
        if context[i].context_id == program_context.context_id:
            context[i] = program_context
            i = len(context)
        i += 1


def create_context(context_id, initial_address, contexts: []):
    program = ProgramsContext()
    program.context_id = context_id
    program.start_address = initial_address
    contexts.append(program)
