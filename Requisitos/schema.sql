--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.6
-- Dumped by pg_dump version 9.5.6

-- Started on 2017-07-20 10:01:56

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 1 (class 3079 OID 12355)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2362 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_with_oids = false;

--
-- TOC entry 181 (class 1259 OID 39463)
-- Name: rel_bolsista_atividade; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE rel_bolsista_atividade (
    nu_bolsista_atividade integer NOT NULL,
    fk_bolsista integer,
    fk_atividade integer
);


--
-- TOC entry 182 (class 1259 OID 39466)
-- Name: rel_bolsista_atividade_nu_bolsista_atividade_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE rel_bolsista_atividade_nu_bolsista_atividade_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2363 (class 0 OID 0)
-- Dependencies: 182
-- Name: rel_bolsista_atividade_nu_bolsista_atividade_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE rel_bolsista_atividade_nu_bolsista_atividade_seq OWNED BY rel_bolsista_atividade.nu_bolsista_atividade;


--
-- TOC entry 183 (class 1259 OID 39468)
-- Name: rel_entidade_responsavel; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE rel_entidade_responsavel (
    nu_entidade_responsavel integer NOT NULL,
    fk_responsavel integer NOT NULL,
    fk_entidade integer NOT NULL,
    fk_cargo integer NOT NULL,
    ic_ativo character(1) DEFAULT 'S'::bpchar
);


--
-- TOC entry 2364 (class 0 OID 0)
-- Dependencies: 183
-- Name: COLUMN rel_entidade_responsavel.ic_ativo; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN rel_entidade_responsavel.ic_ativo IS 'S ou N';


--
-- TOC entry 184 (class 1259 OID 39472)
-- Name: rel_entidade_responsavel_nu_entidade_responsavel_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE rel_entidade_responsavel_nu_entidade_responsavel_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2365 (class 0 OID 0)
-- Dependencies: 184
-- Name: rel_entidade_responsavel_nu_entidade_responsavel_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE rel_entidade_responsavel_nu_entidade_responsavel_seq OWNED BY rel_entidade_responsavel.nu_entidade_responsavel;


--
-- TOC entry 185 (class 1259 OID 39474)
-- Name: rel_plano_individual_atividade; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE rel_plano_individual_atividade (
    fk_plano_individual integer NOT NULL,
    fk_atividade integer NOT NULL,
    de_atividade text
);


--
-- TOC entry 186 (class 1259 OID 39480)
-- Name: rel_projeto_bolsista; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE rel_projeto_bolsista (
    nu_projeto_bolsista integer NOT NULL,
    fk_projeto integer,
    fk_bolsista integer,
    fk_funcao integer,
    dt_inicio date,
    dt_fim date,
    fk_tipo_bolsa_nivel integer,
    vl_bolsa numeric(10,2),
    nu_horas_trabalho integer
);


--
-- TOC entry 2366 (class 0 OID 0)
-- Dependencies: 186
-- Name: COLUMN rel_projeto_bolsista.nu_horas_trabalho; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN rel_projeto_bolsista.nu_horas_trabalho IS 'Número de horas semanais';


--
-- TOC entry 187 (class 1259 OID 39483)
-- Name: rel_projeto_bolsista_nu_projeto_bolsista_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE rel_projeto_bolsista_nu_projeto_bolsista_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2367 (class 0 OID 0)
-- Dependencies: 187
-- Name: rel_projeto_bolsista_nu_projeto_bolsista_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE rel_projeto_bolsista_nu_projeto_bolsista_seq OWNED BY rel_projeto_bolsista.nu_projeto_bolsista;


--
-- TOC entry 212 (class 1259 OID 39641)
-- Name: tbl_bolsistas; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE tbl_bolsistas (
    nu_bolsista integer NOT NULL,
    no_bolsista character varying(80) NOT NULL,
    matricula character varying(15),
    cpf character varying(11),
    banco integer,
    agencia character varying(10),
    conta character varying(15),
    tipo_conta integer,
    fk_municipio integer,
    endereco character varying(100),
    cep character varying(8),
    dt_nascimento date,
    ic_ativo character(1),
    ic_tipo_vinculo integer DEFAULT 3,
    email character varying(60)
);


--
-- TOC entry 2368 (class 0 OID 0)
-- Dependencies: 212
-- Name: COLUMN tbl_bolsistas.conta; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN tbl_bolsistas.conta IS '1 conta corrente pf;  
2 conta corrente pj; 
3 poupança pf; 
4 conta corrente pj';


--
-- TOC entry 2369 (class 0 OID 0)
-- Dependencies: 212
-- Name: COLUMN tbl_bolsistas.ic_ativo; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN tbl_bolsistas.ic_ativo IS 'S ou N';


--
-- TOC entry 2370 (class 0 OID 0)
-- Dependencies: 212
-- Name: COLUMN tbl_bolsistas.ic_tipo_vinculo; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN tbl_bolsistas.ic_tipo_vinculo IS '1 Servidor Público - Professor;
 2 Servidor Público ou Empregado Público; 
3 Colaborador sem vínculo com o serviço';


--
-- TOC entry 2371 (class 0 OID 0)
-- Dependencies: 212
-- Name: COLUMN tbl_bolsistas.email; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN tbl_bolsistas.email IS 'email de login do ldap';


--
-- TOC entry 188 (class 1259 OID 39488)
-- Name: tbl_bolsistas_documentos; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE tbl_bolsistas_documentos (
    nu_documento integer NOT NULL,
    no_documento character varying(50),
    dt_cadastro timestamp without time zone DEFAULT now(),
    fk_tipo_documento integer,
    fk_bolsista integer,
    arquivo bytea
);


--
-- TOC entry 189 (class 1259 OID 39494)
-- Name: tbl_bolsistas_documentos_nu_documento_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE tbl_bolsistas_documentos_nu_documento_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2372 (class 0 OID 0)
-- Dependencies: 189
-- Name: tbl_bolsistas_documentos_nu_documento_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE tbl_bolsistas_documentos_nu_documento_seq OWNED BY tbl_bolsistas_documentos.nu_documento;


--
-- TOC entry 190 (class 1259 OID 39496)
-- Name: tbl_cargos; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE tbl_cargos (
    nu_cargo integer NOT NULL,
    no_cargo character varying(50),
    ic_ativo character varying(1) DEFAULT 'S'::character varying
);


--
-- TOC entry 191 (class 1259 OID 39500)
-- Name: tbl_cargos_nu_cargo_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE tbl_cargos_nu_cargo_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2373 (class 0 OID 0)
-- Dependencies: 191
-- Name: tbl_cargos_nu_cargo_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE tbl_cargos_nu_cargo_seq OWNED BY tbl_cargos.nu_cargo;


--
-- TOC entry 192 (class 1259 OID 39502)
-- Name: tbl_entidades; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE tbl_entidades (
    nu_entidade integer NOT NULL,
    co_entidade character varying(10),
    no_entidade character varying(100),
    sg_entidade character varying(20),
    ic_ativo character(1),
    cnpj character varying(17),
    telefone character varying(20),
    cep character varying(9),
    nu_municipio integer,
    co_esfera character(1),
    de_endereco character varying(200)
);


--
-- TOC entry 2374 (class 0 OID 0)
-- Dependencies: 192
-- Name: COLUMN tbl_entidades.co_esfera; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN tbl_entidades.co_esfera IS 'F - Federal
M - Municipal
E - Estadual';


--
-- TOC entry 193 (class 1259 OID 39505)
-- Name: tbl_entidades_nu_entidade_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE tbl_entidades_nu_entidade_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2375 (class 0 OID 0)
-- Dependencies: 193
-- Name: tbl_entidades_nu_entidade_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE tbl_entidades_nu_entidade_seq OWNED BY tbl_entidades.nu_entidade;


--
-- TOC entry 194 (class 1259 OID 39507)
-- Name: tbl_funcoes; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE tbl_funcoes (
    nu_funcao integer NOT NULL,
    no_funcao character varying(50),
    ic_ativo character varying(1) DEFAULT 'S'::character varying
);


--
-- TOC entry 195 (class 1259 OID 39510)
-- Name: tbl_municipios; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE tbl_municipios (
    nu_municipio integer NOT NULL,
    no_municipio character varying(200),
    sg_uf character(2)
);


--
-- TOC entry 2376 (class 0 OID 0)
-- Dependencies: 195
-- Name: COLUMN tbl_municipios.nu_municipio; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN tbl_municipios.nu_municipio IS 'código IBGE';


--
-- TOC entry 196 (class 1259 OID 39513)
-- Name: tbl_perfil_acesso; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE tbl_perfil_acesso (
    nu_perfil_acesso integer NOT NULL,
    no_perfil_acesso character varying(50)
);


--
-- TOC entry 197 (class 1259 OID 39516)
-- Name: tbl_planos_individuais; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE tbl_planos_individuais (
    nu_plano_individual integer NOT NULL,
    fk_projeto_bolsista integer,
    titulo character varying(100),
    de_atividade text,
    resultado_esperado text,
    ic_completo character(1) DEFAULT 'N'::bpchar
);


--
-- TOC entry 2377 (class 0 OID 0)
-- Dependencies: 197
-- Name: COLUMN tbl_planos_individuais.de_atividade; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN tbl_planos_individuais.de_atividade IS 'Introdução ao Plano de Pesquisa';


--
-- TOC entry 2378 (class 0 OID 0)
-- Dependencies: 197
-- Name: COLUMN tbl_planos_individuais.resultado_esperado; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN tbl_planos_individuais.resultado_esperado IS 'Resultados Esperados na Execução do Plano de Pesquisa';


--
-- TOC entry 2379 (class 0 OID 0)
-- Dependencies: 197
-- Name: COLUMN tbl_planos_individuais.ic_completo; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN tbl_planos_individuais.ic_completo IS 'S - Completo
N - Incompleto';


--
-- TOC entry 198 (class 1259 OID 39522)
-- Name: tbl_planos_individuais_nu_plano_individual_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE tbl_planos_individuais_nu_plano_individual_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2380 (class 0 OID 0)
-- Dependencies: 198
-- Name: tbl_planos_individuais_nu_plano_individual_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE tbl_planos_individuais_nu_plano_individual_seq OWNED BY tbl_planos_individuais.nu_plano_individual;


--
-- TOC entry 199 (class 1259 OID 39524)
-- Name: tbl_projetos; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE tbl_projetos (
    nu_projeto integer NOT NULL,
    no_projeto character varying(500),
    fk_situacao integer,
    fk_entidade_proponente integer,
    fk_responsavel_proponente integer,
    fk_entidade_concedente integer,
    fk_responsavel_concedente integer,
    sg_projeto character varying(50),
    dt_inicio date,
    dt_fim date,
    nu_duracao_meses integer,
    identificacao_objeto text,
    justificativa text,
    referencias_bibliograficas text,
    metodologia text,
    gestao_transferencia_tecnologia text
);


--
-- TOC entry 2381 (class 0 OID 0)
-- Dependencies: 199
-- Name: COLUMN tbl_projetos.sg_projeto; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN tbl_projetos.sg_projeto IS 'sigla';


--
-- TOC entry 2382 (class 0 OID 0)
-- Dependencies: 199
-- Name: COLUMN tbl_projetos.nu_duracao_meses; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN tbl_projetos.nu_duracao_meses IS 'duração em meses';


--
-- TOC entry 2383 (class 0 OID 0)
-- Dependencies: 199
-- Name: COLUMN tbl_projetos.identificacao_objeto; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN tbl_projetos.identificacao_objeto IS 'Identificação do Objeto';


--
-- TOC entry 2384 (class 0 OID 0)
-- Dependencies: 199
-- Name: COLUMN tbl_projetos.justificativa; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN tbl_projetos.justificativa IS 'Justificativa da Proposta';


--
-- TOC entry 2385 (class 0 OID 0)
-- Dependencies: 199
-- Name: COLUMN tbl_projetos.referencias_bibliograficas; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN tbl_projetos.referencias_bibliograficas IS 'Referências Bibliográficas';


--
-- TOC entry 2386 (class 0 OID 0)
-- Dependencies: 199
-- Name: COLUMN tbl_projetos.gestao_transferencia_tecnologia; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN tbl_projetos.gestao_transferencia_tecnologia IS 'Gestão de Projeto e Transferência de Tecnologia';


--
-- TOC entry 200 (class 1259 OID 39530)
-- Name: tbl_projetos_atividades; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE tbl_projetos_atividades (
    nu_atividade integer NOT NULL,
    fk_meta integer,
    no_atividade character varying(200),
    de_atividade text,
    dt_inicio date,
    dt_fim date,
    ic_ativo character(1)
);


--
-- TOC entry 214 (class 1259 OID 39680)
-- Name: tbl_projetos_documentos; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE tbl_projetos_documentos (
    nu_documento integer NOT NULL,
    no_documento character varying(50) NOT NULL,
    dt_cadastro timestamp without time zone DEFAULT now() NOT NULL,
    fk_projeto integer NOT NULL,
    arquivo bytea
);


--
-- TOC entry 213 (class 1259 OID 39678)
-- Name: tbl_projetos_documentos_nu_documento_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE tbl_projetos_documentos_nu_documento_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2387 (class 0 OID 0)
-- Dependencies: 213
-- Name: tbl_projetos_documentos_nu_documento_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE tbl_projetos_documentos_nu_documento_seq OWNED BY tbl_projetos_documentos.nu_documento;


--
-- TOC entry 201 (class 1259 OID 39536)
-- Name: tbl_projetos_metas; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE tbl_projetos_metas (
    nu_meta integer NOT NULL,
    no_meta character varying(500),
    fk_projeto integer,
    de_meta character varying(1000),
    ic_ativo character(1)
);


--
-- TOC entry 2388 (class 0 OID 0)
-- Dependencies: 201
-- Name: COLUMN tbl_projetos_metas.de_meta; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN tbl_projetos_metas.de_meta IS 'descrição da meta';


--
-- TOC entry 202 (class 1259 OID 39542)
-- Name: tbl_projetos_situacoes; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE tbl_projetos_situacoes (
    nu_situacao integer NOT NULL,
    no_situacao character varying(30)
);


--
-- TOC entry 203 (class 1259 OID 39545)
-- Name: tbl_responsavel; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE tbl_responsavel (
    nu_responsavel integer NOT NULL,
    no_responsavel character varying(80),
    cpf character varying(11),
    telefone character varying(20),
    co_matricula character varying(15),
    ic_ativo character(1)
);


--
-- TOC entry 204 (class 1259 OID 39548)
-- Name: tbl_responsavel_nu_responsavel_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE tbl_responsavel_nu_responsavel_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2389 (class 0 OID 0)
-- Dependencies: 204
-- Name: tbl_responsavel_nu_responsavel_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE tbl_responsavel_nu_responsavel_seq OWNED BY tbl_responsavel.nu_responsavel;


--
-- TOC entry 205 (class 1259 OID 39550)
-- Name: tbl_tipos_bolsa; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE tbl_tipos_bolsa (
    nu_tipo_bolsa integer NOT NULL,
    no_tipo_bolsa character varying(50),
    fk_nivel_bolsa integer,
    fk_modalidade_bolsa integer,
    fk_categoria_bolsa integer,
    vl_inicial numeric(10,2),
    vl_final numeric(10,2)
);


--
-- TOC entry 206 (class 1259 OID 39553)
-- Name: tbl_tipos_bolsa_categorias; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE tbl_tipos_bolsa_categorias (
    nu_categoria_bolsa integer NOT NULL,
    no_categoria_bolsa character varying(50)
);


--
-- TOC entry 207 (class 1259 OID 39556)
-- Name: tbl_tipos_bolsa_modalidades; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE tbl_tipos_bolsa_modalidades (
    nu_modalidade_bolsa integer NOT NULL,
    no_modalidade_bolsa character varying(50),
    fk_categoria_bolsa integer
);


--
-- TOC entry 208 (class 1259 OID 39559)
-- Name: tbl_tipos_bolsa_niveis; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE tbl_tipos_bolsa_niveis (
    nu_nivel_bolsa integer NOT NULL,
    no_nivel_bolsa character varying(50),
    fk_modalidade_bolsa integer
);


--
-- TOC entry 209 (class 1259 OID 39562)
-- Name: tbl_tipos_bolsa_nu_tipo_bolsa_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE tbl_tipos_bolsa_nu_tipo_bolsa_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2390 (class 0 OID 0)
-- Dependencies: 209
-- Name: tbl_tipos_bolsa_nu_tipo_bolsa_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE tbl_tipos_bolsa_nu_tipo_bolsa_seq OWNED BY tbl_tipos_bolsa.nu_tipo_bolsa;


--
-- TOC entry 210 (class 1259 OID 39564)
-- Name: tbl_tipos_documentos; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE tbl_tipos_documentos (
    nu_tipo_documento integer NOT NULL,
    no_tipo_documento character varying(50),
    ic_obrigatorio character(1)
);


--
-- TOC entry 211 (class 1259 OID 39567)
-- Name: tbl_usuarios; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE tbl_usuarios (
    login character varying(60) NOT NULL,
    fk_perfil_acesso integer,
    ic_ativo character(1),
    dt_ultimo_acesso timestamp with time zone,
    nome character varying(100)
);


--
-- TOC entry 2391 (class 0 OID 0)
-- Dependencies: 211
-- Name: COLUMN tbl_usuarios.login; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN tbl_usuarios.login IS 'email  do ldap';


--
-- TOC entry 2098 (class 2604 OID 39570)
-- Name: nu_bolsista_atividade; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY rel_bolsista_atividade ALTER COLUMN nu_bolsista_atividade SET DEFAULT nextval('rel_bolsista_atividade_nu_bolsista_atividade_seq'::regclass);


--
-- TOC entry 2100 (class 2604 OID 39571)
-- Name: nu_entidade_responsavel; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY rel_entidade_responsavel ALTER COLUMN nu_entidade_responsavel SET DEFAULT nextval('rel_entidade_responsavel_nu_entidade_responsavel_seq'::regclass);


--
-- TOC entry 2101 (class 2604 OID 39572)
-- Name: nu_projeto_bolsista; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY rel_projeto_bolsista ALTER COLUMN nu_projeto_bolsista SET DEFAULT nextval('rel_projeto_bolsista_nu_projeto_bolsista_seq'::regclass);


--
-- TOC entry 2102 (class 2604 OID 39573)
-- Name: nu_documento; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_bolsistas_documentos ALTER COLUMN nu_documento SET DEFAULT nextval('tbl_bolsistas_documentos_nu_documento_seq'::regclass);


--
-- TOC entry 2105 (class 2604 OID 39574)
-- Name: nu_cargo; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_cargos ALTER COLUMN nu_cargo SET DEFAULT nextval('tbl_cargos_nu_cargo_seq'::regclass);


--
-- TOC entry 2106 (class 2604 OID 39575)
-- Name: nu_entidade; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_entidades ALTER COLUMN nu_entidade SET DEFAULT nextval('tbl_entidades_nu_entidade_seq'::regclass);


--
-- TOC entry 2108 (class 2604 OID 39576)
-- Name: nu_plano_individual; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_planos_individuais ALTER COLUMN nu_plano_individual SET DEFAULT nextval('tbl_planos_individuais_nu_plano_individual_seq'::regclass);


--
-- TOC entry 2113 (class 2604 OID 39683)
-- Name: nu_documento; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_projetos_documentos ALTER COLUMN nu_documento SET DEFAULT nextval('tbl_projetos_documentos_nu_documento_seq'::regclass);


--
-- TOC entry 2110 (class 2604 OID 39577)
-- Name: nu_responsavel; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_responsavel ALTER COLUMN nu_responsavel SET DEFAULT nextval('tbl_responsavel_nu_responsavel_seq'::regclass);


--
-- TOC entry 2111 (class 2604 OID 39578)
-- Name: nu_tipo_bolsa; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_tipos_bolsa ALTER COLUMN nu_tipo_bolsa SET DEFAULT nextval('tbl_tipos_bolsa_nu_tipo_bolsa_seq'::regclass);


--
-- TOC entry 2322 (class 0 OID 39463)
-- Dependencies: 181
-- Data for Name: rel_bolsista_atividade; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2392 (class 0 OID 0)
-- Dependencies: 182
-- Name: rel_bolsista_atividade_nu_bolsista_atividade_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('rel_bolsista_atividade_nu_bolsista_atividade_seq', 1, false);


--
-- TOC entry 2324 (class 0 OID 39468)
-- Dependencies: 183
-- Data for Name: rel_entidade_responsavel; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2393 (class 0 OID 0)
-- Dependencies: 184
-- Name: rel_entidade_responsavel_nu_entidade_responsavel_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('rel_entidade_responsavel_nu_entidade_responsavel_seq', 1, false);


--
-- TOC entry 2326 (class 0 OID 39474)
-- Dependencies: 185
-- Data for Name: rel_plano_individual_atividade; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2327 (class 0 OID 39480)
-- Dependencies: 186
-- Data for Name: rel_projeto_bolsista; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2394 (class 0 OID 0)
-- Dependencies: 187
-- Name: rel_projeto_bolsista_nu_projeto_bolsista_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('rel_projeto_bolsista_nu_projeto_bolsista_seq', 1, false);


--
-- TOC entry 2353 (class 0 OID 39641)
-- Dependencies: 212
-- Data for Name: tbl_bolsistas; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2329 (class 0 OID 39488)
-- Dependencies: 188
-- Data for Name: tbl_bolsistas_documentos; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2395 (class 0 OID 0)
-- Dependencies: 189
-- Name: tbl_bolsistas_documentos_nu_documento_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('tbl_bolsistas_documentos_nu_documento_seq', 1, false);


--
-- TOC entry 2331 (class 0 OID 39496)
-- Dependencies: 190
-- Data for Name: tbl_cargos; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2396 (class 0 OID 0)
-- Dependencies: 191
-- Name: tbl_cargos_nu_cargo_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('tbl_cargos_nu_cargo_seq', 1, false);


--
-- TOC entry 2333 (class 0 OID 39502)
-- Dependencies: 192
-- Data for Name: tbl_entidades; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2397 (class 0 OID 0)
-- Dependencies: 193
-- Name: tbl_entidades_nu_entidade_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('tbl_entidades_nu_entidade_seq', 1, false);


--
-- TOC entry 2335 (class 0 OID 39507)
-- Dependencies: 194
-- Data for Name: tbl_funcoes; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2336 (class 0 OID 39510)
-- Dependencies: 195
-- Data for Name: tbl_municipios; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2337 (class 0 OID 39513)
-- Dependencies: 196
-- Data for Name: tbl_perfil_acesso; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO tbl_perfil_acesso (nu_perfil_acesso, no_perfil_acesso) VALUES (1, 'Administrador');
INSERT INTO tbl_perfil_acesso (nu_perfil_acesso, no_perfil_acesso) VALUES (2, 'Usuário');


--
-- TOC entry 2338 (class 0 OID 39516)
-- Dependencies: 197
-- Data for Name: tbl_planos_individuais; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2398 (class 0 OID 0)
-- Dependencies: 198
-- Name: tbl_planos_individuais_nu_plano_individual_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('tbl_planos_individuais_nu_plano_individual_seq', 1, false);


--
-- TOC entry 2340 (class 0 OID 39524)
-- Dependencies: 199
-- Data for Name: tbl_projetos; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2341 (class 0 OID 39530)
-- Dependencies: 200
-- Data for Name: tbl_projetos_atividades; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2355 (class 0 OID 39680)
-- Dependencies: 214
-- Data for Name: tbl_projetos_documentos; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2399 (class 0 OID 0)
-- Dependencies: 213
-- Name: tbl_projetos_documentos_nu_documento_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('tbl_projetos_documentos_nu_documento_seq', 1, false);


--
-- TOC entry 2342 (class 0 OID 39536)
-- Dependencies: 201
-- Data for Name: tbl_projetos_metas; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2343 (class 0 OID 39542)
-- Dependencies: 202
-- Data for Name: tbl_projetos_situacoes; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO tbl_projetos_situacoes (nu_situacao, no_situacao) VALUES (1, 'Ativo');
INSERT INTO tbl_projetos_situacoes (nu_situacao, no_situacao) VALUES (2, 'Finalizado');
INSERT INTO tbl_projetos_situacoes (nu_situacao, no_situacao) VALUES (3, 'Cancelado');
INSERT INTO tbl_projetos_situacoes (nu_situacao, no_situacao) VALUES (4, 'Elaboração');


--
-- TOC entry 2344 (class 0 OID 39545)
-- Dependencies: 203
-- Data for Name: tbl_responsavel; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2400 (class 0 OID 0)
-- Dependencies: 204
-- Name: tbl_responsavel_nu_responsavel_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('tbl_responsavel_nu_responsavel_seq', 1, false);


--
-- TOC entry 2346 (class 0 OID 39550)
-- Dependencies: 205
-- Data for Name: tbl_tipos_bolsa; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2347 (class 0 OID 39553)
-- Dependencies: 206
-- Data for Name: tbl_tipos_bolsa_categorias; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2348 (class 0 OID 39556)
-- Dependencies: 207
-- Data for Name: tbl_tipos_bolsa_modalidades; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2349 (class 0 OID 39559)
-- Dependencies: 208
-- Data for Name: tbl_tipos_bolsa_niveis; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2401 (class 0 OID 0)
-- Dependencies: 209
-- Name: tbl_tipos_bolsa_nu_tipo_bolsa_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('tbl_tipos_bolsa_nu_tipo_bolsa_seq', 1, false);


--
-- TOC entry 2351 (class 0 OID 39564)
-- Dependencies: 210
-- Data for Name: tbl_tipos_documentos; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2352 (class 0 OID 39567)
-- Dependencies: 211
-- Data for Name: tbl_usuarios; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2158 (class 2606 OID 39580)
-- Name: pk_atividade; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_projetos_atividades
    ADD CONSTRAINT pk_atividade PRIMARY KEY (nu_atividade);


--
-- TOC entry 2181 (class 2606 OID 39646)
-- Name: pk_bolsista; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_bolsistas
    ADD CONSTRAINT pk_bolsista PRIMARY KEY (nu_bolsista);


--
-- TOC entry 2136 (class 2606 OID 39584)
-- Name: pk_cargo; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_cargos
    ADD CONSTRAINT pk_cargo PRIMARY KEY (nu_cargo);


--
-- TOC entry 2141 (class 2606 OID 39586)
-- Name: pk_funcao; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_funcoes
    ADD CONSTRAINT pk_funcao PRIMARY KEY (nu_funcao);


--
-- TOC entry 2161 (class 2606 OID 39588)
-- Name: pk_meta; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_projetos_metas
    ADD CONSTRAINT pk_meta PRIMARY KEY (nu_meta);


--
-- TOC entry 2143 (class 2606 OID 39590)
-- Name: pk_municipio; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_municipios
    ADD CONSTRAINT pk_municipio PRIMARY KEY (nu_municipio);


--
-- TOC entry 2145 (class 2606 OID 39592)
-- Name: pk_perfil_usuario; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_perfil_acesso
    ADD CONSTRAINT pk_perfil_usuario PRIMARY KEY (nu_perfil_acesso);


--
-- TOC entry 2124 (class 2606 OID 39594)
-- Name: pk_plano_indiv_ativ; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY rel_plano_individual_atividade
    ADD CONSTRAINT pk_plano_indiv_ativ PRIMARY KEY (fk_plano_individual, fk_atividade);


--
-- TOC entry 2148 (class 2606 OID 39596)
-- Name: pk_plano_individual; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_planos_individuais
    ADD CONSTRAINT pk_plano_individual PRIMARY KEY (nu_plano_individual);


--
-- TOC entry 2155 (class 2606 OID 39598)
-- Name: pk_projeto; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_projetos
    ADD CONSTRAINT pk_projeto PRIMARY KEY (nu_projeto);


--
-- TOC entry 2121 (class 2606 OID 39600)
-- Name: pk_rel_entid_resp; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY rel_entidade_responsavel
    ADD CONSTRAINT pk_rel_entid_resp PRIMARY KEY (nu_entidade_responsavel);


--
-- TOC entry 2165 (class 2606 OID 39602)
-- Name: pk_responsavel; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_responsavel
    ADD CONSTRAINT pk_responsavel PRIMARY KEY (nu_responsavel);


--
-- TOC entry 2163 (class 2606 OID 39604)
-- Name: pk_situacao; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_projetos_situacoes
    ADD CONSTRAINT pk_situacao PRIMARY KEY (nu_situacao);


--
-- TOC entry 2177 (class 2606 OID 39606)
-- Name: pk_tipo_documento; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_tipos_documentos
    ADD CONSTRAINT pk_tipo_documento PRIMARY KEY (nu_tipo_documento);


--
-- TOC entry 2179 (class 2606 OID 39608)
-- Name: pk_usuarios; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_usuarios
    ADD CONSTRAINT pk_usuarios PRIMARY KEY (login);


--
-- TOC entry 2118 (class 2606 OID 39610)
-- Name: rel_bolsista_atividade_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY rel_bolsista_atividade
    ADD CONSTRAINT rel_bolsista_atividade_pkey PRIMARY KEY (nu_bolsista_atividade);


--
-- TOC entry 2130 (class 2606 OID 39612)
-- Name: rel_projeto_bolsista_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY rel_projeto_bolsista
    ADD CONSTRAINT rel_projeto_bolsista_pkey PRIMARY KEY (nu_projeto_bolsista);


--
-- TOC entry 2134 (class 2606 OID 39614)
-- Name: tbl_bolsistas_documentos_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_bolsistas_documentos
    ADD CONSTRAINT tbl_bolsistas_documentos_pkey PRIMARY KEY (nu_documento);


--
-- TOC entry 2139 (class 2606 OID 39616)
-- Name: tbl_entidades_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_entidades
    ADD CONSTRAINT tbl_entidades_pkey PRIMARY KEY (nu_entidade);


--
-- TOC entry 2185 (class 2606 OID 39689)
-- Name: tbl_projetos_documentos_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_projetos_documentos
    ADD CONSTRAINT tbl_projetos_documentos_pkey PRIMARY KEY (nu_documento);


--
-- TOC entry 2169 (class 2606 OID 39618)
-- Name: tbl_tipos_bolsa_categorias_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_tipos_bolsa_categorias
    ADD CONSTRAINT tbl_tipos_bolsa_categorias_pkey PRIMARY KEY (nu_categoria_bolsa);


--
-- TOC entry 2172 (class 2606 OID 39620)
-- Name: tbl_tipos_bolsa_modalidades_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_tipos_bolsa_modalidades
    ADD CONSTRAINT tbl_tipos_bolsa_modalidades_pkey PRIMARY KEY (nu_modalidade_bolsa);


--
-- TOC entry 2175 (class 2606 OID 39622)
-- Name: tbl_tipos_bolsa_niveis_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_tipos_bolsa_niveis
    ADD CONSTRAINT tbl_tipos_bolsa_niveis_pkey PRIMARY KEY (nu_nivel_bolsa);


--
-- TOC entry 2167 (class 2606 OID 39624)
-- Name: tbl_tipos_bolsa_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_tipos_bolsa
    ADD CONSTRAINT tbl_tipos_bolsa_pkey PRIMARY KEY (nu_tipo_bolsa);


--
-- TOC entry 2183 (class 2606 OID 39786)
-- Name: unique_email; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_bolsistas
    ADD CONSTRAINT unique_email UNIQUE (email);


--
-- TOC entry 2131 (class 1259 OID 39658)
-- Name: fki_bolsista_doc; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX fki_bolsista_doc ON tbl_bolsistas_documentos USING btree (fk_bolsista);


--
-- TOC entry 2125 (class 1259 OID 39748)
-- Name: fki_bolsista_funcao; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX fki_bolsista_funcao ON rel_projeto_bolsista USING btree (fk_funcao);


--
-- TOC entry 2170 (class 1259 OID 39724)
-- Name: fki_categoria_bolsa; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX fki_categoria_bolsa ON tbl_tipos_bolsa_modalidades USING btree (fk_categoria_bolsa);


--
-- TOC entry 2149 (class 1259 OID 39700)
-- Name: fki_ent_concedente_proj; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX fki_ent_concedente_proj ON tbl_projetos USING btree (fk_entidade_proponente);


--
-- TOC entry 2150 (class 1259 OID 39706)
-- Name: fki_ent_concedente_projeto; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX fki_ent_concedente_projeto ON tbl_projetos USING btree (fk_entidade_concedente);


--
-- TOC entry 2156 (class 1259 OID 39665)
-- Name: fki_meta_atividade; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX fki_meta_atividade ON tbl_projetos_atividades USING btree (fk_meta);


--
-- TOC entry 2173 (class 1259 OID 39730)
-- Name: fki_modaidade_nivel_bolsa; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX fki_modaidade_nivel_bolsa ON tbl_tipos_bolsa_niveis USING btree (fk_modalidade_bolsa);


--
-- TOC entry 2137 (class 1259 OID 39638)
-- Name: fki_municipio_entidade; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX fki_municipio_entidade ON tbl_entidades USING btree (nu_municipio);


--
-- TOC entry 2122 (class 1259 OID 39783)
-- Name: fki_plano_indiv_ativ; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX fki_plano_indiv_ativ ON rel_plano_individual_atividade USING btree (fk_atividade);


--
-- TOC entry 2126 (class 1259 OID 39736)
-- Name: fki_proj_bolsista; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX fki_proj_bolsista ON rel_projeto_bolsista USING btree (fk_bolsista);


--
-- TOC entry 2127 (class 1259 OID 39742)
-- Name: fki_proj_proj; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX fki_proj_proj ON rel_projeto_bolsista USING btree (fk_projeto);


--
-- TOC entry 2151 (class 1259 OID 39677)
-- Name: fki_proj_sit; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX fki_proj_sit ON tbl_projetos USING btree (fk_situacao);


--
-- TOC entry 2146 (class 1259 OID 39772)
-- Name: fki_projeto_bolsista; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX fki_projeto_bolsista ON tbl_planos_individuais USING btree (fk_projeto_bolsista);


--
-- TOC entry 2159 (class 1259 OID 39671)
-- Name: fki_projeto_meta; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX fki_projeto_meta ON tbl_projetos_metas USING btree (fk_projeto);


--
-- TOC entry 2115 (class 1259 OID 39760)
-- Name: fki_rel_atividade; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX fki_rel_atividade ON rel_bolsista_atividade USING btree (fk_atividade);


--
-- TOC entry 2116 (class 1259 OID 39766)
-- Name: fki_rel_bolsista; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX fki_rel_bolsista ON rel_bolsista_atividade USING btree (fk_bolsista);


--
-- TOC entry 2152 (class 1259 OID 39718)
-- Name: fki_resp_concedente_pro; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX fki_resp_concedente_pro ON tbl_projetos USING btree (fk_responsavel_concedente);


--
-- TOC entry 2153 (class 1259 OID 39712)
-- Name: fki_resp_prop_proj; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX fki_resp_prop_proj ON tbl_projetos USING btree (fk_responsavel_proponente);


--
-- TOC entry 2128 (class 1259 OID 39754)
-- Name: fki_tipo_bolsa_nivel; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX fki_tipo_bolsa_nivel ON rel_projeto_bolsista USING btree (fk_tipo_bolsa_nivel);


--
-- TOC entry 2132 (class 1259 OID 39652)
-- Name: fki_tipo_doc; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX fki_tipo_doc ON tbl_bolsistas_documentos USING btree (fk_tipo_documento);


--
-- TOC entry 2119 (class 1259 OID 39640)
-- Name: idx_entidade_responsavel; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX idx_entidade_responsavel ON rel_entidade_responsavel USING btree (fk_entidade, fk_responsavel);


--
-- TOC entry 2195 (class 2606 OID 39653)
-- Name: fk_bolsista_doc; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_bolsistas_documentos
    ADD CONSTRAINT fk_bolsista_doc FOREIGN KEY (fk_bolsista) REFERENCES tbl_bolsistas(nu_bolsista);


--
-- TOC entry 2192 (class 2606 OID 39743)
-- Name: fk_bolsista_funcao; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY rel_projeto_bolsista
    ADD CONSTRAINT fk_bolsista_funcao FOREIGN KEY (fk_funcao) REFERENCES tbl_funcoes(nu_funcao);


--
-- TOC entry 2205 (class 2606 OID 39719)
-- Name: fk_categoria_bolsa; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_tipos_bolsa_modalidades
    ADD CONSTRAINT fk_categoria_bolsa FOREIGN KEY (fk_categoria_bolsa) REFERENCES tbl_tipos_bolsa_categorias(nu_categoria_bolsa);


--
-- TOC entry 2199 (class 2606 OID 39695)
-- Name: fk_ent_concedente_proj; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_projetos
    ADD CONSTRAINT fk_ent_concedente_proj FOREIGN KEY (fk_entidade_proponente) REFERENCES rel_entidade_responsavel(nu_entidade_responsavel);


--
-- TOC entry 2200 (class 2606 OID 39701)
-- Name: fk_ent_concedente_projeto; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_projetos
    ADD CONSTRAINT fk_ent_concedente_projeto FOREIGN KEY (fk_entidade_concedente) REFERENCES tbl_entidades(nu_entidade);


--
-- TOC entry 2203 (class 2606 OID 39660)
-- Name: fk_meta_atividade; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_projetos_atividades
    ADD CONSTRAINT fk_meta_atividade FOREIGN KEY (fk_meta) REFERENCES tbl_projetos_metas(nu_meta);


--
-- TOC entry 2206 (class 2606 OID 39725)
-- Name: fk_modaidade_nivel_bolsa; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_tipos_bolsa_niveis
    ADD CONSTRAINT fk_modaidade_nivel_bolsa FOREIGN KEY (fk_modalidade_bolsa) REFERENCES tbl_tipos_bolsa_modalidades(nu_modalidade_bolsa);


--
-- TOC entry 2196 (class 2606 OID 39633)
-- Name: fk_municipio_entidade; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_entidades
    ADD CONSTRAINT fk_municipio_entidade FOREIGN KEY (nu_municipio) REFERENCES tbl_municipios(nu_municipio);


--
-- TOC entry 2189 (class 2606 OID 39778)
-- Name: fk_plano_indiv_ativ; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY rel_plano_individual_atividade
    ADD CONSTRAINT fk_plano_indiv_ativ FOREIGN KEY (fk_atividade) REFERENCES tbl_projetos_atividades(nu_atividade);


--
-- TOC entry 2188 (class 2606 OID 39773)
-- Name: fk_plano_individual; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY rel_plano_individual_atividade
    ADD CONSTRAINT fk_plano_individual FOREIGN KEY (fk_plano_individual) REFERENCES tbl_planos_individuais(nu_plano_individual);


--
-- TOC entry 2190 (class 2606 OID 39731)
-- Name: fk_proj_bolsista; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY rel_projeto_bolsista
    ADD CONSTRAINT fk_proj_bolsista FOREIGN KEY (fk_bolsista) REFERENCES tbl_bolsistas(nu_bolsista);


--
-- TOC entry 2191 (class 2606 OID 39737)
-- Name: fk_proj_proj; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY rel_projeto_bolsista
    ADD CONSTRAINT fk_proj_proj FOREIGN KEY (fk_projeto) REFERENCES tbl_projetos(nu_projeto);


--
-- TOC entry 2198 (class 2606 OID 39672)
-- Name: fk_proj_sit; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_projetos
    ADD CONSTRAINT fk_proj_sit FOREIGN KEY (fk_situacao) REFERENCES tbl_projetos_situacoes(nu_situacao);


--
-- TOC entry 2197 (class 2606 OID 39767)
-- Name: fk_projeto_bolsista; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_planos_individuais
    ADD CONSTRAINT fk_projeto_bolsista FOREIGN KEY (fk_projeto_bolsista) REFERENCES rel_projeto_bolsista(nu_projeto_bolsista);


--
-- TOC entry 2204 (class 2606 OID 39666)
-- Name: fk_projeto_meta; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_projetos_metas
    ADD CONSTRAINT fk_projeto_meta FOREIGN KEY (fk_projeto) REFERENCES tbl_projetos(nu_projeto);


--
-- TOC entry 2207 (class 2606 OID 39690)
-- Name: fk_projetos_doc; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_projetos_documentos
    ADD CONSTRAINT fk_projetos_doc FOREIGN KEY (fk_projeto) REFERENCES tbl_projetos(nu_projeto);


--
-- TOC entry 2186 (class 2606 OID 39755)
-- Name: fk_rel_atividade; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY rel_bolsista_atividade
    ADD CONSTRAINT fk_rel_atividade FOREIGN KEY (fk_atividade) REFERENCES tbl_projetos_atividades(nu_atividade);


--
-- TOC entry 2187 (class 2606 OID 39761)
-- Name: fk_rel_bolsista; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY rel_bolsista_atividade
    ADD CONSTRAINT fk_rel_bolsista FOREIGN KEY (fk_bolsista) REFERENCES tbl_bolsistas(nu_bolsista);


--
-- TOC entry 2202 (class 2606 OID 39713)
-- Name: fk_resp_concedente_pro; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_projetos
    ADD CONSTRAINT fk_resp_concedente_pro FOREIGN KEY (fk_responsavel_concedente) REFERENCES tbl_responsavel(nu_responsavel);


--
-- TOC entry 2201 (class 2606 OID 39707)
-- Name: fk_resp_prop_proj; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_projetos
    ADD CONSTRAINT fk_resp_prop_proj FOREIGN KEY (fk_responsavel_proponente) REFERENCES tbl_responsavel(nu_responsavel);


--
-- TOC entry 2193 (class 2606 OID 39749)
-- Name: fk_tipo_bolsa_nivel; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY rel_projeto_bolsista
    ADD CONSTRAINT fk_tipo_bolsa_nivel FOREIGN KEY (fk_tipo_bolsa_nivel) REFERENCES tbl_tipos_bolsa_niveis(nu_nivel_bolsa);


--
-- TOC entry 2194 (class 2606 OID 39647)
-- Name: fk_tipo_doc; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tbl_bolsistas_documentos
    ADD CONSTRAINT fk_tipo_doc FOREIGN KEY (fk_tipo_documento) REFERENCES tbl_tipos_documentos(nu_tipo_documento);


-- Completed on 2017-07-20 10:01:57

--
-- PostgreSQL database dump complete
--

