from collections import defaultdict

import numpy as np
from team_queue import TeamQueue
import random
import configparser

config_section = 'SIMULATION'
params = configparser.ConfigParser()
params.read('parameters.ini')
wait_time_median = params.getint(config_section, 'wait_time_median')
action_time_median = params.getint(config_section, 'action_time_median')
sideout_percentage_median = params.getfloat(config_section, 'sideout_percentage_median')
sideout_percentage_stdev = params.getfloat(config_section, 'sideout_percentage_stdev')
sideout_percentage_improvement_30_seconds = params.getfloat(config_section, 'sideout_percentage_improvement_30_seconds')
match_time = params.getint(config_section, 'match_time')

rng = np.random.default_rng()


def sideout(count):
    teams = rng.normal(
        sideout_percentage_median,
        sideout_percentage_stdev,
        count)
    return [min(1, max(0, x)) for x in teams]


def wait_time():
    return rng.poisson(wait_time_median)


def action_time():
    return rng.poisson(action_time_median)


def opponents(score):
    return [team[0] for team in sorted(score.items(), key=lambda x: x[1], reverse=True)]


def use_strategy(queue, score, time, variant):
    if variant == 'none':
        return False
    if variant == 'early':
        return True
    if variant == 'last_30':
        return time < 30
    if variant == 'trailing_last_360':
        return time < 360 and queue[1] in opponents(score)[-2:]
    if variant == 'trailing_last_120':
        return time < 120 and queue[1] in opponents(score)[-2:]
    if variant == 'leading_last_120':
        return time < 120 and queue[1] in opponents(score)[0:2]


def play(count, golden_strategy):
    # print('King of the Court with ' + str(count) + ' teams')
    teams = sideout(count)
    time = match_time

    queue = TeamQueue(count)
    # print('Start order: ' + str(queue.order()))

    score = defaultdict(int)

    golden_ball_used = False

    # Play until time runs out
    while time > 0:
        time -= action_time()
        active_team = queue.active()

        sideout_percentage = teams[active_team]
        if time < 30:
            sideout_percentage += sideout_percentage_improvement_30_seconds
        if time > 30 and random.random() < sideout_percentage:
            score[active_team] += 1
            queue.sideout(True)
        elif active_team == 0\
                and not golden_ball_used\
                and use_strategy(queue.order(), score, time, strategy):
            # print('used strategy')
            golden_ball_used = True
            if random.random() < sideout_percentage:
                score[active_team] += 1
                queue.sideout(True)
            else:
                queue.sideout(False)
        else:
            queue.sideout(False)

        time -= wait_time()

    # print(queue.queue)
    if count > 3:
        return not queue.queue[-1] == 0
    else:
        return queue.queue[0] == 0


def sim_results(results):
    return 'Winner: ' + str(results[3]*100/results['total'])\
           + '%, Top-4: ' + str(results[4]*100/results['total'])\
           + '%, Top-5: ' + str(results[5] * 100 / results['total'])


strategies = ['none', 'early', 'last_30', 'trailing_last_360', 'trailing_last_120', 'leading_last_120']
for strategy in strategies:
    simulation = defaultdict(int)
    for i in range(10000):
        simulation['total'] += 1
        for n in range(3, 6):
            if play(n, strategy):
                simulation[n] += 1

    print('Strategy ' + strategy + ': ' + sim_results(simulation))
