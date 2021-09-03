# Author : Seongchun Yang
# Affiliation : Kyoto University

import os
import pandas as pd
from intermine.webservice import Service

def grab(terms):
    '''
    (Literally) grab the information off of the service module by the terms.
    Parameters
    ----------
    terms   :   list
        GOterms
    Returns
    -------
    data    :   pd.DataFrame
        Table containing all the information per the queries defined in this function for all GOterm inputs
    '''
    # initialize service - since this is code specifically for Mus Musculus, this is set in the function.
    service = Service("http://www.mousemine.org/mousemine/service")
    # initialize holder - this will be returned
    data = {}
    # ready print
    print('{:40s} {:10s} {:10s}'.format('GOterm','Unique #', 'Total #'))
    print('------------------------------------------------------------------------------------------')

    for term in terms:
        # New query on the class
        query = service.new_query("SequenceFeature")
        # Type constraint which should come next (before all mentions of the paths they constrain)
        ## 'parents' ensure we are specifically targeting all terms below that parent id.
        query.add_constraint("ontologyAnnotations.ontologyTerm.parents", "GOTerm")
        ## As far as I can tell, this doesn't do anything when overlapped with the parent above.
        query.add_constraint("ontologyAnnotations.ontologyTerm", "GOTerm")

        # Uncomment further views if you are interested.
        # Other query fields can be found in InterMine documentation.
        query.add_view(
            "ontologyAnnotations.ontologyTerm.namespace",
            "ontologyAnnotations.ontologyTerm.identifier",
            "ontologyAnnotations.ontologyTerm.name",
            "ontologyAnnotations.qualifier",
            "ontologyAnnotations.evidence.code.code",
            "ontologyAnnotations.evidence.withText",
            "primaryIdentifier",
            "symbol", 
            "name", 
            "sequenceOntologyTerm.name",
            "chromosome.primaryIdentifier", 
            "length", 
            "description",
            #"expression.assayType",
            #"expression.probe", 
            #"expression.age", 
            #"expression.strength"
        )

        query.add_sort_order("SequenceFeature.symbol", "ASC")
        query.add_constraint("organism.taxonId", "=", "10090") # Mus Musculus (Mouse)
        query.add_constraint("ontologyAnnotations.ontologyTerm.parents.name", "=", term)

        _data = []
        for k,row in enumerate(query.rows()):
            _data.append([
                row["ontologyAnnotations.ontologyTerm.namespace"],
                row["ontologyAnnotations.ontologyTerm.identifier"],
                row["ontologyAnnotations.ontologyTerm.name"],
                row["ontologyAnnotations.qualifier"],
                row["ontologyAnnotations.evidence.code.code"],
                row["ontologyAnnotations.evidence.withText"],
                row["primaryIdentifier"],
                row["symbol"], 
                row["name"], 
                row["sequenceOntologyTerm.name"],
                row["chromosome.primaryIdentifier"], 
                row["length"], 
                row["description"],
                #row["expression.assayType"],
                #row["expression.probe"], 
                #row["expression.age"], 
                #row["expression.strength"]
            ])

        names = [
            "ontologyTerm.namespace",
            "ontologyTerm.identifier",
            "ontologyTerm.name",
            "qualifiers",
            "evidence.code.code",
            "evidence.withText",
            "primaryIdentifier", 
            "symbol", 
            "name", 
            "sequenceOntologyTerm.name",
            "chromosome.primaryIdentifier", 
            "length", 
            "description",
            #"expression.assayType",
            #"expression.probe", 
            #"expression.age", 
            #"expression.strength"
        ]

        df = pd.DataFrame(_data, columns = names)
        data[term] = df
        print('{:40s} {:8d} {:8d}'.format(term,len(list(set(data[term]['symbol'].tolist()))),len(data[term]['symbol'].tolist())))
        print()
    
    return data

def save_to_csv(data,filepath=os.path.curdir):
    # create a folder
    filepath = os.path.join(filepath,'GOterms')
    if os.path.exists(filepath):
        pass
    else:
        os.makedirs(filepath)
    # save
    for term in data.keys():
        newterm = term.replace('/', '_').replace(' ', '_')
        data[term].to_csv(
            os.path.join(filepath,newterm + '.csv'),
            index = False
        )