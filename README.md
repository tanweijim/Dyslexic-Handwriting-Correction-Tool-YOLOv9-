# Dyslexic Handwriting Correction Tool
## **Overview**
This project aims to address the challenges in written communication faced by dyslexic individuals and their caregivers by leveraging on machine learning techniques to provide real-time corrections.
## Challenges faced by dyslexic individuals and their caregivers
- Poor legibility
- Inconsistent letter formation
  - Reversals: letters/numbers are reversed or flipped
  - Sloping: letters/numbers may slope to one side or another
  - Cramping: letters/numbers may cramp or tangle together
  -  Irregularity: irregular/inconsistent sizes and spacings, unable to fit within lines or boxes, mixing uppercase and lowercase letters, cursive/scribbled
- Frequent spelling errors
## **Model Selection**
A series of models from the You Only Look Once (YOLO) family, a popular real-time object detection algorithm, is tested. In particular, the YOLOv9 introduces improved accuracy and speed compared to earlier versions, and can predict bounding boxes and class probabilities simultaneously.
## **Metrics used**
- **Mean Average Precision (mAP)** - assesses the model's overall detection accuracy across all classes
- **Precision** - measures the model's accuracy in identifying key objects by calculating the ratio of true posistives to all detections
- **Recall** - evaluates the model's ability to detect all ground-truth objects, indicating the proportion of true positives among all actual ground-truth instances
## **Model Performances**
After experimenting with various models, the following top three models were chosen:

| Model       | mAP50 Train       | mAP50 Test        |  Precision Train       | Precision Test        |  Recall Train      | Recall Test        | Model Run Time (hrs) |
| ----------- | :----: | :----: |  :----: | :----: | :----: | :----: | :----: |
| YOLOv5 (baseline model) | 0.89    | 0.89       | 0.66     | 0.66     | 0.83      | 0.83         |    0.44    |
| **YOLOv9**   | **0.93**        | **0.92**       | **0.72**       | **0.72**      | **0.86**       | **0.86**   |  **0.68** |
| YOLOV10   | 0.67     | 0.67      | 0.53       | 0.54       | 0.63     |   0.63   |   0.37    |

mAP50 is a detection threshold that indicates that a detection is considered correct if the IoU between the predicted and ground truth bounding boxes is at least 50%. A higher mAP50 value generally indicates better model performance, as it means the model is detecting objects more accurately and with fewer false positives.

YOLOv9 achieves the highest mAP50 on both training and test sets, indicating superior overall object detection accuracy. However the trade off is that the time taken for training the model is slower.

## **Future development / enhancement**
- Continually update the dataset by training with new handwriting
- Detection of numbers and symbols, which are essential for communication
- Detection of full words and paragraphs of texts
- Integrate additional features such as phonetic assistance
- App-based application to further enhance communication or learning experience

## **About Dataset**
The model is trained using close to a thousand handwritten characters by dyslexic students. 26 uppercase and 26 lowercase alphabets for a start. With train, validation and test split at 70:20:10.

The dataset was collected from three sources (uppercase letters are from NIST Special Database 19 [1], while lowercase letters are from Kaggle Dataset [2] and datasets for testing are from dyslexic kids of Seberang Jaya primary school, Penang, Malaysia.
The full dataset contains a total of 78,275 for normal class, 52,196 for reversal class, and 8,029 for corrected class. For the purpose of this exercise.

[1] P. J. Grother, “NIST Special Database 19,” NIST, 2016. [Online]. Available: https://www.nist.gov/srd/nist-special-database-19. [Accessed: 22-May-2019].
[2] S. Patel, “A-Z Handwritten Alphabets in .csv format,” Kaggle, 2017. [Online]. Available: https://www.kaggle.com/sachinpatel21/az-handwritten-alphabets-in-csv-format. [Accessed: 22-May-2019].

**References**
1. M. S. A. B. Rosli, I. S. Isa, S. A. Ramlan, S. N. Sulaiman and M. I. F. Maruzuki, "Development of CNN Transfer Learning for Dyslexia Handwriting Recognition," 2021 11th IEEE International Conference on Control System, Computing and Engineering (ICCSCE), 2021, pp. 194-199, doi: 10.1109/ICCSCE52189.2021.9530971.

2. N. S. L. Seman, I. S. Isa, S. A. Ramlan, W. Li-Chih and M. I. F. Maruzuki, "Notice of Removal: Classification of Handwriting Impairment Using CNN for Potential Dyslexia Symptom," 2021 11th IEEE International Conference on Control System, Computing and Engineering (ICCSCE), 2021, pp. 188-193, doi: 10.1109/ICCSCE52189.2021.9530989.

3. Isa, Iza Sazanita. CNN Comparisons Models On Dyslexia Handwriting Classification / Iza Sazanita Isa … [et Al.]. Universiti Teknologi MARA Cawangan Pulau Pinang, 2021.

4. Isa, I. S., Rahimi, W. N. S., Ramlan, S. A., & Sulaiman, S. N. (2019). Automated detection of dyslexia symptom based on handwriting image for primary school children. Procedia Computer Science, 163, 440-449.

