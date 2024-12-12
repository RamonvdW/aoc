
#  Copyright (c) 2024 Ramon van der Winkel.
#  All rights reserved.
#  Licensed under BSD-3-Clause-Clear. See LICENSE file for details.

import datetime
import json
import sys

class Leaderboard:

    def __init__(self, my_member_nr):
        self.my_member_nr = str(my_member_nr)
        self.per_day_part = dict()  # [(day, part)] = [(ts, index), ..]
        self.ts2member_nr = dict()  # [(ts, index)] = member
        self.member_nr2name = dict()  # [member_nr] = name
        self.first_ts = 0

    def seconds_to_str(self, seconds) -> str:
        minutes = seconds // 60
        if minutes >= 60:
            hours = minutes // 60
            minutes %= 60
            out = '%d:%02d:%02d' % (hours, minutes, seconds % 60)
        else:
            out = '%d:%02d' % (minutes, seconds % 60)
        return out

    def load(self, data):
        # data['event'] = '2024'
        # data['owner_id'] = 960233

        # data['day1_ts'] = 1733029200  # unix timestamp
        self.first_ts = data['day1_ts']
        # print(datetime.datetime.fromtimestamp(ts))

        for member_nr, member_data in data['members'].items():
            name = member_data['name']
            self.member_nr2name[member_nr] = name
            for day, day_data in member_data['completion_day_level'].items():
                for part in ("1", "2"):
                    if part in day_data:
                        part_data = day_data[part]
                        # print(part_data)
                        ts_index = (part_data['get_star_ts'], part_data['star_index'])
                        self.ts2member_nr[ts_index] = member_nr
                        tup = (int(day), int(part))
                        try:
                            self.per_day_part[tup].append(ts_index)
                        except KeyError:
                            self.per_day_part[tup] = [ts_index]
            # for
        # for

    def show_day(self, show_day):
        # show ranking for a specific day
        keys = list(self.per_day_part.keys())
        keys.sort()
        max_count = len(self.member_nr2name)
        prev_day = keys[0][0]
        prev_ts = ts = self.first_ts
        prev_part = 0
        for tup in keys:
            lst = self.per_day_part[tup]
            lst.sort()  # smallest first
            day, part = tup
            if day != prev_day:
                ts += 86400  # to next day
                prev_day = day
                prev_ts = ts
            if day == show_day:
                if part != prev_part:
                    print('day part rank score duration')
                    print('--- ---- ---- ----- --------')
                    prev_part = part
                nr = 0
                for ts_index in lst:
                    nr += 1
                    member_nr = self.ts2member_nr[ts_index]
                    name = self.member_nr2name[member_nr]
                    score = max_count - nr + 1
                    secs = ts_index[0] - prev_ts
                    time_str = self.seconds_to_str(secs)
                    print('%3s %4s %4d %5d %8s %s' % (day, part, nr, score, time_str, name))
                    # total += score
                    # prev_ts = ts_index[0]
        # for

    def select_by_name(self, find_name):
        for member_nr, name in self.member_nr2name.items():
            if name and name.startswith(find_name):
                self.my_member_nr = member_nr
        # for

    def show_user(self):
        # show for a specific user
        print('Results for %s' % self.member_nr2name[self.my_member_nr])
        keys = list(self.per_day_part.keys())
        keys.sort()
        max_count = len(self.member_nr2name)
        total = 0
        prev_day = keys[0][0]
        prev_ts = ts = self.first_ts
        print('day part rank score duration')
        print('--- ---- ---- ----- --------')
        for tup in keys:
            lst = self.per_day_part[tup]
            lst.sort()  # smallest first
            day, part = tup
            if day != prev_day:
                ts += 86400  # to next day
                prev_day = day
                prev_ts = ts
            nr = 0
            for ts_index in lst:
                nr += 1
                member_nr = self.ts2member_nr[ts_index]
                if member_nr == self.my_member_nr:
                    score = max_count - nr + 1
                    secs = ts_index[0] - prev_ts
                    time_str = self.seconds_to_str(secs)
                    print('%3s %4s %4d %5d %8s' % (day, part, nr, score, time_str))
                    total += score
                    prev_ts = ts_index[0]
            # for
        # for
        print('total: %s' % total)


fname = sys.argv[1]
my_member_nr = sys.argv[2]

leaderboard = Leaderboard(my_member_nr)

data = json.loads(open(fname, 'r').read())
leaderboard.load(data)

show_day = None
if len(sys.argv) > 3:
    arg = sys.argv[3]
    try:
        show_day = int(arg)
    except ValueError:
        leaderboard.select_by_name(arg)

if show_day:
    leaderboard.show_day(show_day)
else:
    leaderboard.show_user()

# end of file

