$LOAD_PATH.unshift(File.dirname(__FILE__))
$LOAD_PATH.unshift(File.join(File.dirname(__FILE__), '..', 'lib'))
require 'gene_ontology'

go = GeneOntology.new.from_file("gene_ontology_edit.obo")
go.header # => a GeneOntology::Header object
go.id_to_term # => a hash from GO id to the GeneOntology::Term

id_tmp = ""

aFile_bp = open("res_bp.txt", 'w')
aFile_mf = open("res_mf.txt", 'w')
aFile_cc = open("res_cc.txt", 'w')

go.id_to_term.each do |key, some_term|
	if some_term.is_a.size > 0
		if some_term.namespace =~ /biological_process/i
			some_term.each do |term|
				aFile_bp.write(term.id.to_s + "\t")
			end
			aFile_bp.write("\n")
		elsif some_term.namespace =~ /molecular_function/i
			some_term.each do |term|
				aFile_mf.write(term.id.to_s + "\t")
			end
			aFile_mf.write("\n")
		elsif some_term.namespace =~ /cellular_component/i
			some_term.each do |term|
				aFile_cc.write(term.id.to_s + "\t")
			end
			aFile_cc.write("\n")
		end
	end
end

aFile_bp.close()
aFile_mf.close()
aFile_cc.close()


