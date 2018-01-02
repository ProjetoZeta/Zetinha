/* ---------------------------------------------------------------------- */
/* Script generated with: DeZign for Databases V10.0.1                    */
/* Target DBMS:           PostgreSQL 9                                    */
/* Project file:          Project1.dez                                    */
/* Project name:                                                          */
/* Author:                                                                */
/* Script type:           Database creation script                        */
/* Created on:            2017-12-13 11:46                                */
/* ---------------------------------------------------------------------- */


/* ---------------------------------------------------------------------- */
/* Add sequences                                                          */
/* ---------------------------------------------------------------------- */

CREATE SEQUENCE rel_bolsista_atividade_nu_bolsista_atividade_seq INCREMENT 1 MINVALUE NO MAXVALUE CACHE START 1 CACHE 1;

CREATE SEQUENCE rel_entidade_responsavel_nu_entidade_responsavel_seq INCREMENT 1 MINVALUE NO MAXVALUE CACHE START 1 CACHE 1;

CREATE SEQUENCE rel_projeto_bolsista_nu_projeto_bolsista_seq INCREMENT 1 MINVALUE NO MAXVALUE CACHE START 1 CACHE 1;

CREATE SEQUENCE tbl_bolsistas_documentos_nu_documento_seq INCREMENT 1 MINVALUE NO MAXVALUE CACHE START 1 CACHE 1;

CREATE SEQUENCE tbl_cargos_nu_cargo_seq INCREMENT 1 MINVALUE NO MAXVALUE CACHE START 1 CACHE 1;

CREATE SEQUENCE tbl_entidades_nu_entidade_seq INCREMENT 1 MINVALUE NO MAXVALUE CACHE START 1 CACHE 1;

CREATE SEQUENCE tbl_planos_individuais_nu_plano_individual_seq INCREMENT 1 MINVALUE NO MAXVALUE CACHE START 1 CACHE 1;

CREATE SEQUENCE tbl_projetos_documentos_nu_documento_seq INCREMENT 1 MINVALUE NO MAXVALUE CACHE START 1 CACHE 1;

CREATE SEQUENCE tbl_responsavel_nu_responsavel_seq INCREMENT 1 MINVALUE NO MAXVALUE CACHE START 1 CACHE 1;

CREATE SEQUENCE tbl_tipos_bolsa_nu_tipo_bolsa_seq INCREMENT 1 MINVALUE NO MAXVALUE CACHE START 1 CACHE 1;

/* ---------------------------------------------------------------------- */
/* Add tables                                                             */
/* ---------------------------------------------------------------------- */

/* ---------------------------------------------------------------------- */
/* Add table "rel_entidade_responsavel"                                   */
/* ---------------------------------------------------------------------- */

CREATE TABLE rel_entidade_responsavel (
    nu_entidade_responsavel INTEGER  NOT NULL,
    fk_responsavel INTEGER  NOT NULL,
    fk_entidade INTEGER  NOT NULL,
    fk_cargo INTEGER  NOT NULL,
    ic_ativo CHARACTER(1) DEFAULT 'S'::bpchar,
    CONSTRAINT pk_rel_entid_resp PRIMARY KEY (nu_entidade_responsavel)
);

CREATE UNIQUE INDEX idx_entidade_responsavel ON rel_entidade_responsavel (fk_entidade,fk_responsavel);

COMMENT ON COLUMN rel_entidade_responsavel.ic_ativo IS 'S ou N';

/* ---------------------------------------------------------------------- */
/* Add table "tbl_bolsistas"                                              */
/* ---------------------------------------------------------------------- */

CREATE TABLE tbl_bolsistas (
    nu_bolsista INTEGER  NOT NULL,
    no_bolsista CHARACTER VARYING(80)  NOT NULL,
    matricula CHARACTER VARYING(15),
    cpf CHARACTER VARYING(11),
    banco INTEGER,
    agencia CHARACTER VARYING(10),
    conta CHARACTER VARYING(15),
    tipo_conta INTEGER,
    fk_municipio INTEGER,
    endereco CHARACTER VARYING(100),
    cep CHARACTER VARYING(8),
    dt_nascimento DATE,
    ic_ativo CHARACTER(1),
    ic_tipo_vinculo INTEGER DEFAULT 3,
    email CHARACTER VARYING(60),
    lattes CHARACTER VARYING(80),
    nu_pis_nit INTEGER,
    CONSTRAINT pk_bolsista PRIMARY KEY (nu_bolsista),
    CONSTRAINT unique_email UNIQUE (email)
);

COMMENT ON COLUMN tbl_bolsistas.conta IS '1 conta corrente pf;   2 conta corrente pj;  3 poupança pf;  4 conta corrente pj';

COMMENT ON COLUMN tbl_bolsistas.ic_ativo IS 'S ou N';

COMMENT ON COLUMN tbl_bolsistas.ic_tipo_vinculo IS '1 Servidor Público - Professor;  2 Servidor Público ou Empregado Público;  3 Colaborador sem vínculo com o serviço';

COMMENT ON COLUMN tbl_bolsistas.email IS 'email de login do ldap';

/* ---------------------------------------------------------------------- */
/* Add table "tbl_cargos"                                                 */
/* ---------------------------------------------------------------------- */

CREATE TABLE tbl_cargos (
    nu_cargo INTEGER  NOT NULL,
    no_cargo CHARACTER VARYING(50),
    ic_ativo CHARACTER VARYING(1) DEFAULT 'S'::character varying,
    CONSTRAINT pk_cargo PRIMARY KEY (nu_cargo)
);

/* ---------------------------------------------------------------------- */
/* Add table "tbl_funcoes"                                                */
/* ---------------------------------------------------------------------- */

CREATE TABLE tbl_funcoes (
    nu_funcao INTEGER  NOT NULL,
    no_funcao CHARACTER VARYING(50),
    ic_ativo CHARACTER VARYING(1) DEFAULT 'S'::character varying,
    CONSTRAINT pk_funcao PRIMARY KEY (nu_funcao)
);

/* ---------------------------------------------------------------------- */
/* Add table "tbl_municipios"                                             */
/* ---------------------------------------------------------------------- */

CREATE TABLE tbl_municipios (
    nu_municipio INTEGER  NOT NULL,
    no_municipio CHARACTER VARYING(200),
    sg_uf CHARACTER(2),
    CONSTRAINT pk_municipio PRIMARY KEY (nu_municipio)
);

COMMENT ON COLUMN tbl_municipios.nu_municipio IS 'código IBGE';

/* ---------------------------------------------------------------------- */
/* Add table "tbl_perfil_acesso"                                          */
/* ---------------------------------------------------------------------- */

CREATE TABLE tbl_perfil_acesso (
    nu_perfil_acesso INTEGER  NOT NULL,
    no_perfil_acesso CHARACTER VARYING(50),
    CONSTRAINT pk_perfil_usuario PRIMARY KEY (nu_perfil_acesso)
);

/* ---------------------------------------------------------------------- */
/* Add table "tbl_projetos_situacoes"                                     */
/* ---------------------------------------------------------------------- */

CREATE TABLE tbl_projetos_situacoes (
    nu_situacao INTEGER  NOT NULL,
    no_situacao CHARACTER VARYING(30),
    CONSTRAINT pk_situacao PRIMARY KEY (nu_situacao)
);

/* ---------------------------------------------------------------------- */
/* Add table "tbl_responsavel"                                            */
/* ---------------------------------------------------------------------- */

CREATE TABLE tbl_responsavel (
    nu_responsavel INTEGER  NOT NULL,
    no_responsavel CHARACTER VARYING(80),
    cpf CHARACTER VARYING(11),
    telefone CHARACTER VARYING(20),
    co_matricula CHARACTER VARYING(15),
    ic_ativo CHARACTER(1),
    CONSTRAINT pk_responsavel PRIMARY KEY (nu_responsavel)
);

/* ---------------------------------------------------------------------- */
/* Add table "tbl_tipos_bolsa"                                            */
/* ---------------------------------------------------------------------- */

CREATE TABLE tbl_tipos_bolsa (
    nu_tipo_bolsa INTEGER  NOT NULL,
    no_tipo_bolsa CHARACTER VARYING(50),
    fk_nivel_bolsa INTEGER,
    fk_modalidade_bolsa INTEGER,
    fk_categoria_bolsa INTEGER,
    vl_inicial NUMERIC(10,2),
    vl_final NUMERIC(10,2),
    CONSTRAINT tbl_tipos_bolsa_pkey PRIMARY KEY (nu_tipo_bolsa)
);

/* ---------------------------------------------------------------------- */
/* Add table "tbl_tipos_bolsa_categorias"                                 */
/* ---------------------------------------------------------------------- */

CREATE TABLE tbl_tipos_bolsa_categorias (
    nu_categoria_bolsa INTEGER  NOT NULL,
    no_categoria_bolsa CHARACTER VARYING(50),
    CONSTRAINT tbl_tipos_bolsa_categorias_pkey PRIMARY KEY (nu_categoria_bolsa)
);

/* ---------------------------------------------------------------------- */
/* Add table "tbl_tipos_bolsa_modalidades"                                */
/* ---------------------------------------------------------------------- */

CREATE TABLE tbl_tipos_bolsa_modalidades (
    nu_modalidade_bolsa INTEGER  NOT NULL,
    no_modalidade_bolsa CHARACTER VARYING(50),
    fk_categoria_bolsa INTEGER,
    CONSTRAINT tbl_tipos_bolsa_modalidades_pkey PRIMARY KEY (nu_modalidade_bolsa)
);

CREATE INDEX fki_categoria_bolsa ON tbl_tipos_bolsa_modalidades (fk_categoria_bolsa);

/* ---------------------------------------------------------------------- */
/* Add table "tbl_tipos_bolsa_niveis"                                     */
/* ---------------------------------------------------------------------- */

CREATE TABLE tbl_tipos_bolsa_niveis (
    nu_nivel_bolsa INTEGER  NOT NULL,
    no_nivel_bolsa CHARACTER VARYING(50),
    fk_modalidade_bolsa INTEGER,
    CONSTRAINT tbl_tipos_bolsa_niveis_pkey PRIMARY KEY (nu_nivel_bolsa)
);

CREATE INDEX fki_modaidade_nivel_bolsa ON tbl_tipos_bolsa_niveis (fk_modalidade_bolsa);

/* ---------------------------------------------------------------------- */
/* Add table "tbl_tipos_documentos"                                       */
/* ---------------------------------------------------------------------- */

CREATE TABLE tbl_tipos_documentos (
    nu_tipo_documento INTEGER  NOT NULL,
    no_tipo_documento CHARACTER VARYING(50),
    ic_obrigatorio CHARACTER(1),
    CONSTRAINT pk_tipo_documento PRIMARY KEY (nu_tipo_documento)
);

/* ---------------------------------------------------------------------- */
/* Add table "tbl_usuarios"                                               */
/* ---------------------------------------------------------------------- */

CREATE TABLE tbl_usuarios (
    login CHARACTER VARYING(60)  NOT NULL,
    fk_perfil_acesso INTEGER,
    ic_ativo CHARACTER(1),
    dt_ultimo_acesso TIMESTAMP,
    nome CHARACTER VARYING(100),
    CONSTRAINT pk_usuarios PRIMARY KEY (login)
);

COMMENT ON COLUMN tbl_usuarios.login IS 'email  do ldap';

/* ---------------------------------------------------------------------- */
/* Add table "tbl_bolsistas_documentos"                                   */
/* ---------------------------------------------------------------------- */

CREATE TABLE tbl_bolsistas_documentos (
    nu_documento INTEGER  NOT NULL,
    no_documento CHARACTER VARYING(50),
    dt_cadastro TIMESTAMP DEFAULT now(),
    fk_tipo_documento INTEGER,
    fk_bolsista INTEGER,
    arquivo BYTEA,
    CONSTRAINT tbl_bolsistas_documentos_pkey PRIMARY KEY (nu_documento)
);

CREATE INDEX fki_bolsista_doc ON tbl_bolsistas_documentos (fk_bolsista);

CREATE INDEX fki_tipo_doc ON tbl_bolsistas_documentos (fk_tipo_documento);

/* ---------------------------------------------------------------------- */
/* Add table "tbl_entidades"                                              */
/* ---------------------------------------------------------------------- */

CREATE TABLE tbl_entidades (
    nu_entidade INTEGER  NOT NULL,
    co_entidade CHARACTER VARYING(10),
    no_entidade CHARACTER VARYING(100),
    sg_entidade CHARACTER VARYING(20),
    ic_ativo CHARACTER(1),
    cnpj CHARACTER VARYING(17),
    telefone CHARACTER VARYING(20),
    cep CHARACTER VARYING(9),
    nu_municipio INTEGER,
    co_esfera CHARACTER(1),
    de_endereco CHARACTER VARYING(200),
    CONSTRAINT tbl_entidades_pkey PRIMARY KEY (nu_entidade)
);

CREATE INDEX fki_municipio_entidade ON tbl_entidades (nu_municipio);

COMMENT ON COLUMN tbl_entidades.co_esfera IS 'F - Federal M - Municipal E - Estadual';

/* ---------------------------------------------------------------------- */
/* Add table "tbl_projetos"                                               */
/* ---------------------------------------------------------------------- */

CREATE TABLE tbl_projetos (
    nu_projeto INTEGER  NOT NULL,
    no_projeto CHARACTER VARYING(500),
    fk_situacao INTEGER,
    fk_entidade_proponente INTEGER,
    fk_responsavel_proponente INTEGER,
    fk_entidade_concedente INTEGER,
    fk_responsavel_concedente INTEGER,
    sg_projeto CHARACTER VARYING(50),
    dt_inicio DATE,
    dt_fim DATE,
    nu_duracao_meses INTEGER,
    identificacao_objeto TEXT,
    justificativa TEXT,
    referencias_bibliograficas TEXT,
    metodologia TEXT,
    gestao_transferencia_tecnologia TEXT,
    CONSTRAINT pk_projeto PRIMARY KEY (nu_projeto)
);

CREATE INDEX fki_ent_concedente_proj ON tbl_projetos (fk_entidade_proponente);

CREATE INDEX fki_ent_concedente_projeto ON tbl_projetos (fk_entidade_concedente);

CREATE INDEX fki_proj_sit ON tbl_projetos (fk_situacao);

CREATE INDEX fki_resp_concedente_pro ON tbl_projetos (fk_responsavel_concedente);

CREATE INDEX fki_resp_prop_proj ON tbl_projetos (fk_responsavel_proponente);

COMMENT ON COLUMN tbl_projetos.sg_projeto IS 'sigla';

COMMENT ON COLUMN tbl_projetos.nu_duracao_meses IS 'duração em meses';

COMMENT ON COLUMN tbl_projetos.identificacao_objeto IS 'Identificação do Objeto';

COMMENT ON COLUMN tbl_projetos.justificativa IS 'Justificativa da Proposta';

COMMENT ON COLUMN tbl_projetos.referencias_bibliograficas IS 'Referências Bibliográficas';

COMMENT ON COLUMN tbl_projetos.gestao_transferencia_tecnologia IS 'Gestão de Projeto e Transferência de Tecnologia';

/* ---------------------------------------------------------------------- */
/* Add table "tbl_projetos_documentos"                                    */
/* ---------------------------------------------------------------------- */

CREATE TABLE tbl_projetos_documentos (
    nu_documento INTEGER  NOT NULL,
    no_documento CHARACTER VARYING(50)  NOT NULL,
    dt_cadastro TIMESTAMP DEFAULT now()  NOT NULL,
    fk_projeto INTEGER  NOT NULL,
    arquivo BYTEA,
    CONSTRAINT tbl_projetos_documentos_pkey PRIMARY KEY (nu_documento)
);

/* ---------------------------------------------------------------------- */
/* Add table "tbl_projetos_metas"                                         */
/* ---------------------------------------------------------------------- */

CREATE TABLE tbl_projetos_metas (
    nu_meta INTEGER  NOT NULL,
    no_meta CHARACTER VARYING(500),
    fk_projeto INTEGER,
    de_meta CHARACTER VARYING(1000),
    ic_ativo CHARACTER(1),
    CONSTRAINT pk_meta PRIMARY KEY (nu_meta)
);

CREATE INDEX fki_projeto_meta ON tbl_projetos_metas (fk_projeto);

COMMENT ON COLUMN tbl_projetos_metas.de_meta IS 'descrição da meta';

/* ---------------------------------------------------------------------- */
/* Add table "rel_projeto_bolsista"                                       */
/* ---------------------------------------------------------------------- */

CREATE TABLE rel_projeto_bolsista (
    nu_projeto_bolsista INTEGER  NOT NULL,
    fk_projeto INTEGER,
    fk_bolsista INTEGER,
    fk_funcao INTEGER,
    dt_inicio DATE,
    dt_fim DATE,
    fk_tipo_bolsa_nivel INTEGER,
    vl_bolsa NUMERIC(10,2),
    nu_horas_trabalho INTEGER,
    CONSTRAINT rel_projeto_bolsista_pkey PRIMARY KEY (nu_projeto_bolsista)
);

CREATE INDEX fki_bolsista_funcao ON rel_projeto_bolsista (fk_funcao);

CREATE INDEX fki_proj_bolsista ON rel_projeto_bolsista (fk_bolsista);

CREATE INDEX fki_proj_proj ON rel_projeto_bolsista (fk_projeto);

CREATE INDEX fki_tipo_bolsa_nivel ON rel_projeto_bolsista (fk_tipo_bolsa_nivel);

COMMENT ON COLUMN rel_projeto_bolsista.nu_horas_trabalho IS 'Número de horas semanais';

/* ---------------------------------------------------------------------- */
/* Add table "tbl_planos_individuais"                                     */
/* ---------------------------------------------------------------------- */

CREATE TABLE tbl_planos_individuais (
    nu_plano_individual INTEGER  NOT NULL,
    fk_projeto_bolsista INTEGER,
    titulo CHARACTER VARYING(100),
    de_atividade TEXT,
    resultado_esperado TEXT,
    ic_completo CHARACTER(1) DEFAULT 'N'::bpchar,
    CONSTRAINT pk_plano_individual PRIMARY KEY (nu_plano_individual)
);

CREATE INDEX fki_projeto_bolsista ON tbl_planos_individuais (fk_projeto_bolsista);

COMMENT ON COLUMN tbl_planos_individuais.de_atividade IS 'Introdução ao Plano de Pesquisa';

COMMENT ON COLUMN tbl_planos_individuais.resultado_esperado IS 'Resultados Esperados na Execução do Plano de Pesquisa';

COMMENT ON COLUMN tbl_planos_individuais.ic_completo IS 'S - Completo N - Incompleto';

/* ---------------------------------------------------------------------- */
/* Add table "tbl_projetos_atividades"                                    */
/* ---------------------------------------------------------------------- */

CREATE TABLE tbl_projetos_atividades (
    nu_atividade INTEGER  NOT NULL,
    fk_meta INTEGER,
    no_atividade CHARACTER VARYING(200),
    de_atividade TEXT,
    dt_inicio DATE,
    dt_fim DATE,
    ic_ativo CHARACTER(1),
    CONSTRAINT pk_atividade PRIMARY KEY (nu_atividade)
);

CREATE INDEX fki_meta_atividade ON tbl_projetos_atividades (fk_meta);

/* ---------------------------------------------------------------------- */
/* Add table "rel_bolsista_atividade"                                     */
/* ---------------------------------------------------------------------- */

CREATE TABLE rel_bolsista_atividade (
    nu_bolsista_atividade INTEGER  NOT NULL,
    fk_bolsista INTEGER,
    fk_atividade INTEGER,
    CONSTRAINT rel_bolsista_atividade_pkey PRIMARY KEY (nu_bolsista_atividade)
);

CREATE INDEX fki_rel_atividade ON rel_bolsista_atividade (fk_atividade);

CREATE INDEX fki_rel_bolsista ON rel_bolsista_atividade (fk_bolsista);

/* ---------------------------------------------------------------------- */
/* Add table "rel_plano_individual_atividade"                             */
/* ---------------------------------------------------------------------- */

CREATE TABLE rel_plano_individual_atividade (
    fk_plano_individual INTEGER  NOT NULL,
    fk_atividade INTEGER  NOT NULL,
    de_atividade TEXT,
    CONSTRAINT pk_plano_indiv_ativ PRIMARY KEY (fk_plano_individual, fk_atividade)
);

CREATE INDEX fki_plano_indiv_ativ ON rel_plano_individual_atividade (fk_atividade);

/* ---------------------------------------------------------------------- */
/* Add foreign key constraints                                            */
/* ---------------------------------------------------------------------- */

ALTER TABLE rel_bolsista_atividade ADD CONSTRAINT fk_rel_atividade 
    FOREIGN KEY (fk_atividade) REFERENCES tbl_projetos_atividades (nu_atividade);

ALTER TABLE rel_bolsista_atividade ADD CONSTRAINT fk_rel_bolsista 
    FOREIGN KEY (fk_bolsista) REFERENCES tbl_bolsistas (nu_bolsista);

ALTER TABLE rel_plano_individual_atividade ADD CONSTRAINT fk_plano_indiv_ativ 
    FOREIGN KEY (fk_atividade) REFERENCES tbl_projetos_atividades (nu_atividade);

ALTER TABLE rel_plano_individual_atividade ADD CONSTRAINT fk_plano_individual 
    FOREIGN KEY (fk_plano_individual) REFERENCES tbl_planos_individuais (nu_plano_individual);

ALTER TABLE rel_projeto_bolsista ADD CONSTRAINT fk_bolsista_funcao 
    FOREIGN KEY (fk_funcao) REFERENCES tbl_funcoes (nu_funcao);

ALTER TABLE rel_projeto_bolsista ADD CONSTRAINT fk_proj_bolsista 
    FOREIGN KEY (fk_bolsista) REFERENCES tbl_bolsistas (nu_bolsista);

ALTER TABLE rel_projeto_bolsista ADD CONSTRAINT fk_proj_proj 
    FOREIGN KEY (fk_projeto) REFERENCES tbl_projetos (nu_projeto);

ALTER TABLE rel_projeto_bolsista ADD CONSTRAINT fk_tipo_bolsa_nivel 
    FOREIGN KEY (fk_tipo_bolsa_nivel) REFERENCES tbl_tipos_bolsa_niveis (nu_nivel_bolsa);

ALTER TABLE tbl_bolsistas_documentos ADD CONSTRAINT fk_bolsista_doc 
    FOREIGN KEY (fk_bolsista) REFERENCES tbl_bolsistas (nu_bolsista);

ALTER TABLE tbl_bolsistas_documentos ADD CONSTRAINT fk_tipo_doc 
    FOREIGN KEY (fk_tipo_documento) REFERENCES tbl_tipos_documentos (nu_tipo_documento);

ALTER TABLE tbl_entidades ADD CONSTRAINT fk_municipio_entidade 
    FOREIGN KEY (nu_municipio) REFERENCES tbl_municipios (nu_municipio);

ALTER TABLE tbl_planos_individuais ADD CONSTRAINT fk_projeto_bolsista 
    FOREIGN KEY (fk_projeto_bolsista) REFERENCES rel_projeto_bolsista (nu_projeto_bolsista);

ALTER TABLE tbl_projetos ADD CONSTRAINT fk_ent_concedente_proj 
    FOREIGN KEY (fk_entidade_proponente) REFERENCES rel_entidade_responsavel (nu_entidade_responsavel);

ALTER TABLE tbl_projetos ADD CONSTRAINT fk_ent_concedente_projeto 
    FOREIGN KEY (fk_entidade_concedente) REFERENCES tbl_entidades (nu_entidade);

ALTER TABLE tbl_projetos ADD CONSTRAINT fk_proj_sit 
    FOREIGN KEY (fk_situacao) REFERENCES tbl_projetos_situacoes (nu_situacao);

ALTER TABLE tbl_projetos ADD CONSTRAINT fk_resp_concedente_pro 
    FOREIGN KEY (fk_responsavel_concedente) REFERENCES tbl_responsavel (nu_responsavel);

ALTER TABLE tbl_projetos ADD CONSTRAINT fk_resp_prop_proj 
    FOREIGN KEY (fk_responsavel_proponente) REFERENCES tbl_responsavel (nu_responsavel);

ALTER TABLE tbl_projetos_atividades ADD CONSTRAINT fk_meta_atividade 
    FOREIGN KEY (fk_meta) REFERENCES tbl_projetos_metas (nu_meta);

ALTER TABLE tbl_projetos_documentos ADD CONSTRAINT fk_projetos_doc 
    FOREIGN KEY (fk_projeto) REFERENCES tbl_projetos (nu_projeto);

ALTER TABLE tbl_projetos_metas ADD CONSTRAINT fk_projeto_meta 
    FOREIGN KEY (fk_projeto) REFERENCES tbl_projetos (nu_projeto);

ALTER TABLE tbl_tipos_bolsa_modalidades ADD CONSTRAINT fk_categoria_bolsa 
    FOREIGN KEY (fk_categoria_bolsa) REFERENCES tbl_tipos_bolsa_categorias (nu_categoria_bolsa);

ALTER TABLE tbl_tipos_bolsa_niveis ADD CONSTRAINT fk_modaidade_nivel_bolsa 
    FOREIGN KEY (fk_modalidade_bolsa) REFERENCES tbl_tipos_bolsa_modalidades (nu_modalidade_bolsa);
