def isBST(current, min_range=minint, max_range=maxint):
    return (current.value > min_range and current.value < max_range)
    and isBST(current.left_child,
              min_range=min_range, max_range=current.value)
    and isBST(current.right_child,
              min_range=current.value, max_range=max_range)
