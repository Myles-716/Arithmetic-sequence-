import streamlit as st

def generate_arithmetic_sequence(first_term, common_difference, num_terms):
    """
    Generate an arithmetic sequence given the first term, common difference, and number of terms.
    
    Args:
        first_term (float): The first term of the sequence
        common_difference (float): The common difference between consecutive terms
        num_terms (int): The number of terms to generate
    
    Returns:
        list: A list containing the arithmetic sequence
    """
    sequence = []
    for n in range(num_terms):
        term = first_term + (n * common_difference)
        sequence.append(term)
    return sequence

def main():
    # Set page title and header
    st.set_page_config(
        page_title="Arithmetic Sequence Generator",
        page_icon="🔢",
        layout="centered"
    )
    
    st.title("🔢 Arithmetic Sequence Generator")
    st.markdown("Generate and visualize arithmetic sequences with custom parameters")
    
    # Educational section about arithmetic sequences
    with st.expander("📚 What is an Arithmetic Sequence?"):
        st.markdown("""
        An **arithmetic sequence** is a sequence of numbers where the difference between 
        consecutive terms is constant. This difference is called the **common difference**.
        
        **Formula:** `aₙ = a₁ + (n-1) × d`
        
        Where:
        - `aₙ` = nth term
        - `a₁` = first term
        - `d` = common difference
        - `n` = term position
        
        **Example:** 2, 5, 8, 11, 14... (first term = 2, common difference = 3)
        """)
    
    # Create input section
    st.header("📝 Input Parameters")
    
    # Create three columns for better layout
    col1, col2, col3 = st.columns(3)
    
    with col1:
        first_term = st.number_input(
            "First Term (a₁)",
            value=1.0,
            step=0.1,
            format="%.2f",
            help="The starting number of your sequence"
        )
    
    with col2:
        common_difference = st.number_input(
            "Common Difference (d)",
            value=1.0,
            step=0.1,
            format="%.2f",
            help="The constant difference between consecutive terms"
        )
    
    with col3:
        num_terms = st.number_input(
            "Number of Terms (n)",
            min_value=1,
            max_value=1000,
            value=10,
            step=1,
            help="How many terms to generate (max: 1000)"
        )
    
    # Input validation and warnings
    if num_terms > 100:
        st.warning("⚠️ Generating more than 100 terms may take a moment to display.")
    
    # Generate and display the sequence
    if st.button("🚀 Generate Sequence", type="primary"):
        try:
            # Generate the arithmetic sequence
            sequence = generate_arithmetic_sequence(first_term, common_difference, num_terms)
            
            # Display results section
            st.header("📊 Results")
            
            # Show the formula with actual values
            st.subheader("Formula Used:")
            st.latex(f"a_n = {first_term} + (n-1) \\times {common_difference}")
            
            # Display sequence information
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("First Term", f"{first_term}")
            with col2:
                st.metric("Last Term", f"{sequence[-1]}")
            with col3:
                st.metric("Common Difference", f"{common_difference}")
            with col4:
                st.metric("Total Terms", f"{num_terms}")
            
            # Display the sequence
            st.subheader("Generated Sequence:")
            
            # For better readability, display differently based on sequence length
            if num_terms <= 20:
                # Display as a horizontal list for short sequences
                sequence_str = ", ".join([f"{term:.2f}" if term != int(term) else str(int(term)) for term in sequence])
                st.code(sequence_str, language=None)
            else:
                # Display as a table for longer sequences
                # Create a more compact table view
                import math
                cols_per_row = 10
                rows_needed = math.ceil(num_terms / cols_per_row)
                
                st.markdown("*Displaying in table format for better readability:*")
                
                for row in range(rows_needed):
                    start_idx = row * cols_per_row
                    end_idx = min(start_idx + cols_per_row, num_terms)
                    row_data = sequence[start_idx:end_idx]
                    
                    # Create columns for this row
                    row_cols = st.columns(len(row_data))
                    for i, term in enumerate(row_data):
                        with row_cols[i]:
                            term_num = start_idx + i + 1
                            formatted_term = f"{term:.2f}" if term != int(term) else str(int(term))
                            st.metric(f"a₍{term_num}₎", formatted_term)
            
            # Additional sequence properties
            with st.expander("📈 Sequence Properties"):
                sequence_sum = sum(sequence)
                st.markdown(f"""
                **Sequence Properties:**
                - **Sum of all terms:** {sequence_sum:.2f}
                - **Average value:** {sequence_sum/num_terms:.2f}
                - **Range:** {min(sequence):.2f} to {max(sequence):.2f}
                - **Is increasing:** {'Yes' if common_difference > 0 else 'No' if common_difference < 0 else 'Constant'}
                """)
            
            # Download option for large sequences
            if num_terms > 10:
                sequence_text = "\n".join([f"Term {i+1}: {term}" for i, term in enumerate(sequence)])
                st.download_button(
                    label="📥 Download Sequence as Text File",
                    data=sequence_text,
                    file_name=f"arithmetic_sequence_{first_term}_{common_difference}_{num_terms}.txt",
                    mime="text/plain"
                )
                
        except Exception as e:
            st.error(f"❌ An error occurred while generating the sequence: {str(e)}")
    
    # Add some examples
    st.header("💡 Try These Examples")
    
    examples_col1, examples_col2, examples_col3 = st.columns(3)
    
    with examples_col1:
        if st.button("Even Numbers", help="First term: 2, Difference: 2"):
            st.session_state.update({
                'first_term': 2.0,
                'common_difference': 2.0,
                'num_terms': 10
            })
            st.rerun()
    
    with examples_col2:
        if st.button("Counting by 5s", help="First term: 5, Difference: 5"):
            st.session_state.update({
                'first_term': 5.0,
                'common_difference': 5.0,
                'num_terms': 10
            })
            st.rerun()
    
    with examples_col3:
        if st.button("Decreasing Sequence", help="First term: 100, Difference: -7"):
            st.session_state.update({
                'first_term': 100.0,
                'common_difference': -7.0,
                'num_terms': 15
            })
            st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown("*Built with Streamlit • Perfect for educational and mathematical purposes*")

if __name__ == "__main__":
    main()
