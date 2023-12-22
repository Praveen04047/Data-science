import numpy as np

def apply_confidence_quotient_criterion(confidence_scores, threshold=0.5):
    # Calculate the quotient of the highest confidence score and the sum of all confidence scores
    confidence_quotient = np.max(confidence_scores) / np.sum(confidence_scores)

    # Make a decision based on the confidence quotient
    if confidence_quotient > threshold:
        decision = np.argmax(confidence_scores)  # Choose the class with the highest confidence
        return decision
    else:
        return -1  # Indicate that no decision should be made

# Example usage
confidence_scores_example = [0.6, 0.25, 0.15]

decision = apply_confidence_quotient_criterion(confidence_scores_example)

if decision != -1:
    print(f"Decision: Class {decision} (based on Confidence Quotient Criterion)")
else:
    print("No decision made based on the Confidence Quotient Criterion.")
