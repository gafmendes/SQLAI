from langchain_ollama import OllamaLLM



class OllamaLLMSplit(OllamaLLM):
    def _generate(self, prompts, stop=None, run_manager=None, **kwargs):
        resposta = super()._generate(
            prompts,
            stop=stop,
            run_manager=run_manager,
            **kwargs
        )
        
        for grupo in resposta.generations:
            for geracao in grupo:
                geracao.text = self._strip_code(geracao.text)
        
        return resposta
    
    @staticmethod
    def _strip_code(resposta):    
        if "```" in resposta:
            partes = resposta.split("```")
            resposta = partes[1]
            
            if resposta.strip().lower().startswith("sql"):
                resposta = resposta.strip()[3:]
        
        return resposta.strip()
