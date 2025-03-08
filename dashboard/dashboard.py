import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Judul aplikasi
st.title("Bike Rentals Analysis")
st.write("This web app is created to analyze bike rentals data and provide insights for bike rental companies. The Bike Sharing Analysis helps us understand how people use bike-sharing services, where users can rent a bike from one location and return it to another automatically. This dataset includes hourly bike rental data from the Capital Bikeshare system for the years 2011 and 2012, along with weather and seasonal information that may affect bike usage. By analyzing this data through Exploratory Data Analysis (EDA), we can find patterns and factors that influence bike rentals. Additionally, creating a prediction model will help estimate the number of bike rentals per hour (cnt), allowing for better planning and management of the bike-sharing system.")

# Load data
all_df = pd.read_csv('all_data.csv')
day_df = pd.read_csv('../data/day.csv')
hour_df = pd.read_csv('../data/hour.csv')

# Visualisasi 1: Jumlah Penyewa Sepeda Berdasarkan Bulan
st.subheader("Number of Bike Rentals by Month")
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(data=all_df, x="mnth", y="cnt", hue='yr', errorbar=None, palette=['lightblue', 'blue'], estimator=sum, ax=ax1)
ax1.legend(title='Year')
ax1.set_title("Number of Bike Rentals by Month")
ax1.set_xlabel("Month")
ax1.set_ylabel("Count of total rental bikes")
st.pyplot(fig1)
# Menambahkan tombol view analysis yang bila dipencet berisi komentar pada hasil visualisasi
# Bila tombol dipencet, maka akan muncul komentar pada hasil visualisasi
if st.button("View Analysis"):
    st.write("Jumlah penyewa sepeda meningkat di mulai pada bulan Maret hingga bulan Oktober. Hal tersebut terjadi karena bulan Maret adalah awal musim semi dan bulan Oktober adalah akhir musim panas sehingga cuaca yang cerah dan hangat membuat orang lebih banyak bersepeda. Jadi, kita dapat menambahkan jumlah sepeda pada bulan Maret hingga Oktober.")
    tutup = st.button("Close Analysis")
    if tutup:
        st.write("Analysis Closed")
        st.stop()


# Visualisasi 2a: Jumlah Penyewa Sepeda Berdasarkan Hari Kerja
st.subheader("Number of Bike Rentals by Working Day & Hour")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(data=day_df, x="workingday", y="cnt", hue="workingday", estimator=sum, palette=['lightblue', 'blue'], legend=False, ax=ax2)
ax2.set_title("Number of Bike Rentals by Working Day")
ax2.set_xlabel("Working Day")
ax2.set_ylabel("Count of total rental bikes")
st.pyplot(fig2)

# Visualisasi 2b: Jumlah Penyewa Sepeda Berdasarkan Jam
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.lineplot(data=hour_df, x="hr", y="cnt", estimator=sum, errorbar=None, color='blue', ax=ax3)
ax3.set_xticks(np.arange(0, 24, 5))
ax3.set_title("Number of Bike Rentals by Hour")
ax3.set_xlabel("Hour")
ax3.set_ylabel("Count of total rental bikes")
st.pyplot(fig3)
if st.button("View Analysis", key="analysis1"):
    st.write("Jumlah penyewa sepeda lebih banyak pada hari kerja dibandingkan dengan hari libur dan jumlah penyewa sepeda paling tinggi pada jam 8 pagi dan jam 5 sore. Hal ini terjadi karena sepeda dibutuhkan masyarakat untuk menuju tempat kerja dan banyak masyarakat yang pergi bekerja pada jam 8 pagi dan pulang dari tempat kerja jam 5 sore. Jadi, kita dapat menambahkan jumlah sepeda pada jam-jam tersebut.")
    tutup2 = st.button("Close Analysis", key="close1")
    if tutup2:
        st.write("Analysis Closed")
        st.stop()

# Visualisasi 3: Jumlah Penyewa Sepeda Berdasarkan Musim
st.subheader("Number of Bike Rentals by Season")
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.barplot(data=all_df, x="season", y="cnt", hue="season", errorbar=None, estimator=sum, palette=['lightblue', 'blue', 'lightgreen', 'green'], legend=False, ax=ax4)
ax4.set_title("Number of Bike Rentals by Season")
ax4.set_xlabel("Season")
ax4.set_ylabel("Count of total rental bikes")
st.pyplot(fig4)
if st.button("View Analysis", key="analysis2"):
    st.write("Jumlah penyewa sepeda paling tinggi pada musim summer dan fall. Hal ini mungkin terjadi karena masyarakat lebih nyaman menggunakan sepeda pada musim summer dan fall. Sehingga kita dapat menambahkan jumlah sepeda pada musim tersebut.")
    tutup2 = st.button("Close Analysis", key="close2")
    if tutup2:
        st.write("Analysis Closed")
        st.stop()

# Visualisasi 5: Jumlah Penyewa Sepeda Berdasarkan Cuaca
st.subheader("Number of Bike Rentals by Weather")
fig5, ax5 = plt.subplots(figsize=(10, 6))
sns.barplot(data=all_df, x="weathersit", y="cnt", hue="weathersit", errorbar=None, estimator=sum, palette=['lightblue', 'blue', 'lightgreen', 'green'], legend=False, ax=ax5)
ax5.set_title("Number of Bike Rentals by Weather")
ax5.set_xlabel("Weather")
ax5.set_ylabel("Count of total rental bikes")
st.pyplot(fig5)
if st.button("View Analysis", key="analysis3"):
    st.write("Jumlah penyewa sepeda paling tinggi pada cuaca cerah/clear. Hal ini terjadi karena masyarakat ingin menikmati cuaca yang cerah dengan bersepeda. Sehingga kita dapat menambahkan jumlah sepeda pada cuaca cerah.")
    tutup2 = st.button("Close Analysis", key="close3")
    if tutup2:
        st.write("Analysis Closed")
        st.stop()

# Menampilkan heatmap korelasi
st.subheader("Correlation between Temperature, Humidity, Windspeed, and Bike Rentals")
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(all_df[["temp", "atemp", "hum", "windspeed", "cnt"]].corr(), annot=True, cmap='coolwarm', ax=ax)
ax.set_title("Correlation between Temperature, Humidity, Windspeed, and Count")
st.pyplot(fig)
if st.button("View Analysis", key="analysis4"):
    st.write("Tidak ada korelasi yang signifikan antara suhu, kelembaban, kecepatan angin, dan jumlah penyewa sepeda. Suhu adalah faktor yang paling mempengaruhi jumlah penyewaan sepeda, tetapi pengaruhnya masih kecil. Kelembaban dan kecepatan angin tidak memiliki dampak yang signifikan terhadap jumlah penyewaan sepeda.Oleh karena itu, kita tidak perlu menambahkan jumlah sepeda berdasarkan suhu, kelembaban, dan kecepatan angin.")
    tutup2 = st.button("Close Analysis", key="close4")
    if tutup2:
        st.write("Analysis Closed")
        st.stop()

# Membuat komentar untuk analisis lanjutan
st.subheader("Further Analysis Based on Binning")

# Mengelompokkan data berdasarkan temp_bin, hum_bin, dan windspeed_bin, lalu menghitung jumlah cnt
top_5 = all_df.groupby(by=["temp_bin", "hum_bin", "windspeed_bin"], observed=True)["cnt"].sum().sort_values(ascending=False).head(5)

# Menampilkan chart batang untuk top 5
st.subheader("Top 5 Number of Bike Rentals by Temperature, Humidity, and Windspeed Bins")
fig, ax = plt.subplots(figsize=(10, 6))
top_5.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title("Top 5 Number of Bike Rentals by Temperature, Humidity, and Windspeed Bins")
ax.set_xlabel("Temperature, Humidity, and Windspeed Bins")
ax.set_ylabel("Count of total rental bikes")
ax.tick_params(axis='x', rotation=45)  # Memutar label sumbu x untuk keterbacaan yang lebih baik
st.pyplot(fig)

# Menampilkan data top 5 dalam tabel
st.subheader("Top 5 Data")
st.write(top_5.reset_index())  # Menampilkan data dalam bentuk tabel
if st.button("View Analysis", key="analysis5"):
    st.write("Jika diperhatikan, jumlah penyewa sepeda tertinggi terjadi pada kondisi cuaca panas, kelembaban tinggi, dan kecepatan angin sangat rendah. Hal ini terjadi karena cuaca panas membuat orang ingin bersepeda, kelembaban tinggi membuat orang merasa nyaman, dan kecepatan angin yang sangat rendah membuat orang tidak terganggu oleh angin.")
    tutup2 = st.button("Close Analysis", key="close5")
    if tutup2:
        st.write("Analysis Closed")
        st.stop()

# Tambahkan foto profil
st.sidebar.image("https://media.licdn.com/dms/image/v2/D5603AQEAMK_0-7FsFg/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1718414110140?e=1746662400&v=beta&t=qhrW4BZpg6dR4lKmdLOaRInGGjXhvzSwRHenm7zdiZg", width=75, use_column_width=True)

# Tambahkan founder dan contact info
st.sidebar.title("About")
st.sidebar.info(
    """
    This app is created by:
    - [Leonard Kumaro](https://www.linkedin.com/in/leonadkumaro/)
    """
)
st.sidebar.title("Contact")
st.sidebar.info(
    """
    For further information, please contact me via email:
    - [bkleonard174@gmail.com](mailto:bkleonard174@gmail.com)
    """
)
