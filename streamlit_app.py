import streamlit as st

st.markdown(
    "<br><p style='font-size:24px; font-weight:bold;'>Are you curious about the job market dynamics in the Kingdom?</p>"
    "<p>This analysis uncovers the key trends shaping job opportunities across different regions, gender preferences, salary expectations, and experience levels.</p>",
    "<br><br>" 
    unsafe_allow_html=True
)


st.markdown(
    "<p>In the Kingdom, the distribution of job postings reveals some interesting trends. As depicted in chart below, Riyadh dominates the job market, accounting for a significant 42.8% of the opportunities, followed by Makkah, which holds 24.8% of the postings. Other regions and the Eastern Province also contribute to the job landscape, though to a lesser extent.</p>",
    "<br><br>" 
    unsafe_allow_html=True
)
st.image('Image1.png', caption='Screenshot 1')


st.markdown(
    "<p>Moving forward, the chart below highlights the gender preferences associated with these job postings. It becomes apparent that while a substantial 39.5% of the jobs are open to both genders, there is still a noticeable bias, with 32.7% of positions favoring males and 27.8% favoring females.</p>",
    "<br><br>" 
    unsafe_allow_html=True
)
st.image('image2.png', caption='Screenshot 2')


st.markdown(
    "<p>Delving into the financial aspect, the chart below provides insight into the expected salary range for fresh graduates. The majority of positions offer a starting salary of around 4,000 SAR, with only a few roles extending into higher salary brackets, reflecting the entry-level nature of these opportunities.</p>",
    "<br><br>" 
    unsafe_allow_html=True
)
st.image('Image3.png', caption='Screenshot 3')


st.markdown(
    "<p>Lastly, this chart sheds light on the experience level sought by employers. A striking 800 job postings are aimed at fresh graduates with no prior experience, while experienced professionals are considered for just over 600 positions, underscoring the demand for fresh talent in the Kingdom’s job market.</p>",
    "<br><br>" 
    unsafe_allow_html=True
)
st.image('Image4.png', caption='Screenshot 4')

