import g4f

response = g4f.ChatCompletion.create(
    model=g4f.models.default,
    messages=[{
    	"role": "user", 
    	"content": "Regenerate this text with seo friendly way for professional content writing *Requirement Analysis**: Understanding and documenting the requirements of the system, including functional requirements (what the system should do) and non-functional requirements (quality attributes such as performance, scalability, reliability, etc.).",
    }],
    timeout=300,  # in secs
)

print(f"Result:", response) 