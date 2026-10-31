"""Bind one already-selected literal question to its immediately following answer."""
from .core import content_tokens


def bind_selected_question(index, rows, query):
    query_terms = content_tokens(query)
    if not query_terms:
        return rows
    sources = {}
    positions = {}
    for row in index.rows:
        source = row['source_id']
        info = sources.setdefault(source, dict(end=0, role=row['role'].casefold(),
            key=(row['session_id'], row['request_id'], row['position'])))
        info['end'] = max(info['end'], row['end'])
        positions.setdefault(info['key'], set()).add(source)
    selected = {}
    for position, (_, row) in enumerate(rows):
        selected.setdefault(row['source_id'], []).append(position)
    for answer_position, (_, answer) in enumerate(rows):
        info = sources[answer['source_id']]
        if info['role'] != 'assistant':
            continue
        session, request, position = info['key']
        if len(positions[info['key']]) != 1:
            continue
        previous = positions.get((session, request, position - 1), set())
        if len(previous) != 1:
            continue
        source = next(iter(previous))
        parent = sources[source]
        indices = selected.get(source, [])
        if parent['role'] != 'user' or parent['end'] > 512 or len(indices) != 1:
            continue
        question_position = indices[0]
        if question_position <= answer_position:
            continue
        question = rows[question_position][1]
        if question['start'] != 0 or question['end'] != parent['end']:
            continue
        if '?' not in question['content'] and '？' not in question['content']:
            continue
        missing_query_terms = query_terms - content_tokens(answer['content'])
        if not missing_query_terms.intersection(content_tokens(question['content'])):
            continue
        output = list(rows)
        companion = output.pop(question_position)
        output.insert(answer_position, companion)
        return output
    return rows
