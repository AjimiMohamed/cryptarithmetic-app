import streamlit as st
from simpleai.search import CspProblem, backtrack

def solve_cryptarithmetic(word1, word2, result):
    chars = set(word1 + word2 + result)
    variables = list(chars)
    domains = {}
    for var in variables:
        domains[var] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for word in [word1, word2, result]:
        first_letter = word[0]
        domains[first_letter] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def constraint_unique(variables, values):
        value_set = set(values)
        return len(value_set) == len(values)

    def constraint_add(variables, values):
        var_dict = {}
        for i in range(len(variables)):
            var_dict[variables[i]] = values[i]

        num1 = ""
        for char in word1:
            num1 += str(var_dict[char])
        num1 = int(num1)

        num2 = ""
        for char in word2:
            num2 += str(var_dict[char])
        num2 = int(num2)

        num3 = ""
        for char in result:
            num3 += str(var_dict[char])
        num3 = int(num3)

        return num1 + num2 == num3

    constraints = [
        (variables, constraint_unique),
        (variables, constraint_add),
    ]

    problem = CspProblem(variables, domains, constraints)

    output = backtrack(problem)

    return output

def main():
   
    

    st.markdown("# Cryptarithmetic Puzzle Solver :bulb:")

    # Create a sidebar for input widgets
    with st.sidebar:
        st.image("crypto.jpg")
        st.markdown("## Enter the words for the cryptarithmetic puzzle:")
        word1 = st.text_input("Enter the first word:")
        word2 = st.text_input("Enter the second word:")
        result = st.text_input("Enter the result word:")
        solve_button = st.button("Solve")

    # Display the solution on the main page
    if solve_button:
        solution = solve_cryptarithmetic(word1, word2, result)
        if solution:
            st.write("Solution found :smile:")
            st.balloons()
            equation = f"         {word1}\n+ {word2}\n{'-'*(max(len(word1), len(word2), len(result)) + 2)}\n{result}\n"

            # Construct the solution string
            word1_solution = ''.join([str(solution[char]) for char in word1])
            word2_solution = ''.join([str(solution[char]) for char in word2])
            result_solution = ''.join([str(solution[char]) for char in result])
            code_block = f"```\n{equation}\n  {word1_solution}\n+ {word2_solution}\n{'-'*(max(len(word1), len(word2), len(result)) + 2)}\n  {result_solution}\n```"

            st.markdown(code_block)

            # Display the letter-number mapping
            st.markdown("## Letter-Number Mapping:")
            for char, value in solution.items():
                st.write(f"{char} equals {value}")
        else:
            st.write("No solution found :sob:")


if __name__ == "__main__":
    main()