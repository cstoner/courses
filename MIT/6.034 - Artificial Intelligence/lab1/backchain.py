from production import AND, OR, NOT, PASS, FAIL, IF, THEN, \
     match, populate, simplify, variables
from zookeeper import ZOOKEEPER_RULES

# This function, which you need to write, takes in a hypothesis
# that can be determined using a set of rules, and outputs a goal
# tree of which statements it would need to test to prove that
# hypothesis. Refer to the problem set (section 2) for more
# detailed specifications and examples.

# Note that this function is supposed to be a general
# backchainer.  You should not hard-code anything that is
# specific to a particular rule set.  The backchainer will be
# tested on things other than ZOOKEEPER_RULES.


def backchain_to_goal_tree(rules, hypothesis):
    matched_rules = []
    results = []

    for rule in rules:
        rule_str = rule.consequent()[0]
        if match(rule_str, hypothesis) is not None:
            res = match(rule_str, hypothesis)
            matched_rules.append(populate(rule.antecedent(), res))

    for m in matched_rules:
        if isinstance(m, AND):
            res = []
            for item in m:
                res.append(backchain_to_goal_tree(rules, item))
            results.append(AND(res))

        elif isinstance(m, OR):
            res = []
            for item in m:
                res.append(backchain_to_goal_tree(rules, item))
            results.append(OR(res))

        elif isinstance(m, str):
            results.append(backchain_to_goal_tree(rules, m))

        else:
            raise Exception, "Not sure what do do with object '{}'".format(m) 

    return simplify(OR([hypothesis] + results))

# Here's an example of running the backward chainer - uncomment
# it to see it work:
#print backchain_to_goal_tree(ZOOKEEPER_RULES, 'opus is a penguin') 
