import streamlit as st 

def app():
    st.title("About")

    # Glass Title
    st.markdown(
        """
        <style>
        .glass-title {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 20px;
            backdrop-filter: blur(10px);
            text-align: center;
            font-size: 2rem;
            font-weight: bold;
            color: white;
            width: 100%;
            margin: 0 auto 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        }
        .card {
            background: rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        }
        h3 {
            color: white;
        }
        p {
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display title
    st.markdown('<div class="glass-title">About Us</div>', unsafe_allow_html=True)

    # Creating columns for side-by-side layout
    col1, col2 = st.columns(2)

    # First Card
    with col1:
        st.markdown("""
        <div class="card">
            <h3>Mr Shahzad</h3>
            <p>Computer Science Student | Aspiring AI & Robotics Innovator | Passionate About Coding | Future Tech Entrepreneur</p>
        </div>
        """, unsafe_allow_html=True)

    # Second Card
    with col2:
        st.markdown("""
        <div class="card">
            <h3>Muhammad Abid</h3>
            <p>Frontend Developer | Video Editor | Graphic Designer</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    app()
