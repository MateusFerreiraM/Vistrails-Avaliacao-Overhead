using Pkg
Pkg.activate("vistrailsjl/julia")

using ZipFile
using EzXML

function dump_vt(filename)
    z = ZipFile.Reader(filename)
    local xml_data = ""
    for f in z.files
        if f.name == "vistrail"
            xml_data = read(f, String)
            break
        end
    end
    close(z)
    
    doc = parsexml(xml_data)
    root = doc.root
    
    modules = String[]
    for add in findall("//add[@what='module']", root)
        mod = findfirst("module", add)
        if mod !== nothing
            name = haskey(mod, "name") ? mod["name"] : ""
            package = haskey(mod, "package") ? mod["package"] : ""
            push!(modules, "$name ($package)")
        end
    end
    println("Modules found:")
    for m in unique(modules)
        println("  $m")
    end
end

dump_vt("exemplos/noaa_webservices.vt")
