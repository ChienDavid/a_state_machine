"""
Ex.: create a general state machine
"""

class StateMachine:
    def __init__(self):
        """Initilize a general state machine"""
        self.handlers = {}
        self.startState = None
        self.endState = []

    def add_state(self, name, handler, end_state=0):
        """Add a state
        :param name: is a desired name of a state.
        :param handler: is handler of the state
        :param end_state: is a boolean value, 0 for the last state, 1 for not the last state"""
        name = name.upper()
        self.handlers[name] = handler
        if end_state:
            self.endState.append(name)

    def set_start(self, name):
        """Set a state as a start state"""
        self.startState = name.upper()

    def execute(self, msg):
        try:
            handler = self.handlers[self.startState]
        except:
            raise NotImplementedError("Must call .set_start() before .execute()")
        
        if not self.endState:
            raise NotImplementedError("At least one state must be an en_state.")
        
        while True:
            (newState, msg) = handler(msg)
            if newState.upper() in self.endState:
                print("Reached {}".format(newState))
                break
            else:
                handler = self.handlers[newState.upper()]


