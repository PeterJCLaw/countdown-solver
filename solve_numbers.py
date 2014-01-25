
from operator import add, mul, sub, div
from sympy import symbols

TARGET = 42
NUMBERS = [1,2,2,3,6,6]

def build_combos(main, prefix = []):
    combos = []

    if len(main) == 0:
        combos += [prefix]

    for i in xrange(len(main)):
        main_clone = main[:]
        prefix_clone = prefix[:]
        prefix_clone += [main_clone.pop(i)]
        combos += build_combos(main_clone, prefix_clone)

    return combos

def build_combos_any(items, depth, prefix = []):
    combos = []

    if len(prefix) > 0:
        combos += [prefix]

    if depth:
        for item in items:
            items_clone = items[:]
            prefix_clone = prefix[:]
            prefix_clone += [item]
            combos += build_combos_any(items_clone, depth - 1, prefix_clone)

    return combos

def test_combo_in(expr, nc):
    res = expr
    for i in xrange(len(letters)):
        l = letters[i]
        val = nc[i]
        res = res.subs(l, val)

    if res != TARGET:
        return False

    as_string = str(expr)
    for i in xrange(len(letters)):
        l = str(letters[i])
        val = str(nc[i])
        as_string = as_string.replace(l, val)

    print "Answer:", as_string
    return True


print 'Target:', TARGET
print 'Numbers:', NUMBERS

number_combos = build_combos(NUMBERS)
#print "\n".join(str(c) for c in number_combos)

operators = [add, mul, sub, div]
operator_combos = build_combos_any(operators, len(NUMBERS) - 1)

#print "\n".join(str([op.__name__ for op in oc]) for oc in operator_combos)

letters = symbols(' '.join('a{}'.format(i) for i in xrange(len(NUMBERS))))

#x = build_combos_any(letters, 2)
#print "\n".join(str(c) for c in x)

for oc in operator_combos:
    expr = letters[0]
    for i in xrange(len(oc)):
        op = oc[i]
        expr = op(expr, letters[i+1])

        for nc in number_combos:
            if test_combo_in(expr, nc):
                #print expr
                exit()
