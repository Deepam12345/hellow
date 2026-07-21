import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load the trained model
model = load_model("image_model.h5")

# Class labels (change these according to your model)
class_names = [
    "Cat",
    "Dog"
]

# Path of the image to predict
img_path = "test.jpg"

# Load and resize image
img = image.load_img(img_path, target_size=(224, 224))

# Convert image to array
img_array = image.img_to_array(img)

# Add batch dimension
img_array = np.expand_dims(img_array, axis=0)

# Normalize pixel values
img_array = img_array / 255.0

# Predict
prediction = model.predict(img_array)

# Get predicted class
predicted_class = np.argmax(prediction)

print("Predicted Class:", class_names[predicted_class])
print("Confidence:", prediction[0][predicted_class])