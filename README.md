# King of the Court - How to use the golden ball?


As a big beach volleyball fan, I enjoy watching the [King of the Court](https://www.kingofthecourt.com) events.
In these event the winner of the group phase receives a 'golden ball'.
The purpose of the golden ball is to be allowed to repeat a rallye in a later session.
This could be a huge advantage as the team can continue a sideout streak.
The only question is when to use the golden ball.

## Golden ball strategies
As one King of the Court session contains many rallies, there is a huge number of situations in which the golden ball can be used.
The players do not have any option to calculate the situation on the fly and no coaches are allowed.
Hence, I recommend to stick to a single strategy which is easy to apply:
* Do not use it: Just for comparison or for those teams without the need for any advantage.
* Use it as early as possible: Baseline strategy without the need to think any further about it.
* Use it only in the last 30 seconds: In the last 30 seconds service errors count as points which is good on the queen/king side and leads to easier serves. However, it does not happen to often that you are on this side at the very end.
* Use it only in the last six minutes and only if the serving team is in last or second to last position: This strategy let you wait until it is more evident who might be your direct opponent for elimination and makes it harder for them to get to the queen/king side.
* Use it only in the last two minutes and only if the serving team is in last or second to last position: Like before but focused on the crunch time.
* Usi it only in the last two minutes and only if the serving team is in first or second position: Similar to the other but directed towards winning the session (in case of just three teams).

## Evaluate Strategies with Monte Carlo experiment
As only limited data is available, we need to rely on a [Monte Carlo experiment](https://en.wikipedia.org/wiki/Monte_Carlo_method).
The idea is that an entire session is simulated with slightly different parameters (sideout percantages in this case).
It is the counted how often one strategy leads to a win (in the final round with three teams) or help to avoid elimination (with four or five teams).
This program combines the simulation of king of the court sessions in a Monte Carlo experiment to suggest the best strategy.

## Results
The results show the success rate.
With three teams your goal is to win, while with four or five teams, you just want to avoid elimination.
Keep in mind that a Monte Carlo experiments are not 100% reliable and use random parameters.
Differences of few percent points are within error margins.

|Strategy| 3 Teams | 4 Teams | 5 Teams | Comments |
|---|---|---|---|---|
| Do not use it | 33%| 75% | 80% | All teams have same chance of winning |
| Use it as early as possible | 33%| 74% | 80% | Basically no advantage |
| Use it only in last 30 seconds | **43%**| 74% | 79% | Use this strategy in the final round! |
| Last 6 minutes on trailing teams | 35%| 75% | 80% | Higher success rate for elimination phases but within error margin |
| Last 2 minutes on trailing teams | 35%| 75% | 80% | Same as above |
| Last 2 minutes on leading teams | 38%| 76% | 80% | Slightly higher success rate for last phase |


## Summary
If you compete in King of the Court and you have a golden ball available, the best suggestion is to not use it until the last phase and use it only in the last 30 seconds.