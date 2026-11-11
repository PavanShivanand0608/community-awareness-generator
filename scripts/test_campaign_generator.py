
from src.campaign_generator import generate_campaign

# Sample community problem
problem = (
    "Children in rural areas lack access to quality education "
    "because of limited learning resources and school facilities."
)

# SDG 4 = Quality Education
sdg_id = 4

print("Generating awareness campaign...")

try:
    campaign = generate_campaign(problem, sdg_id)

    print("\n========== GENERATED CAMPAIGN ==========\n")

    for section, content in campaign.items():
        print(f"\n{section.replace('_', ' ').title()}:")

        if isinstance(content, list):
            for item in content:
                print(f"- {item}")
        else:
            print(content)

    print("\n========================================")

except Exception as error:
    print(f"Campaign generation failed: {error}")
