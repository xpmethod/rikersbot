with open('tweets.txt', 'r') as f:
    for line in f:
        # chomp the end of line character
        if len(line.rstrip()) > 140:
            print len(line)
            print line
