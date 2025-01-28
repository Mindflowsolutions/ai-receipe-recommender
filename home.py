import streamlit as st

def app():
    # Add background image with a blur effect using CSS
    st.markdown(
        """
        <style>
        /* Set the background image and apply blur only to the image */
        .stApp {
            background: url('https://wallpapers.com/images/hd/food-4k-spdnpz7bhmx4kv2r.jpg') no-repeat center center;
            background-size: cover;
            height: 100vh;  /* Ensure it takes full height */
            position: relative;
            overflow: hidden;
            filter: blur(0px);  /* Apply blur to the background image */
        }

        /* Style for the title with a glass frame */
        .glass-title {
            margin-top: 200px;   
            background: rgba(255, 255, 255, 0.1);  /* White background with opacity */
            border-radius: 10px;
            padding: 20px;
            backdrop-filter: blur(10px);  /* Apply blur effect to create a glass-like appearance */
            text-align: center;
            font-size: 3rem;
            font-weight: bold;
            color: white;
            position: relative;
            z-index: 1;  /* Ensure title appears above the blurred background */
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        }


        </style>
        """,
        unsafe_allow_html=True
    )

    # Streamlit Title inside a glass frame
    st.markdown('<div class="glass-title">AI Recipe Recommender</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    app()
