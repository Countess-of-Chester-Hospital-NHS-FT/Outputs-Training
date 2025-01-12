import streamlit as st
import pandas as pd
import palmerpenguins
import matplotlib.pyplot as plt
import plotly.express as px

#st.balloons()
st.set_page_config(layout="wide", page_title="Penguins Dashboard")

st.title("Penguins Dashboard")

penguins_df = palmerpenguins.load_penguins()

island_select = st.selectbox("Please select an island",
                            options = penguins_df["island"].unique())

penguins_df = penguins_df[penguins_df["island"] == island_select]

col_1, col_2 = st.columns([0.7, 0.3])

with col_1:

    #another_df = st.file_uploader("Please upload a suitable csv",
                                    #type = ['csv'])
    #if uploaded_file is not None:
    st.dataframe(penguins_df,
                use_container_width=True,
                column_config = {
                    "year": st.column_config.NumberColumn(
                        "Year Collected",
                        format="%f"
                    )
                })

with col_2:
    penguin_scatter = px.scatter(
        penguins_df,
        x="bill_length_mm",
        y="bill_depth_mm",
        color = "species"
    )

    st.plotly_chart(
        penguin_scatter
    )

with st.expander("Click here for more information"):
    st.write("Wohoo! Go penguins")
    st.image("penguin.png")

tab1, tab2 = st.tabs(["Penguin species", "More penguin stuff"])

with tab1:
    st.plotly_chart(
        px.bar(
            penguins_df["species"].value_counts(),
            title = "Penguin species"
        )
    )

with tab2:
    st.write("Nothing to see")

# fig, ax = plt.subplots()

# plt.scatter(
#     x = penguins_df["bill_length_mm"],
#     y = penguins_df["flipper_length_mm"]
# )

# st.subheader("Method 1")

# st.pyplot(fig)

# plt.savefig("penguins.png")

# st.subheader("Method 2")

# st.image("penguins.png")

# #tells it which file to open
# with open("penguins.png", "rb") as img:
#     btn = st.download_button(
#         label = "Download image",
#         data = img,
#         file_name = "downloaded_img.png",
#         mime="image/png"
#     )

