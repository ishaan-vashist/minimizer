import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Data generators
train_datagen = ImageDataGenerator(rescale=1.0/255, validation_split=0.2)
train_generator = train_datagen.flow_from_directory(
    r'C:\Users\ishaa\Desktop\fist images',
    target_size=(128, 128),
    batch_size=32,
    class_mode='categorical',  # Set class_mode to 'categorical'
    subset='training'
)
validation_generator = train_datagen.flow_from_directory(
    r'C:\Users\ishaa\Desktop\fist images',
    target_size=(128, 128),
    batch_size=32,
    class_mode='categorical',  # Set class_mode to 'categorical'
    subset='validation'
)

# Model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(2, activation='softmax')  # Use 2 units and 'softmax' activation for two-class classification
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])  # Use 'categorical_crossentropy' for multi-class classification

model.fit(
    train_generator,
    epochs=10,
    validation_data=validation_generator
)

# Save the model
model.save('hand_gesture_model.h5')
