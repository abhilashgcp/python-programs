def count_universal(root):
    total_count, is_universal = is_universal_opti(root)
    return total_count

def is_universal_opti(root):
    if root == None:
        return 0,True
    left_unversal , left_count = is_universal_opti(root.left)
    right_unversal , right_count = is_universal_opti(root.right)
    is_universal = True
    if ()