
# SchemeSaathi AI - Scheme Matching
# SchemeSaathi AI - Scheme Matching

schemes = [
    {
        "name": "PMEGP - Prime Minister's Employment Generation Programme",
        "categories": [
            "Women entrepreneur",
            "SC",
            "ST",
            "General"
        ],
        "stages": ["Planning to start"],
        "states": ["All"],
        "benefits": (
            "Financial assistance through a bank-linked "
            "scheme for eligible new micro-enterprises. "
            "Assistance is subject to scheme rules and approval."
        ),
        "documents": [
            "Aadhaar or accepted identity documents",
            "PAN and applicant details, as required",
            "Project report",
            "Education certificate, if applicable",
            "Other documents required by the official portal"
        ],
        "status": "Check current guidelines and eligibility",
        "link": "https://www.kviconline.gov.in/pmegpeportal/"
    },
    {
        "name": "National Scholarship Portal",
        "categories": ["Student"],
        "stages": ["Studying"],
        "states": ["All"],
        "benefits": (
            "Find scholarship programmes. Benefits and "
            "eligibility depend on the individual scholarship."
        ),
        "documents": [
            "Identity details",
            "Academic records",
            "Income or category certificate, if required",
            "Bank details, if required"
        ],
        "status": "Check individual scholarship availability",
        "link": "https://scholarships.gov.in/"
    },
    {
        "name": "myScheme - Government Scheme Finder",
        "categories": [
            "Student",
            "Women entrepreneur",
            "SC",
            "ST",
            "General"
        ],
        "stages": [
            "Studying",
            "Planning to start",
            "Existing business"
        ],
        "states": ["All"],
        "benefits": (
            "Discover Central and State Government schemes "
            "based on personal details and eligibility."
        ),
        "documents": [
            "Requirements vary by scheme",
            "Check the official scheme details"
        ],
        "status": "Government scheme discovery portal",
        "link": "https://www.myscheme.gov.in/"
    }
]



def match_schemes(user):
    matches = []

    for scheme in schemes:
        reasons = []

        # Check applicant category
        if user["category"] in scheme["categories"]:
            reasons.append("Applicant category matches")

        # Check current stage
        if user["stage"] in scheme["stages"]:
            reasons.append("Applicant stage matches")

        # Check state
        if (
            "All" in scheme["states"]
            or user["state"] in scheme["states"]
        ):
            reasons.append("State requirement matches")

        # Check age only for PMEGP
        if "PMEGP" in scheme["name"]:
            if user.get("age", 0) >= 18:
                reasons.append("Age is 18 or above")
            else:
                continue

        # Return potential matches
        if len(reasons) >= 3:
            matches.append({
                "name": scheme["name"],
                "reasons": reasons,
                "link": scheme["link"],
                "benefits": scheme["benefits"],
                "documents": scheme["documents"],
                "status": scheme["status"],
                "verify": [
                    "Check official age requirements",
                    "Check income and category conditions",
                    "Confirm project requirements",
                    "Verify current application dates",
                    "Confirm eligibility on the official portal"
                ]
            })

    return matches



    


def main():
    print("Welcome to SchemeSaathi AI!")

    state = input("Enter your state: ")
    business_type = input("Enter your business type: ")
    stage = input("Enter business stage: ")
    category = input("Enter your category: ")

    user = {
        "state": state,
        "business_type": business_type,
        "stage": stage,
        "category": category
    }

    results = match_schemes(user)

    print("\n--- Matching Results ---")

    if results:
        for scheme in results:
            print("\nScheme:", scheme["name"])
            print("Why matched:", ", ".join(scheme["reasons"]))
            print("Details to verify:", ", ".join(scheme["verify"]))
            print("Official portal:", scheme["link"])
            print("Benefits:", scheme["benefits"])
            print("Required documents:", ", ".join(scheme["documents"]))
            print("Current status:", scheme["status"])
    else:
        print("No sample schemes matched.")


if __name__ == "__main__":
    main()








