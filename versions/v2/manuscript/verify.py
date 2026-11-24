import json
import re
from fractions import Fraction
from itertools import product


def native_scan(word):
    output = []
    position = 0
    while position < len(word):
        if word.startswith('00', position):
            output.append('0101')
            position += 2
        elif word[position] == '1':
            output.append('011')
            position += 1
        else:
            output.append('0')
            position += 1
    return ''.join(output)


def regex_scan(word):
    return re.sub('00|1', lambda match: {'00': '0101', '1': '011'}[match[0]], word)


def matrix_product(left, right):
    return [[sum(first * second for first, second in zip(row, column))
             for column in zip(*right)] for row in left]


def matrix_sum(*matrices):
    return [[sum(matrix[row][column] for matrix in matrices)
             for column in range(3)] for row in range(3)]


def matrix_scale(matrix, coefficient):
    return [[coefficient * value for value in row] for row in matrix]


def polynomial(value):
    return value ** 3 - value ** 2 - 4 * value + 2


def greedy_code(word):
    letters = []
    position = 0
    while position < len(word):
        if word[position] == '1':
            letters.append('O')
            position += 1
        elif position + 1 < len(word):
            letters.append('D' if word[position + 1] == '0' else 'E')
            position += 2
        else:
            return ''.join(letters), 1
    return ''.join(letters), 0


def main():
    substitution = {'D': 'EE', 'E': 'DOO', 'O': 'EO'}
    encoding = {'D': '00', 'E': '01', 'O': '1'}
    native = regex = '00'
    ternary = 'D'
    lengths = [2, 4, 8]
    for index in range(3, 2001):
        lengths.append(lengths[index - 1] + 4 * lengths[index - 2] - 2 * lengths[index - 3])
    parity_words = {}
    for index in range(15):
        coded = ''.join(encoding[letter] for letter in ternary)
        assert native == regex == coded
        assert len(native) == lengths[index]
        parity_words[index % 2] = native
        native = native_scan(native)
        regex = regex_scan(regex)
        ternary = ''.join(substitution[letter] for letter in ternary)
    boundary_cases = 0
    for suffix_length in range(9):
        for number in range(2 ** suffix_length):
            suffix = format(number, f'0{suffix_length}b') if suffix_length else ''
            for letter in substitution:
                left = native_scan(encoding[letter] + suffix)
                right = ''.join(encoding[image] for image in substitution[letter]) + native_scan(suffix)
                assert left == right
                boundary_cases += 1
    for parity, word in parity_words.items():
        assert '000' not in word and '111' not in word
        zero_positions = [index + 1 for index, digit in enumerate(word) if digit == '0']
        one_positions = [index + 1 for index, digit in enumerate(word) if digit == '1']
        for index, position in enumerate(zero_positions, 1):
            assert index <= position <= 3 * index - 2
            ratio = Fraction(position, index)
            assert Fraction(7, 3) - ratio > -1
            assert Fraction(12, 5) - ratio < 2
        for index, position in enumerate(one_positions, 1):
            assert index <= position <= 2 * index + 1
            ratio = Fraction(position, index)
            assert Fraction(12, 7) - ratio > (-2 if parity == 0 else -1)
            assert Fraction(7, 4) - ratio < 1
        assert len(zero_positions) >= 10000 and len(one_positions) >= 10000
    incidence = [[0, 1, 0], [2, 0, 1], [0, 2, 1]]
    identity = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    square = matrix_product(incidence, incidence)
    cube = matrix_product(square, incidence)
    assert matrix_sum(cube, matrix_scale(square, -1), matrix_scale(incidence, -4),
                      matrix_scale(identity, 2)) == [[0] * 3 for row in range(3)]
    intervals = [(Fraction(-2), Fraction(-3, 2)), (Fraction(0), Fraction(1, 2)),
                 (Fraction(7, 3), Fraction(12, 5))]
    assert all(polynomial(lower) * polynomial(upper) < 0 for lower, upper in intervals)
    coefficients = [2, 2, -4]
    for index in range(2001):
        coefficient = lengths[index]
        if index >= 1:
            coefficient -= lengths[index - 1]
        if index >= 2:
            coefficient -= 4 * lengths[index - 2]
        if index >= 3:
            coefficient += 2 * lengths[index - 3]
        assert coefficient == (coefficients[index] if index < 3 else 0)
    count_sequences = {'zeros': [], 'ones': []}
    word = '00'
    for index in range(15):
        count_sequences['zeros'].append(word.count('0'))
        count_sequences['ones'].append(word.count('1'))
        word = native_scan(word)
    for values in count_sequences.values():
        for index in range(12):
            assert values[index + 3] == values[index + 2] + 4 * values[index + 1] - 2 * values[index]
    seed_cases = 0
    terminal_zero_cases = 0
    seed_parity_prefixes = 0
    for seed_length in range(9):
        for symbols in product('01', repeat=seed_length):
            seed = ''.join(symbols)
            coded_seed, terminal_zero = greedy_code(seed)
            assert ''.join(encoding[letter] for letter in coded_seed) + '0' * terminal_zero == seed
            seed_cases += 1
            terminal_zero_cases += terminal_zero
            native_seed = seed
            coded_word = coded_seed
            seed_lengths = []
            for index in range(8):
                coded_bits = ''.join(encoding[letter] for letter in coded_word) + '0' * terminal_zero
                assert native_seed == coded_bits
                seed_lengths.append(len(native_seed))
                native_seed = native_scan(native_seed)
                coded_word = ''.join(substitution[letter] for letter in coded_word)
            for index in range(5):
                assert seed_lengths[index + 3] == (seed_lengths[index + 2] + 4 * seed_lengths[index + 1]
                                                   - 2 * seed_lengths[index] - 2 * terminal_zero)
            for index in range(4):
                assert seed_lengths[index + 4] == (2 * seed_lengths[index + 3] + 3 * seed_lengths[index + 2]
                                                   - 6 * seed_lengths[index + 1] + 2 * seed_lengths[index])
            if not coded_seed:
                assert native_seed == seed
                continue
            for index in [8, 9]:
                reference_parity = index % 2 if coded_seed[0] in ['D', 'O'] else 1 - index % 2
                assert len(native_seed) >= 64
                assert native_seed[:64] == parity_words[reference_parity][:64]
                seed_parity_prefixes += 1
                native_seed = native_scan(native_seed)
    print(json.dumps({
        'arithmetic': 'integers and rational numbers',
        'native_regex_coding_agreement': {'first_index': 0, 'last_index': 14,
                                         'last_length': lengths[14]},
        'boundary_identity_cases': boundary_cases,
        'generating_function_coefficients': {'first_index': 0, 'last_index': 2000},
        'position_inequalities': {'even_iterate': 14, 'odd_iterate': 13,
                                 'range': 'every zero and one position in each stated finite iterate'},
        'cubic_matrix_identity': True,
        'three_disjoint_rational_root_intervals': [[str(lower), str(upper)] for lower, upper in intervals],
        'symbol_count_recurrences': {'first_index': 0, 'last_index': 14,
                                     'zeros_initial': count_sequences['zeros'][:3],
                                     'ones_initial': count_sequences['ones'][:3]},
        'arbitrary_seeds': {'seed_lengths': [0, 8], 'seeds': seed_cases,
                            'terminal_zero_seeds': terminal_zero_cases,
                            'coding_iterates': [0, 7], 'cubic_recurrence_start_indices': [0, 4],
                            'quartic_recurrence_start_indices': [0, 3],
                            'parity_comparisons': seed_parity_prefixes,
                            'parity_iterates': [8, 9], 'parity_prefix_length': 64},
        'scope': 'Finite checks supplement the all-index and limiting arguments in the note.'
    }, indent=2))


if __name__ == '__main__':
    main()
