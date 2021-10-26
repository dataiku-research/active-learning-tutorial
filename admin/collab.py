try:
  from google.colab import drive
  import os


  drive.mount('/content/drive')
  os.chdir('/content/drive/MyDrive/active-learning-tutorial-main/')
  !pip install -r requirements_collab.txt
except Exception as e:
  print(e)

