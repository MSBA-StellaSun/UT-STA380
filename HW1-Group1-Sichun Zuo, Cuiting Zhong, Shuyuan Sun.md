
**1 Rock, Paper, Scissors (30 points)**


```python
import random
import operator

def comp(n, d):
    if n == 1:
        a = random.randint(1, 3)
        if a == 1:
            comp_choice = "rock"
        elif a == 2:
            comp_choice = "paper"
        else:
            comp_choice = "scissors"
    else:
        maxv=max(d.values())
        pre_player=[]
        for i in d.keys():
            if d[i] == maxv:
                pre_player.append(i)
        if len(pre_player)==1:
            if "rock" in pre_player:
                comp_choice = "paper"
            elif "paper" in pre_player:
                comp_choice = "scissors"
            else:
                comp_choice = "rock"
        elif len(pre_player)==2:
            if ('rock' in pre_player) and ('paper' in pre_player):
                comp_choice='paper'
            elif ('rock' in pre_player) and ('scissors' in pre_player):
                comp_choice='rock'
            else:
                comp_choice='scissors'
        else:
            comp_choice=random.choice(['rock','paper','scissors'])
    return comp_choice


def result(c, p):
    if c == p:
        return "The result is: Draw"
    if c == "rock":
        if p == "scissors":
            return "The result is: Computer Win"
        elif p == "paper":
            return "The result is: Player Win"
    if c == "scissors":
        if p == "rock":
            return "The result is: Player Win"
        elif p == "paper":
            return "The result is: Computer Win"
    if c == "paper":
        if p == "scissors":
            return "The result is: Player Win"
        elif p == "rock":
            return "The result is: Computer Win"

def count_number(p, d):
    if p == "rock":
        d['rock'] += 1
    elif p == "paper":
        d['paper'] += 1
    else:
        d['scissors'] += 1
    return d

def play(n):
    player='null'
    if n==1:
        player='rock'
    if n==2:
        player='paper'
    if n==3:
        player='scissors'
    return player

print "Welcome to Rock-paper-scissors Game!\n"

def main():
    n = 0
    w = 0
    count = {'rock': 0, 'paper': 0, 'scissors':0}
    while(True):
        n += 1
        print "Round", n
        comp_choice = comp(n, count)
        player_choice = int(raw_input("Rock, Paper Scissors Game begins!\nChoose one of them:\n1-Rock;\n2-Paper;\n3-Scissors;\n4-Quit Game.\n"))
        while player_choice != 1 and player_choice != 2 and player_choice != 3\
                and player_choice != 4:
            player_choice = int(raw_input("Please follow the instruction.\nChoose one of them:\n1-Rock;\n2-Paper;\n3-Scissors;\n4-Quit Game.\n"))
        if player_choice == 4:
            print "\n","Total round is", n-1,'times\n', "Player wins", w,'times'
            break
        else:
            print "Computer choice is",comp_choice, ";", "Player choice is", play(player_choice)
            r = result(comp_choice, play(player_choice))
            if r == "The result is: Player Win":
                w += 1
            print result(comp_choice, play(player_choice))
            count=count_number(play(player_choice), count)
        print count,'\n'

main()
```

    Welcome to Rock-paper-scissors Game!
    
    Round 1
    Rock, Paper Scissors Game begins!
    Choose one of them:
    1-Rock;
    2-Paper;
    3-Scissors;
    4-Quit Game.
    1
    Computer choice is scissors ; Player choice is rock
    The result is: Player Win
    {'scissors': 0, 'paper': 0, 'rock': 1} 
    
    Round 2
    Rock, Paper Scissors Game begins!
    Choose one of them:
    1-Rock;
    2-Paper;
    3-Scissors;
    4-Quit Game.
    1
    Computer choice is paper ; Player choice is rock
    The result is: Computer Win
    {'scissors': 0, 'paper': 0, 'rock': 2} 
    
    Round 3
    Rock, Paper Scissors Game begins!
    Choose one of them:
    1-Rock;
    2-Paper;
    3-Scissors;
    4-Quit Game.
    2
    Computer choice is paper ; Player choice is paper
    The result is: Draw
    {'scissors': 0, 'paper': 1, 'rock': 2} 
    
    Round 4
    Rock, Paper Scissors Game begins!
    Choose one of them:
    1-Rock;
    2-Paper;
    3-Scissors;
    4-Quit Game.
    3
    Computer choice is paper ; Player choice is scissors
    The result is: Player Win
    {'scissors': 1, 'paper': 1, 'rock': 2} 
    
    Round 5
    Rock, Paper Scissors Game begins!
    Choose one of them:
    1-Rock;
    2-Paper;
    3-Scissors;
    4-Quit Game.
    2
    Computer choice is paper ; Player choice is paper
    The result is: Draw
    {'scissors': 1, 'paper': 2, 'rock': 2} 
    
    Round 6
    Rock, Paper Scissors Game begins!
    Choose one of them:
    1-Rock;
    2-Paper;
    3-Scissors;
    4-Quit Game.
    1
    Computer choice is paper ; Player choice is rock
    The result is: Computer Win
    {'scissors': 1, 'paper': 2, 'rock': 3} 
    
    Round 7
    Rock, Paper Scissors Game begins!
    Choose one of them:
    1-Rock;
    2-Paper;
    3-Scissors;
    4-Quit Game.
    4
    
    Total round is 6 times
    Player wins 2 times
    

**2 Voters in Florida (30 points)**


```python
import re

fp=open('C:/Users/ayuan/OneDrive/Documents/2. UT Summer/2.MIS Data Analytics Programming/Assignments/HW1/FloridaVoters.HTML','r')
line=fp.readlines()
i1=line.index('<td>ALACHUA</td>\n')
i2=line.index('<td>12,215,216</td>\n')
line=line[i1:i2+1]
line2=[]

# Select County, Republican and Democrat.
for i in range(int((len(line)+2)/8)):
# There are two items of 'blanks' after each datapoint,except for the last datapoint 'TOTAL'.
    line2.append(line[8*i])
    line2.append(line[8*i+1])
    line2.append(line[8*i+2])
    
line3=[]
for each in line2:
    each=each.lstrip('<td>').rstrip('</td>\n')
    slices=re.findall('\d+',each)
    num=''
    for i in range(int(len(slices))):
        num=num+slices[i]
    if len(slices)==0:
        line3.append(each)
    else:
        line3.append(int(num))
        
tb=[] #[(county, republican, democart)]
for i in range(int(len(line3)/3)):
    n1=line3[3*i]
    n2=line3[3*i+1]
    n3=line3[3*i+2]
    tb.append([n1,n2,n3])
tb.sort(key=lambda x:x[2])
for each in tb:
    print each[0],' ',each[1],' ',each[2]
```

    LAFAYETTE   1373   2672
    GLADES   2190   3110
    LIBERTY   720   3372
    UNION   2752   3579
    GILCHRIST   5789   3652
    FRANKLIN   2234   4319
    HOLMES   5282   4434
    GULF   4234   4521
    HARDEE   4859   4702
    HAMILTON   2154   4796
    DIXIE   3314   4839
    CALHOUN   2201   5324
    WASHINGTON   7101   5687
    JEFFERSON   2636   5802
    BAKER   6963   5813
    BRADFORD   6878   6533
    TAYLOR   3950   6915
    MADISON   2992   7158
    DESOTO   4870   7181
    OKEECHOBEE   7755   7756
    HENDRY   5862   7999
    WAKULLA   7374   8889
    LEVY   11665   9509
    WALTON   25609   10013
    SUWANNEE   10745   11126
    NASSAU   32958   14013
    COLUMBIA   15790   14797
    JACKSON   9626   15706
    MONROE   20602   17614
    HIGHLANDS   27100   19997
    PUTNAM   17067   20606
    GADSDEN   4372   22161
    SUMTER   47158   22977
    FLAGLER   30047   24734
    OKALOOSA   75154   25172
    SANTA ROSA   73627   26114
    MARTIN   53800   27358
    INDIAN RIVER   47794   28204
    CITRUS   46373   30440
    BAY   57456   30733
    CLAY   76584   31285
    CHARLOTTE   54421   35602
    ST. JOHNS   88385   39531
    HERNANDO   51254   42499
    COLLIER   100167   45511
    LAKE   93604   67237
    MANATEE   96063   67926
    ESCAMBIA   90265   70180
    OSCEOLA   44594   75657
    ST. LUCIE   59626   76163
    MARION   97306   76268
    ALACHUA   47329   77996
    SARASOTA   125872   89711
    SEMINOLE   107833   91686
    LEON   54554   103140
    PASCO   125305   104324
    LEE   180718   114633
    VOLUSIA   121402   124136
    BREVARD   167129   127435
    POLK   140619   143799
    PINELLAS   223077   221968
    DUVAL   210195   229501
    ORANGE   206174   303458
    HILLSBOROUGH   257436   314265
    PALM BEACH   245452   367236
    MIAMI-DADE   362161   539367
    BROWARD   249762   566185
    Total   4377713   4637026
    

**3 The Google of Quotes (40 points)**

(a) Build a list of full quotes (5 points).


```python
import math
import re

fp=open('C:/Users/ayuan/OneDrive/Documents/2. UT Summer/2.MIS Data Analytics Programming/Assignments/HW1/quotes.txt','r')

line=fp.readline()
text=[line.rstrip('\n')]
for line in fp:
    line=line.rstrip('\n')
    text.append(line)
pool=[]
for i in range(int(len(text)/2)):
    pool.append(text[2*i]+' - '+text[2*i+1])
pool
```




    ['How we spend our days is, of course, how we spend our lives. - Annie Dillard',
     'Two roads diverged in a wood, and I...I took the one less traveled by, and that has made all the difference. - Robert Frost',
     'What is happiness? The feeling that power is growing, that resistance is overcome. - Friedrich Nietzsche',
     'A great deal of intelligence can be invested in ignorance when the need for illusion is deep. - Saul Bellow',
     'Those who are preoccupied with `making a statement` usually don`t have any statements worth making. - Thomas Sowell',
     'Women need a reason to have sex -- men just need a place. - Billy Crystal',
     'The heart has its reasons, of which the mind knows nothing. - Blaise Pascal',
     'It is necessary for the welfare of society that genius should be privileged to utter sedition, to blaspheme, to outrage good taste, to corrupt the youthful mind, and generally to scandalize one`s uncles. - George Bernard Shaw',
     'Freedom is not something that anybody can be given; freedom is something people take and people are as free as they want to be. - James Baldwin',
     'Collecting more taxes than is absolutely necessary is legalized robbery. - Calvin Coolidge',
     'I almost had a pyschic girlfriend, but she left me before we met. - Steven Wright',
     'The man who disobeys his parents will have disobedient sons. - Nachman of Bratslav',
     'I know God will not give me anything I can`t handle. I just wish that He didn`t trust me so much. - Mother Teresa',
     'When an American says that he loves his country, he means not only that he loves the New England hills, the prairies glistening in the sun, the wide and rising plains, the great mountains, and the sea. He means that he loves an inner air, an inner light in which freedom lives and in which a man can draw the breath of self-respect. - Adlai Stevenson',
     'Words which do not give the light of Christ increase the darkness. - Mother Teresa',
     'My dream is of a place and a time where America will once again be seen as the last best hope of earth. - Abraham Lincoln',
     'An actor is at most a poet and at least an entertainer. - Marlon Brando',
     'Humility is the foundation of all the other virtues hence, in the soul in which this virtue does not exist there cannot be any other virtue except in mere appearance. - Saint Augustine',
     'The object of teaching a child is to enable him to get along without a teacher. - Elbert Hubbard',
     'Avoid the base hypocrisy of condemning in one man what you pass over in silence when committed by another. - Theodore Roosevelt',
     'Most football teams are temperamental. That`s 90% temper and 10% mental. - Doug Plank',
     'There can be no liberty unless there is economic liberty. - Margaret Thatcher',
     'Idealism is fine, but as it approaches reality, the costs become prohibitive. - William F. Buckley',
     'I didn`t attend the funeral, but I sent a nice letter saying I approved of it. - Mark Twain',
     'Every woman knows all about everything. - Rudyard Kipling',
     'Perfect humility dispenses with modesty. - C.S. Lewis',
     'I think a good gift for the president would be a chocolate revolver. And since he`s so busy, you`d probably have to run up to him and hand it to him. - Jack Handey',
     'The thought of being president frightens me. I do not think I want the job. - Ronald Reagan',
     'A journey of a thousand miles begins with a single step. - Confucius',
     'Most modern freedom is at root fear. It is not so much that we are too bold to endure rules; it is rather that we are too timid to endure responsibilities. - GK Chesterton',
     'Television is a medium of entertainment which permits millions of people to listen to the same joke at the same time, and yet remain lonesome. - T.S. Eliot',
     'Imagination will often carry us to worlds that never were. But without it, we go nowhere. - Carl Sagan',
     'In any fairly large and talkative community such as a university there is always the danger that those who think alike should gravitate together where they will henceforth encounter opposition only in the emasculated form of rumour that the outsiders say thus and thus. The absent are easily refuted, complacent dogmatism thrives, and differences of opinion are embittered by the group hostility. Each group hears not the best, but the worst, that the other group can say. - C.S. Lewis',
     'Success does not consist in never making mistakes but in never making the same one a second time. - George Bernard Shaw',
     'Take time to deliberate, but when the time for action has arrived, stop thinking and go in. - Napoleon Bonaparte',
     'I`m never going to be famous. My name will never be writ large on the roster of Those Who Do Things. I don`t do any thing. Not one single thing. I used to bite my nails, but I don`t even do that any more. - Dorothy Parker',
     'Money doesn`t talk, it swears. - Bob Dylan',
     'Advertising is the life of trade. - Calvin Coolidge',
     'Christmas can be celebrated in the school room with pine trees, tinsel and reindeers, but there must be no mention of the man whose birthday is being celebrated. One wonders how a teacher would answer if a student asked why it was called Christmas. - Ronald Reagan',
     'Experience is that marvelous thing that enables you to recognize a mistake when you make it again. - Franklin Jones',
     'He that would make his own liberty secure, must guard even his enemy from opposition; for if he violates this duty he establishes a precedent that will reach himself. - Thomas Paine',
     'Originality is the fine art of remembering what you hear but forgetting where you heard it. - Laurence Peter',
     'I arrive at the end of this review having done my duty as a critic. I have described the movie accurately and you have a good idea what you are in for if you go to see it. Most of you will not. I cannot argue with you. Some of you will--the brave and the curious. You embody the spirit of the man who first wondered what it would taste like to eat an oyster. - Roger Ebert',
     'Men marry to make an end; women to make a beginning. - Alexis Dupuy',
     'Show me a thoroughly satisfied man and I will show you a failure. - Thomas Edison',
     'I have often wondered how it is that every man loves himself more than all the rest of men, but yet sets less value on his own opinion of himself than on the opinion of others. - Marcus Aurelius',
     'You find out more about God from the Moral Law than from the univerise in general just as you find out more about a man by listening to his conversation than by looking at a house he has built. - C.S. Lewis',
     'Instead of a trap door, what about a trap window? The guy looks out it, and if he leans too far, he falls out. Wait. I guess that`s like a regular window. - Jack Handey',
     'Man was made for action, and to promote by the exertion of his faculties such changes in the external circumstances both of himself and others, as may seem most favourable to the happiness of all. - Adam Smith',
     'In every man`s heart there is a secret nerve that answers to the vibrations of beauty. - Christopher Morley',
     'If Jack`s in love, he`s no judge of Jill`s beauty. - Benjamin Franklin',
     'The Democrats seem to be basically nicer people, but they have demonstrated time and again that they have the management skills of celery. - Dave Barry',
     'Without courage, wisdom bears no fruit. - Baltasar Gracian',
     'I thought it completely absurd to mention my name in the same breath as the Presidency. - Dwight Eisenhower',
     'The only reason for time is so that everything doesn`t happen at once. - Albert Einstein',
     'The fool doth think he is wise, but the wise man knows himself to be a fool. - William Shakespeare',
     'You don`t have to stay up nights to succeed; you have to stay awake days. - Author Unknown',
     'Life is what happens to you while you`re busy making other plans. - John Lennon',
     'Fear not those who argue but those who dodge. - Dale Carnegie',
     'I have a hobby...I have the world`s largest collection of sea shells. I keep it scattered on beaches all over the world. Maybe you`ve seen some of it... - Steven Wright',
     'The art of being happy lies in the power of extracting happiness from common things. - Henry Ward Beecher',
     'Demoralize the enemy from within by surprise, terror, sabotage, assassination. This is the war of the future. - Adolf Hitler',
     'If eighty percent of your sales come from twenty percent of all of your items, just carry those twenty percent. - Henry Kissinger',
     'It`s not how old you are, it`s how hard you work at it. - Jonah Barrington',
     'What sunshine is to flowers, smiles are to humanity. These are but trifles, to be sure; but scattered along life`s pathway, the good they do is inconceivable. - Joseph Addison',
     'You got to be very careful if you don`t know where you`re going, because you might not get there. - Yogi Berra',
     'Life is not a support system for art. It`s the other way around. - Stephen King',
     'Love is the delightful interval between meeting a beautiful girl and discovering that she looks like a haddock. - John Barrymore',
     'The supernatural is the natural not yet understood. - Elbert Hubbard',
     'Those who forget good and evil and seek only to know the facts are more likely to achieve good than those who view the world through the distorting medium of their own desires. - Bertrand Russell',
     'Experience proves this, or that, or nothing, according to the preconceptions we bring to it. - C.S. Lewis',
     'Nothing separates the generations more than music. By the time a child is eight or nine, he has developed a passion for his own music that is even stronger than his passions for procrastination and weird clothes. - Bill Cosby',
     'The hour of departure has arrived, and we go our ways - I to die, and you to live. Which is better God only knows. - Plato',
     'The statistics on sanity are that one out of every four Americans are suffering from some form of mental illness. Think of your three best friends. If they`re okay, then it`s you. - Rita Mae Brown',
     'Nietzsche was stupid and abnormal. - Leo Tolstoy',
     'Everybody can be great... because anybody can serve. You don`t have to have a college degree to serve. You don`t have to make your subject and verb agree to serve. You only need a heart full of grace. A soul generated by love. - Martin Luther King Jr.',
     'People have a way of becoming what you encourage them to be, not what you nag them to be. - Author Unknown',
     'All men are frauds. The only difference between them is that some admit it. I myself deny it. - Henry Mencken',
     'America is not like a blanket: one piece of unbroken cloth, the same color, the same texture, the same size. America is more like a quilt: many patches, many pieces, many colors, many sizes, all woven and held together by a common thread. - Jesse Jackson',
     'When nothing seems to help, I go and look at a stonecutter hammering away at his rock perhaps a hundred times without as much as a crack showing in it. Yet at the hundred and first blow it will split in two, and I know it was not that blow that did it, but all that had gone before. - Jacob August Riis',
     'In any moment of decision, the best thing you can do is the right thing. The worst thing you can do is nothing. - Theodore Roosevelt',
     'Self-denial is the shining sore on the leprous body of Christianity. - Oscar Wilde',
     'I have never been hurt by what I have not said. - Calvin Coolidge',
     'If you judge people, you have no time to love them. - Mother Teresa',
     'The means of defense against foreign danger historically have become the instruments of tyranny at home. - James Madison',
     'He who is not courageous enough to take risks will accomplish nothing in life. - Muhammad Ali',
     'He that fights and runs away, may turn and fight another day; but he that is in battle slain, will never rise to fight again. - Tacitus',
     'America did not invent human rights. In a very real sense...human rights invented America. - Jimmy Carter',
     'No matter how much cats fight, there always seem to be plenty of kittens. - Abraham Lincoln',
     'Success, the real success, does not depend upon the position you hold but upon how you carry yourself in that position. - Theodore Roosevelt',
     'Happiness makes up in height for what it lacks in length. - Robert Frost',
     'Poetry is the art of creating imaginary gardens with real toads. - Marianne Moore',
     'It is by the goodness of God that, in this country, we have three benefits: freedom of speech, freedom of thought, and the wisdom never to use either. - Mark Twain',
     'The Bible is not my book, and Christianity is not my religion. I could never give assent to the long, complicated statements of Christian dogma. - Abraham Lincoln',
     'He wrapped himself in quotations--as a beggar would enfold himself in the purple of Emperors. - Rudyard Kipling',
     'The truth is always a trick to those who live among lies. - Author Unknown',
     'What you do speaks so loudly that I cannot hear what you say. - Ralph Waldo Emerson',
     'All glory is fleeting. - George Patton',
     'No distance of place or lapse of time can lessen the friendship of those who are thoroughly persuaded of each other`s worth. - Robert Southey',
     'Washington is a city of Southern efficiency and Northern charm. - John F. Kennedy',
     'If you`re in a boxing match, try not to let the other guy`s glove touch your lips, because you don`t know where that glove has been. - Jack Handey',
     'Never discourage anyone who continually makes progress, no matter how slow. - Plato',
     'Not only is there no God, but try finding a plumber on Sunday. - Woody Allen',
     'Rome remained free for four hundred years and Sparta eight hundred, although their citizens were armed all that time; but many other states that have been disarmed have lost their liberties in less than forty years. - Nicolo Machiavelli',
     'Science without religion is lame, religion without science is blind. - Albert Einstein',
     'Knowledge rests not upon truth alone, but upon error also. - Carl Jung',
     'In politics shared hatreds are almost always the basis of friendships. - Alexis de Tocqueville',
     'Genius may have its limitations, but stupidity is not thus handicapped. - Elbert Hubbard',
     'In life, as in art, the beautiful moves in curves. - Edward Bulwer-Lytton',
     'I planted some bird seed. A bird came up. Now I don`t know what to feed it. - Steven Wright',
     'Not everybody trusts paintings, but people believe photographs. - Ansel Adams',
     'The things that will destroy America are prosperity at any price, peace at any price, safety first instead of duty first, the love of soft living and the get rich quick theory of life. - Theodore Roosevelt',
     'There are people who put their dreams in a little box and say, Yes, I`ve got dreams, of course I`ve got dreams. Then they put the box away and bring it out once in awhile to look in it, and yep, they`re still there. - Erna Bombeck',
     'Knowledge comes, but wisdom lingers. - Calvin Coolidge',
     'Men are born ignorant, not stupid; they are made stupid by education. - Bertrand Russell',
     'If we do not help a man in trouble, it is as if we caused the trouble. - Nachman of Bratslav',
     'Patience is the companion of wisdom. - Saint Augustine',
     'Marriage is our last, best chance to grow up. - Joseph Barth',
     'Patriotism is not short, frenzied outbursts of emotion, but the tranquil and steady dedication of a lifetime. - Adlai Stevenson',
     'A man`s very highest moment is, I have no doubt at all, when he kneels in the dust, and beats his breast, and tells all the sins of his life. - Oscar Wilde',
     'Associate yourself with men of good quality if you esteem your own reputation; for `tis better to be alone than in bad company. - George Washington',
     'Beauty is all very well at first sight; but whoever looks at it when it has been in the house three days? - George Bernard Shaw',
     'I had a dream the other night. I dreamed that Jimmy Carter came to me and asked why I wanted his job. I told him I didn`t want his job. I want to be President. - Ronald Reagan',
     'To assert that the earth revolves around the sun is as erroneous as to claim that Jesus was not born of a virgin. - Cardinal Bellarmine',
     'Reality is that which, when you stop believing in it, doesn`t go away. - Phillip K. Dick',
     'Deliberation and debate is the way you stir the soul of our democracy. - Jesse Jackson',
     'Nothing noble is done without risk. - Andr\xe9 Gide',
     'Fatherhood is pretending the present you love most is soap on-a-rope. - Bill Cosby',
     'No nation keeps its word. A nation is a big, blind worm, following what? Fate perhaps. A nation has no honor, it has no word to keep. - Carl Jung',
     'Democracy means that anyone can grow up to be president, and anyone who doesn`t grow up can be vice president. - Johnny Carson',
     'All men desire to know. - Aristotle',
     'Women are the only realists; their whole object in life is to pit their realism against the extravagant, excessive, and occasionally drunken idealism of men. - GK Chesterton',
     'Don`t go around saying the world owes you a living. The world owes you nothing. It was here first. - Mark Twain',
     'I could not handle being a woman, I would stay home all day and play with my breasts. - Steve Martin',
     'I confess, I do not believe in time. - Vladimir Nabokov',
     'Man is the only animal that blushes - or needs to. - Mark Twain',
     'True wisdom comes to each of us when we realize how little we understand about life, ourselves, and the world around us. - Socrates',
     'Any reviewer who expresses rage and loathing for a novel is preposterous. He or she is like a person who has put on full armor and attacked a hot fudge sundae. - Kurt Vonnegut',
     'There is no substitute for hard work. - Thomas Edison',
     'Cast your cares on God; that anchor holds. - Frank Moore Colby',
     'She is not perfect. You are not perfect. The question is whether or not you are perfect for each other. - Robin Williams',
     'Fanaticism consists of redoubling your efforts when you have forgotten your aim. - George Santayana',
     'Government is not reason; it is not eloquent; it is force. Like fire, it is a dangerous servant and a fearful master. - George Washington',
     'Let us not forget that the cultivation of the earth is the most important labor of man. When tillage begins, other arts will follow. The farmers, therefore, are the founders of civilization. - Daniel Webster',
     'A right delayed is a right denied. - Martin Luther King Jr.',
     'Against criticism a man can neither protest nor defend himself; he must act in spite of it, and then it will gradually yield to him. - Johann Wolfgang von Goethe',
     'Everything is simpler than you think and at the same time more complex than you imagine. - Johann Wolfgang von Goethe',
     'The world is full of suffering. It is also full of overcoming it. - Helen Keller',
     'Love is repaid by love alone! - Mother Teresa',
     'The only way to keep your health is to eat what you don`t want, drink what you don`t like, and do what you`d rather not. - Mark Twain',
     'No man but a blockhead ever wrote, except for money. - Samuel Johnson',
     'It behooves every man to remember that the work of the critic is of altogether secondary importance, and that, in the end, progress is accomplished by the man who does things. - Theodore Roosevelt',
     'Why are people`s ``deepest desires`` always so shallow? - Author Unknown',
     'Were it possible for us to wait for ourselves to come into the room, not many of us would find our hearts breaking into flower as we heard the door handle turn. - Rebecca West',
     'Thus the metric system did not really catch on in the States, unless you count the increasing popularity of the nine-millimeter bullet. - Dave Barry',
     'Ask not what your country can do for you - ask what you can do for your country. - John F. Kennedy',
     'It is error alone which needs the support of government. Truth can stand by itself. - Thomas Jefferson',
     'To have the reputation of possessing the most perfect social tact, talk to every woman as if you loved her, and to every man as if he bored you. - Oscar Wilde',
     'Remember, if you smoke after sex you`re doing it too fast. - Woody Allen',
     'Fame is a fickle food upon a shifting plate. - Emily Dickinson',
     'Philosophy is to the real world as masturbation is to sex. - Karl Marx',
     'It is always thus, impelled by a state of mind which is destined not to last, that we make our irrevocable decisions. - Marcel Proust',
     'Love anything and your heart will be wrung and possibly broken. If you want to make sure of keeping it intact you must give it to no one, not even an animal. Wrap it carefully round with hobbies and little luxuries; avoid all entanglements. Lock it up safe in the casket or coffin of your selfishness. But in that casket, safe, dark, motionless, airless, it will change. It will not be broken; it will become unbreakable, impenetrable, irredeemable. To love is to be vulnerable. - C.S. Lewis',
     'Ignorance more frequently begets confidence than does knowledge. - Charles Darwin',
     'When I see a play and understand it the first time, then I know it can`t be much good. - T.S. Eliot',
     'To explain the unknown by the known is a logical procedure; to explain the known by the unknown is a form of theological lunacy. - David Brooks',
     'I mistrust the judgment of every man in a case in which his own wishes are concerned. - Daniel Webster',
     'We ascribe beauty to that which is simple; which has no superfluous parts; which exactly answers its end; which stands related to all things; which is the mean of many extremes. - Ralph Waldo Emerson',
     'Americans are so enamored of equality, they would rather be equal in slavery than unequal in freedom. - Alexis de Tocqueville',
     'In the long run, we shape our lives and we shape ourselves. The process never ends until we die, and the choices that we make are ultimately our responsibility. - Eleanor Roosevelt',
     'Don`t ever take a fence down until you know why it was put up. - Robert Frost',
     'I am Envy. I cannot read and therefore wish all books burned. - Christopher Marlowe',
     'Of all bad men religious bad men are the worst. - C.S. Lewis',
     'God`s colors all are fast. - John Greenleaf Whittier',
     'Christmas is a time when you get homesick, even when you`re home. - Carol Nelson',
     'We all wish to be judged by our peers, by the men `after our own heart.` Only they really know our mind and only they judge it by standards we fully acknowledge. Theirs is the praise we really covet and the blame we really dread. The little pockets of early Chrstians survived because they cared exclusively for the love of `the bretheren` and stopped their ears to the opinion of the Pagan society around them. But a circle of criminals, cranks, or perverts survives in just the same way; by becoming deaf to the opinion of the outer world, by discounting it as the chatter of outsiders who `don`t understand,` of the `conventional,` the `bourgeois,` the `Establishment,` of prigs, prudes, and humbugs. - C.S. Lewis',
     'Duties are not performed for duty`s sake, but because their neglect would make the man uncomfortable. A man performs but one duty - the duty of contenting his spirit, the duty of making himself agreeable to himself. - Mark Twain',
     'A free society is one where it is safe to be unpopular. - Adlai Stevenson',
     'If variety is the spice of life, marriage is the big can of leftover Spam. - Johnny Carson',
     'Truth sits upon the lips of dying men. - Matthew Arnold',
     'As a woman, I find it very embarrassing to be in a meeting and realize I`m the only one in the room with balls. - Rita Mae Brown',
     'A mind that is stretched by a new experience can never go back to its old dimensions. - Oliver Wendell Holmes',
     'If there is any principle of the Constitution that more imperatively calls for attachment than any other it is the principle of free thought, not free thought for those who agree with us but freedom for the thought that we hate. - Oliver Wendell Holmes',
     'Thus far, the reputed idiot Bush has graduated from Yale and Harvard, made a stack of cash in the oil industry, become the first consecutive-term governor of Texas, defeated a dual-term VP for the presidency, and led his party to [November 5th`s] extraordinary triumphs. Let his opponents keep calling him stupid; if they do, within five years Bush will be King of England, the Pope, and world Formula One motor racing champion. - Tim Blair',
     'All art is but imitation of nature. - Lucius Annaeus Seneca',
     'We should take care not to make the intellect our god; it has, of course, powerful muscles, but no personality. - Albert Einstein',
     'Every author should weigh his work and ask, `Will humanity gain any benefit from it?` - Nachman of Bratslav',
     'The older I grow the more I distrust the familiar doctrine that age brings wisdom. - Henry Mencken',
     'The significant problems we face cannot be solved at the same level of thinking we were at when we created them. - Albert Einstein',
     'Heroism is not only in the man, but in the occasion. - Calvin Coolidge',
     'Nothing is wrong with Southern California that a rise in the ocean level wouldn`t cure. - Kenneth Millar',
     'Nothing that you have not given away will ever be really yours. - C.S. Lewis',
     'A `geek` by definition is someone who eats live animals....I`ve never eaten live animals. - Crispin Glover',
     'Politics is perhaps the only profession for which no preparation is thought necessary. - Robert Louis Stevenson',
     'The only kind of seafood I trust is the fish stick, a totally featureless fish that doesn`t have eyeballs or fins. - Dave Barry',
     'I have never taken any exercise except sleeping and resting. - Mark Twain',
     'Skepticism is a virtue in history as well as in philosophy. - Napoleon Bonaparte',
     'The sleeping fox catches no poultry. - Benjamin Franklin',
     'Obstacles do not exist to be surrendered to, but only to be broken. - Adolf Hitler',
     'A man can`t be too careful in the choice of his enemies. - Oscar Wilde',
     'After silence, that which comes nearest to expressing the inexpressible is Music. - Aldous Huxley',
     'To one who has faith, no explanation is necessary. To one without faith, no explanation is possible. - Thomas Aquinas',
     'Thinking is the hardest work there is, which is the probable reason why so few engage in it. - Henry Ford',
     'A government which robs Peter to pay Paul can always depend on the support of Paul. - George Bernard Shaw',
     'Don`t let people drive you crazy when you know it`s in walking distance. - Author Unknown',
     'Well-timed silence hath more eloquence than speech. - Martin Farquhar Tupper',
     'The first principle is that you must not fool yourself - and you are the easiest person to fool. - Richard P. Feynman',
     'Guard with jealous attention the public liberty. Suspect everyone who approaches that jewel. - Patrick Henry',
     'In the beginning, the universe was created. This made a lot of people very angry, and has been widely regarded as a bad idea. - Douglas Adams',
     'Anyone who invokes authors in discussion is not using his intelligence but his memory. - Leonardo da Vinci',
     'To me there has never been a higher source of earthly honor or distinction than that connected with advances in science. - Isaac Newton',
     'You know, there`s a million fine looking women in the world, dude. But they don`t all bring you lasagna at work. Most of `em just cheat on you. - Kevin Smith',
     'Government consists in nothing else but so controlling subjects that they shall neither be able to, nor have cause to do it harm. - Nicolo Machiavelli',
     'There is no glory in battle worth the blood it costs. - Dwight Eisenhower',
     'Being born is like being kidnapped. And then sold into slavery. - Andy Warhol',
     'The magic of first love is our ignorance that it can never end. - Benjamin Disraeli',
     'Art, like morality, consists in drawing the line somewhere. - GK Chesterton',
     'If music be the food of love, play on. - William Shakespeare',
     'Politics has got so expensive that it takes lots of money to even get beat with. - Will Rogers',
     'Back in the old days, most families were close-knit. Grown children and their parents continued to live together, under the same roof, sometimes in the same small, crowded room, year in and year out, until they died, frequently by strangulation. - Dave Barry',
     'Without computers, the government would be unable to function at the level of effectiveness and efficiency that we have come to expect.  This is because the primary function of the government is -- and here I am quoting directly from the U.S. Constitution -- `to spew out paper.` - Dave Barry',
     'In politics, if you want anything said, ask a man; if you want anything done, ask a woman. - Margaret Thatcher',
     'Nobody can have the consolations of religion or philosophy unless he has first experienced their desolations. - Aldous Huxley',
     'Everything that irritates us about others can lead us to an understanding of ourselves. - Carl Jung',
     'I`m not normally a religious man, but if you`re up there, save me, Superman! - Homer Simpson',
     'The practice of art isn`t to make a living. It`s to make your soul grow. - Kurt Vonnegut',
     'There cannot be true democracy unless women`s voices are heard. - Hillary Clinton',
     'Just as your hand, held before the eye, can hide the tallest mountain, so this small earthly life keeps us from seeing the vast radiance that fills the core of the universe. - Nachman of Bratslav',
     'There are several good protections against temptation, but the surest is cowardice. - Mark Twain',
     'A Native American elder once described his own inner struggles in this manner: Inside of me there are two dogs. One of the dogs is mean and evil. The other dog is good. The mean dog fights the good dog all the time. When asked which dog wins, he reflected. - George Bernard Shaw',
     'Surely what a man does when he is caught off his guard is the best evidence as to what sort of man he is. - C.S. Lewis',
     'For each illness that doctors cure with medicine, they provoke ten in healthy people by inoculating them with the virus that is a thousand times more powerful than any microbe: the idea that one is ill. - Marcel Proust',
     'When I took office, only high energy physicists had ever heard of what is called the Worldwide Web....now even my cat has its own page. - Bill Clinton',
     'The president cannot escape from his office. - Dwight Eisenhower',
     'Of all the animals, man is the only one that lies. - Mark Twain',
     'The greatest thing in this world is not so much where we are, but in what direction we are moving. - Oliver Wendell Holmes',
     'How did it get so late so soon? It`s night before it`s afternoon. December is here before it`s June. My goodness how the time has flewn. How did it get so late so soon? - Theodor Seuss Geisel',
     'Humor is mankind`s greatest blessing. - Mark Twain',
     'It takes a lot of courage to show your dreams to someone else. - Erna Bombeck',
     'I love Thanksgiving. It`s the only time in Los Angeles that you see natural breasts. - Arnold Schwarzenegger',
     'The aging process has you firmly in its grasp if you never get the urge to throw a snowball. - Doug Larson',
     'The surest way of spoiling a pleasure is to start examining your satisfaction. - C.S. Lewis',
     'There are some who`ve forgotten why we have a military. It`s not to promote war; it`s to be prepared for peace. - Ronald Reagan',
     'Bashfulness is an ornament to youth, but a reproach to old age. - Aristotle',
     'You are never too old to set another goal or to dream a new dream. - C.S. Lewis',
     'If you could kick the person in the pants responsible for most of your trouble, you wouldn`t sit for a month. - Theodore Roosevelt',
     'The philosophy of one century is the common sense of the next. - Henry Ward Beecher',
     'The broad masses of a population are more amenable to the appeal of rhetoric than to any other force. - Adolf Hitler',
     'Plato was a bore. - Friedrich Nietzsche',
     'The MPAA rates this PG-13. It is too vulgar for anyone under 13, and too dumb for anyone over 13. - Roger Ebert',
     'Dying is the most embarrassing thing that can ever happen to you, because someone`s got to take care of all your details. - Andy Warhol',
     'It has been said that man is a rational animal. All my life I have been searching for evidence which could support this. - Bertrand Russell',
     'The laws of gravity cannot be held responsible for people falling in love. - Albert Einstein',
     'Of course the people dont want war...that is understood. But voice or no voice, the people can always be brought to the bidding of the leaders. That is easy. All you have to do is tell them they are being attacked, and denounce the pacifists for lack of patriotism and exposing the country to danger. It works the same in any country. - Hermann Goering',
     'One thing they never tell you about child raising is that for the rest of your life, at the drop of a hat, you are expected to know your child`s name and how old he or she is. - Erna Bombeck',
     'If we have no peace, it is because we have forgotten that we belong to each other. - Mother Teresa',
     'I think it`s the duty of the comedian to find out where the line is drawn and cross it deliberately. - George Carlin',
     'Nothing in the world is more dangerous than sincere ignorance and conscientious stupidity. - Martin Luther King Jr.',
     'If a man is called to be a streetsweeper, he should sweep streets even as Michelangelo painted, or Beethoven composed music, or Shakespeare wrote poetry. He should sweep streets so well that all the host of heaven and earth will pause to say, here lived a great streetsweeper who did his job well. - Martin Luther King Jr.',
     'There is a great deal of difference between an eager man who wants to read a book and the tired man who wants a book to read. - GK Chesterton',
     'To find out a girl`s faults, praise her to her girl friends. - Benjamin Franklin',
     'Forever is composed of nows. - Emily Dickinson',
     'Alexander, Caesar, Charlemagne, and myself founded empires; but what foundation did we rest the creations of our genius? Upon force. Jesus Christ founded an empire upon love; and at this hour millions of men would die for Him. - Napoleon Bonaparte',
     'Man`s best possession is a sympathetic wife. - Euripides',
     'A grandmother pretends she doesn`t know who you are on Halloween. - Erna Bombeck',
     'Perhaps one of the most important accomplishments of my administration has been minding my own business. - Calvin Coolidge',
     'Laughter is the sun that drives winter from the human face. - Victor Hugo',
     'If I feel physically as if the top of my head were taken off, I know that is poetry. - Emily Dickinson',
     'Love is a fruit in season at all times, and within reach of every hand. - Mother Teresa',
     'Having someone wonder where you are when you don`t come home at night is a very old human need. - Margaret Mead',
     'I paid too much for it, but it`s worth it. - Samuel Goldwyn',
     'I think the best possible social program is a job. - Ronald Reagan',
     'Ocean: A body of water occupying 2/3 of a world made for man...who has no gills. - Ambrose Bierce',
     'Moral indignation is jealousy with a halo. - H.G. Wells',
     'Information is not knowledge. - Albert Einstein',
     'The price of greatness is responsibility. - Winston Churchill',
     'There is hope for the future because God has a sense of humor and we are funny to God. - Bill Cosby',
     'Why, you can take the most gallant sailor, the most intrepid airman or the most audacious soldier, put them at a table together - what do you get? The sum of their fears. - Winston Churchill',
     'The mind of the thoroughly well-informed man is a dreadful thing. It is like a bric-\xe0-brac shop, all monsters and dust, with everything priced above its proper value. - Oscar Wilde',
     'Cooking was invented in prehistoric times, when a primitive tribe had a lucky accident. The tribe had killed an animal and was going to eat it raw, when a tribe member named Woog tripped and dropped it into the fire. At first the other tribe members were angry at Woog, but then, as the aroma of burning meat filled the air, they had an idea. So they ate Woog raw. - Dave Barry',
     'I have been the artist with the longest career, and I am so proud and honoured to be chosen from heaven to be invincible. - Michael Jackson',
     'On the plus side, death is one of the few things that can be done just as easily lying down. - Woody Allen',
     'If we will be quiet and ready enough, we shall find compensation in every disappointment. - Henry Thoreau',
     'I get to go to lots of overseas places, like Canada. - Britney Spears',
     'Imagination is a quality given a man to compensate him for what he is not, and a sense of humor was provided to console him for what he is. - Oscar Wilde',
     'Without music, life would be a mistake. - Friedrich Nietzsche',
     'I will honor Christmas in my heart, and try to keep it all the year. - Charles Dickens',
     'Don`t walk in front of me, I may not follow. Don`t walk behind me, I may not lead. Just walk beside me and be my friend. - Albert Camus',
     'You can`t depend on your eyes when your imagination is out of focus. - Mark Twain',
     'I like your Christ, I do not like your Christians. Your Christians are so unlike your Christ. - Mahatma Gandhi',
     'Let us now set forth one of the fundamental truths about marriage: the wife is in charge. - Bill Cosby',
     'True patriotism hates injustice in its own land more than anywhere else. - Clarence Darrow',
     'If a man is proud of his wealth, he should not be praised until it is known how he employs it. - Socrates',
     'I like to say that I`m bisexual...when I want sex, I buy it. - Boy George',
     'We`ve got to live. No matter how many skies have fallen. - D.H. Lawrence',
     'Do good by stealth, and blush to find it fame. - Alexander Pope',
     'There is a theory which states that if ever anyone discovers exactly what the Universe is for and why it is here, it will instantly disappear and be replaced by something even more bizarre and inexplicable. There is another theory which states that this has already happened. - Douglas Adams',
     'I don`t care what is written about me, so long as it isn`t true. - Dorothy Parker',
     'Get mad, then get over it. - Colin Powell',
     'I always cheer up immensely if an attack is particularly wounding because I think, well, if they attack one personally, it means they have not a single political argument left. - Margaret Thatcher',
     'Observe constantly that all things take place by change, and accustom thyself to consider that the nature of the Universe love nothing so much as to change. The Universe is change. - Marcus Aurelius',
     'You give me a credit to which I have no claim in calling me `the writer of the Constitution of the United States.` This was not, like the fabled Goddess of Wisdom, the offspring of a single brain. It ought to be regarded as the work of many heads and many hands. - James Madison',
     'Since love grows within you, so beauty grows. For love is the beauty of the soul. - Saint Augustine',
     'You know you`re getting old when the candles cost more than the cake. - Bob Hope',
     'Freedom is the right to question and change the established way of doing things. It is the continuous revolution of the marketplace. It is the understanding that allows us to recognize shortcomings and seek solutions. - Ronald Reagan',
     'There is time for everything. - Thomas Edison',
     'The nation which forgets its defenders will be itself forgotten. - Calvin Coolidge',
     'Show me your hands. Do they have scars from giving? Show me your feet. Are they wounded in service? Show me your heart. Have you left a place for divine love? - Fulton J. Sheen',
     'There are no secrets to success. It is the result of preparation, hard work, and learning from failure. - Colin Powell',
     'The movie`s director is the pilot. It`s his vision. For an actor, the time to worry about flying is when you`re on the ground. If you don`t want to fly with the director, don`t get on the plane. - Denzel Washington',
     'My aim is to put down on paper what I see and what I feel in the best and simplest way. - Ernest Hemingway',
     'Don`t marry a man to reform him - that`s what reform schools are for. - Mae West',
     'Analyzing humor is like dissecting a frog. Few people are interested and the frog dies of it. - E.B. White',
     'If you`re afraid to ask the question, it`s probably because you already know the answer. - Miriam M. Wynn',
     'You should do your own car repairs. It`s an easy way to save money and possibly maim yourself for life. - Dave Barry',
     'The ACLU is always yakking about the Constitution, and most of us are getting mighty tired of it. I mean, if the Constitution is so great, how come it was amended so many times? Huh? - Dave Barry',
     'One definition of an economist is somebody who sees something happen in practice and wonders if it will work in theory. - Ronald Reagan',
     'Chicago sounds rough to the maker of verse. One comfort we have: Cincinnati sounds worse. - Oliver Wendell Holmes',
     'There are men in all ages who mean to govern well, but they mean to govern. They promise to be good masters, but they mean to be masters. - Daniel Webster',
     'A leader is a man who can adapt principles to circumstances. - George Patton',
     'Sex at age ninety is like trying to shoot pool with a rope. - George Burns',
     'You don`t take a photograph, you make it. - Ansel Adams',
     'The mintage of wisdom is to know that rest is rust, and that real life is in love, laughter, and work. - Elbert Hubbard',
     'He therefore is the truest friend to the liberty of this country who tries most to promote its virtue, and who, so far as his power and influence extend, will not suffer a man to be chosen into any office of power and trust who is not a wise and virtuous man. - Samuel Adams',
     'The biggest bore is the person who is bored by everyone and everything. - Frank Tyger',
     'I hate war as only a soldier who has lived it can, only as one who has seen its brutality, its futility, its stupidity. - Dwight Eisenhower',
     'Success is going from failure to failure without losing enthusiasm. - Winston Churchill',
     'We have the Bill of Rights. What we need is a Bill of Responsibilities. - Bill Maher',
     'Even peace may be purchased at too high a price. - Benjamin Franklin',
     'The last thing a political party gives up is its vocabulary. - Alexis de Tocqueville',
     'Many of life`s failures are people who did not realize how close they were to success when they gave up. - Thomas Edison',
     'We are what we repeatedly do. Excellence, therefore, is not an act, but a habit. - Aristotle',
     'Would you live with ease? Do what you ought, not what you please. - Benjamin Franklin',
     'Men have always been afraid that women could get along without them. - Margaret Mead',
     'Being is desirable because it is identical with Beauty, and Beauty is loved because it is Being. We ourselves possess Beauty when we are true to our own being; ugliness is in going over to another order; knowing ourselves, we are beautiful; in self-ignorance, we are ugly. - Ambrose Bierce',
     'Money never made a man happy yet, nor will it. There is nothing in its nature to produce happiness. The more a man has, the more he wants. Instead of its filling a vacuum, it makes one. If it satisfies one want, it doubles and trebles that want another way. That was a true proverb of the wise man, rely upon it; ``Better is little with the fear of the Lord, than great treasure, and trouble therewith. - Benjamin Franklin',
     'Science is not about building a body of known `facts`. It is a method for asking awkward questions and subjecting them to a reality-check, thus avoiding the human tendency to believe whatever makes us feel good. - Terry Pratchett',
     'A man is never more truthful than when he acknowledges himself a liar. - Mark Twain',
     'The writer\x92s job is not to judge, but to seek to understand. - Ernest Hemingway',
     'When in doubt, do it. - Oliver Wendell Holmes',
     'This is the second most exciting indoor sport, and the other one shouldn`t have spectators. - Dick Vertleib',
     'Nothing before had ever made me thoroughly realise, though I had read various scientific books, that science consists in grouping facts so that general laws or conclusions may be drawn from them. - Charles Darwin',
     'Death and life have their determined appointments; riches and honors depend upon heaven. - Confucius',
     'Those who expect to reap the blessings of freedom must, like men, undergo the fatigue of supporting it. - Thomas Paine',
     'Maturity is a bitter disappointment for which no remedy exists, unless laughter can be said to remedy anything. - Kurt Vonnegut',
     'Once you have flown, you will walk the earth with your eyes turned skywards, for there you have been, and there you long to return. - Leonardo da Vinci',
     'Let him who desires peace prepare for war. - Vegetius',
     'We live in an age when unnecessary things are our only necessities. - Oscar Wilde',
     'A typical vice of American politics is the avoidance of saying anything real on real issues. - Theodore Roosevelt',
     '`Tis the business of little minds to shrink, but he whose heart is firm, and whose conscience approves his conduct, will pursue his principles unto death. - Thomas Paine',
     'It is impossible to experience one`s death objectively and still carry a tune. - Woody Allen',
     'Serious sport has nothing to do with fair play. It is bound up with hatred, jealousy, boastfulness, disregard of all rules and sadistic pleasure in witnessing violence. In other words: it is war minus the shooting. - George Orwell',
     'How did it happen that their lips came together? How does it happen that birds sing, that snow melts, that the rose unfolds, that the dawn whitens behind the stark shapes of trees on the quivering summit of the hill? A kiss, and all was said. - Victor Hugo',
     'Four-fifths of all our troubles would disappear, if we would only sit down and keep still. - Calvin Coolidge',
     'Character is what you are in the dark. - John Whorfin',
     'Opera is when a guy gets stabbed in the back and, instead of bleeding, he sings. - Ed Gardner',
     'Anybody can become angry - that is easy, but to be angry with the right person and to the right degree and at the right time and for the right purpose, and in the right way - that is not within everybody`s power and is not easy. - Aristotle',
     'If you are resolutely determined to make a lawyer of yourself, the thing is more than half done already. - Abraham Lincoln',
     'It is only by doing things others have not that one can advance. - George Patton',
     'No doubt those who really founded modern science were usually those whose love of truth exceeded their love of power. - C.S. Lewis',
     'I don`t make jokes. I just watch the government and report the facts. - Will Rogers',
     'The customs and fashions of men change like leaves on the bough, some of which go and others come. - Dante Alighieri',
     'Friendship is a single soul dwelling in two bodies. - Aristotle',
     'We must repsect the other fellow`s religion, but only in the sense and to the extent that we respect his theory that his wife is beautiful and his children are smart. - Henry Mencken',
     'Happiness is so hard to define and foolish to define. Am I acting? That`s the worst thing you can ask yourself. You can be happy suddenly. It can spring on you, not when you reach a plateau. You can be happy going backward or going down. You can be happy at the loss of something. - Steve Martin',
     'Every gun that is made, every warship launched, every rocket fired, signifies in the final sense a theft from those who hunger and are not fed, those who are cold and are not clothed. - Dwight Eisenhower',
     'The greatness of our country has been based on our thinking that everyone has a right even to be wrong. - Ronald Reagan',
     'Unless the religious claims of the Bible are again acknowledged, its literary claims will, I think, be given only `mouth honour` and that decreasingly. - C.S. Lewis',
     'There are a thousand hacking at the branches of evil to one who is striking at the root. - Henry Thoreau',
     'The best of life is conversation, and the greatest success is confidence, or perfect understanding between two people. - Ralph Waldo Emerson',
     'Those whom the gods love grow young. - Oscar Wilde',
     'We are all worms, but I do believe I am a glow-worm. - Winston Churchill',
     'It is better to be bold than too circumspect, because fortune is of a sex which likes not a tardy wooer and repulses all who are not ardent. - Nicolo Machiavelli',
     'Hanging is too good for a man who makes puns -- he should be drawn and quoted. - Fred Allen',
     'I would not join any club that would have someone like me for a member. - Groucho Marx',
     'Never judge a philosophy by its abuse. - Saint Augustine',
     'Errors of haste are seldom committed singly. The first time a man always does too much. And precisely on that account he commits a second error, and then he does too little. - Friedrich Nietzsche',
     'It is better to keep your mouth closed and let people think you are a fool than to open it and remove all doubt. - Mark Twain',
     'I believe this government cannot endure permanently half slave and half free. - Abraham Lincoln',
     'There are very few monsters who warrant the fear we have of them. - Andr\xe9 Gide',
     'A radical is a man with both feet firmly planted in the air. - Franklin D. Roosevelt',
     'Who does not thank for little will not thank for much. - Author Unknown',
     'My role in society, or any artist`s or poet`s role, is to try and express what we all feel. Not to tell people how to feel. Not as a preacher, not as a leader, but as a reflection of us all. - John Lennon',
     'I am a strong believer in luck and I find the harder I work the more I have of it. - Benjamin Franklin',
     'We know too much, and are convinced of too little. Our literature is a substitute for religion, and so is our religion. - T.S. Eliot',
     'Happy, happy Christmas, that can win us back to the delusions of our childhood days, recall to the old man the pleasures of his youth, and transport the traveler back to his own fireside and quiet home! - Charles Dickens',
     'Our nettlesome task is to discover how to organize our strength into compelling power. - Martin Luther King Jr.',
     'This does not mean that the enemy is to be allowed to escape. The object is to make him believe that there is a road to safety, and thus prevent his fighting with the courage of despair. After that, you may crush him. - Sun Tzu',
     'People sleep peaceably in their beds at night only because rough men stand ready to do violence on their behalf. - George Orwell',
     'Are you entitled to the fruits of your labor or does government have some presumptive right to spend and spend and spend? - Ronald Reagan',
     'Don`t worry about the world coming to an end today. It`s already tomorrow in Australia. - Charles Schulz',
     'There are painters who transform the sun to a yellow spot, but there are others who with the help of their art and their intelligence, transform a yellow spot into the sun. - Pablo Picasso',
     'What I don`t like about office Christmas parties is looking for a job the next day. - Phyllis Diller',
     'Never give in--never, never, never, never, in nothing great or small, large or petty, never give in except to convictions of honour and good sense. Never yield to force; never yield to the apparently overwhelming might of the enemy. - Winston Churchill',
     'They that can give up essential liberty to obtain a little temporary safety deserve neither liberty nor safety. - Benjamin Franklin',
     'This is slavery, not to speak one`s thought. - Euripides',
     'Where knowledge ends, religion begins. - Benjamin Disraeli',
     'For me, survival is the ability to cope with difficulties, with circumstances, and to overcome them. - Nelson Mandela',
     'I went out to the country so i could examine the simple things in life. - Henry Thoreau',
     'Of course I don`t believe in it. But I understand that it brings you luck whether you believe in it or not. - Niels Bohr',
     'In all chaos there is a cosmos, in all disorder a secret order. - Carl Jung',
     'The direction in which education starts a man will determine his future life. - Plato',
     'If society fits you comfortably enough, you call it freedom. - Robert Frost',
     'I hope that when you are my age, you will be able to say as I have been able to say: We lived in freedom. We lived lives that were a statement, not an apology. - Ronald Reagan',
     'In Heaven all the interesting people are missing. - Friedrich Nietzsche',
     'The days of looking the other way while despotic regimes trample human rights, rob their nations` wealth, and then excuse their failings by feeding their people a steady diet of anti-Western hatred are over. - Dick Cheney',
     'If tyranny and oppression come to this land, it will be in the guise of fighting a foreign enemy. - James Madison',
     'I love deadlines. I especially like the whooshing sound they make as they go flying by. - Douglas Adams',
     'I made this letter longer than usual because I lack the time to make it short. - Blaise Pascal',
     'There is only one force of history that can break the reign of hatred and resentment, and expose the pretensions of tyrants, and reward the hopes of the decent and tolerant, and that is the force of human freedom. - George W. Bush',
     'Dogs look up to you. Cats look down on you. Pigs treat you like equals. - Winston Churchill',
     'The act of policing is, in order to punish less often, to punish more severely. - Napoleon Bonaparte',
     'The health of a democratic society may be measured by the quality of functions performed by private citizens. - Alexis de Tocqueville',
     'Nobody expects to trust his body overmuch after the age of fifty. - Alexander Hamilton',
     'An oppressive government is more to be feared than a tiger. - Confucius',
     'I`m a middle age white guy, which means I`m constantly reminded that my particular group is responsible for the oppression of every known minority PLUS most wars PLUS government corruption PLUS pollution of the environment, not to mention that it was middle-age white guys who killed Bambi`s mom. - Dave Barry',
     'I cried because I had no shoes, `till I met a man who had no feet. So I said, `You got any shoes you`re not using`? - Steven Wright',
     'New knowledge is the most valuable commodity on earth. The more truth we have to work with, the richer we become. - Kurt Vonnegut',
     'The giving of love is an education in itself. - Eleanor Roosevelt',
     'By a curious confusion, many modern critics have passed from the proposition that a masterpiece may be unpopular to the other proposition that unless it is unpopular it cannot be a masterpiece. - GK Chesterton',
     'Such is the delicacy of man alone, that no object is produced to his liking. He finds that in everything there is need for improvement. The whole industry of human life is employed not in procuring the supply of our three humble necessities, food, clothes and lodging, but in procuring the conveniences of it according to the nicety and delicacy of our tastes. - Adam Smith',
     'Being president is like being a jackass in a hailstorm. There`s nothing to do but stand there and take it. - Lyndon B. Johnson',
     'Men marry because they are tired; women because they are curious. Both are disappointed. - Oscar Wilde',
     'The greatest happiness of life is the conviction that we are loved, loved for ourselves, or rather, loved in spite of ourselves. - Victor Hugo',
     'Though I am not naturally honest, I am sometimes by chance. - William Shakespeare',
     'Experts tell us that if the Millennium Bug is not fixed, when the year 2000 arrives, our financial records will be inaccurate, our telephone system will be unreliable, our government will be paralyzed and airline flights will be canceled without warning. In other words, things will be pretty much the same as they are now. - Dave Barry',
     'People can misinterpret almost anything so that it coincides with views they already hold. They take from art what they already believe. - Stanley Kubrick',
     'In framing a government which is to be administered by men over men the great difficulty lies in this: You must first enable the government to control the governed, and in the next place, oblige it to control itself. - Alexander Hamilton',
     'There`s nothing sadder in this world than to awake Christmas morning and not be a child. - Erna Bombeck',
     'When we die, our bodies are buried. When we live, our souls are buried. - Jason Mechalek',
     'You must be the change you wish to see in the world. - Mahatma Gandhi',
     'The eyes of the world are upon you. The hopes and prayers of liberty-loving people everywhere march with you. - Dwight Eisenhower',
     'No man will make a great leader who wants to do it all himself or get all the credit for doing it. - Andrew Carnegie',
     'Three grand essentials to happiness in this life are something to do, something to love, and something to hope for. - Joseph Addison',
     'Trust the people. This is the one irrefutable lesson of the entire postwar period contradicting the notion that rigid government controls are essential to economic development. - Ronald Reagan',
     'Education is an admirable thing, but it is well to remember from time to time that nothing that is worth knowing can be taught. - Oscar Wilde',
     'I love writing. I love the swirl and swing of words as they tangle with human emotions. - James Michener',
     'It is only our bad temper that we put down to being tired or worried or hungry; we put our good temper down to ourselves. - C.S. Lewis',
     'This country was built on rape, slavery, murder, degradation and affiliation with crime. - Mike Tyson',
     'The good thing about being bisexual is that it doubles your chance of a date on a Saturday night. - Woody Allen',
     'Every year, back comes Spring, with nasty little birds yapping their fool heads off and the ground all mucked up with plants. - Dorothy Parker',
     'Every difference of opinion is not a difference of principle. We have called by different names brethren of the same principle. - Thomas Jefferson',
     'The best way to win an argument is to begin by being right. - Jill Ruckleshaus',
     'You can discover more about a person in an hour of play than in a year of conversation. - Plato',
     'To think is to differ. - Clarence Darrow',
     'I have come to the conclusion that my subjective account of my motivation is largely mythical on almost all occasions. I don`t know why I do things. - J.B.S. Haldane',
     'If your kid makes one of those little homemade guitars out of a cigar box and rubber bands, don`t let him just play it once or twice and then throw it away. Make him practice on it, every day, for about three hours a day. Later, he`ll thank you. - Jack Handey',
     'I feel impelled to speak today in a language that in a sense is new-one which I, who have spent so much of my life in the military profession, would have preferred never to use. That new language is the language of atomic warfare. - Dwight Eisenhower',
     'To write a good love letter, you ought to begin without knowing what you mean to say and to finish without knowing what you have written. - Jean-Jacques Rousseau',
     'Accept the challenges so that you can feel the exhilaration of victory. - George Patton',
     'God enters by a private door into every individual. - Ralph Waldo Emerson',
     'To grasp the full significance of life is the actor`s duty, to interpret it is his problem and to express it his dedication. - Marlon Brando',
     'There is one thing alone that stands the brunt of life throughout its course: a quiet conscience. - Euripides',
     'Mothers are fonder than fathers of their children because they are more certain they are their own. - Aristotle',
     'If we command our wealth, we shall be rich and free; if our wealth commands us, we are poor indeed. - Edmund Burke',
     'The great nations have always acted like gangsters, and the small nations like prostitutes. - Stanley Kubrick',
     'When angry, count ten before you speak; if very angry, a hundred. - Thomas Jefferson',
     'Don`t ask God to change the laws of nature for you. - Nachman of Bratslav',
     'It is said that gifts persuade even the gods. - Euripides',
     'PRESIDENCY, n. The greased pig in the field game of American politics. - Ambrose Bierce',
     'Those who make peaceful revolution impossible will make violent revolution inevitable. - John F. Kennedy',
     'As scarce as truth is, the supply has always been in excess of the demand. - Josh Billings',
     'A people that values its privileges above its principles soon loses both. - Dwight Eisenhower',
     'A University of Chicago professor said the greatest day in the world was when a water puppy crawled out on land and decided to stay. The water puppy, he said, went on to become a man. If he proves that, I am willing to give up Christmas, Thanksgiving, and New Year`s Day, and to celebrate Water Puppy Day. - William Jennings Bryan',
     'You know what the fellow said: In Italy for thirty years under the Borgias they had warfare, terror, murder, and bloodshed, but they produced Michaelangelo, Leonardo Da Vinci, and the Renaissance. In Switzerland, they had brotherly love--they had five hundred years of democracy and peace, and what did they produce? The cuckoo clock. - Orson Welles',
     'The leading cause of death among fashion models is falling through street grates. - Dave Barry',
     'If you have an apple and I have an apple and we exchange these apples then you and I will still each have one apple. But if you have an idea and I have an idea and we exchange these ideas, then each of us will have two ideas. - George Bernard Shaw',
     'Some succeed by what they know; some by what they do; and a few by what they are. - Elbert Hubbard',
     'Philosophy is questions that may never be answered. Religion is answers that may never be questioned. - Author Unknown',
     'My formula for success is rise early, work late, and strike oil. - Paul Getty',
     'Intoxicated with unbroken success, we have become too self-sufficient to feel the necessity of redeeming and preserving grace, too proud to pray to the God that made us. - Abraham Lincoln',
     'I`ve had a wonderful time, but this wasn`t it. - Groucho Marx',
     'The difference between sex and death is that with death you can do it alone and no one is going to make fun of you. - Woody Allen',
     'When you have the facts on your side, argue the facts. When you have the law on your side, argue the law. When you have neither, holler. - Al Gore',
     'The worst moment for the athieist is when he feels thankful and has no one to thank. - Dante Gabriel Rossetti',
     'It is most unwise for people in love to marry. - George Bernard Shaw',
     'Reason is experimental intelligence, conceived after the pattern of science, and used in the creation of social arts; it has something to do. It liberates man from the bondage of the past, due to ignorance and accident hardened into custom. It projects a better future and assists man in its realization. - John Dewey',
     'Playwriting gets into your blood and you can`t stop it. At least, not until the producers or the public tell you to. - T.S. Eliot',
     'Though force can protect in emergency, only justice, fairness, consideration and cooperation can finally lead men to the dawn of eternal peace. - Dwight Eisenhower',
     'Wedding: a ceremony at which two persons undertake to become one, one undertakes to become nothing, and nothing undertakes to become supportable. - Ambrose Bierce',
     'Just because I look sexy on the cover of Rolling Stone doesn`t mean I`m naughty. - Britney Spears',
     'Slang is the language which takes off its coat, spits on its hands - and goes to work. - Carl Sandburg',
     'It is a scientific fact that your body will not absorb cholesterol if you take it from another person`s plate. - Dave Barry',
     'Having a male gynecologist is like going to an auto mechanic who doesn`t own a car. - Carrie Snow',
     'Always leave something to wish for; otherwise you will be miserable from your very happiness. - Baltasar Gracian',
     'In the Orthodox spiritual tradition, the ultimate moral question we ask is the following: Is what we are doing, is what I am doing, beautiful or not? - Carolyn Gifford',
     'Don`t take life too seriously; you`ll never get out of it alive. - Elbert Hubbard',
     'America is the only country ever founded on a creed. - GK Chesterton',
     'Theology is only thought applied to religion. - GK Chesterton',
     'Every man must decide whether he will walk in the light of creative altruism or in the darkness of destructive selfishness. - Martin Luther King Jr.',
     'Mothers all want their sons to grow up to be president, but they don`t want them to become politicians in the process. - John F. Kennedy',
     'Love means loving the unlovable - or it is no virtue at all. - GK Chesterton',
     'It does not require a majority to prevail, but rather an irate, tireless minority keen to set brush fires in people`s minds. - Samuel Adams',
     'To be a philosopher is not merely to have subtle thoughts; but so to love wisdom as to live according to its dictates. - Henry Thoreau',
     'Corrupt politicians make the other ten percent look bad. - Henry Kissinger',
     'To be awake is to be alive. - Henry Thoreau',
     'Black holes are where God divided by zero. - Steven Wright',
     'He that cannot obey, cannot command. - Benjamin Franklin',
     'The puritanism of Christianity has played havoc with the moderation that an enlightened and tolerant critical spirit would have produced. I`ve noticed that in whatever country, county, town, or other region there is a regulation enjoining temperance, the population seems to be entirely composed of teetotallers and drunkards. There`s a Bible on that shelf there. But I keep it next to Voltaire - poison and antidote. - Bertrand Russell',
     'She was what we used to call a suicide blond - dyed by her own hand. - Saul Bellow',
     'Returning violence for violence multiplies violence, adding deeper darkness to a night already devoid of stars. - Martin Luther King Jr.',
     'Egalitarians create the most dangerous inequality of all -- inequality of power. Allowing politicians to determine what all other human beings will be allowed to earn is one of the most reckless gambles imaginable. Like the income tax, it may start off being applied only to the rich but it will inevitably reach us all. - Thomas Sowell',
     'A brain has to digest its food, too. - Jason Mechalek',
     'Middle age is when you`ve met so many people that every new person you meet reminds you of someone else. - Ogden Nash',
     'Humility is no substitute for a good personality. - Fran Lebowitz',
     'If you see ten troubles coming down the road, you can be sure that nine will run into the ditch before they reach you. - Calvin Coolidge',
     'A powerful idea communicates some of its strength to him who challenges it. - Marcel Proust',
     'I realise that I`m making gender-based generalizations here, but my feeling is that if God did not want us to make gender-based generalizations, She would not have given us genders. - Dave Barry',
     'Science is facts; just as houses are made of stones, so is science made of facts; but a pile of stones is not a house and a collection of facts is not necessarily science. - Henri Poincare',
     'It is unbecoming for young men to utter maxims. - Aristotle',
     'Humanity is acquiring all the right technology for all the wrong reasons. - Buckminster Fuller',
     'As I would not be a slave, so I would not be a master. This expresses my idea of democracy. Whatever differs from this, to the extent of the difference, is no democracy. - Abraham Lincoln',
     'Democratic nations must try to find ways to starve the terrorist and the hijacker of the oxygen of publicity on which they depend. - Margaret Thatcher',
     'Regarding the debate about faith and works: It\x92s like asking which blade in a pair of scissors is most important. - C.S. Lewis',
     'Few people think more than two or three times a year. I have made an international reputation for myself by thinking once or twice a week. - George Bernard Shaw',
     'If everything seems under control, you`re just not going fast enough. - Mario Andretti',
     'Happiness is the full use of your powers along lines of excellence. - John F. Kennedy',
     'Christ died for men precisely because men are not worth dying for; to make them worth it. - C.S. Lewis',
     'I am a writer of books in retrospect. I talk in order to understand; I teach in order to learn. - Robert Frost',
     'I think and think for months and years, ninety-nine times, the conclusion is false. The hundredth time I am right. - Albert Einstein',
     'The least of things with a meaning is worth more in life than the greatest of things without it. - Carl Jung',
     'Prediction is very difficult, especially about the future. - Niels Bohr',
     'All I want out of life, is that when I walk down the street folks will say, `There goes the greatest hitter that ever lived.` - Ted Williams',
     'Love is the triumph of imagination over intelligence. - Henry Mencken',
     'He that would live in peace and at ease must not speak all he knows or all he sees. - Benjamin Franklin',
     'What is the most important for democracy is not that great fortunes should not exist, but that great fortunes should not remain in the same hands. In that way there are rich men, but they do not form a class. - Alexis de Tocqueville',
     'Facts do not cease to exist because they are ignored. - Aldous Huxley',
     'The first thing I do in the morning is brush my teeth and sharpen my tongue. - Dorothy Parker',
     'I once said cynically of a politician, `He`ll doublecross that bridge when he comes to it.` - Oscar Levant',
     'Live as if you were to die tomorrow. Learn as if you were to live forever. - Mahatma Gandhi',
     'Freedom is never voluntarily given by the oppressor; it must be demanded by the oppressed. - Martin Luther King Jr.',
     'With the sleep of dreams comes nightmares. - William Shakespeare',
     'Those who bring sunshine to the lives of others, cannot keep it from themselves. - James Matthew Barrie',
     'To be pleased with one`s limits is a wretched state. - Johann Wolfgang von Goethe',
     'There is wishful thinking in Hell as well as on Earth. - C.S. Lewis',
     'I never knew what real happiness was until I got married, and by then it was too late. - Max Kaufman',
     'There is hardly a political question in the United States which does not sooner or later turn into a judicial one. - Alexis de Tocqueville',
     'No passion so effectually robs the mind of all its powers of acting and reasoning as fear. - Edmund Burke',
     'My friends are my estate. - Emily Dickinson',
     'I do not believe one can settle how much we ought to give. I am afraid the only safe rule is to give more than we can spare. - C.S. Lewis',
     'No sooner do we depart from sense and instinct to follow reason but we are insensibly drawn into uncouth paradoxes, difficulties, and inconsistencies, which multiply and grow upon us as we advance in speculation; till at length, having wandered through many intricate mazes, we find ourselves just where we were, or, which is worse, sit down in a forlorn scepticism. - George Berkeley',
     'What is now proved was once only imagined. - William Blake',
     'Parents are not interested in justice, they`re interested in peace and quiet. - Bill Cosby',
     'That men do not learn very much from the lessons of history is the most important of all the lessons of history. - Aldous Huxley',
     'He has all the virtues I dislike and none of the vices I admire. - Winston Churchill',
     'Enthusiasm is the great hill-climber. - Elbert Hubbard',
     'It ain`t what you don`t know that gets you into trouble. It`s what you know for sure that just ain`t so. - Mark Twain',
     'I have gathered a posie of other men\x92s flowers, and nothing but the thread that binds them is mine own. - John Bartlett',
     'Too many poets delude themselves by thinking that the mind is dangerous and must be left out. Well, the mind is dangerous and must be left in. - Robert Frost',
     'If Al Gore invented the Internet, I invented spell check. - Dan Quayle',
     'History doesn`t repeat itself, but it does rhyme. - Mark Twain',
     'It must be remembered that there is nothing more difficult to plan, more doubtful of success nor more dangerous to manage than the creation of a new system. For the initiator has the enmity of all who profit by the preservation of the old institution and merely lukewarm defenders in those who would gain by the new one. - Nicolo Machiavelli',
     'One can resist the invasion of an army but one cannot resist the invasion of ideas. - Victor Hugo',
     'You may delay, but time will not. - Benjamin Franklin',
     'If you can`t convince them, confuse them. - Harry Truman',
     'When you work seven days a week, fourteen hours a day, you get lucky. - Armand Hammer',
     'It is a good idea to ``shop around`` before you settle on a doctor. Ask about the condition of his Mercedes. Ask about the competence of his mechanic. Don`t be shy! After all, you`re paying for it. - Dave Barry',
     'Whatever affects one directly, affects all indirectly. I can never be what I ought to be until you are what you ought to be. This is the interrelated structure of reality. - Martin Luther King Jr.',
     'My main objective is to be professional but to kill him. - Mike Tyson',
     'The covers of this book are too far apart. - Ambrose Bierce',
     'Feminism was established to allow unattractive women easier access to the mainstream. - Rush Limbaugh',
     'Must not all things at the last be swallowed up in death? - Plato',
     'The last thing one discovers in composing a work is what to put first. - Blaise Pascal',
     'The most exciting phrase to hear in science, the one that heralds new discoveries, is not `Eureka!` (I found it!) but `That`s funny...` - Isaac Asimov',
     'I don`t always know what I`m talking about but I know I`m right. - Muhammad Ali',
     'A successful marriage requires falling in love many times, always with the same person. - Germaine Greer',
     'Wisdom begins at the end. - Daniel Webster',
     'Is there anything more beautiful than a beautiful, beautiful flamingo, flying across in front of a beautiful sunset? And he`s carrying a beautiful rose in his beak, and also he`s carrying a very beautiful painting with his feet. And also, you`re drunk. - Jack Handey',
     'It is your work in life that is the ultimate seduction. - Pablo Picasso',
     'Have children while your parents are still young enough to take care of them. - Rita Rudner',
     'Your children need your presence more than your presents. - Jesse Jackson',
     'It is your mind that creates this world. - Siddhartha Buddha',
     'There are three ingredients in the good life: learning, earning and yearning. - Christopher Morley',
     'Nothing so dates a man as to decry the younger generation. - Adlai Stevenson',
     'Blood is the ink of our life`s story. - Jason Mechalek',
     'It ain`t over till it`s over. - Yogi Berra',
     'No easy problem ever comes to the President of the United States. If they are easy to solve, somebody else has solved them. - John F. Kennedy',
     'We make a living by what we get, but we make a life by what we give. - Winston Churchill',
     'Ah, yes, divorce...from the Latin word meaning to rip out a man`s genitals through his wallet. - Robin Williams',
     'Before reciting his prayers, a man should give to charity. - Nachman of Bratslav',
     'The greatest monarch on the proudest throne is obliged to sit upon his own arse. - Benjamin Franklin',
     'The reason we hold truth in such respect is because we have so little opportunity to get familiar with it. - Mark Twain',
     'I didn`t come to Washington to be loved and I haven`t been disappointed. - Philip L. Gramm',
     'Remember not only to say the right thing in the right place, but far more difficult still, to leave unsaid the wrong thing at the tempting moment. - Benjamin Franklin',
     'One of the great attractions of patriotism -- it fulfills our worst wishes. In the person of our nation we are able, vicariously, to bully and cheat. Bully and cheat, what`s more, with a feeling that we are profoundly virtuous. - Aldous Huxley',
     'If God had wanted us to spend our time fretting about the problems of home ownership, He would never have invented beer. - Dave Barry',
     'As every divided kingdom falls, so every mind divided between many studies confounds and saps itself. - Leonardo da Vinci',
     'My most brilliant achievement was my ability to be able to persuade my wife to marry me. - Winston Churchill',
     'There are perhaps no days of our childhood we lived so fully as those we spent with a favorite book. - Marcel Proust',
     'Children today know more about sex than I or my father did. - Bill Cosby',
     'It is a grand mistake to think of being great without goodness and I pronounce it as certain that there was never a truly great man that was not at the same time truly virtuous. - Benjamin Franklin',
     'Never continue in a job you don`t enjoy. If you`re happy in what you`re doing, you`ll like yourself, you`ll have inner peace. And if you have that, along with physical health, you will have had more success than you could possibly have imagined. - Johnny Carson',
     'Marriage is the alliance of two people, one of whom never remembers birthdays and the other who never forgets. - Ogden Nash',
     'The greatest pleasure of life is love. - William Temple',
     'There is no question that there is an unseen world. The problem is, how far is it from midtown and how late is it open? - Woody Allen',
     'From kindergarten to graduation, I went to public schools, and I know that they are a key to being sure that every child has a chance to succeed and to rise in the world. - Dick Cheney',
     'Failure is success if we learn from it. - Malcolm Forbes',
     'A good novel tells us the truth about its hero; but a bad novel tells us the truth about its author. - GK Chesterton',
     'God loves each of us as if there were only one of us. - Saint Augustine',
     'I think, at a child`s birth, if a mother could ask a fairy godmother to endow it with the most useful gift, that gift should be curiosity. - Eleanor Roosevelt',
     'Satisfaction lies in the effort, not in the attainment. Full effort is full victory. - Mahatma Gandhi',
     'For a time, at least, I was the most famous person in the entire world. - Jesse Owens',
     'Inspiration exists, but it has to find you working. - Pablo Picasso',
     'All human actions have one or more of these seven causes: chance, nature, compulsions, habit, reason, passion, desire. - Aristotle',
     'It is very easy to tell the difference between man-made and God-made objects. The more you magnify man-made objects, the cruder they look, but the more you magnify God-made objects, the more precise and intricate they appear. - Luther Sutherland',
     'Speeches are for the younger men who are going places. And I`m not going anyplace except six feet under the floor of that little chapel adjoining the museum and library at Abilene. - Dwight Eisenhower',
     'Through pride we are ever deceiving ourselves. But deep down below the surface of the average conscience a still, small voice says to us, something is out of tune. - Carl Jung',
     'If you wanna be free, you`ve gotta accept everything. - Jason Mechalek',
     'Rhis is to be asserted in general of men: that they are ungrateful, fickle, false, cowardly, covetous, and as long as you succeed, are yours entirely; they will offer you their blood, property, life, and children...when the need is far distant; but when it approaches, they will turn against you. - Nicolo Machiavelli',
     'Let the word go forth from this time and place, to friend and foe alike, that the torch has been passed to a new generation of Americans. - John F. Kennedy',
     'He who is of calm and happy nature will hardly feel the pressure of age, but to him who is of an opposite disposition youth and age are equally a burden. - Plato',
     'A truly great book should be read in youth, again in maturity and once more in old age, as a fine building should be seen by morning light, at noon and by moonlight. - Robertson Davies',
     'When you`re through changing, you`re through. - Bruce Barton',
     'If people don\x92t come to the games, you can\x92t stop them. - Yogi Berra',
     'When this girl at the museum asked me who I liked better, Monet or Manet, I said, `I like mayonnaise.` She just stared at me, so I said it again, louder. Then she left. I guess she went to try to find some mayonnaise for me. - Jack Handey',
     'Either write something worth reading or do something worth writing. - Benjamin Franklin',
     'Everything that used to be a sin is now a disease. - Bill Maher',
     'The time which we have at our disposal every day is elastic; the passions we feel expand it, those that we inspire contract it, and habit fills up what remains. - Marcel Proust',
     'The right to swing my fist ends where the other man`s nose begins. - Oliver Wendell Holmes',
     'God help the man who won`t marry until he finds a perfect woman, and God help him still more if he finds her. - Benjamin Tillet',
     'Every exit is an entry somewhere. - Tom Stoppard',
     'Being a leader is like being a lady, if you have to go around telling people you are one, you aren`t. - Margaret Thatcher',
     'If men will not act for themselves, what will they do when the benefit of their effort is for all? - Elbert Hubbard',
     'I love argument, I love debate. I don`t expect anyone just to sit there and agree with me, that`s not their job. - Margaret Thatcher',
     'That the innocent, though they may have some connexion or dependency upon the guilty (which, perhaps, they themselves cannot help), should not, upon that account, suffer or be punished for the guilty, is one of the plainest and most obvious rules of justice. - Adam Smith',
     'I believe one of the reasons so many do not get a higher education is the fear of their parents that they will lose more morally than they will receive mentally. - William Jennings Bryan',
     'Love is the master key which opens the gates of happiness. - Oliver Wendell Holmes',
     'All enterprises that are entered into with indiscreet zeal may be pursued with great vigor at first, but are sure to collapse in the end. - Tacitus',
     'Just think of the tragedy of teaching children not to doubt. - Clarence Darrow',
     'What the country needs is dirtier fingernails and cleaner minds. - Will Rogers',
     'And what\x92s romance? Usually, a nice little tale where you have everything As You Like It, where rain never wets your jacket and gnats never bite your nose and it\x92s always daisy-time. - D.H. Lawrence',
     'To me, clowns aren`t funny. In fact, they`re kinda scary. I`ve wondered where this started, and I think it goes back to the time I went to the circus and a clown killed my dad. - Jack Handey',
     'Ever notice that `what the hell` is always the right decision? - Marilyn Monroe',
     'Knowledge that is paid for will be longer remembered. - Nachman of Bratslav',
     'No matter what they`re charging to get in, it`s worth more to get out. - Roger Ebert',
     'I was angry with my friend I told my wrath, my wrath did end. I was angry with my foe: I told it not, my wrath did grow. - William Blake',
     'If my children wake up on Christmas morning and have someone to thank for putting candy in their stocking, have I no one to thank for putting two feet in mine? - GK Chesterton',
     'Of all tyrannies, a tyranny exercised for the good of its victims may be the most oppressive. It may be better to live under robber barons than under omnipotent moral busybodies. The robber baron`s cruelty may sometimes sleep, his cupidity may at some point be satiated; but those who torment us for our own good will torment us without end, for they do so with the approval of their own conscience. - C.S. Lewis',
     'I`ve got more trophies than Wayne Gretzky & The Pope combined! - Homer Simpson',
     'Life is anything that dies when you stomp on it. - Dave Barry',
     'Without question, the greatest invention in the history of mankind is beer. Oh, I grant you that the wheel was also a fine invention, but the wheel does not go nearly as well with pizza. - Dave Barry',
     'Sin has many tools, but a lie is the handle which fits them all. - Edmund Burke',
     'There is no joy in life like the joy of sharing. - Billy Graham',
     'The object of war is not to die for your country but to make the other bastard die for his. - George Patton',
     'Good manners will open doors that the best education cannot. - Clarence Thomas',
     'Learning carries within itself certain dangers because out of necessity one has to learn from one`s enemies. - Leon Trotsky',
     'Eros will have naked bodies; Friendship naked personalities. - C.S. Lewis',
     'This will never be a civilized country until we expend more money for books than we do for chewing gum. - Elbert Hubbard',
     'May God have mercy upon my enemies, because I won`t. - George Patton',
     'My mind is my own church. - Thomas Paine',
     'Life is a fatal complaint, and an eminently contagious one. - Oliver Wendell Holmes',
     'Genius is one per cent inspiration, ninety-nine per cent perspiration. - Thomas Edison',
     'It`s not how much we give but how much love we put into giving. - Mother Teresa',
     'Some of your countrymen were unable to distinguish between their native dislike for war and the stainless patriotism of those who suffered its scars. But there has been a rethinking and now we can say to you, and say as a nation, thank you for your courage. - Ronald Reagan',
     'When they call the roll in the Senate, the Senators do not know whether to answer `Present` or `Not guilty.` - Theodore Roosevelt',
     'Religion to me has always been the wound, not the bandage. - Dennis Potter',
     'Life is just one damned thing after another. - Elbert Hubbard',
     'Simplicity is the ultimate sophistication. - Leonardo da Vinci',
     'The difference between genius and stupidity is that genius has its limits. - Albert Einstein',
     'Goldie and I did have a car stolen right out of our yard. It took us three days to notice. - Kurt Russell',
     'Film lovers are sick people. - Francois Truffaut',
     'To be wise and love exceeds man`s might. - William Shakespeare',
     'Life does not cease to be funny when people die any more than it ceases to be serious when people laugh. - George Bernard Shaw',
     'Imitation is the sincerest of flattery. - Charles Caleb Colton',
     'It is hard to fail, but it is worse never to have tried to succeed. - Theodore Roosevelt',
     'We are healed from suffering only by experiencing it to the full. - Marcel Proust',
     'What is a wedding? Webster`s dictionary defines a wedding as `the process of removing weeds from one`s garden.` - Homer Simpson',
     'It is one of the blessings of old friends that you can afford to be stupid with them. - Ralph Waldo Emerson',
     'Ten people who speak make more noise than ten thousand who are silent. - Napoleon Bonaparte',
     'An unjust punishment is never forgotten. - Penelope Fitzgerald',
     'The fruit that can fall without shaking, indeed is too mellow for me. - Lady Mary Wortley Montagu',
     'Don`t knock the weather; nine-tenths of the people couldn`t start a conversation if it didn`t change once in a while. - Kin Hubbard',
     'Nature thrives on patience; man on impatience. - Paul Boese',
     'Children are innocent and love justice, while most adults are wicked and prefer mercy. - GK Chesterton',
     'Advice to young writers who want to get ahead without annoying delays: don\x92t write about Man, write about `a` man. - E.B. White',
     'Nature is trying very hard to make us succeed, but nature does not depend on us. We are not the only experiment. - Buckminster Fuller',
     'All good art is about something deeper than it admits. - Roger Ebert',
     'Karate is a form of marital arts in which people who have had years and years of training can, using only their hands and feet, make some of the worst movies in the history of the world. - Dave Barry',
     'A single death is a tragedy; a million deaths is a statistic. - Joseph Stalin',
     'A star on a movie set is like a time bomb. That bomb has got to be defused so people can approach it without fear. - Jack Nicholson',
     'To be a leader means to be able to move masses. - Adolf Hitler',
     'We turn not older with years, but newer every day. - Emily Dickinson',
     'It is hard to believe that a man is telling the truth when you know that you would lie if you were in his place. - Henry Mencken',
     'To defend Western Europe we have to let the Pentagon buy all these tanks and guns and things, and the Pentagon is unable to buy any object that that costs less than a condominium in Vail. If the Pentagon needs, say, fruit, it will argue that it must have fruit that can withstand the rigors of combat conditions, and it will wind up purchasing the FX-700 Seedless Tactical Grape, which will cost $160,000 per bunch, and will have an 83 percent failure rate. - Dave Barry',
     'Love is the wisdom of the fool and the folly of the wise. - Samuel Johnson',
     'There are three rules for writing a novel. Unfortunately, no one knows what they are. - W. Somerset Maugham',
     'Even if there is only one possible unified theory, it is just a set of rules and equations. What is it that breathes fire into the equations and makes a universe for them to describe? - Stephen Hawking',
     'The United States stands at the pinnacle of world power. This is a solemn moment for the American democracy. For with primacy in power is joined an awe-inspiring accountability for the future. - Winston Churchill',
     'There`s no present. There`s only the immediate future and the recent past. - George Carlin',
     'Art is man`s expression of his joy in labor. - Henry Kissinger',
     'The only paradise is paradise lost. - Marcel Proust',
     'War - an act of violence whose object is to constrain the enemy, to accomplish our will. - George Washington',
     'One swallow does not make a summer. - Aristotle',
     'People will pay more to be entertained than educated. - Johnny Carson',
     'I have one yardstick by which I test every major problem-and that yardstick is: Is it good for America? - Dwight Eisenhower',
     'Children always understand. They have open minds. They have built-in shit detectors. - Madonna Ciccone',
     'Probable impossibilities are to be preferred to improbable possibilities. - Aristotle',
     'The best and most beautiful things in the world cannot be seen or even touched. They must be felt with the heart. - Helen Keller',
     'Nothing gives one person so much advantage over another as to remain always cool and unruffled under all circumstances. - Thomas Jefferson',
     'All men are timid on entering any fight. Whether it is the first or the last fight, all of us are timid. Cowards are those who let their timidity get the better of their manhood. - George Patton',
     'I believe in Christianity as I believe that the sun has risen, not only because I see it, but because by it I see everything else. - C.S. Lewis',
     'We seem to be going through a period of nostalgia, and everyone seems to think yesterday was better than today. I don`t think it was, and I would advise you not to wait ten years before admitting today was great. If you`re hung up on nostalgia, pretend today is yesterday and just go out and have one hell of a time. - Art Buchwald',
     'There is nothing funny about Halloween. This sarcastic festival reflects, rather, an infernal demand for revenge by children on the adult world. - Jean Baudrillard',
     'The thing we all have to understand to put these last two years in focus, is that liberals in this country care more about whether European leaders like us than they do about whether terrorists are killing us. - Rush Limbaugh',
     'In the councils of government, we must guard against the acquisition of unwarranted influence, whether sought or unsought, by the military-industrial complex. - Dwight Eisenhower',
     'There are fathers who do not love their children; there is no grandfather who does not adore his grandson. - Victor Hugo',
     'Forgive, O Lord, my little jokes on Thee, and I`ll forgive Thy great big joke on me. - Robert Frost',
     'Certain thoughts are prayers. There are moments when, whatever be the attitude of the body, the soul is on its knees. - Victor Hugo',
     'This moment contains all moments. - C.S. Lewis',
     'Of all lies, art is the least untrue. - Gustave Flaubert',
     'Punctuality is the thief of time. - Oscar Wilde',
     'Diligence is the mother of good luck. - Benjamin Franklin',
     'What we are today comes from our thoughts of yesterday and our present thoughts build our life tomorrow. Our life is the creation of our mind. - Siddhartha Buddha',
     'The recipe for perpetual ignorance is: be satisfied with your opinions and content with your knowledge. - Elbert Hubbard',
     'Washington is a Hollywood for ugly people. Hollywood is a Washington for the simpleminded. - John McCain',
     'Life`s Tragedy is that we get old to soon and wise too late. - Benjamin Franklin',
     'Old age is fifteen years older than I am. - Oliver Wendell Holmes',
     'Your faith is what you believe, not what you know. - Mark Twain',
     'We are living in a world, where what we earn is a function of what we learn. - Bill Clinton',
     'Call on God, but row away from the rocks. - Hunter S. Thompson',
     'The cost of freedom is always high, but Americans have always paid it. And one path we shall never choose, and that is the path of surrender, or submission. - John F. Kennedy',
     'I may be drunk, Miss, but in the morning I will be sober and you will still be ugly. - Winston Churchill',
     'The greatest lesson in life is to know that even fools are right sometimes. - Winston Churchill',
     'My life is my message. - Mahatma Gandhi',
     'Remember that happiness is a way of travel, not a destination. - Roy Goodman',
     'PRESIDENT, n. The leading figure in a small group of men of whom \x97 and of whom only \x97 it is positively known that immense numbers of their countrymen did not want any of them for President. - Ambrose Bierce',
     'I`ve worked for four presidents and watched two others up close, and I know that there`s no such thing as a routine day in the Oval Office. - Dick Cheney',
     'We know life is futile. A man who considers that his life is of very wonderful importance is awfully close to a padded cell. - Clarence Darrow',
     'Education is the ability to listen to almost anything without losing your temper or your self-confidence. - Robert Frost',
     'There is nothing more exhilarating than to be shot at without result. - Winston Churchill',
     'Remember when safe sex meant not getting caught? - Author Unknown',
     'The Nation which indulges toward another an habitual hatred or an habitual fondness is in some degree a slave. It is a slave to its animosity or to its affection, either of which is sufficient to lead it astray from its duty and its interest. - George Washington',
     'To know what is impenetrable to us really exists, manifesting itself as the highest wisdom and the most radiant beauty...this knowledge, this feeling is at the center of true religiousness. - Albert Einstein',
     'I believe the highest aspiration of man should be individual freedom and the development of the individual. - Ronald Reagan',
     'If a woman has to choose between catching a fly ball and saving an infant`s life, she will choose to save the infant`s life without even considering if there are men on base. - Dave Barry',
     'We all want progress, but if you`re on the wrong road, progress means doing an about-turn and walking back to the right road; in that case, the man who turns back soonest is the most progressive. - C.S. Lewis',
     'I told my psychiatrist that everyone hates me. He said I was being ridiculous - everyone hasn`t met me yet. - Rodney Dangerfield',
     'You are young, my son, and, as the years go by, time will change and even reverse many of your present opinions. Refrain therefore awhile from setting yourself up as a judge of the highest matters. - Plato',
     'Religion operates not only on the vertical plane but also on the horizontal. It seeks not only to integrate men with God but to integrate men with men and each man with himself. - Martin Luther King Jr.',
     'It is always more difficult to fight against faith than against knowledge. - Adolf Hitler',
     'A nickel isn`t worth a dime today. - Yogi Berra',
     'The worst thing that could happen to anybody, would be to not be used for anything by anybody. - Kurt Vonnegut',
     'Let us have faith that right makes might, and in that faith, let us, to the end, dare to do our duty as we understand it. - Abraham Lincoln',
     'An optimist is a person who starts a new diet on Thanksgiving Day. - Irv Kupcinet',
     'If the primary aim of a captain were to preserve his ship, he would keep it in port forever. - Thomas Aquinas',
     'All virtue is summed up in dealing justly. - Aristotle',
     'Like many intellectuals, he was incapable of saying a simple thing in a simple way. - Marcel Proust',
     'Life`s most persistent and urgent question is, `What are you doing for others?` - Martin Luther King Jr.',
     'Talent alone won`t make you a success. Neither will being in the right place at the right time, unless you are ready. The most important question is: `Are you ready?` - Johnny Carson',
     'Sex is emotion in motion. - Mae West',
     'I`d rather hear an old truth than a new lie. - Chris Bowyer',
     'Cocaine is God`s way of telling someone that they`re too rich. - Robin Williams',
     'The most incomprehensible thing about the world is that it is at all comprehensible. - Albert Einstein',
     'Everything except God has some natural superior; everything except unformed matter has some natural inferior. - C.S. Lewis',
     'When we got into office, the thing that surprised me the most was that things were as bad as we`d been saying they were. - John F. Kennedy',
     'If the United Nations once admits that international disputes can be settled by using force, then we will have destroyed the foundation of the organization and our best hope of establishing a world order. - Dwight Eisenhower',
     'Beauty is ever to the lonely mind a shadow fleeting; she is never plain. She is a visitor who leaves behind the gift of grief, the souvenir of pain. - Christopher Morley',
     'Money can help you to get medicines but not health. Money can help you to get soft pillows, but not sound sleep. Money can help you to get material comforts, but not eternal bliss. Money can help you to get ornaments, but not beauty. Money will help you to get an electric earphone, but not natural hearing. Attain the supreme wealth, wisdom, and you will have everything. - Benjamin Franklin',
     'Be thankful we`re not getting all the government we`re paying for. - Will Rogers',
     'On account of being a democracy and run by the people, we are the only nation in the world that has to keep a government four years, no matter what it does. - Will Rogers',
     'Immature love says: `I love you because I need you.` Mature love says: `I need you because I love you.` - Erich Fromm',
     'Rings and jewels are not gifts but apologies for gifts. The only true gift is a portion of yourself. - Ralph Waldo Emerson',
     'Let the river roll which way it will, cities will rise on its banks. - Ralph Waldo Emerson',
     'I like television. I still believe that television is the most powerful form of communication on Earth -- I just hate what is being done with it. - Alton Brown',
     'No side will win the Battle of the Sexes. There`s too much fraternizing with the enemy. - Henry Kissinger',
     'I just want to do God`s will. - Martin Luther King Jr.',
     'God does not give heed to the ambitiousness of our prayers, because he is always ready to give to us his light, not a visible light but an intellectual and spiritual one; but we are not always ready to receive it when we turn aside and down to other things out of a desire for temporal things. - Saint Augustine',
     '.I had to face the horrible truth: The antitobacco people are lying. Smoking really is cool. And I`m less cool for not doing it. - Tucker Carlson',
     'Life is no brief candle to me. It is a sort of splendid torch which I have got a hold of for the moment, and I want to make it burn as brightly as possible before handing it onto future generations. - George Bernard Shaw',
     'Everyone is in awe of the lion tamer in a cage with half a dozen lions -- everyone but a school bus driver. - Laurence Peter',
     'Peace is its own reward. - Mahatma Gandhi',
     'I never see what has been done; I only see what remains to be done. - Siddhartha Buddha',
     'There is only one rule for being a good talker - learn to listen. - Christopher Morley',
     'Under the doctrine of the separation of powers, the manner in which the president personally exercises his assigned executive powers is not subject to questioning by another branch of government. - Richard Nixon',
     'We have it in our power to begin the world over again. - Thomas Paine',
     'I think computer viruses should count as life. I think it says something about human nature that the only form of life we have created so far is purely destructive. We`ve created life in our own image. - Stephen Hawking',
     'Our attitude towards others determines their attitude towards us. - Earl Nightingale',
     'Reason and judgment are the qualities of a leader. - Tacitus',
     'Death is psychologically as important as birth. Shrinking away from it is something unhealthy and abnormal which robs the second half of life of its purpose. - Carl Jung',
     'A mathematician is a blind man in a dark room looking for a black cat which isn`t there. - Charles Robert',
     'There is no strength in unbelief. Even the unbelief of what is false is no source of might. It is the truth shining from behind that gives the strength to disbelieve. - George MacDonald',
     'Parting is all we know of heaven and all we need to know of hell. - Emily Dickinson',
     'The nice thing about being a celebrity is that, if you bore people, they think it`s their fault. - Henry Kissinger',
     'It takes a long time to turn a big country around. - Bill Clinton',
     'It still remains true that no justification of virtue will enable a man to be virtuous. - C.S. Lewis',
     'I have never started a poem yet whose end I knew. Writing a poem is discovering. - Robert Frost',
     'Freedom is nothing else but a chance to be better. - Albert Camus',
     'When the human race has once acquired a supersitition nothing short of death is ever likely to remove it. - Mark Twain',
     'Some folks look at me and see a certain swagger, which in Texas is called `walking.` - George W. Bush',
     'In politics, an organized minority is a political majority. - Jesse Jackson',
     'No one can make you feel inferior without your consent. - Eleanor Roosevelt',
     'I have never let my schooling interfere with my education. - Mark Twain',
     'Humility must always be the portion of any man who receives acclaim earned in blood of his followers and sacrifices of his friends. - Dwight Eisenhower',
     'Many a man`s reputation would not know his character if they met on the street. - Elbert Hubbard',
     'Indeed, man wishes to be happy even when he so lives as to make happiness impossible. - Saint Augustine',
     'History does not long entrust the care of freedom to the weak or the timid. - Dwight Eisenhower',
     'The whole life of an American is passed like a game of chance, a revolutionary crisis, or a battle. - Alexis de Tocqueville',
     'You can`t build a reputation on what you are going to do. - Henry Ford',
     'I`m the type who`d be happy not going anywhere as long as I was sure I knew exactly what was happening at the places I wasn`t going to. I`m the type who`d like to sit home and watch every party that I`m invited to on a monitor in my bedroom. - Andy Warhol',
     'My life has no purpose, no direction, no aim, no meaning, and yet I`m happy. I can`t figure it out. What am I doing right? - Charles Schulz',
     'Don`t join the book burners. Do not think you are going to conceal thoughts by concealing evidence that they ever existed. - Dwight Eisenhower',
     'Men show their characters in nothing more clearly than in what they think laughable. - Johann Wolfgang von Goethe',
     'Providence protects children and idiots. I know because I have tested it. - Mark Twain',
     'Where there`s marriage without love, there will be love without marriage. - Benjamin Franklin',
     'The intellect is not a serious thing, and never has been. It is an instrument on which one plays, that is all. - Oscar Wilde',
     'More than kisses, letters mingle souls. - John Donne',
     'There is luxury in self-reproach. When we blame ourselves, we feel no one else has a right to blame us. - Oscar Wilde',
     'You do not lead by hitting people over the head \x97 that`s assault, not leadership. - Dwight Eisenhower',
     'As soon as one is unhappy one becomes moral. - Marcel Proust',
     'The function of RAM is to give us guys a way of deciding whose computer has the biggest, studliest, most tumescent MEMORY. This is important, because with today`s complex software, the more memory a computer has, the faster it can produce error messages. So the bottom line is, if you`re a guy, you cannot have enough RAM. - Dave Barry',
     'The public is wonderfully tolerant. It forgives everything except genius. - Oscar Wilde',
     'Take everything you like seriously, except yourselves. - Rudyard Kipling',
     'We need not just a new generation of leadership but a new gender of leadership. - Bill Clinton',
     'Accept good advice gracefully--as long as it doesn`t interfere with what you intended to do in the first place. - Gene Brown',
     'By the time we`ve made it, we`ve had it. - Malcolm Forbes',
     'An idea that is developed and put into action is more important than an idea that exists only as an idea. - Siddhartha Buddha',
     'I dote on his very absence. - William Shakespeare',
     'Anger is never without an argument, but seldom with a good one. - George Savile',
     'He who controls the present, controls the past. He who controls the past, controls the future. - George Orwell',
     'Those who believe they are exclusively in the right are generally those who achieve something. - Aldous Huxley',
     'The man who does not read good books has no advantage over the man who cannot read them. - Mark Twain',
     'From the prodigious hilltops of New Hampshire, let freedom ring. From the mighty mountains of New York, let freedom ring. From the heightening Alleghenies of Pennsylvania, let freedom ring. But not only that: Let freedom ring from every hill and molehill of Mississippi. - Martin Luther King Jr.',
     'Music expresses that which cannot be said and on which it is impossible to be silent. - Victor Hugo',
     'Every decent man is ashamed of the government he lives under. - Henry Mencken',
     'What a man`s mind can create, man`s character can control. - Thomas Edison',
     'Never confuse the size of your paycheck with the size of your talent. - Marlon Brando',
     'To me, it`s always a good idea to always carry two sacks of something when you walk around. That way, if anybody says, `Hey, can you give me a hand?,` you can say, `Sorry, got these sacks.` - Jack Handey',
     'The mystic chords of memory, stretching from every battlefield and patriot grave to every living heart and hearthstone all over this broad land, will yet swell the chorus of the Union, when again touched, as surely they will be, by the better angels of our nature. - Abraham Lincoln',
     'Sex without love is a meaningless experience, but as far as meaningless experiences go, it`s pretty damn good. - Woody Allen',
     'Forgiveness is not an occasional act: it is a permanent attitude. - Martin Luther King Jr.',
     'A man who desires to get married should know either everything or nothing. - Oscar Wilde',
     'When we`re unemployed, we`re called lazy; when the whites are unemployed it`s called a depression. - Jesse Jackson',
     'He who learns but does not think, is lost! He who thinks but does not learn is in great danger. - Confucius',
     'The illegal we do immediately. The unconstitutional takes a little longer. - Henry Kissinger',
     'Not only does God play dice, but he sometimes throws them where they cannot be seen. - Stephen Hawking',
     'One of the striking differences between a cat and a lie is that a cat has only nine lives. - Mark Twain',
     'A few hours of mountain climbing turn a villain and a saint into two rather equal creature. Exhaustion is the shortest way to equality and fraternity, and liberty is added eventually by sleep. - Friedrich Nietzsche',
     'If all our misfortunes were laid in one common heap, whence everyone must take an equal portion, most people would be content to take their own and depart. - Socrates',
     'It is the madness of folly, to expect mercy from those who have refused to do justice; and even mercy, where conquest is the object, is only a trick of war; the cunning of the fox is as murderous as the violence of the wolf. - Thomas Paine',
     'When you stop giving and offering something to the rest of the world, it`s time to turn out the lights. - George Burns',
     'I don`t work according to nature, but infront and together with it. An artist must observe the nature, but never confuse it with the art. - Pablo Picasso',
     'Grief can take care of itself, but to get the full value of joy you must have somebody to divide it with. - Mark Twain',
     'A diplomat is a man who always remembers a woman`s birthday but never remembers her age. - Robert Frost',
     'If you start to think about your physical or moral condition, you usually find that you are sick. - Johann Wolfgang von Goethe',
     'No human relation gives one possession in another...every two souls are absolutely different. In friendship and in love, the two side by side raise hands together to find what one cannot reach alone. - Kahlil Gibran',
     'A word is dead when it is said, some say. I say it just begins to live that day. - Emily Dickinson',
     'You cannot go on `explaining away` for ever: you will find that you have explained explanation itself away. You cannot go on `seeing through` things for ever. The whole point of seeing through something is to see something through it. - C.S. Lewis',
     'The invisible and the non-existent look very much alike. - Delos McKown',
     'To you taxpayers out there, let me say this: Make sure you file your tax return on time! And remember that, even though income taxes can be a \x93pain in the neck,\x94 the folks at the IRS are regular people just like you, except that they can destroy your life. - Dave Barry',
     'We do survive every moment, after all, except the last one. - John Updike',
     'Andy Warhol made fame more famous. - Fran Lebowitz',
     'It is the dissimilarities and inequalities among men which give rise to the notion of honor; as such differences become less, it grows feeble; and when they disappear, it will vanish too. - Alexis de Tocqueville',
     'Time is a great teacher, but unfortunately it kills all its pupils. - Louis Hector Berlioz',
     'To be prepared for war is one of the most effectual means of preserving peace. - George Washington',
     'What is it that makes a complete stranger dive into an icy river to save a solid-gold baby? Maybe we`ll never know. - Jack Handey',
     'All children are artists. The problem is how to remain an artist once he grows up. - Pablo Picasso',
     '\x93Take a chance! All life is a chance. The man who goes farthest is generally the one who is willing to do and dare. - Dale Carnegie',
     'Time makes more converts than reason. - Thomas Paine',
     'Painting is just another way of keeping a diary. - Pablo Picasso',
     'Anyone who has never made a mistake has never tried anything new. - Albert Einstein',
     'Sacred cows make the best hamburger. - Mark Twain',
     'We have to make America the best place in the world to do business. - Dick Cheney',
     'Love yourself first and everything else falls into line. You really have to love yourself to get anything done in this world. - Lucille Ball',
     'As Mankind becomes more liberal, they will be more apt to allow that all those who conduct themselves as worthy members of the community are equally entitled to the protections of civil government. I hope ever to see America among the foremost nations of justice and liberality. - George Washington',
     'Many who seem to be struggling with adversity are happy; many, amid great affluence, are utterly miserable. - Tacitus',
     'I wake each morning torn between the desire to improve the world and the desire to enjoy it. It makes it hard to plan the day. - E.B. White',
     'Worry is interest paid on trouble before it falls due. - W. R. Inge',
     'Games lubricate the body and the mind. - Benjamin Franklin',
     'The surface of American society is covered with a layer of democratic paint, but from time to time one can see the old aristocratic colours breaking through. - Alexis de Tocqueville',
     'The commonest thing is delightful if only one hides it. - Oscar Wilde',
     'That is the true season of love, when we believe that we alone can love, that no one could ever have loved so before us, and that no one will love in the same way after us. - Johann Wolfgang von Goethe',
     'I`ve been accused of vulgarity. I say that`s bullshit. - Mel Brooks',
     'Journalism is literature in a hurry. - Matthew Arnold',
     'Man [has] always assumed that he was more intelligent than dolphins because he had achieved so much-the wheel, New York, wars and so on-while all the dolphins had ever done was muck about in the water having a good time. But conversely, the dolphins had always believed that they were far more intelligent than man-for precisely the same reason. - Douglas Adams',
     'You can`t teach an old dogma new tricks. - Dorothy Parker',
     'If you will not fight for the right when you can easily win without bloodshed; if you will not fight when your victory will be sure and not too costly; you may come to the moment when you will have to fight with all the odds against you and only a small chance of survival. There may even be a worse case: you may have to fight when there is no hope of victory, because it is better to perish than to live as slaves. - Winston Churchill',
     'The best defense against usurpatory government is an assertive citizenry. - William F. Buckley',
     'Cowards die many times before their deaths. The valiant never taste of death but once. - William Shakespeare',
     'It is astonishing what an effort it seems to be for many people to put their brains definitely and systematically to work. - Thomas Edison',
     'Liberty exists in proportion to wholesome restraint. - Daniel Webster',
     'To be what we are, and to become what we are capable of becoming, is the only end of life. - Robert Louis Stevenson',
     'I honestly think it is better to be a failure at something you love than to be a success at something you hate. - George Burns',
     'The power of accurate observation is commonly called cynicism by those who have not got it. - George Bernard Shaw',
     'Question with boldness even the existence of a God; because, if there be one, he must more approve of the homage of reason, than that of blind-folded fear. - Thomas Jefferson',
     'We are never deceived; we deceive ourselves. - Johann Wolfgang von Goethe',
     'Government is not a solution to our problem, government is the problem. - Ronald Reagan']



(b) Words from full quotes (5 points).


```python
def words(quote):
    quote=quote.lower()
    w=re.split('\W+',quote)
    return w

print words(pool[0])
```

    ['how', 'we', 'spend', 'our', 'days', 'is', 'of', 'course', 'how', 'we', 'spend', 'our', 'lives', 'annie', 'dillard']
    

(c) Build the postings-list dictionary (6 points).


```python
postings_list={}
for quote in pool:
    word=words(quote)
    count={}
    for j in word:
        if j in count:
            count[j]+=1
        else:
            count[j]=1
    postings_list[quote]=count
    
postings_list[pool[0]]
```




    {'annie': 1,
     'course': 1,
     'days': 1,
     'dillard': 1,
     'how': 2,
     'is': 1,
     'lives': 1,
     'of': 1,
     'our': 2,
     'spend': 2,
     'we': 2}



(d) Build the reverse postings-list dictionary (6 points).


```python
reverse_postings_list={}
for quote in pool:
    word=words(quote)
    count={}
    for j in word:
        if j in count:
            count[j]+=1
        else:
            count[j]=1
    for w in word:
        if w not in reverse_postings_list:
            reverse_postings_list[w]={}
            reverse_postings_list[w][quote]=count[w]
        else:
            reverse_postings_list[w][quote]=count[w]
            
reverse_postings_list['entertainer']
```




    {'An actor is at most a poet and at least an entertainer. - Marlon Brando': 1}



(e) Write a TF-IDF function (8 points).


```python
def TF_IDF(quote,w):
    word=words(quote)
    count={}
    for j in word:
        if j in count:
            count[j]+=1
        else:
            count[j]=1
    v=[]
    for c in count:
        v.append(count[c])
    TF=1.0*count[w]/max(v)
    IDF=math.log(int(len(pool))/int(len(reverse_postings_list[w])))
    TFIDF=TF*IDF
    return TFIDF

print TF_IDF(pool[16],'entertainer')
```

    3.3933584753
    

(f) Quote search using a single word (5 points).


```python
def single(word):
    temp=reverse_postings_list[word]
    for each in temp:
        temp[each]=TF_IDF(each,word)
    return temp

print single('road')
```

    {'This does not mean that the enemy is to be allowed to escape. The object is to make him believe that there is a road to safety, and thus prevent his fighting with the courage of despair. After that, you may crush him. - Sun Tzu': 1.421743839084955, 'We all want progress, but if you`re on the wrong road, progress means doing an about-turn and walking back to the right road; in that case, the man who turns back soonest is the most progressive. - C.S. Lewis': 2.84348767816991, 'If you see ten troubles coming down the road, you can be sure that nine will run into the ditch before they reach you. - Calvin Coolidge': 1.8956584521132733}
    

(g) Quote search using multiple words (5 points).


```python
def multiple(wordlist):
    dic2={}
    for w in wordlist:
        temp=single(w)
        for each in temp:
            if each not in dic2:
                dic2[each]=temp[each]
            else:
                dic2[each]+=temp[each]
    return dic2

print multiple(['entertainer','poet'])
```

    {'My role in society, or any artist`s or poet`s role, is to try and express what we all feel. Not to tell people how to feel. Not as a preacher, not as a leader, but as a reflection of us all. - John Lennon': 2.0311899233483786, 'An actor is at most a poet and at least an entertainer. - Marlon Brando': 6.440143360325108}
    