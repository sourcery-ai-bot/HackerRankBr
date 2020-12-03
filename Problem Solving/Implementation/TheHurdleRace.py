"""
HackerRank - Algorithms - Implemation
The Herdle Race
"""

def hurdleRace(k, height):
    max_height = max(height)
    if k < max_height:
        return max_height - k
    else:
        return 0



# Outra opção
# def hundkeRace(k, height)
#     return max(0, max(height) - k)
