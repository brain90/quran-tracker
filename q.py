total = 0
with open('quran.csv') as f:
    next(f)
    for line in f:
        memo = (line.split(';')[3]).strip()
        memo = memo.split(',')

        if len(memo) == 1 and memo[0].strip() == "":
            continue

        for e in memo:
            if '-' in e:
                total += abs(eval(e)) + 1
            else:
                total += int(e)

percent = (float(total) / float(6236)) * 100
remain = 6236 - total
remain_percent = 100-percent

print "memorized : {} of 6236 ({:.2f}%)".format(total, percent)
print "remainder : {} ({:.2f}%)".format(remain, remain_percent)
