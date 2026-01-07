from flask import Flask, render_template, request

app = Flask(__name__)

# ส่วนของการคำนวณทางพันธุศาสตร์ (ทำนายหมู่เลือดลูก)
def get_child_blood_types(parent1, parent2):
    '''เนื่องจากหมู่เลือด A และ B เป็นลักษณะเด่น
       ส่วน O เป็นลักษณะด้อย เราจึงต้องจำลอง Genotype ที่เป็นไปได้ทั้งหมด 
       (เช่น A อาจเป็น AA หรือ AO) เพื่อความแม่นยำตามกฎของ Mendel'''
    genotypes_map = {
        'A': ['AA', 'AO'],
        'B': ['BB', 'BO'],
        'AB': ['AB'],
        'O': ['OO']
    }
    phenotype_map = {
        'AA': 'A', 'AO': 'A',
        'BB': 'B', 'BO': 'B',
        'AB': 'AB',
        'OO': 'O'
    }
    possible_child_phenotypes = set()
    '''ใช้ Nested Loop เพื่อจับคู่กับ Allele จากพ่อและแม่ทุกความเป็นไปได้
       เหมือนการเขียนตาราง Punnett Square'''
    for p1_geno in genotypes_map[parent1]:
        for p2_geno in genotypes_map[parent2]:
            for allele1 in p1_geno:
                for allele2 in p2_geno:
                    child_genotype = "".join(sorted(allele1 + allele2))
                    possible_child_phenotypes.add(phenotype_map[child_genotype])
    return sorted(list(possible_child_phenotypes))

# ส่วนของการให้และรับเลือด
'''โปรแกรมนี้คำนวณเฉพาะระบบ ABO system เท่านั้น
   ในการนำไปใช้จริงทางแพทย์ ต้องพิจารณา Rh Factor (+/-) 
   และ Cross-matching ร่วมด้วย'''
def get_compatible_donors(recipient):
    compatibility = {
        'A': ['A', 'O'],
        'B': ['B', 'O'],
        'AB': ['A', 'B', 'AB', 'O'],
        'O': ['O']
    }
    return compatibility.get(recipient, [])

def get_compatible_recipients(donor):
    compatibility = {
        'A': ['A', 'AB'],
        'B': ['B', 'AB'],
        'AB': ['AB'],
        'O': ['A', 'B', 'AB', 'O']
    }
    return compatibility.get(donor, [])

@app.route('/', methods=['GET', 'POST'])
def index():
    child_result = None
    donor_result = None
    recipient_result = None
    
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'predict_child':
            p1 = request.form['parent1']
            p2 = request.form['parent2']
            if p1 and p2:
                results = get_child_blood_types(p1, p2)
                child_result = f"🧬 Possible child blood types for parents {p1} & {p2}: {', '.join(results)}"

        elif action == 'find_donors':
            recipient = request.form['recipient']
            if recipient:
                results = get_compatible_donors(recipient)
                donor_result = f"👍 A person with blood type {recipient} can receive from: {', '.join(results)}"

        elif action == 'find_recipients':
            donor = request.form['donor']
            if donor:
                results = get_compatible_recipients(donor)
                recipient_result = f"❤️ A person with blood type {donor} can donate to: {', '.join(results)}"
                
    return render_template('index.html', child_result=child_result, donor_result=donor_result, recipient_result=recipient_result)

if __name__ == '__main__':
    app.run(debug=True)