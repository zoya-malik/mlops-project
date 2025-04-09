# End-to-End MLOps Pipeline for Image Classification (CIFAR-10)

This project demonstrates a complete MLOps pipeline for solving an image classification problem using the CIFAR-10 dataset. The pipeline covers all critical stages of machine learning operations, including data ingestion, preprocessing, model development, deployment, and monitoring. It is designed to reflect real-world ML workflows with modular, scalable, and production-ready code.

---

## Dataset

The CIFAR-10 dataset consists of:
- `train.7z`: Folder of training images in PNG format
- `test.7z`: Folder of test images (includes 290,000 junk images to discourage cheating)
- `trainLabels.csv`: CSV file mapping training images to their corresponding labels

### Label Classes:
- airplane
- automobile
- bird
- cat
- deer
- dog
- frog
- horse
- ship
- truck

---

## Features

- Full image preprocessing and augmentation pipeline
- Custom CNN and transfer learning with state-of-the-art architectures
- Hyperparameter tuning and cross-validation
- Experiment tracking with MLflow or Weights & Biases
- Model serialization and versioning
- RESTful model deployment with Flask or FastAPI
- CI/CD pipeline with Docker and GitHub Actions
- Monitoring for data drift and model performance degradation

---

## Technologies Used

- Python (PyTorch or TensorFlow)
- NumPy, Pandas, OpenCV, scikit-learn
- MLflow / Weights & Biases
- Docker, Git, GitHub Actions
- Flask or FastAPI

## Citations
Learning Multiple Layers of Features from Tiny Images, Alex Krizhevsky, 2009.
Will Cukierski. CIFAR-10 - Object Recognition in Images. https://kaggle.com/competitions/cifar-10, 2013. Kaggle.
