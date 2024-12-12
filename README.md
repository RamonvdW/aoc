# aoc
Advent of Code private leaderboard detailed reporting

See https://adventofcode.com/

How to run:
1) Copy contents of your session cookie from your browser.
   Put it in the SESSION variable in the `get.sh` script.
   This will work for 1 month and allows download if the leaderboard json.
   
2) Find your personal member number on the AoC site under Settings.
   Put the number in the `MY_MEMBER_NR` variable in the `show.sh` script.
   
3) run `./get.sh` to download the private leaderboard data.

4) run the show.sh script to get the detailed report.

   run `./show.sh` (no arguments) to get your detailed report.
   see sample below.

   run `./show.sh PartOfName` to show the detailed report for a specific user.
   run `./show.sh "Part of name"` to show the detailed report for a specific user.

   run `./show.sh 5` to show the detailed report for day 5.

Sample output:

    Results for Ramon van der Winkel
    day part rank score duration
    --- ---- ---- ----- --------
      1    1   47   154 11:31:05
      1    2   45   156     2:50
      2    1   14   187  1:11:04
      2    2   11   190    14:23
      3    1    2   199     6:08
      3    2    2   199     7:47
      4    1   12   189    32:30
      4    2   11   190    34:28
      5    1    7   194    19:23
      5    2    4   197     9:08
      6    1    5   196    16:43
      6    2    3   198    33:08
      7    1    1   200    11:13
      7    2    1   200     1:36
      8    1    6   195    21:48
      8    2    4   197     3:44
      9    1    6   195    22:36
      9    2    4   197    16:55
     10    1    1   200    13:29
     10    2    1   200     1:17
     11    1    2   199     7:19
     11    2   19   182  1:42:01
     12    1    8   193    34:47
     12    2    2   199    27:55
    total: 4606
 