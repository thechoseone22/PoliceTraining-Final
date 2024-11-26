# De-escalation Model Project: README

## Project Overview

This project focuses on developing and demonstrating a **De-escalation Model** aimed at analyzing and predicting outcomes of law enforcement interactions. The model is trained on custom datasets, using text-based features derived from synthetic transcripts of interactions. The aim is to identify successful de-escalation strategies of law enforcement officers.

---

## Objectives

1. **Develop a Predictive Model**:
   - Train a model to predict the outcome of de-escalation interactions based on syn transcripts.
2. **Explore and Analyze Data**:
   - Use features like context, officer actions, and subject behavior to train the model.
3. **Real-Time Demonstration**:
   - Implement a Gradio interface to test the model on real-world bodycam videos. - but this on back burner / we get to it, we get to it. 
4. **Provide Insights**:
   - Highlight areas for improvement and propose actionable inplementation based on the model's performance.

---

## Workflow and Methodology

### 1. **Data Collection and Preprocessing**
   - **Dataset**: Custom data was created using prompts.
   - **Features**:
     - Contextual description of the scenario.
     - Officer's action plan.
     - Subject’s responses and behavior.
     - Outcome classification (e.g., success, failure).
   - **Preprocessing**:
     - Text tokenization using **HuggingFace Tokenizer**.
     - Feature engineering to standardize input for the model.

### 2. **Model Training**
   - **Model Architecture**:
     - Base model: Pre-trained transformer-based model (T5).
     - Use custom loss function with class weighting to address dataset imbalance.
   - **Training Challenges**:
     - Slow learning rate.
     - Initial accuracy was low due to model complexity and limited data.
   - **Results**:
     - Achieved a final accuracy of **57%** after several iterations.

### 3. **Insights and Recommendations**
   - **Challenges Identified**:
     - Model performance was hindered by:
       - Small dataset size.
       - Complex interactions.
       - Simplistic features needs nuances of audio and video with transcript combined.
   - **Proposed Improvements**:
     - Collect larger, more diverse datasets.
     - Integrate multimodal inputs (audio, video) for richer context.
     - use more advanced architectures.

---

## Results and Conclusion

- **Key Achievements**:
  - Successfully trained and deployed a text-based predictive model for de-escalation outcomes.
  - Demonstrated real-time performance using bodycam footage with a functional Gradio interface.
- **Limitations**:
  - Accuracy (57%, an inverted 75%). 
- **Potential Applications**:
  - Identifying effective de-escalation strategies.
  - Developing real-time feedback systems for active law enforcement scenarios.

---

## Future Enhancements

1. **Dataset Expansion**:
   - Incorporate real-world examples.
2. **Multimodal Analysis**:
   - Integrate audio cues, facial expressions, and tone analysis.
3. **Visualization Tools**:
   - Include graphical representations like confusion matrices or timeline breakdowns for interpretability.
