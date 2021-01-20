"""
Constant variables
"""
DESC = 'desc'
MOVES = 'moves'
SUCCESS = 'success'
FAIL = 'fail'
DC = 'dc'
NEWPOSITION = 'new position'
ENEMYPOS = 'enemy position'
IMAGE = 'image'

globalPositions = {
    'Bottom Back Mount': {DESC: 'Your opponent has gotten your back! This is the strongest position for your opponent '
                                'and the worst one for you, and you must fight to survive.',
                          MOVES: ['Escape to Bottom Mount'],
                          IMAGE: 'Images/backmount.jpg'},
    'Bottom Mount': {DESC: 'Your opponent has mounted you! You are now in full defense mode, and must make sure to '
                           'keep your elbows in, and fight your way out.',
                     MOVES: ['Recover Half-Guard', 'Kip and Roll'],
                     IMAGE: 'Images/mount.jpg'},
    'Bottom Side Mount': {DESC: 'You are in bottom side control, with your opponent controlling your head and arm and '
                                'their knees beside your head and hip. This position is not immediately deadly, '
                                'but you must recover a guard quickly!',
                          MOVES: ['Recover Half-Guard', 'Recover Closed-Guard'],
                          IMAGE: 'Images/sidemount.jpg'},
    'Bottom Half-Guard': {DESC: 'You are in bottom half-guard, with your opponent on top of you and your legs '
                                'trapping one of his. This can be an equal position, with attacking opportunities for'
                                ' you and your opponent!',
                          MOVES: ['Kimura', 'Guillotine', 'Recover Closed-Guard', 'John Wayne Sweep'],
                          IMAGE: 'Images/halfguard.jpg'},
    'Bottom Closed Guard': {DESC: 'You are in bottom closed guard, where you are on your back and you have your legs '
                                  'locked around your kneeling opponent. Your opponent must break your guard to '
                                  'initiate his offense, while you can threaten him with submissions and sweeps. '
                                  'Attack your opponent!',
                            MOVES: ['Kimura', 'Hip-Bump Sweep', 'Triangle'],
                            IMAGE: 'Images/closedguard.jpg'},
    'Top Closed Guard': {DESC: 'You are in top closed guard, where you are kneeling and your opponent has their legs '
                               'wrapped around you. You must break this guard and pass to a safer attacking '
                               'position.',
                         MOVES: ['Pass to Half-Guard', 'Pass to Side Mount'],
                         IMAGE: 'Images/closedguard.jpg'},
    'Top Half-Guard': {DESC: 'You are in top half guard, with you kneeling over your prone opponent, who has one of '
                             'your legs locked between their legs. This position can be dangerous for both parties! '
                             'Pass quickly, or threaten with submissions.',
                       MOVES: ['Pass to Side Mount', 'Guillotine', 'Kimura', 'Pass to Mount'],
                       IMAGE: 'Images/halfguard.jpg'},
    'Top Side Mount': {DESC: 'You are in top side mount, where you have passed your opponent\'s legs, and have '
                             'tightly clasped their head and arm to control their upper body, your knees beside your '
                             'opponents head and hip. There are not many attacking options from here, '
                             'so keep advancing to a better position! ',
                       MOVES: ['Pass to Mount', 'Take the Back'],
                       IMAGE: 'Images/sidemount.jpg'},
    'Top Mount': {DESC: 'You are in top mount, with you on top of your opponent, your knees on either side of their '
                        'torso. This is one of the premium positions in Brazilian Jiu Jitsu, and you can attack '
                        'freely here, while making sure to keep balanced.',
                  MOVES: ['Armbar', 'Triangle', 'Kimura', 'Take the Back'],
                  IMAGE: 'Images/mount.jpg'},
    'Top Back Mount': {DESC: 'You have taken the opponent\'s back, and have clasped your hands around their torso, '
                             'with your legs wrapped around their waist. Your opponent has no offense here, '
                             'so attack them until they submit!',
                       MOVES: ['Rear Naked Choke', 'Armbar', 'Triangle'],
                       IMAGE: 'Images/backmount.jpg'},
    'Submission': {DESC: 'You have achieved a submission!',
                   MOVES: [],
                   IMAGE: 'Images/victory.jpg'},
    'Submitted': {DESC: 'You have been submitted!',
                  MOVES: [],
                  IMAGE: 'Images/victory.jpg'}
}

globalMoves = {
    'Escape to Bottom Mount': {SUCCESS: ' managed to escape their way to bottom mount!',
                               FAIL: ' failed the escape!',
                               NEWPOSITION: 'Bottom Mount',
                               ENEMYPOS: 'Top Mount',
                               DC: 15},
    'Recover Half-Guard': {SUCCESS: ' recovered half-guard!',
                           FAIL: ' failed to recover half-guard!',
                           NEWPOSITION: 'Bottom Half-Guard',
                           ENEMYPOS: 'Top Half-Guard',
                           DC: 10},
    'Kip and Roll': {SUCCESS: ' swept them!',
                     FAIL: ' failed the sweep!',
                     NEWPOSITION: 'Top Closed Guard',
                     ENEMYPOS: 'Bottom Closed Guard',
                     DC: 12},
    'Recover Closed-Guard': {SUCCESS: ' recovered closed-guard!',
                             FAIL: ' failed to recover!',
                             NEWPOSITION: 'Bottom Closed Guard',
                             ENEMYPOS: 'Top Closed Guard',
                             DC: 12},
    'Kimura': {SUCCESS: ' submitted their opponent with a kimura lock!',
               FAIL: ' failed to submit their opponent!',
               NEWPOSITION: 'Submission',
               ENEMYPOS: 'Submitted',
               DC: 10},
    'Guillotine': {SUCCESS: ' submitted their opponent with a guillotine!',
                   FAIL: ' failed to submit their opponent!',
                   NEWPOSITION: 'Submission',
                   ENEMYPOS: 'Submitted',
                   DC: 10},
    'John Wayne Sweep': {SUCCESS: ' swept their opponent!',
                         FAIL: ' failed to sweep their opponent!',
                         NEWPOSITION: 'Top Half-Guard',
                         ENEMYPOS: 'Bottom Half-Guard',
                         DC: 12},
    'Hip-Bump Sweep': {SUCCESS: ' swept their opponent!',
                       FAIL: ' failed to sweep their opponent!',
                       NEWPOSITION: 'Top Mount',
                       ENEMYPOS: 'Bottom Mount',
                       DC: 12},
    'Triangle': {SUCCESS: ' submitted their opponent with a triangle!',
                 FAIL: ' failed to submit their opponent!',
                 NEWPOSITION: 'Submission',
                 ENEMYPOS: 'Submitted',
                 DC: 10},
    'Pass to Half-Guard': {SUCCESS: ' passed their opponent\'s guard!',
                           FAIL: ' failed to pass their opponent!',
                           NEWPOSITION: 'Top Half-Guard',
                           ENEMYPOS: 'Bottom Half-Guard',
                           DC: 10},
    'Pass to Side Mount': {SUCCESS: ' passed their opponent\'s guard!',
                           FAIL: ' failed to pass their opponent!',
                           NEWPOSITION: 'Top Side Mount',
                           ENEMYPOS: 'Bottom Side Mount',
                           DC: 10},
    'Pass to Mount': {SUCCESS: ' passed their opponent\'s guard',
                      FAIL: ' failed to pass their opponent!',
                      NEWPOSITION: 'Top Mount',
                      ENEMYPOS: 'Bottom Mount',
                      DC: 10},
    'Take the Back': {SUCCESS: ' has taken the back of their opponent!',
                      FAIL: ' failed to take the back of their opponent!',
                      NEWPOSITION: 'Top Back Mount',
                      ENEMYPOS: 'Bottom Back Mount',
                      DC: 8},
    'Armbar': {SUCCESS: ' submitted their opponent with an armbar!',
               FAIL: ' failed to submit their opponent!',
               NEWPOSITION: 'Submission',
               ENEMYPOS: 'Submitted',
               DC: 8},
    'Rear Naked Choke': {SUCCESS: ' submitted their opponent with a rear-naked choke!',
                         FAIL: ' failed to submit their opponent!',
                         NEWPOSITION: 'Submission',
                         ENEMYPOS: 'Submitted',
                         DC: 8},
}
