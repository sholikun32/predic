# page title
            st.title('Prediction Penyakit Jantung')
            col1, col2, col3 = st.columns(3)
            with col1:
                age = st.number_input('Umur')
            with col2: 
                sex = st.number_input('Jenis Kelamin (1 = laki-laki; 0 = perempuan)')
            with col3:
                cp = st.number_input('Chest Pain types (0 = typical, 1 = asymptotic, 2 = nonanginal, 3 = nontypical)')
            with col1:
                trestbps = st.number_input('Resting Blood Pressure')
            with col2:
                chol = st.number_input('Serum Cholestoral in mg/dl')
            with col3:
                fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl (1 = benar; 0 = salah)')
            with col1:
                restecg = st.number_input('Resting Electrocardiographic results')
        
            with col2:
                thalach = st.number_input('Maximum Heart Rate achieved')
            with col3:
                exang = st.number_input('Exercise Induced Angina (1 = ya; 0 = tidak)')  
            with col1:
                oldpeak = st.number_input('ST depression induced by exercise')
            with col2:
                slope = st.number_input('Slope of the peak exercise ST segment')
            with col3:
                ca = st.number_input('Major vessels colored by flourosopy (0 - 3)')
            with col1:
                thal = st.number_input('thal: 1 = normal; 2 = fixed defect; 3 = reversable defect')
