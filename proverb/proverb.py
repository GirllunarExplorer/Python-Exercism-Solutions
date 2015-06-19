__author__ = 'tracyrohlin'

# For want of a nail the shoe was lost.
# For want of a shoe the horse was lost.
# For want of a horse the rider was lost.
# For want of a rider the message was lost.
# For want of a message the battle was lost.
# For want of a battle the kingdom was lost.
# And all for the want of a horseshoe nail.

def proverb(prov_list, qualifier=None):
    proverb_s = ""
    for i in range(len(prov_list)-1):
        proverb_s += 'For want of a {0} the {1} was lost.\n'.format(prov_list[i], prov_list[i+1])
    if not qualifier:
        qualifier = ""
    else:
        qualifier = qualifier+" "
    end_line = 'And all for the want of a %(qual)s%(original)s.' % {"qual":qualifier, "original":prov_list[0]}
    return proverb_s + end_line

print proverb(['nail', 'shoe', 'horse', 'rider',
                'message', 'battle', 'kingdom'],qualifier='horseshoe')