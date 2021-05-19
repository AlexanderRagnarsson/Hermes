from Environment import Environment
env = Environment(True)

while not env.is_terminal(env.current_state):
    print(env.current_state.board)
    legal = env.legal_moves(env.current_state)
    for i in range(len(legal)):
        print(f"{i} {legal[i]}")
    move = input("Enter move: ")
    env.apply_move_to_current(legal[int(move)])
