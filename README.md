# Coronary Artery Disease (CAD) Prediction Model

# Overview
Coronary Artery Disease (CAD) is a leading cause of heart-related illnesses and mortality worldwide. Early detection and intervention play a crucial role in managing and preventing the progression of CAD. This project aims to provide a Machine Learning (ML) solution for the early prediction of CAD based on relevant health parameters.

# Objective
The primary goal of this project is to develop a predictive model that can assess the risk of Coronary Artery Disease in individuals based on specific health attributes. By leveraging machine learning algorithms, we aim to enable early detection, allowing for timely medical intervention and lifestyle modifications.

# Dataset
The model is trained on a dataset containing information such as age, sex, chest pain type, resting blood pressure, cholesterol levels, fasting blood sugar, resting electrocardiographic results, maximum heart rate achieved, exercise-induced angina, ST depression induced by exercise relative to rest, the slope of the peak exercise ST segment, number of major vessels colored by fluoroscopy, and thalassemia. The dataset is carefully curated to ensure accuracy and relevance.

# Machine Learning Algorithms
The project employs various machine learning algorithms, including Logistic Regression, Random Forest, KNN, Naive Bayes, Gradient Boosting, and others. The choice of algorithms aims to create a robust and accurate predictive model.

# How to Use
Clone the repository to your local machine:
git clone https://github.com/yourusername/heart-disease-prediction.git

Install the required dependencies:
pip install -r requirements.txt

Run the app.py

Enter the required health parameters when prompted, and the model will provide a prediction regarding the likelihood of Coronary Artery Disease.
Results
# Parameters Explanation

# Attributes: Age, Sex, Chest-pain type, Resting Blood Pressure, Cholesterol, Fasting Blood Sugar, Resting ECG, Max heart rate, Exercise Angina, Oldpeak, ST Slope

 Age: The age of the patient in years.

 Sex: The gender of the patient (1 = male, 0 = female)

 Chest-pain type: The type of chest-pain experienced by the patient in following format :
 0 = typical angina
 1 = atypical angina
 2 = non — anginal pain
 3 = asymptotic

 Resting Blood Pressure: The resting blood pressure value of the patient in mmHg (unit)

 Cholesterol: The serum cholesterol in mg/dl (unit)

 Fasting Blood Sugar: The fasting blood sugar value of an individual with (120mg/dl)
 If fasting blood sugar > 120mg/dl then: (1 = true, : 0 = false)

 Resting ECG: The resting electrocardiographic results
 0 = normal
 1 = having ST-T wave abnormality
 2 = left ventricular hypertrophy

 Max heart rate: The max heart rate achieved by the patient.

 Exercise Angina:  (1 = yes, 0 = no)

 Oldpeak: The depression induced by exercise relative to rest, is the value which is an integer or float.

 ST Slope:
 1 = up sloping
 2 = flat
 3 = down sloping

 # Detailed Explanation: 

1. *Age*: This is your age in years. If you're over 50, it could increase your risk.

2. *Sex*: This refers to whether you're male or female. Males tend to have a higher risk.

3. *Chest pain type*: This describes the kind of chest discomfort you might feel:
   - Typical angina: Classic chest pain, pressure, or tightness.
   - Atypical angina: Discomfort that feels different from typical angina.
   - Non-anginal pain: Chest discomfort not related to the heart.
   - Asymptomatic: No chest pain or discomfort.

4. *Resting Blood Pressure*: This measures the force of your blood against the walls of your arteries when you're not active. High blood pressure is a concern.

5. *Cholesterol*: This is a fatty substance in your blood. High cholesterol levels can clog your arteries and increase heart disease risk.

6. *Fasting Blood Sugar*: This measures your blood sugar level after fasting for a period of time. High levels may indicate diabetes, which is a risk factor for heart disease.

7. *Resting ECG*: This records the electrical activity of your heart while you're at rest. Abnormalities in the heart's rhythm or structure may be detected.

8. *Max heart rate*: This is the highest number of times your heart beats in a minute during intense exercise. A rapid heart rate may signal a problem.

9. *Exercise Angina*: This is chest pain or discomfort that occurs when your heart doesn't get enough oxygen-rich blood during physical activity.

10. *Oldpeak*: This measures the degree of change in your heart's electrical activity during exercise compared to when you're at rest. A significant change may indicate heart stress.

11. *ST Slope*: This refers to the pattern of the ST segment on an electrocardiogram (ECG) during exercise. Changes in this slope may indicate heart problems.

# In Hindi

Certainly, here are the translations in Hindi:

1. *आयु*: यह आपकी आयु को वर्षों में बताता है। यदि आप 50 साल से अधिक उम्र के हैं, तो यह आपके जोखिम को बढ़ा सकता है।

2. *लिंग*: यह यह बताता है कि आप पुरुष या महिला हैं। पुरुषों का जोखिम अधिक होता है।

3. *सीने का दर्द का प्रकार*: यह बताता है कि आप कैसा सीने में असहनीय अनुभव कर सकते हैं:
   - सामान्य एंजाइना: क्लासिक सीने का दर्द, दबाव या तंगी।
   - असामान्य एंजाइना: सामान्य एंजाइना से अलग अनुभव होने वाला असहनीय अनुभव।
   - गैर-एंजाइनल पीड़ा: हृदय से संबंधित नहीं होने वाली सीने की असहनीयता।
   - असंवेदनशील: कोई सीने का दर्द या असहनीयता नहीं।

4. *विश्राम रक्तचाप*: यह आपकी धमनियों की दीवारों के खिलाफ आपके रक्त की शक्ति को मापता है जब आप गतिहीन होते हैं। उच्च रक्तचाप एक चिंता का कारण हो सकता है।

5. *कोलेस्ट्रोल*: यह आपके रक्त में एक वसायु संबंधी पदार्थ है। उच्च कोलेस्ट्रॉल स्तर आपकी धमनियों को ढकने और हृदय रोग का जोखिम बढ़ा सकते हैं।

6. *निरोगी रक्त शर्करा*: यह आपकी रक्त शर्करा का स्तर बताता है जब आप किसी समय के लिए उपवास करते हैं। उच्च स्तर डायबिटीज का संकेत हो सकता है, जो हृदय रोग का एक कारक है।

7. *निरोगी ईसीजी*: यह आपके हृदय की विद्युतीय गतिविधि को रेकॉर्ड करता है जब आप विश्राम कर रहे होते हैं। हृदय की गति या संरचना में असामान्यताओं को पहचाना जा सकता है।

8. *अधिकतम हृदय दर*: यह यह बताता है कि आपके हृदय कितनी बार एक मिनट में अधिकतम बार धड़कता है। तेज धड़कने का मतलब एक समस्या का संकेत हो सकता है।

9. *व्यायाम एंजाइना*: यह व्यायाम के दौरान जब आपके हृदय को पर्याप्त ऑक्सीजन-संगत रक्त नहीं मिलता है तो सीने में दर्द या असहनीयता होती है।

10. *पुरानी पीक*: यह आपके हृदय की विद्युतीय गतिविधि में परिवर्तन का माप है, जब आप व्यायाम कर

 रहे होते हैं, तुलना में जब आप आराम कर रहे होते हैं। कोई महत्वपूर्ण परिवर्तन दिल की तनाव की ओर संकेत कर सकता है।

11. *एसटी स्लोप*: यह व्यायाम के दौरान इलेक्ट्रोकार्डियोग्राम (ईसीजी) पर एसटी सेगमेंट के पैटर्न का संदर्भ है। इस स्लोप में परिवर्तन हृदय समस्याओं की ओर संकेत देता हो सकता है।     

# Contribution
Contributions to enhance the model's accuracy, add features, or improve documentation are welcome. Please follow the guidelines outlined in the CONTRIBUTING.md file.

# License
This project is licensed under the MIT License - see the LICENSE.md file for details.

# Acknowledgments
The project acknowledges the importance of early detection in managing Coronary Artery Disease.
Thanks to the open-source community for their contributions to machine learning libraries used in this project.
Thanks to IEEE DataPort for providing a comprehensive CAD Dataset for free
Feel free to use this README template for your GitHub project and customize it according to your project's specifics.

Note: For more details, we will publish our research paper soon, and provide the link here.

This is a research based project
Wakil Ahmad Hamidi

follow on Github:https://github.com/wakilahmadhamidi
follow on LinkedIn: https://www.linkedin.com/in/wakil-ahmad-hamidi-34aa37174/
