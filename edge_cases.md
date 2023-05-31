# Edge Cases

## Multiple Handlers

"state machine" code can use a different handler for each state. For example, instead of

```python
FUNCTION_MAPPINGS = {
    STATE.ELECTION_RESULTS: {
        SHEPHERD_HEADERS.END_ELECTION_RESULTS.name: end_election_results
    },
    STATE.PRESIDENT_DISCARD: {
        SHEPHERD_HEADERS.PRESIDENT_DISCARDED.name: president_discarded
    },
    STATE.CHANCELLOR_DISCARD: {
        SHEPHERD_HEADERS.CHANCELLOR_DISCARDED.name: chancellor_discarded,
        SHEPHERD_HEADERS.CHANCELLOR_VETOED.name: chancellor_vetoed,
    },
}
```

it would look like:

```python
HANDLERS = {
    STATE.ELECTION_RESULTS: Handler(),
    STATE.PRESIDENT_DISCARD: Handler(),
    STATE.CHANCELLOR_DISCARD: Handler(),
}
```

and each function would be annotated like this:

```python
@on_header(HANDLERS[STATE.ELECTION_RESULTS], SHEPHERD_HEADERS.END_ELECTION_RESULTS)
def end_election_results():
    pass
```

## Multiple Annotations

It is possible to annotate a function multiple times if needed:


```python
@on_header(HANDLERS[STATE.TELEOP_1], PONG_HEADERS.CHEESE)
@on_header(HANDLERS[STATE.TELEOP_2], PONG_HEADERS.CHEESE)
@on_header(HANDLERS[STATE.TELEOP_2], PONG_HEADERS.FOOD)
def send_cheese():
    pass
```