from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()
APIKEY = os.getenv("GROQ_API_KEY")
client = Groq(
    api_key=APIKEY,
)

completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {
            "role": "user",
            "content": "can you explain what is the RTI\n"
        },
        {
            "role": "assistant",
            "content": "RTI stands for Response to Intervention (RTI), which is a multi-tiered approach to providing academic and behavioral support to students in schools. RTI is designed to facilitate early identification and support for students who are at risk of not meeting state or national academic standards.\n\nThe RTI process has three levels of intervention:\n\n1. **Tier 1**: Universal instruction: Here, all students receive high-quality, research-based instruction and support. This is the foundation of the RTI process and aims to ensure that all students have access to a high-quality education.\n\n2. **Tier 2**: Supplemental instruction: For students who may be at risk of not meeting state or national academic standards, Tier 2 interventions are designed to provide additional support. These interventions are targeted to specific skills or subgroups of students.\n\n3. **Tier 3**: Intensive intervention: Tier 3 is usually reserved for students who require intensive, individualized support to catch up or make significant progress. This level of support is typically provided by a small group or one-on-one with a trained teacher or intervention specialist.\n\nThe RTI process is designed to ensure that all students receive the right level of support to help them succeed academically. The key principles of RTI include:\n\n1. **Early Identification**: Identify students at risk of not meeting state or national academic standards early in the year, when possible, to provide targeted support.\n\n2. **Multi-Tiered Interventions**: Offer a range of interventions at different levels (Tiers 1, 2, and 3) to meet the diverse needs of students.\n\n3. **Monitoring and Progress**: Continuously monitor student progress and adjust interventions as needed to ensure that students make adequate progress.\n\n4. **Collaboration with Teachers and Parents**: Encourage collaboration among teachers, parents, and other support staff to ensure that students receive consistent support across settings.\n\nBy providing a well-structured and tiered approach to support, RTI aims to reduce the achievement gap, improve student outcomes, and ensure that all students have access to a high-quality education.\n\nWould you like me to elaborate on any specific aspects of RTI?"
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
