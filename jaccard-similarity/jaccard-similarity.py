def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    sa = set(set_a)
    sb = set(set_b)
    union = len(sa.union(sb))
    intersection = len(sa.intersection(sb))
    if not union:
        return 0.0
    return 1.0 * (intersection / union)