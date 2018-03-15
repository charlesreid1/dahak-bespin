import random
import string


"""
Random Labels

Generate random labels for labeling
all the AWS assets
"""


def random_ip():
    """
    Return a random IP of the form
    10.*.0.0
    """
    block = random.randint(15,99)
    return "10.%d.0.{addr}"%(block)

def random_label():
    # Generate a random label to uniquely identify this group
    
    a1 = random.choices(string.ascii_lowercase,k=2)
    a2 = random.choices(string.digits,k=1)
    a3 = random.choices(string.ascii_lowercase,k=2)

    label = ''.join(a1+a2+a3)

    return label

