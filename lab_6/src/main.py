class FiniteStateMachine:
    def __init__(self, states, transitions):
        self.states = states
        self.transitions = transitions

    def process_input(self, input_string):
        all_needle_starts = []
        starting_state = "s0"
        current_state = starting_state

        for symbol_index, symbol in enumerate(input_string):
            try:
                current_state = self.transitions[current_state][symbol]
            except KeyError:
                try:
                    current_state = self.transitions[starting_state][symbol]
                except KeyError:
                    current_state = starting_state

            if current_state == f"s{len(self.states)}":
                all_needle_starts.append(symbol_index - len(self.states) + 1)

        return all_needle_starts


def transitions_init(haystack, needle):
    if len(needle) == 0:
        return []

    states = {f"s{i}" for i in range(len(needle))}
    transitions = {}

    for i in range(len(needle)):
        current_state = "s" + str(i)
        next_state = "s" + str(i + 1)
        transitions[current_state] = {needle[i]: next_state}

    transitions["s" + str(len(needle))] = {}

    fsm = FiniteStateMachine(states, transitions)
    return fsm.process_input(haystack)


if __name__ == "__main__":
    haystack = "ababcdeabcabcabc"
    needle = "abc"
    print(transitions_init(haystack, needle))
