class FiniteStateMachine:
    def __init__(self, states, transitions):
        self.states = states
        self.transitions = transitions

    def process_input(self, input_string):
        all_needle_starts = []
        starting_state = "s0"
        current_state = starting_state
        states = self.states

        for symbol_index, symbol in enumerate(input_string):
            try:
                current_state = self.transitions[current_state][symbol]
            except KeyError:
                try:
                    current_state = self.transitions[starting_state][symbol]
                except KeyError:
                    current_state = starting_state

            if current_state == f"s{len(self.states)}":
                current_state = starting_state
                all_needle_starts.append(symbol_index - len(self.states) + 1)

        return all_needle_starts


def transitions_init(haystack, needle):
    if len(needle) == 0:
        return []

    states = {f"s{i}" for i in range(len(needle))}
    transitions = {}

    first_symbol = needle[0]

    for i in range(len(needle)):
        current_state = "s" + str(i)
        next_state = "s" + str(i + 1)
        if first_symbol is not None and first_symbol is not needle[i]:
            transitions[current_state] = {
                needle[i]: next_state,
                first_symbol: f"s{str(i-1)}",
            }
            first_symbol = None
        else:
            transitions[current_state] = {needle[i]: next_state}

    for i in range(len(needle)):
        current_state = "s" + str(i)

    transitions["s" + str(len(needle))] = {}
    print(transitions)

    fsm = FiniteStateMachine(states, transitions)
    return fsm.process_input(haystack)


if __name__ == "__main__":
    haystack = "ababcdeabcabcabc"
    needle = "abc"
    print(transitions_init(haystack, needle))
