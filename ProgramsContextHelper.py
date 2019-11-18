from ProgramsContext import ProgramsContext


def save_context(program_context: ProgramsContext, context: []):
    """
    Update a program context in an array that already contains the context
    :param program_context: the new program context
    :param context: the contexts array
    """
    i = 0
    while i < len(context):
        if context[i].context_id == program_context.context_id:
            context[i] = program_context
            i = len(context)
        i += 1


def create_context(context_id, initial_address, contexts: []):
    """
    Create a new program context and add it to a context array
    :param context_id: the new context id
    :param initial_address: the new context initial address
    :param contexts: the context array
    """
    program = ProgramsContext()
    program.context_id = context_id
    program.start_address = initial_address
    contexts.append(program)
