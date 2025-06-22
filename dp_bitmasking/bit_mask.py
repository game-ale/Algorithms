# mask basic in python
# on bit masking OPERATIONS
def set_bit(mask, pos):
    """Set the bit at position 'pos' to 1"""
    return mask | (1 << pos)

def clear_bit(mask, pos):
    """Clear the bit at position 'pos' (set to 0)"""
    return mask & ~(1 << pos)

def toggle_bit(mask, pos):
    """Flip/Toggle the bit at position 'pos'"""
    return mask ^ (1 << pos)

def check_bit(mask, pos):
    """Check if bit at position 'pos' is set (1)"""
    return (mask >> pos) & 1

def modify_bit(mask, pos, value):
    """Set bit at 'pos' to 'value' (0 or 1)"""
    mask = clear_bit(mask, pos)
    return mask | (value << pos)
def count_bits(mask):
    """Count the number of bits set to 1 in the mask"""
    count = 0
    while mask:
        count += mask & 1
        mask >>= 1
    return count   


def get_bit(mask, pos):
    """Get the bit at position 'pos'"""
    return (mask >> pos) & 1        
def get_mask(n):
    """Get a mask with n bits set to 1"""
    return (1 << n) - 1             

def get_mask_from_list(lst):
    """Get a mask from a list of positions"""
    mask = 0
    for pos in lst:
        mask = set_bit(mask, pos)
    return mask 
def get_list_from_mask(mask):
    """Get a list of positions where bits are set to 1"""
    lst = []
    pos = 0
    while mask:
        if mask & 1:
            lst.append(pos)
        mask >>= 1
        pos += 1
    return lst      
def get_mask_from_range(start, end):
    """Get a mask with bits set from 'start' to 'end' (inclusive)"""
    return ((1 << (end + 1)) - 1) ^ ((1 << start) - 1)      

def get_mask_from_range_exclusive(start, end):
    """Get a mask with bits set from 'start' to 'end' (exclusive)"""
    return ((1 << end) - 1) ^ ((1 << start) - 1) if start < end else 0
def get_mask_from_range_inclusive(start, end):
    """Get a mask with bits set from 'start' to 'end' (inclusive)"""
    return ((1 << (end + 1)) - 1) ^ ((1 << start) - 1) if start <= end else 0
