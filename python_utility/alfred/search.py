def fruit_search(workflow):
    if len(workflow.args):
        query = workflow.args[0]
    else:
        query = None

    if query:
        for line in workflow.filter(query, open('tests/fixture/fruit.txt')):
            workflow.add_item(title=line, arg=line.rstrip(), valid=True)

    workflow.send_feedback()
