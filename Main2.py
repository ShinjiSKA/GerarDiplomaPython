import json
from VerificaCPF import cpf_validate
from datetime import datetime
import os

UF = [ "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO" ]
Modalidade = [ "Presencial", "EAD" ]
ModalidadeNSF = [ "Presencial", "EAD", "Semipresencial" ]
TituloConferido = ["Licenciado", "Tecnólogo", "Técnico", "Bacharel", "Médico", "Psicólogo"]


isNsfEscolha = input("A Universidade está fora do sistema federal de ensino? ")
if isNsfEscolha == "Sim":
    isNsf = True
else:
    isNsf = False

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
while diplomadoNaturalidadeUF not in UF:
    diplomadoNaturalidadeUF = input("Digite a UF do Município de naturalidade do Diplomado: ")
diplomadoNaturalidadeMunicipioEstrangeiro = input("Digite o Município de naturalidade estrangeira do Diplomado: ")
if diplomadoNaturalidadeMunicipioEstrangeiro == "":
    diplomadoNaturalidadeMunicipioEstrangeiro = None

diplomadoCPF = input("Digite o Número do CPF do Diplomado: ")
cpf_validate(diplomadoCPF)
while cpf_validate(diplomadoCPF) == False:
    print("CPF Inválido! Tente Novamente")
    diplomadoCPF = input("Digite o Número do CPF do Diplomado: ")
    cpf_validate(diplomadoCPF)

diplomadoNumeroRG = input("Digite o Número do RG do Diplomado (Caso não tenha RG, deixe em branco): ")

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
    while diplomadoUFRG not in UF:
        diplomadoUFRG = input("Digite a UF do Município de naturalidade do Diplomado: ")
    diplomadoOrgaoExpedidorRG = input("Digite o Orgão Expedidor do RG do Diplomado: ")
    diplomadoRG = {
        "numero": diplomadoNumeroRG,
        "uf": diplomadoUFRG,
        "orgaoExpedidor": diplomadoOrgaoExpedidorRG
    }
    outroDocumentoID = None

diplomadoDataNascimento = input("Digite a Data de Nascimento do Diplomado (Exemplo: \"1900-12-30T00:00:00\"): ")
dadosDiplomaDataConclusao = input("Digite a Data de Conclusão do Diplomado (Exemplo: \"1900-12-30T00:00:00\"): ")

dadosCursoNomeCurso = input("Digite o Nome do Curso: ")
dadosCursoCodCursoEMEC = input("Digite o Código do Curso EMEC: ")

dadosCursoinformacoesTramitacaoEmecEscolha = input("Tem Informações de Tramitação EMEC? Sim ou Não: ")
if dadosCursoinformacoesTramitacaoEmecEscolha == "Sim":
    dadosCursoinformacoesTramitacaoEmecNumeroProcesso = input(
        "Digite o número do processo da Tramitação EMEC do curso: ")
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

nomesHabilitacao = []
datasHabilitacao = []

i = 0

while 1:
    i += 1
    nomeHabilitacao = input('Nome da Habilitação %d: ' %i)
    dataHabilitacao = input('Data da Habilitação %d: ' %i)
    nomesHabilitacao.append(nomeHabilitacao)
    datasHabilitacao.append(dataHabilitacao)
    outrahabilitacao = input("Há mais habilitações? ")
    if outrahabilitacao == 'Não':
        break


dadosCursoHabilitacao = {}


for a in range(i):
    dadosCursoHabilitacao[a] = {
        "nomeHabilitacao" : nomesHabilitacao[a],
        "dataHabilitacao" : datasHabilitacao[a]
    }
dadosCursoHabilitacoes = []
for key, value in dadosCursoHabilitacao.items():
    dadosCursoHabilitacoes.append(value)

dadosCursoEnfasesEscolha = input("Há enfase no curso? ")
if dadosCursoEnfasesEscolha == "Sim":
    dadosCursoEnfases = []
    i = 0
    while 1:
        i += 1
        dadosCursoEnfase = input("Digite a enfase do Curso %d: " % i)
        dadosCursoEnfases.append(dadosCursoEnfase)
        outraEnfase = input("Há mais enfases? ")
        if outraEnfase == 'Não':
            break
else:
    dadosCursoEnfases = None


if not isNsf:
    dadosCursoModalidadeNSF = None
    dadosCursoModalidade = {}
    dadosCursoModalidade = input("Digite a modalidade do Curso [ Presencial, EAD ]: ")
    while dadosCursoModalidade not in Modalidade:
        dadosCursoModalidade = input("Digite a modalidade do Curso [ Presencial, EAD ]: ")

else:
    dadosCursoModalidade = None
    dadosCursoModalidadeNSF = {}
    dadosCursoModalidadeNSF = input("Digite a modalidade do Curso [ Presencial, EAD, Semipresencial ]: ")
    while dadosCursoModalidadeNSF not in ModalidadeNSF:
        dadosCursoModalidadeNSF = input("Digite a modalidade do Curso [ Presencial, EAD, Semipresencial ]: ")



dadosCursoTituloConferido = input("Digite o Titulo Conferido do Diplomado [ Licenciado, Tecnólogo, Técnico, Bacharel, Médico, Psicólogo ]: ")
dadosCursoOutroTituloConferido = dadosCursoTituloConferido

if dadosCursoTituloConferido not in TituloConferido:
    dadosCursoOutroTituloConferido = None
else:
    dadosCursoOutroTituloConferido = None


dadosCursoGrauConferido = input("Digite o Grau Conferido do Curso [ Tecnólogo, Bacharelado, Licenciatura, Curso sequencial ]: ")


dadosCursoLogradouro = input("Digite o Logradouro do Endereço do Curso: ")
dadosCursoNumero = input("(Opcional) Digite o Numero do Endereço do Curso: ")
if dadosCursoNumero == "":
    dadosCursoNumero = None
dadosCursoComplemento = input("(Opcional) Digite o Complemento do Endereço do Curso: ")
if dadosCursoComplemento == "":
    dadosCursoComplemento = None
dadosCursoBairro = input("Digite o Bairro do Endereço do Curso: ")
dadosCursoCodMunicipio = input("Digite o Código do Município do Endereço do Curso: ")
dadosCursoNomeMunicipio = input("Digite o Nome do Município do Endereço do Curso: ")
dadosCursoUF = input("Digite a UF do Endereço do Curso: ")
while dadosCursoUF not in UF:
    dadosCursoUF = input("Digite a UF do Curso: ")
dadosCursoNomeMunicipioEstrangeiro = input("(Opcional) Digite o Nome do Município Estrangeiro do Endereço do Curso: ")
if dadosCursoNomeMunicipioEstrangeiro == "":
    dadosCursoNomeMunicipioEstrangeiro = None
dadosCursoCEP = input("Digite o CEP do Endereço do Curso: ")


dadosEmissoraPolo = input("Tem polo? Sim ou Não: ")
if dadosEmissoraPolo == "Sim":
    dadosEmissoraPoloNome = input("Digite o nome do Polo: ")
    dadosEmissoraPoloLogradouro = input("Digite o Logradouro do Endereço do Polo: ")
    dadosEmissoraPoloNumero = input("(Opcional) Digite o Numero do Endereço do Polo: ")
    if dadosEmissoraPoloNumero == "":
        dadosEmissoraPoloNumero = None
    dadosEmissoraPoloComplemento = input("(Opcional) Digite o Complemento do Endereço do Polo: ")
    if dadosEmissoraPoloComplemento == "":
        dadosEmissoraPoloComplemento = None
    dadosEmissoraPoloBairro = input("Digite o Bairro do Endereço do Polo: ")
    dadosEmissoraPoloCodMunicipio = input("Digite o Código do Município do Endereço do Polo: ")
    dadosEmissoraPoloNomeMunicipio = input("Digite o Nome do Município do Endereço do Polo: ")
    dadosEmissoraPoloUF = input("Digite a UF do Endereço do Polo: ")
    while dadosEmissoraPoloUF not in UF:
        dadosEmissoraPoloUF = input("Digite a UF do Polo: ")
    dadosEmissoraPoloNomeMunicipioEstrangeiro = input("(Opcional) Digite o Nome do Município Estrangeiro do Endereço do Polo: ")
    if dadosEmissoraPoloNomeMunicipioEstrangeiro == "":
        dadosEmissoraPoloNomeMunicipioEstrangeiro = None
    dadosEmissoraPoloCEP = input("Digite o CEP do Endereço do Polo: ")
    dadosPoloCodEMEC = input("Digite o Código EMEC do Polo: ")
    dadosEmissoraPoloInformacoesTramitacaoEmecEscolha = input("Tem Informações de Tramitação EMEC? Sim ou Não: ")
    if dadosEmissoraPoloInformacoesTramitacaoEmecEscolha == "Sim":
        dadosEmissoraPoloInformacoesTramitacaoEmecNumeroProcesso = input(
            "Digite o número do processo da Tramitação EMEC do Polo: ")
        dadosEmissoraPoloInformacoesTramitacaoEmecTipoProcesso = input(
            "Digite o tipo do processo da Tramitação EMEC do Polo: ")
        dadosEmissoraPoloInformacoesTramitacaoEmecDataCadastro = input(
            "Digite a data de cadastro da Tramitação EMEC do Polo: ")
        dadosEmissoraPoloInformacoesTramitacaoEmecDataProtocolo = input(
            "Digite a data do protocolo da Tramitação EMEC do Polo: ")

        dadosEmissoraPoloInformacoesTramitacaoEmec = {
            "numeroProcesso": dadosEmissoraPoloInformacoesTramitacaoEmecNumeroProcesso,
            "tipoProcesso": dadosEmissoraPoloInformacoesTramitacaoEmecTipoProcesso,
            "dataCadastro": dadosEmissoraPoloInformacoesTramitacaoEmecDataCadastro,
            "dataProtocolo": dadosEmissoraPoloInformacoesTramitacaoEmecDataProtocolo
        }
    else:
        dadosEmissoraPoloInformacoesTramitacaoEmec = None

    dadosEmissoraPolo = {
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
    }
else:
    dadosEmissoraPolo = None




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
                                "habilitacoes": dadosCursoHabilitacoes,
                                "enfases": dadosCursoEnfases,
                                "modalidade": dadosCursoModalidade,
                                "modalidadeNSF": dadosCursoModalidadeNSF,
                                "tituloConferido": {
                                    "titulo": dadosCursoTituloConferido,
                                    "outroTitulo": dadosCursoOutroTituloConferido
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
                                "polo": dadosEmissoraPolo
                            }
                    }
            },
        "isNsf": isNsf
    }
]
now = datetime.now()
date_time = now.strftime('%H%M%S')
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file, indent=4)
    json_str = json.dumps(data, indent=4)
print(json_str)

os.rename('data_file.json', f'Diploma{date_time}.json')
