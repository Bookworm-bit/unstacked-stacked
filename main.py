from person import Person
import matplotlib.pyplot as plt
import numpy as np

def get_good_consistent(team):
    num = 0
    for p in team:
        num += p.get_good_consistent()
    return num

def trial():
    num = 100

    performances = { Person() : 0 for _ in range(num) }
    for tm in performances.keys():
        performances[tm] += tm.get_performance()

    performances = dict(sorted(performances.items(), key=lambda x: x[1], reverse=True))
    performances = dict(list(performances.items())[:45])
    print(performances)

    stacked_team_a_people = [list(performances.keys())[i] for i in range(15)]
    
    invites = 5
    for _ in range(invites):
        for tm in performances.keys():
            performances[tm] += tm.get_performance()

    performances = dict(sorted(performances.items(), key=lambda x: x[1], reverse=True))
    print(performances)

    unstacked_team_a_people = [list(performances.keys())[i] for i in range(15)]

    return (get_good_consistent(unstacked_team_a_people), get_good_consistent(stacked_team_a_people))


def main():
    trials = 100
    stacked = []
    unstacked = []
    for _ in range(trials):
        a, b = trial()
        stacked.append(b)
        unstacked.append(a)

    plt.plot(range(trials), stacked, label='Stacked')
    plt.plot(range(trials), unstacked, label='Unstacked')

    # Trendlines
    # z_stacked = np.polyfit(range(trials), stacked, 1)
    # p_stacked = np.poly1d(z_stacked)
    # plt.plot(range(trials), p_stacked(range(trials)), linestyle='--', color='blue', label='Stacked Trendline')

    # z_unstacked = np.polyfit(range(trials), unstacked, 1)
    # p_unstacked = np.poly1d(z_unstacked)
    # plt.plot(range(trials), p_unstacked(range(trials)), linestyle='--', color='orange', label='Unstacked Trendline')

    plt.xlabel('Trial')
    plt.ylabel('Good Consistent People')
    plt.title('Performance of Stacked vs Unstacked Teams')
    plt.legend()
    plt.show()

    

if __name__ == "__main__":
    main()