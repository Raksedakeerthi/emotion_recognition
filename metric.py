# Make predictions on the validation set
predictions = emotion_model.predict(validation_generator)

# Get true labels for the validation set
true_labels = validation_generator.classes

# Convert predictions to class labels
predicted_labels = np.argmax(predictions, axis=1)

# Compute metrics
from sklearn.metrics import classification_report

print("Classification Report:")
print(classification_report(true_labels, predicted_labels))
