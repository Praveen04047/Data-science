import numpy as np

def apply_confidence_criterion(confidence_scores, threshold=0.2):
    # Sort the confidence scores in descending order
    sorted_confidences = np.sort(confidence_scores)[::-1]

    # Calculate the difference between the highest and second-highest confidence scores
    confidence_difference = sorted_confidences[0] - sorted_confidences[1]

    # Make a decision based on the confidence difference
    if confidence_difference > threshold:
        decision = np.argmax(confidence_scores)  # Choose the class with the highest confidence
        return decision
    else:
        return -1  # Indicate that no decision should be made

# Example usage
confidence_scores_example = [0.6, 0.25, 0.15]

decision = apply_confidence_criterion(confidence_scores_example)

if decision != -1:
    print(f"Decision: Class {decision} (based on Confidence Difference Criterion)")
else:
    print("No decision made based on the Confidence Difference Criterion.")
