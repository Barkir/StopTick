# Portable Device for Treating or Preventing Nervous Tic by Biofeedback Therapy

## Overview
This project aims to design a portable, affordable, and easy-to-use device for treating nervous tics using biofeedback therapy. Nervous tics are sudden and uncontrollable movements of body parts caused by stress or nervous system issues, making everyday tasks like talking, eating, and studying difficult. While biofeedback therapy is an effective treatment, it is often inaccessible due to high costs and limited availability in hospitals. This project seeks to address these challenges by creating a compact and cost-effective solution that can be used anywhere.

---

## Engineering Problem and Goal

### Problem:
- **Nervous Tics:** A widespread issue affecting both adults and children.
- **Current Treatments:** Medicine, physical exercises, and biofeedback therapy are available, but biofeedback therapy devices are expensive (~20-200$ per session) and not widely accessible.
- **Accessibility Gap:** Many people cannot afford or access biofeedback therapy due to financial or logistical constraints.

### Goal:
To design a mobile device for treating nervous tics using biofeedback therapy. The device will:
1. Be small, affordable, and easy-to-use.
2. Use biofeedback principles to train the brain to control nervous tics.
3. Provide an alternative method using computer vision (webcam) for tracking facial tics without additional hardware.

---

## Key Features of the Device

### Version 1: Wired Device
- **Hardware:** 
  - EMG sensor with three wet electrodes.
  - Arduino UNO microcontroller.
- **Software:** 
  - Programmed in C++ and Python.
  - Video player application for biofeedback therapy.
- **Functionality:** 
  - Monitors bioelectric potential from muscles.
  - Pauses positive stimulus (e.g., video playback) when a tic is detected.

### Version 2: Mobile Device
- **Hardware:** 
  - Wireless with Bluetooth module.
  - Single dry electrode for comfort and ease of use.
  - Vibration motor as a negative stimulus.
- **Modes:** 
  - Biofeedback therapy mode.
  - Everyday use mode (vibration alerts for tic detection).
- **Portability:** Can be carried in a special arm bag.

### Webcam-Based Tracking
- **Technology:** Uses computer vision and open-source libraries like MediaPipe.
- **Advantages:** 
  - No additional hardware required.
  - Tracks 468 facial landmarks for precise tic detection.
  - Cost-effective and accessible.

---

## Methods and Procedures

### Stage 1: Research
- Studied nervous tics and biofeedback therapy.
- Explored how positive and negative stimuli can train the brain to control tics.

### Stage 2: Prototyping
- Built a breadboard version using an EMG sensor and Arduino UNO.
- Developed a video player application in Python for biofeedback therapy.

### Stage 3: Testing
- Conducted six sessions with a person diagnosed with facial tics.
- Results showed a ~50% reduction in tics and improved concentration during video playback.

### Stage 4: Improvements
- Addressed limitations of wet electrodes (skin irritation, inaccurate readings).
- Developed a webcam-based method for tracking facial tics.
- Created a mobile version of the device with wireless connectivity and dry electrodes.

---

## Results

### Achievements:
1. **Version 1 Device:**
   - Successfully reduced tics in real-world testing.
   - Improved user concentration during therapy sessions.
2. **Webcam-Based Method:**
   - Enabled biofeedback therapy without additional hardware.
   - Made the therapy more accessible and cost-effective.
3. **Mobile Version:**
   - Compact, wireless, and easy to use.
   - Two modes: biofeedback therapy and everyday use.

### Interpretation:
- The project demonstrates the potential of biofeedback therapy devices to be smarter, cheaper, and more effective.
- Challenges like data transmission, electrode attachment, and wireless connectivity were resolved.

---

## Future Work

### Short-Term Goals:
- Develop a unified application for smartphones and PCs to collect and analyze data.
- Create a game-based biofeedback therapy system for enhanced engagement.

### Long-Term Goals:
- Deploy the device in clinics and hospitals to help patients with nervous tics.
- Explore advanced machine learning techniques for improved tic detection.

---

## Conclusions

The project successfully developed two versions of a biofeedback therapy device and a webcam-based method for tracking nervous tics. These innovations make biofeedback therapy more accessible and affordable while maintaining effectiveness. The final goal is to create a user-friendly product with its own application for seamless data collection and analysis.

---

## References

1. Zavadenko NN, Doronina OB, Nesterovsky YE. [Chronic tics and Tourette syndrome in children and adolescents: diagnostic and treatment characteristics]. Zh Nevrol Psikhiatr Im S S Korsakova. 2015;115(1):102-109. Russian. doi: 10.17116/jnevro201511511102-109. PMID: 25909798.
2. Biofeedback: A Practitioner's Guide (4th edition). Edited by Mark S. Schwartz and Frank Andrasik. New York, NY: Guilford Press, 2016. 764 pages. ISBN 978-1-4625-2254-5
3. Son C, Hegde S, Markert C, Zahed K, Sasangohar F. Use of a Mobile Biofeedback App to Provide Health Coaching for Stress Self-management: Pilot Quasi-Experiment. JMIR Form Res 2023;7:e41018. URL: https://formative.jmir.org/2023/1/e41018. DOI: 10.2196/41018
4. Sanger TD, Chen D, Fehlings DL, et al. Definition and classification of hyperkinetic movements in childhood. Mov Disord. 2010;25(11):1538-1549. doi:10.1002/mds.23088
5. Tinius, T. (2007). The combination of cognitive training exercises and neurofeedback. In J. R. Evans (Ed.), Handbook of neurofeedback: Dynamics and clinical applications (pp. 137–153). The Haworth Medical Press/The Haworth Press. https://doi.org/10.1201/b14658-10
