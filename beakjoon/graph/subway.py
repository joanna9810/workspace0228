'''
he Stockholm subway is very inefficient. The city does not look like it did when the current subway lines were built,
 meaning certain parts are highly overutilized while some lines are barely used.

Therefore, the city council has decided to rebuild the subway. Currently,
 the system consists of N stations, with N −1 pairs of stations connected by tracks such that it is possible
 to travel between any pair of stations by subway. The council has developed a new plan that still consists
 of the same N stations, but with another set of N − 1 tracks (still in such a way that all stations are connected).

To minimize disruptions in the busy subway, the reconstruction must be performed one track at a time. Every weekend,
a single track must be closed and a new track built. This means that there will always be N − 1 tracks.
 Furthermore, it must always be possible to travel between any pair of stations after the constructions during a weekend.

Your task is to find a way of constructing the new subway network, such that these conditions hold.
Your plan must use as few weekends as possible.

입력
The first line contains the integer 1 ≤ N. The next N − 1 lines contains the tracks in the current
subway system. Each track is described by two space-separated integers a b between 0 and N − 1,
the zero-indexed numbers of the stations the track connects. It will be possible to travel between
any pair of stations using a sequence of the tracks.

The next N − 1 lines contains the tracks that should be part of the new subway system, in the same format.

출력
First, output the number of weekends K your construction plan needs.
Then, output K lines, one for each weekend in chronological order.
A line should contain four integers a1, b1, a2, b2, meaning that the track connecting a1 and b1 should be closed,
and a track connecting a2 and b2 should be built.

서브태스크 1 (33점)
N ≤ 10
서브태스크 2 (33점)
N ≤ 1000
서브태스크 3 (34점)
N ≤ 100 000
예제 입력 1
3
0 1
1 2
0 1
0 2
예제 출력 1
1
2 1 2 0
'''