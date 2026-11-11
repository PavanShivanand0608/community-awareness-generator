# SDG CLASSIFIER EVALUATION REPORT

Generated: 2026-11-11 15:10:43

## Overall Results

- Total test inputs: 170
- Completed predictions: 170
- Correct predictions: 132
- Wrong predictions: 38
- Exact matches: 93
- Errors: 0
- Expected-label hit rate: 77.65%
- Exact-match rate: 54.71%

## SDG-wise Summary

| SDG | Completed | Correct | Wrong | Exact | Hit Rate | Exact Rate | Errors |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 10 | 9 | 1 | 2 | 90.00% | 20.00% | 0 |
| 2 | 10 | 9 | 1 | 8 | 90.00% | 80.00% | 0 |
| 3 | 10 | 8 | 2 | 7 | 80.00% | 70.00% | 0 |
| 4 | 10 | 10 | 0 | 6 | 100.00% | 60.00% | 0 |
| 5 | 10 | 4 | 6 | 2 | 40.00% | 20.00% | 0 |
| 6 | 10 | 6 | 4 | 6 | 60.00% | 60.00% | 0 |
| 7 | 10 | 8 | 2 | 8 | 80.00% | 80.00% | 0 |
| 8 | 10 | 9 | 1 | 5 | 90.00% | 50.00% | 0 |
| 9 | 10 | 7 | 3 | 4 | 70.00% | 40.00% | 0 |
| 10 | 10 | 6 | 4 | 3 | 60.00% | 30.00% | 0 |
| 11 | 10 | 10 | 0 | 4 | 100.00% | 40.00% | 0 |
| 12 | 10 | 8 | 2 | 6 | 80.00% | 60.00% | 0 |
| 13 | 10 | 8 | 2 | 4 | 80.00% | 40.00% | 0 |
| 14 | 10 | 9 | 1 | 9 | 90.00% | 90.00% | 0 |
| 15 | 10 | 7 | 3 | 6 | 70.00% | 60.00% | 0 |
| 16 | 10 | 7 | 3 | 7 | 70.00% | 70.00% | 0 |
| 17 | 10 | 7 | 3 | 6 | 70.00% | 60.00% | 0 |

## Wrong Predictions

| Expected SDG | Input | Predicted SDGs | Input Text |
|---:|---:|---|---|
| 1 | 6 | 11 | Single parent households cannot afford housing and childcare expenses. |
| 2 | 2 | None | Small farmers lose crops because of unpredictable rainfall and drought. |
| 3 | 9 | None | Poor sanitation contributes to preventable diseases in underserved communities. |
| 3 | 10 | None | Residents need awareness about first aid and emergency medical services. |
| 5 | 2 | 4, 10 | Girls face discrimination and are discouraged from continuing their education. |
| 5 | 4 | None | Domestic violence survivors need access to protection and support services. |
| 5 | 7 | None | Young women need mentorship in science, technology and entrepreneurship. |
| 5 | 8 | 4 | Child marriage prevents girls from continuing education and achieving independence. |
| 5 | 9 | None | Women farmers lack equal access to land ownership and agricultural resources. |
| 5 | 10 | None | Communities need awareness programmes promoting equal rights for all genders. |
| 6 | 2 | None | Open drains and inadequate toilets create sanitation problems in communities. |
| 6 | 5 | 4 | Schools lack clean toilets and proper handwashing facilities for students. |
| 6 | 8 | 11 | Rural households lack affordable sanitation facilities and safe toilets. |
| 6 | 9 | None | Children need awareness about handwashing to prevent waterborne diseases. |
| 7 | 3 | None | Families need awareness about installing rooftop solar panels. |
| 7 | 9 | 13, 17 | Community centres could use solar powered lighting facilities. |
| 8 | 7 | None | Child labour prevents children from attending school and exposes them to danger. |
| 9 | 2 | None | Small manufacturers need modern equipment to improve production quality. |
| 9 | 3 | 2, 11 | Poor rural roads make transportation of agricultural products difficult. |
| 9 | 7 | None | Entrepreneurs lack access to research facilities and technical support. |
| 10 | 3 | 4 | Children from disadvantaged backgrounds have fewer educational opportunities. |
| 10 | 4 | 1, 16 | Older residents need better access to inclusive public services. |
| 10 | 5 | 11, 16 | Minority communities are excluded from local decision making. |
| 10 | 7 | 4 | Displaced families need equal access to education and healthcare. |
| 12 | 3 | None | Consumers need awareness about repairing and reusing products. |
| 12 | 9 | 2 | Markets need better storage systems to reduce food wastage. |
| 13 | 5 | 14 | Coastal communities face risks from rising sea levels. |
| 13 | 8 | 6 | Drought conditions affect village water supplies and local livelihoods. |
| 14 | 5 | None | Coral reefs are damaged by pollution and destructive activities. |
| 15 | 2 | None | Communities need awareness about protecting endangered animals. |
| 15 | 7 | 11 | Wetlands are destroyed by construction and other human activities. |
| 15 | 9 | None | Illegal hunting reduces wildlife populations and damages ecosystems. |
| 16 | 5 | None | Community members need safe ways to report abuse and human rights violations. |
| 16 | 7 | 4 | Young people need education about peaceful conflict resolution and legal rights. |
| 16 | 9 | None | Journalists need safe conditions to report public concerns. |
| 17 | 3 | 1 | Nonprofit organisations need cooperation with public institutions to reduce poverty. |
| 17 | 8 | None | Government agencies and civil society groups should collaborate to monitor development goals. |
| 17 | 9 | None | Local businesses and public institutions need shared plans to address community challenges. |

## Interpretation and Limitations

- These 170 manually written examples are supplementary smoke tests.
- They are not a representative or independently labelled benchmark.
- CORRECT means the intended SDG appears anywhere in the predictions.
- WRONG means the intended SDG does not appear in the predictions.
- Exact match means the model predicts only the intended SDG.
- These results must not replace the official held-out UNDP test evaluation.
- This script tests classification only, not campaign quality or Docker.
