mids = {}
reduced_corp = []

A = 'a'
B = 'b'
C = 'c'
D = 'd'
E = 'e'
F = 'f'
G = 'g'
H = 'h'
I = 'i'
J = 'j'
K = 'k'
L = 'l'
M = 'm'
N = 'n'
O = 'o'
P = 'p'
Q = 'q'
R = 'r'
S = 's'
T = 't'
U = 'u'
V = 'v'
W = 'w'
X = 'x'
Y = 'y'
Z = 'z'

corp = [[G, O, L],
        [C, K, [B, E, R]],
        [K, O, [V, W]],
        [[H, M, N], N, G],
        [M, G, R],
        [D, I, [O, Q]],
        [L, L, [E, B, F, P, R]],
        [L, K, [E, B]],
        [E, L, [O, Q]],
        [F, O, R],
        [K, E, S],
        [[H, M, N, I], G, G],
        [S, T, [B, E, H]],
        [S, T, [H, B, E, R]],
        [U, A, [N, M]],
        [E, T, [R, B, H, E]],
        [F, R, N],
        [M, G, R],
        [E, C, K],
        [U, E, Z],
        [L, D, [D, I, R, M, N]],
        [H, A, M],
        [U, A, C],
        [L, W, A],
        [A, R, R],
        [G, R, S],
        [B, O, K],
        [E, C, K],
        [R, D, R],
        [L, L, [E, F, P, R]],
        [E, L, L],
        [E, S, D],
        [L, O, U],
        [E, L, O],
        [E, O, U],
        [P, O, L],
        [B, O, K],
        [C, A, R],
        [R, L, L],
        [N, E, L],
        [E, F, [O, Q, C]],
        [K, E, [O, C, Q]],
        [A, M, G],
        [B, E, O],
        [A, E, [H, P, R]],
        [G, R, S],
        [L, K, [H, B, R]],
        [R, R, L],
        [G, F, L],
        [M, G, R],
        [L, W, A],
        [E, L, L],
        [[I, M, H], N, G],
        [O, L, D],
        [A, N, [E, F, H]],
        [T, E, R],
        [K, E, T],
        [S, T, [E, P, R, B]],
        [E, R, D],
        [R, S, H],
        [O, L, K],
        [E, C, K],
        [D, R, [E, B]],
        [L, L, [E, B, H]],
        [F, O, R],
        [E, N, [P, F]],
        [G, R, O],
        [N, G, [P, F]],
        [B, O, K],
        [N, B, O],
        [O, L, W],
        [G, O, L],
        [R, S, T],
        [C, K, [E, B, H]],
        [K, E, I],
        [O, L, D],
        [K, E, O],
        [Z, E, N],
        [L, E, Y],
        [Y, H, [H, B, E]],
        [O, V, M],
        [M, G, R],
        [E, S, D],
        [R, S, T],
        [U, E, Z],
        [E, C, K],
        [E, I, [H, E]],
        [H, E, L],
        [N, G, R],
        [S, H, A],
        [F, L, E],
        [E, L, O],
        [L, K, [E, B, H]],
        [R, L, L],
        [I, E, R],
        [M, A, Q],
        [L, E, I],
        [R, N, Z],
        [G, R, S],
        [Q, W, [B, H, E]],
        [G, G, O],
        [P, O, L],
        [K, E, I],
        [L, C, A],
        [T, O, I],
        [L, L, [E, R, P, B]],
        [L, K, [B, E, H]],
        [R, O, I],
        [D, I, G],
        [O, R, S],
        [U, A, M],
        [F, O, R],
        [K, E, S],
        [L, P, O],
        [O, U, A],
        [A, R, R],
        [A, Q, U],
        [Z, M, A],
        [M, G, R],
        [E, O, U],
        [O, K, O],
        [R, E, R],
        [F, O, R],
        [R, E, I],
        [T, E, H],
        [A, N, E],
        [A, L, P],
        [L, I, N],
        [D, I, O],
        [E, L, L],
        [L, P, O],
        [G, R, S],
        [C, A, R],
        [U, A, O],
        [C, K, H],
        [O, L, I],
        [A, C, K],
        [L, L, C],
        [C, K, [H, B]],
        [R, N, Z],
        [K, E, [C, O]],
        [I, C, K],
        [F, R, N],
        [G, F, L],
        [N, Z, E],
        [B, E, C],
        [L, L, [B, H]],
        [L, K, [B, E, H]],
        [E, I, N],
        [W, A, I],
        [E, I, E],
        [I, C, K],
        [G, F, L],
        [E, F, O],
        [K, E, T],
        [A, M, G],
        [K, E, T],
        [A, M, G],
        [G, O, L],
        [L, I, N],
        [G, R, O],
        [N, G, R],
        [E, I, T],
        [O, L, K],
        [E, C, K],
        [I, C, K],
        [L, E, Y],
        [R, O, L],
        [D, I, G],
        [Y, H, [E, H]],
        [U, E, Z],
        [Q, U, [H, E]],
        [D, R, E],
        [R, E, R],
        [I, E, R],
        [H, A, M],
        [R, L, L],
        [E, T, H],
        [Z, E, N],
        [E, R, D],
        [E, T, [B, H]],
        [H, E, L],
        [L, L, O],
        [L, C, A],
        [A, C, K],
        [R, R, L],
        [M, A, Q],
        [M, G, R],
        [L, K, [H, E, B]],
        [E, F, O],
        [N, G, P],
        [G, R, O],
        [C, K, E],
        [E, I, E],
        [O, K, O],
        [T, O, I],
        [I, C, K],
        [G, G, O],
        [R, E, I],
        [P, O, I],
        [L, P, O],
        [W, A, I],
        [L, L, E],
        [A, M, G],
        [L, O, U],
        [I, N, G],
        [O, L, K]
]

reduced_corp = []

def append_item(item):
    letter = item[1]
    tri_set = mids.get(letter, None)
    if mids.get(letter, None):
        if item in tri_set:
            return
        mids[letter].append(item)
        return
    mids[letter] = [item]
    return


def is_list(i):
    return hasattr(i, '__iter__')


def is_item_confident(item):
    return not (is_list(item[0]) or is_list(item[2]))


def fuzzy_match_tail(item, center_matches):
    return filter(lambda i: i[:2] == item[:2], center_matches)\


def fuzzy_match_head(item, center_matches):
    return filter(lambda i: i[1:] == item[1:], center_matches)


def fuzzle_next(item, center_matches):
    return filter(lambda i: i[:2] == item[1:], center_matches)

if False:
    # build dictionary based on center letter
    for item in corp:
        append_item(item)

    for item in corp:
        if item not in reduced_corp:
            if is_item_confident(item):
                reduced_corp.append(item)
            else:
                # find close matches
                center_matches = mids[item[1]]
                matches = []
                if is_list(item[0]):
                    matches = filter(lambda i: i[1:] == item[1:], center_matches)
                if is_list(item[2]):
                    matches = filter(lambda i: i[:2] == item[:2], center_matches)
                if len(matches) == 1:
                    reduced_corp.append(item)
                else:
                    print('Item: ', item)
                    print('~~~~ other options ~~~~')
                    for m in matches:
                        print('match: {} in list already {}'.format(m, m in reduced_corp))
                    replace = raw_input('possible repeats found add {}? y, n: '.format(item))
                    if replace == 'y':
                        reduced_corp.append(item)
else:
    reduced_corp = [['g', 'o', 'l'], ['c', 'k', ['b', 'e', 'r']], ['k', 'o', ['v', 'w']], ['m', 'g', 'r'], ['l', 'k', ['e', 'b']], ['f', 'o', 'r'], ['k', 'e', 's'], [['h', 'm', 'n', 'i'], 'g', 'g'], ['s', 't', ['h', 'b', 'e', 'r']], ['u', 'a', ['n', 'm']], ['f', 'r', 'n'], ['e', 'c', 'k'], ['u', 'e', 'z'], ['l', 'd', ['d', 'i', 'r', 'm', 'n']], ['h', 'a', 'm'], ['u', 'a', 'c'], ['l', 'w', 'a'], ['a', 'r', 'r'], ['g', 'r', 's'], ['b', 'o', 'k'], ['r', 'd', 'r'], ['l', 'l', ['e', 'f', 'p', 'r']], ['e', 'l', 'l'], ['e', 's', 'd'], ['l', 'o', 'u'], ['e', 'l', 'o'], ['e', 'o', 'u'], ['p', 'o', 'l'], ['c', 'a', 'r'], ['r', 'l', 'l'], ['n', 'e', 'l'], ['e', 'f', ['o', 'q', 'c']], ['k', 'e', ['o', 'c', 'q']], ['a', 'm', 'g'], ['b', 'e', 'o'], ['a', 'e', ['h', 'p', 'r']], ['l', 'k', ['h', 'b', 'r']], ['r', 'r', 'l'], ['g', 'f', 'l'], [['i', 'm', 'h'], 'n', 'g'], ['o', 'l', 'd'], ['t', 'e', 'r'], ['k', 'e', 't'], ['e', 'r', 'd'], ['r', 's', 'h'], ['o', 'l', 'k'], ['e', 'n', ['p', 'f']], ['g', 'r', 'o'], ['n', 'b', 'o'], ['o', 'l', 'w'], ['r', 's', 't'], ['k', 'e', 'i'], ['k', 'e', 'o'], ['z', 'e', 'n'], ['l', 'e', 'y'], ['y', 'h', ['h', 'b', 'e']], ['o', 'v', 'm'], ['h', 'e', 'l'], ['n', 'g', 'r'], ['s', 'h', 'a'], ['f', 'l', 'e'], ['i', 'e', 'r'], ['m', 'a', 'q'], ['l', 'e', 'i'], ['r', 'n', 'z'], ['q', 'w', ['b', 'h', 'e']], ['g', 'g', 'o'], ['l', 'c', 'a'], ['t', 'o', 'i'], ['r', 'o', 'i'], ['d', 'i', 'g'], ['o', 'r', 's'], ['u', 'a', 'm'], ['l', 'p', 'o'], ['o', 'u', 'a'], ['a', 'q', 'u'], ['z', 'm', 'a'], ['o', 'k', 'o'], ['r', 'e', 'r'], ['r', 'e', 'i'], ['t', 'e', 'h'], ['a', 'n', 'e'], ['a', 'l', 'p'], ['l', 'i', 'n'], ['d', 'i', 'o'], ['u', 'a', 'o'], ['c', 'k', 'h'], ['o', 'l', 'i'], ['a', 'c', 'k'], ['l', 'l', 'c'], ['i', 'c', 'k'], ['n', 'z', 'e'], ['b', 'e', 'c'], ['e', 'i', 'n'], ['w', 'a', 'i'], ['e', 'i', 'e'], ['e', 'f', 'o'], ['e', 'i', 't'], ['r', 'o', 'l'], ['q', 'u', ['h', 'e']], ['d', 'r', 'e'], ['e', 't', 'h'], ['l', 'l', 'o'], ['n', 'g', 'p'], ['c', 'k', 'e'], ['p', 'o', 'i'], ['l', 'l', 'e'], ['i', 'n', 'g']]

# re-based on reduced corp
trips = {}
mids = {}
# build dictionary based on center letter
# build set of bottle objects with a next and previous and a used flag
for item in reduced_corp:
    append_item(item)
    trips[str(item)] = {'set': item, 'used': False, 'previous': None, 'Next': None}

i1 = reduced_corp[0]
center_matches = mids[i1[2]]
print fuzzle_next(i1, center_matches)