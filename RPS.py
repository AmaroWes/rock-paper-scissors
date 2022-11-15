predict_opponent = dict()

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    guess = "R"
    num = 4

    if len(opponent_history) > num:
        data = ''.join(opponent_history[-num:])
        possible = [data+'R', data+'P', data+'S']
        guess = {'R':'P', 'S':'R', 'P':'S'}

        if ''.join(opponent_history[-(num + 1):]) in predict_opponent.keys():
            predict_opponent[''.join(opponent_history[-(num + 1):])]+=1
        else:
            predict_opponent[''.join(opponent_history[-(num + 1):])]=1

        for i in possible:
            if not i in predict_opponent.keys():
                predict_opponent[i] = 0
        
        predict = max(possible, key=lambda key: predict_opponent[key])
        predict = predict[-1]
        
        return guess[predict]

    return guess