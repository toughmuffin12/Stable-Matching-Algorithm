import sys
sys.path.append('/Desktop/Algoritms and Analysis/Preferences')
from Preferences import men, women, women_preference, men_preference
from collections import deque

#Converts a preferance dictionary to ra dictionary with rankings assigned
def preference_to_rank(preferences):
    return {
        a: {b: idx for idx, b in enumerate(a_preference)}
        for a, a_preference in preferences.items()
    }

#Gale-Sharply Algorithm that creates a stable match of two lists with dictionary preferences lists
def stable_match(A, B, A_preference, B_preference):
    B_rank = preference_to_rank(B_preference)
    ask_list = {a: deque(bs) for a, bs in A_preference.items()}
    pair = {}
    remaining_A = set(A)

    while len(remaining_A) > 0:
        a = remaining_A.pop()
        b = ask_list[a].popleft()
        if b not in pair:
            pair[b] = a
        else:
            a0 = pair[b]
            B_preference_a0 = B_rank[b][a0] < B_rank[b][a]
            if B_preference_a0:
                remaining_A.add(a)
            else:
                remaining_A.add(a0)
                pair[b] = a
    return [(a, b) for b, a in pair.items()]

print(stable_match(men, women, men_preference, women_preference))