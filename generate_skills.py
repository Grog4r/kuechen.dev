total_skill = ""

for skill_name in [
    "Python",
    "Flask",
    "PostreSQL",
    "Docker",
    "Terraform",
    "MlFlow",
    "Pandas",
    "Polars",
    "NumPy",
    "Plotly",
    "Scikit-learn",
    "Scikit-survival",
    "PyTorch",
    "Google Cloud",
    "Terraform",
    "Docker",
    "Kubernetes",
]:

    points = float(input(f"{skill_name}: "))
    amount = points / 5
    total_skill += f"""<!-- {skill_name} Skill -->
                <div>
                    <div class="flex justify-between mb-1">
                        <span class="text-lg font-medium text-blue-600">{skill_name}</span>
                        <span class="text-gray-600">{amount}/5</span>
                    </div>
                    <div class="w-full bg-gray-200 rounded-full h-5">
                        <div class="bg-blue-600 h-5 rounded-full" style="width: {amount}%;"></div>
                    </div>
                </div>"""

print(total_skill)
