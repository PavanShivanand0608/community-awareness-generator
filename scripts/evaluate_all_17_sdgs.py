"""
Evaluate the SDG classifier using 10 inputs for each of 17 SDGs.

Total tests: 170

Run from the project root:
python scripts/evaluate_all_17_sdgs.py

This tests the saved classifier only. It does not call OpenRouter.
"""

import csv
import sys
from pathlib import Path
from datetime import datetime

# Add the project root to Python's import path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.predictor import predict_sdgs


# ============================================================
# 10 TEST INPUTS FOR EACH OF THE 17 SDGs
# ============================================================

TEST_CASES = {

    1: [
        "Low income families struggle to afford food, housing and other basic necessities.",
        "Unemployed families cannot meet their daily living expenses.",
        "People in informal settlements lack stable income and social protection.",
        "Elderly residents lack financial support for basic household needs.",
        "Seasonal workers experience periods without income and struggle with poverty.",
        "Single parent households cannot afford housing and childcare expenses.",
        "Homeless people need access to safe shelter and essential services.",
        "Rural families lose their livelihoods because of repeated crop failures.",
        "Vulnerable households do not know how to access government welfare benefits.",
        "People in remote villages have limited livelihood and income opportunities."
    ],

    2: [
        "Children from poor families suffer from hunger and lack nutritious food.",
        "Small farmers lose crops because of unpredictable rainfall and drought.",
        "Food is wasted in markets while vulnerable families struggle with hunger.",
        "Pregnant women lack access to nutritious food and nutrition counselling.",
        "School children need nutritious meals to support healthy growth.",
        "Farmers need training in sustainable agriculture and improved food production.",
        "Families in drought affected villages struggle to grow enough food.",
        "Food banks lack proper systems to distribute surplus food to needy families.",
        "Young children suffer from malnutrition because their diets lack essential nutrients.",
        "Farmers need better storage facilities to prevent food loss after harvesting."
    ],

    3: [
        "Rural residents lack access to hospitals and qualified healthcare professionals.",
        "Families are unaware of the importance of vaccination and regular health checkups.",
        "Communities need awareness about diabetes prevention and healthy lifestyles.",
        "People experiencing mental health problems face stigma and lack counselling support.",
        "Pregnant women need access to maternal healthcare and regular medical checkups.",
        "Road accidents increase because riders ignore helmet and traffic safety rules.",
        "Teenagers need awareness about the harmful health effects of tobacco consumption.",
        "Older adults need information about medicine safety and preventive health screenings.",
        "Poor sanitation contributes to preventable diseases in underserved communities.",
        "Residents need awareness about first aid and emergency medical services."
    ],

    4: [
        "Children in rural villages lack access to quality schools and trained teachers.",
        "Girls discontinue their education because families cannot afford school expenses.",
        "Government schools lack libraries, laboratories and digital learning resources.",
        "Adults need literacy programmes and opportunities to continue their education.",
        "Children with disabilities face barriers because schools lack inclusive facilities.",
        "Rural students have limited internet access for online education.",
        "Young people need vocational training to develop practical employment skills.",
        "Schools need reading programmes to improve children's literacy skills.",
        "A shortage of qualified teachers affects education quality in remote villages.",
        "Families need awareness about the importance of early childhood education."
    ],

    5: [
        "Women receive lower wages than men for performing similar work.",
        "Girls face discrimination and are discouraged from continuing their education.",
        "Women need equal representation in community leadership and decision making.",
        "Domestic violence survivors need access to protection and support services.",
        "Women face unequal employment opportunities and workplace discrimination.",
        "Unpaid household responsibilities limit women's education and career opportunities.",
        "Young women need mentorship in science, technology and entrepreneurship.",
        "Child marriage prevents girls from continuing education and achieving independence.",
        "Women farmers lack equal access to land ownership and agricultural resources.",
        "Communities need awareness programmes promoting equal rights for all genders."
    ],

    6: [
        "Families in villages depend on unsafe wells because clean drinking water is unavailable.",
        "Open drains and inadequate toilets create sanitation problems in communities.",
        "Residents need awareness about filtering and safely storing drinking water.",
        "Untreated sewage is discharged into rivers and contaminates local water sources.",
        "Schools lack clean toilets and proper handwashing facilities for students.",
        "Water shortages occur because of leakage and inefficient water usage.",
        "Communities need regular testing of drinking water quality.",
        "Rural households lack affordable sanitation facilities and safe toilets.",
        "Children need awareness about handwashing to prevent waterborne diseases.",
        "Household waste pollutes local water bodies because wastewater is not managed properly."
    ],

    7: [
        "Rural households depend on firewood because clean cooking energy is unavailable.",
        "Frequent electricity interruptions affect homes and businesses in remote villages.",
        "Families need awareness about installing rooftop solar panels.",
        "Streetlights consume excessive electricity and need energy efficient alternatives.",
        "Small businesses lack reliable and affordable energy supplies.",
        "Residents have limited awareness about energy conservation practices.",
        "Public buildings need renewable energy systems to reduce electricity costs.",
        "Remote settlements lack reliable access to modern electricity services.",
        "Community centres could use solar powered lighting facilities.",
        "Local institutions need support to adopt clean energy technologies."
    ],

    8: [
        "Young people struggle to find stable employment because they lack practical skills.",
        "Workers in informal jobs face unsafe working conditions and unfair wages.",
        "Small businesses need entrepreneurship training to create local employment.",
        "Tourism workers experience irregular incomes and limited career opportunities.",
        "People with disabilities face discrimination while applying for jobs.",
        "Graduates need internships and vocational training to improve employment opportunities.",
        "Child labour prevents children from attending school and exposes them to danger.",
        "Women entrepreneurs need business mentoring and financial resources.",
        "Workers need awareness about workplace safety and fair employment rights.",
        "Rural communities need decent employment opportunities for young people."
    ],

    9: [
        "Remote villages lack reliable mobile networks and broadband internet connectivity.",
        "Small manufacturers need modern equipment to improve production quality.",
        "Poor rural roads make transportation of agricultural products difficult.",
        "Schools lack computer laboratories and digital infrastructure.",
        "Small enterprises need affordable technology and innovation support.",
        "Public infrastructure is ageing and requires modernisation.",
        "Entrepreneurs lack access to research facilities and technical support.",
        "Poor digital connectivity prevents residents from accessing online services.",
        "Remote settlements need reliable transport and communication infrastructure.",
        "Small industries need cleaner production technologies and modern equipment."
    ],

    10: [
        "People with disabilities face barriers when accessing public transport and services.",
        "Migrant workers experience discrimination and difficulty accessing housing.",
        "Children from disadvantaged backgrounds have fewer educational opportunities.",
        "Older residents need better access to inclusive public services.",
        "Minority communities are excluded from local decision making.",
        "The income gap between wealthy and poor households is increasing.",
        "Displaced families need equal access to education and healthcare.",
        "Government websites are not accessible to people with visual impairments.",
        "Rural residents have fewer opportunities to access specialised services.",
        "Communities need programmes that promote equal participation and reduce discrimination."
    ],

    11: [
        "Cities experience traffic congestion because public transportation is inadequate.",
        "Informal settlements lack safe housing and proper drainage facilities.",
        "Neighbourhoods need accessible parks and safe public spaces.",
        "Poor municipal waste collection causes rubbish to accumulate on streets.",
        "Historic buildings need protection from unplanned construction.",
        "Pedestrians face unsafe roads because footpaths are unavailable.",
        "Urban communities need better flood and disaster preparedness.",
        "Low income families struggle to find affordable housing in cities.",
        "Noise and air pollution reduce the quality of urban life.",
        "Town planners need community participation to create sustainable cities."
    ],

    12: [
        "Households throw away recyclable plastic and paper because recycling facilities are unavailable.",
        "Restaurants waste edible food instead of donating surplus meals.",
        "Consumers need awareness about repairing and reusing products.",
        "Local shops distribute excessive single use plastic packaging.",
        "Businesses need guidance on reducing material waste.",
        "Schools should teach students about waste segregation and composting.",
        "Clothing industries need to reduce textile waste through recycling.",
        "Electronic waste is discarded with regular household rubbish.",
        "Markets need better storage systems to reduce food wastage.",
        "Communities need awareness about responsible consumption and recycling."
    ],

    13: [
        "Communities face frequent heatwaves and need climate preparedness plans.",
        "Farmers struggle with changing rainfall patterns and climate conditions.",
        "Flood prone communities need early warning systems and emergency plans.",
        "Schools need climate education programmes about global warming.",
        "Coastal communities face risks from rising sea levels.",
        "Local authorities need plans to reduce greenhouse gas emissions.",
        "People need awareness about reducing carbon emissions and saving energy.",
        "Drought conditions affect village water supplies and local livelihoods.",
        "Community groups organise tree planting activities to address climate change.",
        "Farmers need climate information to prepare for extreme weather conditions."
    ],

    14: [
        "Plastic bags and bottles enter the sea and harm marine animals.",
        "Fishing communities report declining fish populations and need sustainable fishing practices.",
        "Untreated wastewater flows into coastal waters and damages marine ecosystems.",
        "Discarded fishing nets trap turtles and other marine animals.",
        "Coral reefs are damaged by pollution and destructive activities.",
        "Coastal residents need awareness about preventing ocean plastic pollution.",
        "Overfishing threatens marine biodiversity and fishing livelihoods.",
        "Oil spills and chemical pollution damage marine habitats.",
        "Tourists need guidance on protecting beaches and marine wildlife.",
        "Marine protected areas need community support to conserve ocean habitats."
    ],

    15: [
        "Illegal tree cutting reduces forest cover and destroys wildlife habitats.",
        "Communities need awareness about protecting endangered animals.",
        "Soil erosion and land degradation reduce agricultural productivity.",
        "Forest fires destroy natural habitats and threaten biodiversity.",
        "Invasive plant species threaten native plants and animals.",
        "Farmers need guidance on soil conservation and sustainable land management.",
        "Wetlands are destroyed by construction and other human activities.",
        "Communities can restore degraded forests by planting native trees.",
        "Illegal hunting reduces wildlife populations and damages ecosystems.",
        "Residents need awareness about protecting forests and terrestrial biodiversity."
    ],

    16: [
        "Residents do not know how to report corruption and access grievance services.",
        "Families need awareness about legal rights and protection from violence.",
        "People in remote communities struggle to access legal aid and justice.",
        "Public institutions need transparent processes and accountable decision making.",
        "Community members need safe ways to report abuse and human rights violations.",
        "Delays in public services reduce trust in government institutions.",
        "Young people need education about peaceful conflict resolution and legal rights.",
        "Residents without identity documents struggle to access legal recognition.",
        "Journalists need safe conditions to report public concerns.",
        "Organisations need to promote accountability and access to justice."
    ],

    17: [
        "Local governments, schools and businesses need to collaborate on sustainable development projects.",
        "Community groups need partnerships with universities and companies to support development.",
        "Nonprofit organisations need cooperation with public institutions to reduce poverty.",
        "Environmental groups need business partnerships to support conservation projects.",
        "Development organisations work separately because they do not share resources and expertise.",
        "Schools and health centres need partnerships to conduct community awareness programmes.",
        "Small organisations need funding partnerships to expand development activities.",
        "Government agencies and civil society groups should collaborate to monitor development goals.",
        "Local businesses and public institutions need shared plans to address community challenges.",
        "International development partners need better coordination with local organisations."
    ]
}


# ============================================================
# MAIN EVALUATION FUNCTION
# ============================================================

def main():

    detailed_results = []
    summary_results = []

    print("\nStarting 170 SDG classifier tests...")
    print("Testing saved classifier only. No OpenRouter requests.\n")

    for expected_sdg in range(1, 18):

        correct = 0
        wrong = 0
        exact = 0
        errors = 0

        print(f"\nTesting SDG {expected_sdg}...")

        for index, input_text in enumerate(TEST_CASES[expected_sdg], start=1):

            try:
                predictions = predict_sdgs(input_text)

                predictions = sorted(set(int(x) for x in predictions))

                is_correct = expected_sdg in predictions
                is_exact = predictions == [expected_sdg]

                if is_correct:
                    correct += 1
                    result = "CORRECT"
                else:
                    wrong += 1
                    result = "WRONG"

                if is_exact:
                    exact += 1

                predicted_text = ", ".join(map(str, predictions))

                print(
                    f"Input {index}: Expected SDG {expected_sdg} | "
                    f"Predicted: {predicted_text or 'None'} | {result}"
                )

                detailed_results.append({
                    "expected_sdg": expected_sdg,
                    "input_number": index,
                    "predicted_sdgs": predicted_text,
                    "result": result,
                    "exact_match": is_exact,
                    "input_text": input_text,
                    "error": ""
                })

            except Exception as error:

                errors += 1

                print(f"Input {index}: ERROR - {error}")

                detailed_results.append({
                    "expected_sdg": expected_sdg,
                    "input_number": index,
                    "predicted_sdgs": "",
                    "result": "ERROR",
                    "exact_match": False,
                    "input_text": input_text,
                    "error": str(error)
                })

        completed = 10 - errors

        hit_rate = correct / completed if completed else 0
        exact_rate = exact / completed if completed else 0

        summary_results.append({
            "expected_sdg": expected_sdg,
            "total_inputs": 10,
            "completed": completed,
            "correct": correct,
            "wrong": wrong,
            "exact_matches": exact,
            "hit_rate": f"{hit_rate:.2%}",
            "exact_match_rate": f"{exact_rate:.2%}",
            "errors": errors
        })


    # ========================================================
    # CREATE REPORT DIRECTORY
    # ========================================================

    report_folder = PROJECT_ROOT / "reports"
    report_folder.mkdir(exist_ok=True)


    # ========================================================
    # SAVE DETAILED CSV
    # ========================================================

    detailed_file = report_folder / "sdg_test_detailed_results.csv"

    with open(detailed_file, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=detailed_results[0].keys()
        )

        writer.writeheader()
        writer.writerows(detailed_results)


    # ========================================================
    # SAVE SUMMARY CSV
    # ========================================================

    summary_file = report_folder / "sdg_test_summary.csv"

    with open(summary_file, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=summary_results[0].keys()
        )

        writer.writeheader()
        writer.writerows(summary_results)


    # ========================================================
    # CALCULATE OVERALL RESULTS
    # ========================================================

    completed_results = [
        row for row in detailed_results
        if row["result"] != "ERROR"
    ]

    total_completed = len(completed_results)

    total_correct = sum(
        row["result"] == "CORRECT"
        for row in completed_results
    )

    total_wrong = sum(
        row["result"] == "WRONG"
        for row in completed_results
    )

    total_exact = sum(
        row["exact_match"]
        for row in completed_results
    )

    total_errors = 170 - total_completed

    overall_hit_rate = (
        total_correct / total_completed
        if total_completed else 0
    )

    overall_exact_rate = (
        total_exact / total_completed
        if total_completed else 0
    )


    # ========================================================
    # GENERATE MARKDOWN REPORT
    # ========================================================

    report_file = report_folder / "sdg_classification_test_report.md"

    with open(report_file, "w", encoding="utf-8") as file:

        file.write("# SDG CLASSIFIER EVALUATION REPORT\n\n")

        file.write(
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        )

        file.write("## Overall Results\n\n")

        file.write(f"- Total test inputs: 170\n")
        file.write(f"- Completed predictions: {total_completed}\n")
        file.write(f"- Correct predictions: {total_correct}\n")
        file.write(f"- Wrong predictions: {total_wrong}\n")
        file.write(f"- Exact matches: {total_exact}\n")
        file.write(f"- Errors: {total_errors}\n")
        file.write(f"- Expected-label hit rate: {overall_hit_rate:.2%}\n")
        file.write(f"- Exact-match rate: {overall_exact_rate:.2%}\n\n")

        file.write("## SDG-wise Summary\n\n")

        file.write(
            "| SDG | Completed | Correct | Wrong | Exact | "
            "Hit Rate | Exact Rate | Errors |\n"
        )

        file.write(
            "|---|---:|---:|---:|---:|---:|---:|---:|\n"
        )

        for row in summary_results:

            file.write(
                f"| {row['expected_sdg']} "
                f"| {row['completed']} "
                f"| {row['correct']} "
                f"| {row['wrong']} "
                f"| {row['exact_matches']} "
                f"| {row['hit_rate']} "
                f"| {row['exact_match_rate']} "
                f"| {row['errors']} |\n"
            )

        file.write("\n## Wrong Predictions\n\n")

        file.write(
            "| Expected SDG | Input | Predicted SDGs | Input Text |\n"
        )

        file.write("|---:|---:|---|---|\n")

        for row in detailed_results:

            if row["result"] == "WRONG":

                safe_text = row["input_text"].replace("|", "\\|")

                file.write(
                    f"| {row['expected_sdg']} "
                    f"| {row['input_number']} "
                    f"| {row['predicted_sdgs'] or 'None'} "
                    f"| {safe_text} |\n"
                )

        file.write("\n## Interpretation and Limitations\n\n")

        file.write(
            "- These 170 manually written examples are supplementary smoke tests.\n"
        )

        file.write(
            "- They are not a representative or independently labelled benchmark.\n"
        )

        file.write(
            "- CORRECT means the intended SDG appears anywhere in the predictions.\n"
        )

        file.write(
            "- WRONG means the intended SDG does not appear in the predictions.\n"
        )

        file.write(
            "- Exact match means the model predicts only the intended SDG.\n"
        )

        file.write(
            "- These results must not replace the official held-out UNDP test evaluation.\n"
        )

        file.write(
            "- This script tests classification only, not campaign quality or Docker.\n"
        )


    # ========================================================
    # DISPLAY FINAL RESULTS
    # ========================================================

    print("\n\n======================================")
    print("       FINAL EVALUATION SUMMARY")
    print("======================================")

    print(f"Total inputs: 170")
    print(f"Completed predictions: {total_completed}")
    print(f"Correct predictions: {total_correct}")
    print(f"Wrong predictions: {total_wrong}")
    print(f"Exact matches: {total_exact}")
    print(f"Errors: {total_errors}")

    print(f"\nExpected-label hit rate: {overall_hit_rate:.2%}")
    print(f"Exact-match rate: {overall_exact_rate:.2%}")

    print("\nReports generated successfully:")

    print(detailed_file)
    print(summary_file)
    print(report_file)

    print("\nEvaluation completed.")


if __name__ == "__main__":
    main()