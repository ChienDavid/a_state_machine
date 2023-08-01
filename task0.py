"""
Task 0: implement Fail Safe Function based on Finite state machine
"""

from statemachine import StateMachine

def start(msg):
    pass

def mid_1(msg):
    pass

def mid_2(msg):
    pass

def mid_3(msg):
    pass

def end_1(msg):
    pass

def end_2(msg):
    pass



def main():
    print("Implementation of Fail Safe Function.")
    # create a state machine
    fsf = StateMachine()

    # add states to the state machine
    fsf.add_state("Start", start)
    fsf.add_state("mid_1", mid_1)
    fsf.add_state("mid_2", mid_2)
    fsf.add_state("mid_3", mid_3)
    fsf.add_state("end_1", end_1, None, end_state=1)
    fsf.add_state("end_2", end_2, None, end_state=1)

    # set start the state machine
    fsf.set_start("Start")

    # run the state machine
    msg = "something"
    fsf.execute(msg)

if __name__=="__main__":
    main()

