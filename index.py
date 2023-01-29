
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
import io 
from sqlalchemy import create_engine
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns


# Koneksi kedatabase
user = 'root'
password = ''
host = '127.0.0.1'
port = 3306
database = 'mlearning'
def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )
engine = get_connection()

with st.sidebar:
    choose = option_menu("Menu", ["Home","Data Film", "Input Data", "Tentang"],
                         icons=['house', 'file-spreadsheet-fill', 'list', 'person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#f0f2f6"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#abdbe3"},
        "nav-link-selected": {"background-color": "#154c79","font-size":"20px"},
    }
    )

logo = Image.open(r'C:\Users\bpw\anaconda3\Project\logo.png')
anime = Image.open(r'C:\Users\bpw\anaconda3\Project\bag.png')
tentang = Image.open(r'C:\Users\bpw\anaconda3\Project\tentang.png')

if choose == "Home":
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:         
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Kelompok 5 Clustering | Machine Learning</p>', unsafe_allow_html=True)    
    with col2:
        st.image(logo, width=200 )
    st.markdown('<h3><b><br>Nama Kelompok : </h3></b><h5><br>Alfian Bagus <br> Aulia Rahmadhani <br> Mhd Anwar <br> Hartanto Situmorang <br> Yasmin Nadhifa</h5>', unsafe_allow_html=True)   
    st.image(anime, width=700)

elif choose == "Input Data":    
    title = st.text_input('Judul FLim', 'Input Judul')
    title1 = st.text_input('Bugdet', 'Input Bugdet')
    title2 = st.text_input('revenue', 'Input revenue')
    title3 = st.text_input('vote_count', 'Input Jumlah vote_count')
    title4 = st.text_input('vote_average', 'Input vote_average')
    title5 = st.text_input('Runtime', 'Input Runtime')  
    if st.button('Submit'):
        query="INSERT INTO  `flim` (`budget`, `revenue`, `runtime`, `vote_count`, `vote_average`, `title`) VALUES(%s,%s,%s,%s,%s,%s)"
        my_data=(title1,title2,title5,title3,title4,title)
        id=engine.execute(query,my_data)
        df = pd.read_sql_table('flim', engine)
        st.write(df.sort_values('id', ascending=False))
    else:
        st.write('*tekan enter ketika input')

elif choose == "Tentang":
    col1, col2 = st.columns( [0.8, 0.2])
    st.image(tentang, width=700)
    with col1:
        st.markdown(""" <style> .font {
        font-size:40px ; font-family: 'Cooper Black'; color: #042f66;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Clustering Flim<br>Dengan K-Means</p>', unsafe_allow_html=True)    

    st.markdown('<h5>K-means clustering adalah salah satu algoritma unsupervised learning yang termasuk ke dalam analisis klaster (cluster analysis) non hirarki yang digunakan untuk  mengelompokkan  data berdasarkan variabel atau feature.</h5>', unsafe_allow_html=True)   
    
    st.markdown('<br><br><h3>Contoh aplikasi  K-means</h3>', unsafe_allow_html=True)
    st.markdown('<p>Segmentasi pasar (market segmentation)</p>', unsafe_allow_html=True)
    st.markdown('<p>Segmentasi citra</p>', unsafe_allow_html=True)
    st.markdown('<p>Kompresi gambar</p>', unsafe_allow_html=True)
    st.markdown('<p>Klasifikasi citra penginderaan jauh</p>', unsafe_allow_html=True)


# elif choose == "Proses Clustering":
#     try:
#         df = pd.read_sql_table('flim', engine)
#         st.write(df.head(20))
#     except Exception as ex:
#         st.write("Connection could not be made due to the following error: \n", ex)

# # MACHINE LEARNING DISINI       | K-MEANS
# # ========================================================================================================================================================================================================================

#     df=df[['budget','revenue','runtime','vote_count','vote_average','title']]
#     st.write(df.isna().sum())
#     st.write(df['vote_count'].describe())
    
#     st.write(len(df))
#     df2=df[df['vote_count']> 30]

#     st.write(len(df),len(df2))
#     st.write(df2.head())
#     st.write(df2.isna().sum())
#     from sklearn import preprocessing
#     minmax=preprocessing.MinMaxScaler().fit_transform(df2.drop('title',axis=1))
#     st.write(minmax)

#     df3=pd.DataFrame(minmax,index=df2.index,columns=df2.columns[:-1])
#     KMeans(n_clusters=2).fit(df3).score(df3)
#     st.write(KMeans(n_clusters=2).fit(df3).score(df3))
#     scr=[]
#     for i in range(1,20):
#         score=KMeans(n_clusters=i).fit(df3).score(df3)
#         print(score)
#         scr.append(score)

#     st.write(scr)
#     st.write(plt.plot(scr))
#     kmeans=KMeans(n_clusters=5)
#     kmeans.fit(df3)
#     df3['cluster']=kmeans.labels_

#     st.write(plt.hist(df3['cluster']))
#     st.write(sns.pairplot(df3,hue='cluster'))
#     df3['title']=df2['title']

#     df3.sort_values("cluster")
#     st.write(df3)

#     st.markdown(""" <style> .font {
#     font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
#     </style> """, unsafe_allow_html=True)
#     st.markdown('<p class="font">Terimakasih</p>', unsafe_allow_html=True)    

elif choose == "Data Film":
    df = pd.read_sql_table('flim', engine)
    df=df[['budget','revenue','runtime','vote_count','vote_average','title']]
    df['vote_count'].describe()
    df2=df[df['vote_count']> 30]
    df2.isna().sum()
    from sklearn import preprocessing
    minmax=preprocessing.MinMaxScaler().fit_transform(df2.drop('title',axis=1))

    df3=pd.DataFrame(minmax,index=df2.index,columns=df2.columns[:-1])
    KMeans(n_clusters=2).fit(df3).score(df3)
    KMeans(n_clusters=2).fit(df3).score(df3)
    scr=[]
    for i in range(1,20):
        score=KMeans(n_clusters=i).fit(df3).score(df3)
        print(score)
        scr.append(score)

    plt.plot(scr)
    kmeans=KMeans(n_clusters=5)
    kmeans.fit(df3)
    df3['cluster']=kmeans.labels_

    plt.hist(df3['cluster'])
    sns.pairplot(df3,hue='cluster')
    df3['title']=df2['title']

    df3.sort_values("cluster")
    cluster1 = df3[df3['cluster']== 0]
    cluster2 = df3[df3['cluster']== 1]
    cluster3 = df3[df3['cluster']== 2]
    cluster4 = df3[df3['cluster']== 3]
    cluster5 = df3[df3['cluster']== 4]

    col1, col2 = st.columns(2)
    col3 ,col4 = st.columns(2)
    st.write("Clustering 1")
    st.write(cluster1)
    st.write("Clustering 2")
    st.write(cluster2)  
    st.write("Clustering 3")
    st.write(cluster3)
    st.write("Clustering 4")
    st.write(cluster4)
    st.write("Clustering 5")
    st.write(cluster5)
    try:
        title = st.text_input('Cari Flim', 'Input Judul')
        if st.button('Submit'):
            cari = df3[df3['title']== title]
            st.write(cari)
            where = cari['cluster'].loc[cari.index[0]]
            st.markdown('<h3>Rekomendasi Flim Yang Sama</h3>', unsafe_allow_html=True)  
            st.write(df3[df3['cluster']==where])
            # st.write()
    except:
        st.write("Data Tidak Ditemukan")
