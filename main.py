import json


diplomadoId = input("Digite o ID do Diplomado: ")
diplomadoNome = input("Digite o Nome do Diplomado: ")
diplomadoNomeSocial = input("(Opcional) Digite o Nome Social do Diplomado: ")
if diplomadoNomeSocial == "":
    diplomadoNomeSocial = None
diplomadoSexo = input("Digite o Sexo do Diplomado [F ou M] : ")
diplomadoNacionalidade = input("Digite a Nacionalidade do Diplomado: ")
diplomadoNaturalidadeCodMunicipio = input("Digite o Código do Município de naturalidade do Diplomado: ")
diplomadoNaturalidadeNomeMunicipio = input("Digite o Nome do Município de naturalidade do Diplomado: ")
diplomadoNaturalidadeUF = input("Digite a UF do Município de naturalidade do Diplomado: ")
diplomadoNaturalidadeMunicipioEstrangeiro = input("Digite o Município de naturalidade estrangeira do Diplomado: ")
diplomadoCPF = input("Digite o Número do CPF do Diplomado: ")
diplomadoNumeroRG = input("Digite o Número do RG do Diplomado: ")

if diplomadoNumeroRG == "":
    diplomadoRG = None
    diplomadoTipoDocumento = input("Digite o Tipo de Documento do Diplomado: ")
    diplomadoIdentificador = input("Digite o Identificador do documento do Diplomado: ")
    outroDocumentoID = {
        "tipoDocumento": diplomadoTipoDocumento,
        "identificador": diplomadoIdentificador
    }

else:
    diplomadoUFRG = input("Digite a UF do RG do Diplomado: ")
    diplomadoOrgaoExpedidorRG = input("Digite o Orgão Expedidor do RG do Diplomado: ")
    diplomadoRG = {
        "numero": diplomadoNumeroRG,
        "uf": diplomadoUFRG,
        "orgaoExpedidor": diplomadoOrgaoExpedidorRG
    }
    outroDocumentoID = None

diplomadoDataNascimento = input("Digite a Data de Nascimento do Diplomado: ")
dadosDiplomaDataConclusao = input("Digite a Data de Conclusão do Diplomado: ")

dadosCursoNomeCurso = input("Digite o Nome do Curso: ")
dadosCursoCodCursoEMEC = input("Digite o Código do Curso EMEC: ")

dadosCursoinformacoesTramitacaoEmecEscolha = input("Tem Informações de Tramitação EMEC? Sim ou Não: ")
if dadosCursoinformacoesTramitacaoEmecEscolha == "Sim":
    dadosCursoinformacoesTramitacaoEmecNumeroProcesso = input("Digite o número do processo da Tramitação EMEC do curso: ")
    dadosCursoinformacoesTramitacaoEmecTipoProcesso = input("Digite o tipo do processo da Tramitação EMEC do curso: ")
    dadosCursoinformacoesTramitacaoEmecDataCadastro = input("Digite a data de cadastro da Tramitação EMEC do curso: ")
    dadosCursoinformacoesTramitacaoEmecDataProtocolo = input("Digite a data do protocolo da Tramitação EMEC do curso: ")

    dadosCursoinformacoesTramitacaoEmec = {
        "numeroProcesso": dadosCursoinformacoesTramitacaoEmecNumeroProcesso,
        "tipoProcesso": dadosCursoinformacoesTramitacaoEmecTipoProcesso,
        "dataCadastro": dadosCursoinformacoesTramitacaoEmecDataCadastro,
        "dataProtocolo": dadosCursoinformacoesTramitacaoEmecDataProtocolo
    }
else:
    dadosCursoinformacoesTramitacaoEmec = None

dadosCursoNomeHabilitacao = input("Digite o Nome de Habilitação do Curso: ")
dadosCursoModalidade = input("Digite a modalidade do Curso (Presencial, EAD, Semipresencial): ")
tituloConferidoTitulo = input("Digite o Título Conferido (Licenciado, Técnico, Bacharel, Médico, Psicólogo), se não for nenhum desses, deixe em branco: ")
tituloConferidoOutroTitulo = None
if tituloConferidoTitulo == "":
    tituloConferidoOutroTitulo = input("Digite o Título Conferido: ")
dadosCursoGrauConferido = input("Digite o Grau Conferido [Tecnólogo, Bacharelado, Licenciatura, Curso sequencial]: ")
dadosCursoLogradouro = input("Digite o Logradouro da IES: ")
dadosCursoNumero = input("Digite o Número da IES: ")
dadosCursoComplemento = input("Digite o Complemento da IES: ")
dadosCursoBairro = input("Digite o Bairro da IES: ")
dadosCursoCodMunicipio = input("Digite o Código do Município da IES: ")
dadosCursoNomeMunicipio = input("Digite o Nome do Município da IES: ")
dadosCursoUF = input("Digite a UF da IES: ")
dadosCursoNomeMunicipioEstrangeiro = input("Digite o Nome do Município Estrangeiro da IES: ")
dadosCursoCEP = input("Digite o CEP da IES: ")

dadosEmissoraPoloNome = input("Digite o nome do Polo do Curso: ")
dadosEmissoraPoloLogradouro = input("Digite o Logradouro do Polo do Curso: ")
dadosEmissoraPoloNumero = input("Digite o Número do Polo do Curso: ")
dadosEmissoraPoloComplemento = input("Digite o Complemento do Polo do Curso: ")
dadosEmissoraPoloBairro = input("Digite o Bairro do Polo do Curso: ")
dadosEmissoraPoloCodMunicipio = input("Digite o Código do Polo do Curso: ")
dadosEmissoraPoloNomeMunicipio = input("Digite o Nome do Município do Polo do Curso: ")
dadosEmissoraPoloUF = input("Digite a UF do Polo do Curso: ")
dadosEmissoraPoloNomeMunicipioEstrangeiro = input("Digite o Nome do Município Estrangeiro do Polo do Curso: ")
dadosEmissoraPoloCEP = input("Digite o CEP do Polo do Curso: ")
dadosPoloCodEMEC = input("Digite o Código EMEC do Polo do Curso: ")
dadosEmissoraPoloInformacoesTramitacaoEmecEscolha = input("Tem Informações de Tramitação EMEC? Sim ou Não: ")
if dadosEmissoraPoloInformacoesTramitacaoEmecEscolha == "Sim":
    dadosEmissoraPoloInformacoesTramitacaoEmecNumeroProcesso = input("Digite o número do processo da Tramitação EMEC do polo: ")
    dadosEmissoraPoloInformacoesTramitacaoEmecTipoProcesso = input("Digite o tipo do processo da Tramitação EMEC do polo: ")
    dadosEmissoraPoloInformacoesTramitacaoEmecDataCadastro = input("Digite a data de cadastro da Tramitação EMEC do polo: ")
    dadosEmissoraPoloInformacoesTramitacaoEmecDataProtocolo = input("Digite a data do protocolo da Tramitação EMEC do polo: ")

    dadosEmissoraPoloInformacoesTramitacaoEmec = {
        "numeroProcesso": dadosEmissoraPoloInformacoesTramitacaoEmecNumeroProcesso,
        "tipoProcesso": dadosEmissoraPoloInformacoesTramitacaoEmecTipoProcesso,
        "dataCadastro": dadosEmissoraPoloInformacoesTramitacaoEmecDataCadastro,
        "dataProtocolo": dadosEmissoraPoloInformacoesTramitacaoEmecDataProtocolo
    }
else:
    dadosEmissoraPoloInformacoesTramitacaoEmec = None

dadosEmissoraAutorizacaoTipo = input("Digite o Tipo de Autorização do Curso: ")
dadosEmissoraAutorizacaoNumero = input("Digite o Número da Autorização do Curso: ")
dadosEmissoraAutorizacaoData = input("Digite a Data da Autorização do Curso: ")
dadosEmissoraAutorizacaoVeiculoPublicacao = input("Digite o Veiculo de Publicação da Autorização do Curso: ")
dadosEmissoraAutorizacaoDataPublicacao = input("Digite a Data da Publicação Da Autorização do Curso: ")
dadosEmissoraAutorizacaoSecaoPublicacao = input("Digite a Seção da Publicação da Autorização do Curso: ")
dadosEmissoraAutorizacaoPaginaPublicacao = input("Digite a Página da Publicação da Autorização do Curso: ")
dadosEmissoraAutorizacaoNumeroDOU = input("Digite o Número do DOU da Autorização do Curso: ")
dadosEmissoraAutorizacaoInformacoesTramitacaoEmecEscolha = input("Tem Informações de Tramitação EMEC? Sim ou Não: ")
if dadosEmissoraAutorizacaoInformacoesTramitacaoEmecEscolha == "Sim":
    dadosEmissoraAutorizacaoInformacoesTramitacaoEmecNumeroProcesso = input("Digite o número do processo da Tramitação EMEC da Autorização: ")
    dadosEmissoraAutorizacaoInformacoesTramitacaoEmecTipoProcesso = input("Digite o tipo do processo da Tramitação EMEC da Autorização: ")
    dadosEmissoraAutorizacaoInformacoesTramitacaoEmecDataCadastro = input("Digite a data de cadastro da Tramitação EMEC da Autorização: ")
    dadosEmissoraAutorizacaoInformacoesTramitacaoEmecDataProtocolo = input("Digite a data do protocolo da Tramitação EMEC da Autorização: ")

    dadosEmissoraAutorizacaoInformacoesTramitacaoEmec = {
        "numeroProcesso": dadosEmissoraAutorizacaoInformacoesTramitacaoEmecNumeroProcesso,
        "tipoProcesso": dadosEmissoraAutorizacaoInformacoesTramitacaoEmecTipoProcesso,
        "dataCadastro": dadosEmissoraAutorizacaoInformacoesTramitacaoEmecDataCadastro,
        "dataProtocolo": dadosEmissoraAutorizacaoInformacoesTramitacaoEmecDataProtocolo
    }
else:
    dadosEmissoraAutorizacaoInformacoesTramitacaoEmec = None

dadosEmissoraReconhecimentoTipo = input("Digite o Tipo do Reconhecimento do Curso: ")
dadosEmissoraReconhecimentoNumero = input("Digite o Número do Reconhecimento do Curso: ")
dadosEmissoraReconhecimentoData = input("Digite a Data do Reconhecimento do Curso: ")
dadosEmissoraReconhecimentoVeiculoPublicacao = input("Digite o Veiculo de Publicação do Reconhecimento do Curso: ")
dadosEmissoraReconhecimentoDataPublicacao = input("Digite a Data da Publicação do Reconhecimento do Curso: ")
dadosEmissoraReconhecimentoSecaoPublicacao = input("Digite a Seção da Publicação do Reconhecimento do Curso: ")
dadosEmissoraReconhecimentoPaginaPublicacao = input("Digite a Página da Publicação do Reconhecimento do Curso: ")
dadosEmissoraReconhecimentoNumeroDOU = input("Digite o Número do DOU do Reconhecimento do Curso: ")
dadosEmissoraReconhecimentoInformacoesTramitacaoEmecEscolha = input("Tem Informações de Tramitação EMEC? Sim ou Não: ")
if dadosEmissoraReconhecimentoInformacoesTramitacaoEmecEscolha == "Sim":
    dadosEmissoraReconhecimentoInformacoesTramitacaoEmecNumeroProcesso = input("Digite o número do processo da Tramitação EMEC do Reconhecimento: ")
    dadosEmissoraReconhecimentoInformacoesTramitacaoEmecTipoProcesso = input("Digite o tipo do processo da Tramitação EMEC do Reconhecimento: ")
    dadosEmissoraReconhecimentoInformacoesTramitacaoEmecDataCadastro = input("Digite a data de cadastro da Tramitação EMEC do Reconhecimento: ")
    dadosEmissoraReconhecimentoInformacoesTramitacaoEmecDataProtocolo = input("Digite a data do protocolo da Tramitação EMEC do Reconhecimento: ")

    dadosEmissoraReconhecimentoInformacoesTramitacaoEmec = {
        "numeroProcesso": dadosEmissoraReconhecimentoInformacoesTramitacaoEmecNumeroProcesso,
        "tipoProcesso": dadosEmissoraReconhecimentoInformacoesTramitacaoEmecTipoProcesso,
        "dataCadastro": dadosEmissoraReconhecimentoInformacoesTramitacaoEmecDataCadastro,
        "dataProtocolo": dadosEmissoraReconhecimentoInformacoesTramitacaoEmecDataProtocolo
    }
else:
    dadosEmissoraReconhecimentoInformacoesTramitacaoEmec = None

dadosEmissoraRenovReconhecimentoTipo = input("Digite o Tipo da Renovação de Reconhecimento do Curso: ")
dadosEmissoraRenovReconhecimentoNumero = input("Digite o Número da Renovação de Reconhecimento do Curso: ")
dadosEmissoraRenovReconhecimentoData = input("Digite a Data da Renovação de Reconhecimento do Curso: ")
dadosEmissoraRenovReconhecimentoVeiculoPublicacao = input("Digite o Veiculo de Publicação da Renovação de Reconhecimento do Curso: ")
dadosEmissoraRenovReconhecimentoDataPublicacao = input("Digite a Data da Publicação da Renovação de Reconhecimento do Curso: ")
dadosEmissoraRenovReconhecimentoSecaoPublicacao = input("Digite a Seção da Publicação da Renovação de Reconhecimento do Curso: ")
dadosEmissoraRenovReconhecimentoPaginaPublicacao = input("Digite a Página da Publicação da Renovação de Reconhecimento do Curso: ")
dadosEmissoraRenovReconhecimentoNumeroDOU = input("Digite o Número do DOU da Renovação de Reconhecimento do Curso: ")
dadosEmissoraRenovReconhecimentoInformacoesTramitacaoEmecEscolha = input("Tem Informações de Tramitação EMEC? Sim ou Não: ")
if dadosEmissoraRenovReconhecimentoInformacoesTramitacaoEmecEscolha == "Sim":
    dadosEmissoraRenovReconhecimentoInformacoesTramitacaoEmecNumeroProcesso = input("Digite o número do processo da Tramitação EMEC da Renovação de Reconhecimento: ")
    dadosEmissoraRenovReconhecimentoInformacoesTramitacaoEmecTipoProcesso = input("Digite o tipo do processo da Tramitação EMEC da Renovação de Reconhecimento: ")
    dadosEmissoraRenovReconhecimentoInformacoesTramitacaoEmecDataCadastro = input("Digite a data de cadastro da Tramitação EMEC da Renovação de Reconhecimeno: ")
    dadosEmissoraRenovReconhecimentoInformacoesTramitacaoEmecDataProtocolo = input("Digite a data do protocolo da Tramitação EMEC da Renovação de Reconhecimento: ")

    dadosEmissoraRenovReconhecimentoInfoTramitacaoEmec = {
        "numeroProcesso": dadosEmissoraRenovReconhecimentoInformacoesTramitacaoEmecNumeroProcesso,
        "tipoProcesso": dadosEmissoraRenovReconhecimentoInformacoesTramitacaoEmecTipoProcesso,
        "dataCadastro": dadosEmissoraRenovReconhecimentoInformacoesTramitacaoEmecDataCadastro,
        "dataProtocolo": dadosEmissoraRenovReconhecimentoInformacoesTramitacaoEmecDataProtocolo
    }
else:
    dadosEmissoraRenovReconhecimentoInfoTramitacaoEmec = None




data = [
    {
        "diploma":
            {
                "dadosDiploma":
                    {
                        "diplomado":
                            {
                                "id": diplomadoId,
                                "nome": diplomadoNome,
                                "nomeSocial": diplomadoNomeSocial,
                                "sexo": diplomadoSexo,
                                "nacionalidade": diplomadoNacionalidade,
                                "naturalidade":
                                    {
                                        "codigoMunicipio": diplomadoNaturalidadeCodMunicipio,
                                        "nomeMunicipio": diplomadoNaturalidadeNomeMunicipio,
                                        "uf": diplomadoNaturalidadeUF,
                                        "nomeMunicipioEstrangeiro": diplomadoNaturalidadeMunicipioEstrangeiro
                                    },
                                "cpf": diplomadoCPF,
                                "rg": diplomadoRG,
                                "outroDocumentoIdentificacao": outroDocumentoID,
                                "dataNascimento": diplomadoDataNascimento
                            },
                        "dataConclusao": dadosDiplomaDataConclusao,
                        "dadosCurso":
                            {
                                "nomeCurso": dadosCursoNomeCurso,
                                "codigoCursoEMEC": dadosCursoCodCursoEMEC,
                                "informacoesTramitacaoEmec": dadosCursoinformacoesTramitacaoEmec,
                                "nomeHabilitacao": dadosCursoNomeHabilitacao,
                                "modalidade": dadosCursoModalidade,
                                "tituloConferido": {
                                    "titulo": tituloConferidoTitulo,
                                    "outroTitulo": tituloConferidoOutroTitulo
                                },
                                "grauConferido": dadosCursoGrauConferido,
                                "enderecoCurso": {
                                    "logradouro": dadosCursoLogradouro,
                                    "numero": dadosCursoNumero,
                                    "complemento": dadosCursoComplemento,
                                    "bairro": dadosCursoBairro,
                                    "codigoMunicipio": dadosCursoCodMunicipio,
                                    "nomeMunicipio": dadosCursoNomeMunicipio,
                                    "uf": dadosCursoUF,
                                    "nomeMunicipioEstrangeiro": dadosCursoNomeMunicipioEstrangeiro,
                                    "cep": dadosCursoCEP
                                },
                                "polo": {
                                    "nome": dadosEmissoraPoloNome,
                                    "endereco": {
                                        "logradouro": dadosEmissoraPoloLogradouro,
                                        "numero": dadosEmissoraPoloNumero,
                                        "complemento": dadosEmissoraPoloComplemento,
                                        "bairro": dadosEmissoraPoloBairro,
                                        "codigoMunicipio": dadosEmissoraPoloCodMunicipio,
                                        "nomeMunicipio": dadosEmissoraPoloNomeMunicipio,
                                        "uf": dadosEmissoraPoloUF,
                                        "nomeMunicipioEstrangeiro": dadosEmissoraPoloNomeMunicipioEstrangeiro,
                                        "cep": dadosEmissoraPoloCEP
                                    },
                                    "codigoEMEC": dadosPoloCodEMEC,
                                    "informacoesTramitacaoEmec": dadosEmissoraPoloInformacoesTramitacaoEmec
                                },
                                "autorizacao": {
                                    "tipo": dadosEmissoraAutorizacaoTipo,
                                    "numero": dadosEmissoraAutorizacaoNumero,
                                    "data": dadosEmissoraAutorizacaoData,
                                    "veiculoPublicacao": dadosEmissoraAutorizacaoVeiculoPublicacao,
                                    "dataPublicacao": dadosEmissoraAutorizacaoDataPublicacao,
                                    "secaoPublicacao": dadosEmissoraAutorizacaoSecaoPublicacao,
                                    "paginaPublicacao": dadosEmissoraAutorizacaoPaginaPublicacao,
                                    "numeroDOU": dadosEmissoraAutorizacaoNumeroDOU,
                                    "informacoesTramitacaoEmec": dadosEmissoraAutorizacaoInformacoesTramitacaoEmec
                                },
                                "reconhecimento": {
                                    "tipo": dadosEmissoraReconhecimentoTipo,
                                    "numero": dadosEmissoraReconhecimentoNumero,
                                    "data": dadosEmissoraReconhecimentoData,
                                    "veiculoPublicacao": dadosEmissoraReconhecimentoVeiculoPublicacao,
                                    "dataPublicacao": dadosEmissoraReconhecimentoDataPublicacao,
                                    "secaoPublicacao": dadosEmissoraReconhecimentoSecaoPublicacao,
                                    "paginaPublicacao": dadosEmissoraReconhecimentoPaginaPublicacao,
                                    "numeroDOU": dadosEmissoraReconhecimentoNumeroDOU,
                                    "informacoesTramitacaoEmec": dadosEmissoraReconhecimentoInformacoesTramitacaoEmec
                                },
                                "renovacaoReconhecimento": {
                                    "tipo": dadosEmissoraRenovReconhecimentoTipo,
                                    "numero": dadosEmissoraRenovReconhecimentoNumero,
                                    "data": dadosEmissoraRenovReconhecimentoData,
                                    "veiculoPublicacao": dadosEmissoraRenovReconhecimentoVeiculoPublicacao,
                                    "dataPublicacao": dadosEmissoraRenovReconhecimentoDataPublicacao,
                                    "secaoPublicacao": dadosEmissoraRenovReconhecimentoSecaoPublicacao,
                                    "paginaPublicacao": dadosEmissoraRenovReconhecimentoPaginaPublicacao,
                                    "numeroDOU": dadosEmissoraRenovReconhecimentoNumeroDOU,
                                    "informacoesTramitacaoEmec": dadosEmissoraRenovReconhecimentoInfoTramitacaoEmec
                                }
                            }
                    }
            }
    }
]

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file, indent=4)
    json_str = json.dumps(data, indent=4)
print(json_str)
