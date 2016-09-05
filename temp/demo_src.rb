$LOAD_PATH.unshift(File.dirname(__FILE__))
$LOAD_PATH.unshift(File.join(File.dirname(__FILE__), '..', 'lib'))
require 'gene_ontology'

go = GeneOntology.new.from_file("gene_ontology_edit.obo")
go.header # => a GeneOntology::Header object
go.id_to_term # => a hash from GO id to the GeneOntology::Term

id_tmp = ""
some_term = go.id_to_term.values.first

aFile = File.new("output.txt","a")

# traverse the tree upwards, beginning with the current Term
puts some_term.id
puts some_term.name
puts some_term.level
some_term.each do |term|
	puts term.id
	puts term.name
  puts term.level
  term.name =~ /Plasma Membrane/i
  puts term.name
end
some_term.level  # => how many levels down from the top 3
                 # molecular_function, biol comp. etc are level 0