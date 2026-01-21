# 🔍 SCRIPT PARA VERIFICAR QUAIS IDs ESTÃO FALTANDO
# Cole este código e rode para ver quais templates faltam

from pecas_juridicas import PECAS_JURIDICAS
from templates_especificos import gerar_template_especifico

print("🔍 VERIFICANDO IDs DAS PEÇAS...\n")
print("=" * 80)

ids_sem_template = []
ids_com_template = []

for area_id, area_data in PECAS_JURIDICAS.items():
    print(f"\n📂 ÁREA: {area_data['nome']}")
    print("-" * 80)
    
    for peca in area_data['pecas']:
        peca_id = peca['id']
        peca_nome = peca['nome']
        
        # Testar se o template existe
        try:
            resultado = gerar_template_especifico(peca_id, area_id, {})
            
            if resultado.startswith('[ERRO:'):
                print(f"❌ SEM TEMPLATE: {peca_id} ({peca_nome})")
                ids_sem_template.append({
                    'id': peca_id,
                    'nome': peca_nome,
                    'area': area_id
                })
            else:
                print(f"✅ COM TEMPLATE: {peca_id}")
                ids_com_template.append(peca_id)
        except Exception as e:
            print(f"❌ ERRO: {peca_id} - {str(e)}")
            ids_sem_template.append({
                'id': peca_id,
                'nome': peca_nome,
                'area': area_id
            })

print("\n" + "=" * 80)
print(f"\n📊 RESUMO:")
print(f"✅ Com template: {len(ids_com_template)}")
print(f"❌ Sem template: {len(ids_sem_template)}")

if ids_sem_template:
    print("\n🚨 FALTAM TEMPLATES PARA:")
    print("-" * 80)
    for item in ids_sem_template:
        print(f"ID: {item['id']}")
        print(f"   Nome: {item['nome']}")
        print(f"   Área: {item['area']}")
        print()