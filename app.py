
import streamlit as st
from matching import match_schemes

st.set_page_config(
    page_title="SchemeSaathi AI",
    page_icon="🤝",
    layout="wide"
)

# Header
st.title("🤝 SchemeSaathi AI")
st.subheader("Your Guide to Government Schemes 🇮🇳")

st.write(
    "Discover government schemes that may suit "
    "your profile through a simple guided search."
)

st.divider()

# Important notice
st.info(
    "Prototype notice: Results are potential matches only. "
    "Always verify eligibility and current availability "
    "on official government websites."
)

# Profile form
st.header("📝 Tell Us About Yourself")

with st.form("scheme_form"):
    col1, col2 = st.columns(2)

    with col1:
        state = st.selectbox(
            "Select your state",
            ["Andhra Pradesh", "Telangana", "Other"]
        )

        age = st.number_input(
            "Applicant age (years)",
            min_value=1,
            max_value=100,
            value=18,
            step=1
        )

        category = st.selectbox(
            "Applicant category",
            [
                "Women entrepreneur",
                "SC",
                "ST",
                "General",
                "Student"
            ]
        )

    with col2:
        business_type = st.selectbox(
            "Business type",
            ["Retail", "Manufacturing", "Services", "Other"]
        )

        stage = st.selectbox(
            "Current stage",
            [
                "Planning to start",
                "Existing business",
                "Studying"
            ]
        )

    submitted = st.form_submit_button(
        "🔎 Find Suitable Schemes",
        use_container_width=True
    )

# Matching results
if submitted:
    user = {
        "state": state,
        "age": age,
        "category": category,
        "business_type": business_type,
        "stage": stage
    }

    results = match_schemes(user)

    st.divider()
    st.header("🎯 Your Matching Results")

    if results:
        st.success(
            f"We found {len(results)} potential match(es)!"
        )

        for scheme in results:
            with st.container(border=True):
                st.subheader(f"🏛️ {scheme['name']}")

                st.caption(
                    "Potential match — eligibility not confirmed"
                )

                st.markdown("#### ✨ Benefits")
                st.write(
                    scheme.get(
                        "benefits",
                        "Check the official scheme website."
                    )
                )

               
                st.warning(
                    scheme.get(
                        "status",
                        "Verify current availability officially."
                    )
                )

                st.link_button(
                    "🌐 Visit Official Website",
                    scheme["link"],
                    use_container_width=True
                )

    else:
        st.warning(
            "No potential matches found in our current dataset. "
            "Try different profile details or explore official portals."
        )

# Footer
st.divider()




# SchemeSaathi AI Chat Assistant
st.divider()
st.header("🤖 Ask SchemeSaathi")
st.write(
    "Ask a question about government schemes, "
    "documents, or how to apply."
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input(
    "Example: What documents are needed for PMEGP?"
)

if question:
    st.session_state.chat_history.append({
        "role": "user",
        "content": question
    })

    text = question.lower()

    if any(word in text for word in ["document", "papers", "certificate"]):
        answer = (
            "Required documents depend on the scheme. They may include "
            "identity proof, bank details, income or category certificates, "
            "and a project report for some business schemes. Check the official portal."
        )

    elif any(word in text for word in ["apply", "application", "register"]):
        answer = (
            "Visit the official website listed on the scheme card. "
            "Check eligibility, prepare the required documents, and "
            "follow the portal's application instructions."
        )

    elif any(word in text for word in ["woman", "women", "female", "entrepreneur"]):
        answer = (
            "Women entrepreneurs may be eligible for government support "
            "depending on their profile and business plan. Explore "
            "https://www.myscheme.gov.in/ and verify current eligibility."
        )

    elif any(word in text for word in ["andhra pradesh", "telangana", "my state"]):
        answer = (
            "State-specific schemes may be available. Explore "
            "https://www.myscheme.gov.in/ and verify details with "
            "the relevant official department."
        )

    elif any(word in text for word in ["existing business", "already started", "business owner"]):
        answer = (
            "Support for existing businesses depends on the scheme and "
            "applicant eligibility. Explore https://www.myscheme.gov.in/ "
            "for possible options."
        )

    elif any(word in text for word in ["student", "scholarship", "study"]):
        answer = (
            "Students can explore scholarships at "
            "https://scholarships.gov.in/. Eligibility and application "
            "dates vary by scholarship."
        )

    elif any(word in text for word in ["pmegp", "business", "loan", "shop"]):
        answer = (
            "PMEGP supports eligible new micro-enterprises through a "
            "bank-linked programme. Check current rules at "
            "https://www.kviconline.gov.in/pmegpeportal/"
        )

    else:
        answer = (
            "I can answer basic questions about scholarships, business "
            "schemes, documents, and applications. Try asking about PMEGP, "
            "women entrepreneurs, scholarships, or required documents. "
            "Please verify details on official portals."
        )

    st.session_state.chat_history.append({
        "role": "assistant",
        "content": answer
    })

    st.rerun()

# Footer
st.caption(
    "SchemeSaathi AI | Hackathon Prototype | "
    "Please verify scheme eligibility and availability officially."
)
