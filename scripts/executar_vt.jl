using Pkg
Pkg.activate("vistrailsjl/julia")
Pkg.instantiate()  # Instala dependencias automaticamente se for a primeira execucao na maquina

# Configura o PyCall para usar o Python correto desta maquina automaticamente
# Isso resolve o erro "PyCall not configured" em maquinas novas
let
    python_cmd = Sys.which("python") !== nothing ? Sys.which("python") : Sys.which("python3")
    if python_cmd !== nothing
        current_python = get(ENV, "PYCALL_JL_RUNTIME_PYTHON", "")
        if current_python != python_cmd
            ENV["PYTHON"] = python_cmd
            Pkg.build("PyCall")
        end
    end
end


using VisTrailsJL
using Dates

if length(ARGS) < 1
    println("Usage: julia run_vt.jl <caminho_para_arquivo.vt>")
    exit(1)
end

vt_file = ARGS[1]

# Carrega o workflow (não contabilizamos o tempo de I/O de carregar o arquivo na métrica de execução do pipeline)
vt = load_vistrail(vt_file)

# Forçar uma compilação prévia se desejado seria rodar execute(vt) descartando o tempo, mas 
# para ser justo com o Python (onde os imports são carregados na hora), 
# mediremos o tempo da chamada `execute` crua.

start_time = time()
try
    res = execute(vt)
    end_time = time()
    elapsed = end_time - start_time
    println("RESULTADO_EXECUCAO: SUCESSO")
    println("TEMPO_EXECUCAO_SEGUNDOS: ", elapsed)
catch e
    end_time = time()
    elapsed = end_time - start_time
    println("RESULTADO_EXECUCAO: ERRO")
    println("TEMPO_EXECUCAO_SEGUNDOS: ", elapsed)
    showerror(stdout, e)
end
