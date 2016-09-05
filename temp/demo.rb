$LOAD_PATH.unshift(File.dirname(__FILE__))
$LOAD_PATH.unshift(File.join(File.dirname(__FILE__), '..', 'lib'))
require 'gene_ontology'

go = GeneOntology.new.from_file("gene_ontology_edit.obo")
go.header # => a GeneOntology::Header object
go.id_to_term # => a hash from GO id to the GeneOntology::Term

id_tmp = ""
some_term = go.id_to_term.values.first

=begin
while !(some_term.name =~ /cellular process/i)
	 some_term = go.id_to_term.values.next
end
=end

#aFile = File.new("output.txt","a")

# traverse the tree upwards, beginning with the current Term
print some_term.id," ",some_term.name," ",some_term.level,
some_term.each do |term|
	if term.name =~ /biological_process/i
		
	end
=begin
	puts term.id
	puts term.name
  puts term.level
=end
	#print term.id," ",term.name," ",term.level,".\n"
  #term.name =~ /Plasma Membrane/i
  #puts term.name
end
#print some_term.level,"\n"  # => how many levels down from the top 3
                 # molecular_function, biol comp. etc are level 0