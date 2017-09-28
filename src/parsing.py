#!/usr/bin/env python3

import re

################################################################################
#                                File parser                                   #
################################################################################

################################## regexps #####################################

# Space_pattern = ' |\t|\n'
# #fact_regexp = '[A-Z]'
# atomic_predicate_regexp = '[_a-zA-Z][_a-zA-Z0-9]*'
# not_predicate_regexp = '(?P<not>!)'


# rule_regexp = '\w+(?P<p1>{predicate})\w+(?P<operator><?=>)\w+(?P<p2>{predicate})\w+'

space_regex = re.compile(' |\t|\n')

################################# functions ####################################

def clean_line(l):
    """
    clean_line() removes possible comments and space characters (using
    space_regex from global scope).
    """
    
    return space_regex.sub( # replace occurences by first argument
        '',
        l.split('#')[0])


def parse_rule(l):
    if l.find('<=>') != -1:
        p = l.split('<=>')
        if len(p) == 2:
            p1 = create_predicate(p[0])
            p2 = create_predicate(p[1])
            create_equivalence(p1, p2)
        else:
            raise Exception('Syntax error when parsing rule %r.' % l)
    elif l.find('=>') != -1:
        p = l.split('=>')
        if len(p) == 2:
            p1 = create_predicate(p[0])
            p2 = create_predicate(p[1])
            create_implication(p1, p2)
        else:
            raise Exception('Syntax error when parsing rule %r.' % l)
    else:
        raise Exception('Syntax error when parsing rule %r.' % l)


def parse_initial_facts(l):
    for letter in clean_line(l)[1:]:
        src.Predicates.AtomicPredicate(letter).set_initial_state()


def parse_queries(l):
    queries = set()
    for letter in clean_line(l)[1:]:
        queries.add(src.Predicates.AtomicPredicate(letter))
    return queries

        
def parse(filename):
    """
    parse() parses the file content, interprets rules and initial states, and
    returns queries.
    """

    AWAITING_RULES_STATE = 0
    RULES_STATE = 1
    AWAITING_FACTS_STATE = 2
    FACTS_STATE = 3
    AWAITING_QUERIES_STATE = 4
    QUERIES_STATE = 5
    ENDING_STATE = 6
    
    state = AWAITING_RULES_STATE = 0
    with open(filename) as f:
        for line in f:
            line = clean_line(line)
            if state == AWAITING_RULES_STATE:
                if line != '':
                    state = RULES_STATE
            if state == RULES_STATE:
                if line.startswith('?'):
                    state = QUERIES_STATE
                elif line.startswith('='):
                    state = FACTS_STATE
                elif line == 0:
                    state = AWAITING_FACTS_STATE
                else:
                    parse_rule(line)
            if state == AWAITING_FACTS_STATE:
                if line != '':
                    state = FACTS_STATE
            if state == FACTS_STATE:
                if not line.startswith('='):
                    raise Exception("Syntax error in file when parsing facts.")
                parse_initial_facts(line)
                state = AWAITING_QUERIES_STATE
                continue
            if state == AWAITING_QUERIES_STATE:
                if line != '':
                    state = QUERIES_STATE
            if state == QUERIES_STATE:
                if not line.startswith('?'):
                    raise Exception('Syntax error in file when parsing queries')
                queries = parse_queries(line)
                state = ENDING_STATE
                continue
            if state == ENDING_STATE:
                if line != '':
                    raise Exception('Syntax error in file when ending parsing')
        if state != ENDING_STATE:
            raise Exception("Syntax error in file : unexpected.")
    return queries


if __name__ == '__main__':
    pass
