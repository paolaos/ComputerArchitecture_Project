from cpu.ProgramsContext import ProgramsContext


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
