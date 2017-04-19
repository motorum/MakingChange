 ```

n = int(IN[0])

panel_a = IN[1]
panel_b = IN[2]
panel_c = IN[3]
coins = [panel_a, panel_b, panel_c]

def change(n, coins_avalible, coins_so_far):
	if sum(coins_so_far) == n:
		yield coins_so_far
	elif sum(coins_so_far) > n:
		pass
	elif coins_avalible == []:
		pass
	else:
		for c in change(n, coins_avalible[:], coins_so_far+[coins_avalible[0]]):
			yield c
		for c in change(n, coins_avalible[1:], coins_so_far):
			yield c

solutions = [s for s in change(n, coins, [])]

OUT = solutions

 ```
