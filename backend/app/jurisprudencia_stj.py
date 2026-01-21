import requests
from bs4 import BeautifulSoup
import re
from typing import List, Dict

class STJJurisprudenciaService:
    """
    Serviço para buscar jurisprudências REAIS do STJ
    """
    
    def __init__(self):
        self.base_url = "https://scon.stj.jus.br/SCON/jurisprudencia/toc.jsp"
        self.search_url = "https://scon.stj.jus.br/SCON/SearchBRS"
    
    def buscar_jurisprudencia(self, tema: str, limit: int = 5) -> List[Dict]:
        """
        Busca jurisprudências reais no STJ
        
        Args:
            tema: Tema da busca (ex: "dano moral atraso voo")
            limit: Quantidade máxima de resultados
            
        Returns:
            Lista de jurisprudências com dados reais
        """
        try:
            # Parâmetros da consulta (formato do STJ)
            params = {
                'action': 'QUERY',
                'base': 'JURISPRUDENCIA',
                'livre': tema,  # Termo de busca
                'operador': 'E',
                'b': '1',
                'thesaurus': 'JURIDICO',
                'p': 'true',
                'l': str(limit),
                'i': '1'
            }
            
            # Faz a requisição
            response = requests.get(
                self.search_url,
                params=params,
                timeout=15,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                }
            )
            
            if response.status_code != 200:
                print(f"❌ Erro na busca: {response.status_code}")
                return []
            
            # Parse do HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extrai as jurisprudências
            jurisprudencias = []
            resultados = soup.find_all('div', class_='jurisprudenciaResult')
            
            for resultado in resultados[:limit]:
                try:
                    # Extrai dados
                    numero = self._extrair_numero_processo(resultado)
                    ementa = self._extrair_ementa(resultado)
                    relator = self._extrair_relator(resultado)
                    data = self._extrair_data(resultado)
                    url = self._extrair_url(resultado)
                    
                    if ementa:  # Só adiciona se tiver ementa
                        jurisprudencias.append({
                            'tribunal': 'STJ',
                            'numero': numero or 'Não informado',
                            'data': data or 'Data não disponível',
                            'relator': relator or 'Relator não informado',
                            'ementa': ementa,
                            'url': url or 'https://scon.stj.jus.br'
                        })
                except Exception as e:
                    print(f"⚠️ Erro ao processar resultado: {e}")
                    continue
            
            print(f"✅ {len(jurisprudencias)} jurisprudências encontradas")
            return jurisprudencias
            
        except Exception as e:
            print(f"❌ Erro geral na busca: {e}")
            return []
    
    def _extrair_numero_processo(self, elemento) -> str:
        """Extrai o número do processo"""
        try:
            numero_elem = elemento.find('span', class_='processo')
            if numero_elem:
                return numero_elem.get_text(strip=True)
        except:
            pass
        return None
    
    def _extrair_ementa(self, elemento) -> str:
        """Extrai a ementa"""
        try:
            ementa_elem = elemento.find('p', class_='ementa')
            if ementa_elem:
                texto = ementa_elem.get_text(strip=True)
                # Limita a 500 caracteres para não ficar muito grande
                return texto[:500] + '...' if len(texto) > 500 else texto
        except:
            pass
        return None
    
    def _extrair_relator(self, elemento) -> str:
        """Extrai o nome do relator"""
        try:
            relator_elem = elemento.find('span', class_='relator')
            if relator_elem:
                return relator_elem.get_text(strip=True).replace('Rel. ', '')
        except:
            pass
        return None
    
    def _extrair_data(self, elemento) -> str:
        """Extrai a data do julgamento"""
        try:
            data_elem = elemento.find('span', class_='data')
            if data_elem:
                return data_elem.get_text(strip=True)
        except:
            pass
        return None
    
    def _extrair_url(self, elemento) -> str:
        """Extrai o link para o inteiro teor"""
        try:
            link_elem = elemento.find('a', href=True)
            if link_elem:
                return 'https://scon.stj.jus.br' + link_elem['href']
        except:
            pass
        return None