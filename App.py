def start():
    loop = True
    while loop:
        print("Jo-Tech Mod Maker For Software Inc.")
        print(".If it says Y/N simply put a lower or uppercase Y or N")
        print(".If it says dec put a decimal e.g 0.4")
        print(".If it says opt it is an optional feature and can be skipped my clicking enter")
        print(".The end product will be named softwarename.txt move it to your software types folder and change the extesion to .xml")
        option = input("Do you want to make a new file? (Y/N)")
        if option == "y" or option == "Y":
              loop = False

              creatnew()
        else:
            quit()


def creatnew():
    print("Jo-Tech Mod Maker For Software Inc.")
    softwarename = input("Software Name: ")
    description = input("Description: ")
    delete = input("Delete? (Y/N)")
    category = input("Category: ")
    random = input("Random (Dec): ")
    os = input("OSSpecific (Y/N): ")
    if delete == "Y" or delete == "y":
        delete = "TRUE"
    else:
        delete = "FALSE"
    if os == "Y" or os == "y":
        os = "TRUE"
    else:
        os = "FALSE"
    global filename
    filename = softwarename + ".txt"

    file =  open(filename, "a")
    softwarename = " <Name>"+ softwarename + "</Name>"
    delete = " <Delete>"+delete+"</Delete>"
    category = " <Category>"+ category+"</Category>"
    os = " <OSSpecific>"+ os+"</OSSpecific>"
    description = " <Description>"+ description+"</Description>"
    file.write("<SoftwareType>")
    file.write("\n")
    file.write(softwarename)
    file.write("\n")
    file.write(delete)
    file.write("\n")
    file.write(category)
    file.write("\n")
    file.write(os)
    file.write("\n")
    file.write(description)
    file.write("\n")
    file.write(" <Categories>")
    file.write("\n")
    file.close()
    categories()

def categories():
    file = open(filename, "a")
    print("Jo-Tech Mod Maker For Software Inc.")
    print("Category Maker")
    categoryname = input("Name: ")
    categorydescription = input("Description: ")
    categorypopularity = input("Popularity (Dec): ")
    categoryunlock = input("Unlock Year: ")
    categoryretention = input("Retention (Dec, How long people use): ")
    categorytimescale = input("Timescale (Dec): ")
    categoryinteractive = input("Interactive (Dec+ Sequals)")
    categoryname =  "  <Category Name=\""+categoryname+"\">"
    categorydescription = "   <Description>"+categorydescription+"</Description>"
    categorypopularity = "   <Popularity>"+categorypopularity+"</Popularity>"
    categoryunlock = "   <Unlock>"+categoryunlock+"</Unlock>"
    categoryretention = "   <Retention>"+categoryretention+"</Retention>"
    categorytimescale = "   <Timescale>"+categorytimescale+"</Timescale>"
    categoryinteractive = "   <Interactive>"+categoryinteractive+"</Interactive>"
    file.write(categoryname)
    file.write("\n")
    file.write(categorydescription)
    file.write("\n")
    file.write(categorypopularity)
    file.write("\n")
    file.write(categoryunlock)
    file.write("\n")
    file.write(categoryretention)
    file.write("\n")
    file.write(categorytimescale)
    file.write("\n")
    file.write(categoryinteractive)
    file.write("\n")
    option = input("Would you like to make category? Y/N")
    if option == "Y" or option == "y":
        categories()
    else:
        file.write(" </Categories>")
        file.write("\n")
        file.write(" <OneClient>FALSE</OneClient>")
        file.write("\n")
        file.write(" InHouse>TRUE</InHouse>")
        file.write("\n")
        file.write(" <Features>")
        file.write("\n")
        file.close()
        newfeature()

def newfeature():
    file = open(filename, "a")
    print("Jo-Tech Mod Maker For Software Inc.")
    print("Feature Maker")
    featureforced = input("Forced (Y/N): ")
    featurevital = input("Vital (Y/N): ")
    featureresearch = input("Research (Y/N): ")
    if featureforced == "Y" or featureforced == "y":
    	featureforced = "TRUE"
    else:
    	featureforced = "FALSE"
    if featurevital == "Y" or featurevital == "y":
    	featurevital = "TRUE"
    else:
    	featurevital = "FALSE"
    if featureresearch == "Y" or featureresearch == "y":
    	featureresearch = "TRUE"
    else:
    	featureresearch = "FALSE"
    featurefrom = input("From: ")
    featurename = str(input("Name: "))
    featurecategory = input("Category: ")
    featuredescription = input("Description: ")
    featuredevtime = input("Devtime: ")
    featureinnovation = input("Innovation (Num): ")
    featureusability = input("Usablity (Num): ")
    featurestability = input("Stabiltiy (Num): ")
    featurecodeart = input("Codeart (Dec): ")
    featuresoftcategory = input("Software Category: ")
    featuredependency = input("Dependency: ")
    featureunlock = input("Unlock year: ")
    if featuredependency != "":
    	featuredepfeat = input("Feature of Dependency: ")

    feature = "  <Feature "
    if featureforced:
        feature = feature + "Forced=\"TRUE\""
    if featurevital:
        feature = feature + "Vital=\"TRUE\""
    if featureresearch:
        feature = feature + "Research=\"TRUE\""
    if featurefrom != "":
        feature = feature  + "From=\""+featurefrom+"\""
    feature = feature + ">"
    print(featurename)

    featurename = "   <Name>" + featurename+"</Name>"
    featurecategory = "   <Category>"+featurecategory+"</Category>"
    featuredescription = "   <Description>"+featuredescription+"</Description>"
    featuredevtime = "   <Devtime>"+featuredevtime+"</Devtime>"
    featureinnovation = "   <Innovation>"+featureinnovation+"</Innovation>"
    featureusability = "   <Usability>"+featureusability+"</Usability>"
    featurestability = "   <Stability>"+featureusability+"</Stability>"
    featurecodeart = "   <CodeArt>"+featurecodeart+"</Codeart>"
    featuresoftcategory = "   <Softwarecategory category=\""+featuresoftcategory+"\">"+featureunlock+"</Softwarecategory>"

    file.write(feature)
    file.write("\n")
    file.write(featurename)
    file.write("\n")
    file.write(featurecategory)
    file.write("\n")
    file.write(featuredescription)
    file.write("\n")
    file.write(featuredevtime)
    file.write("\n")
    file.write(featureinnovation)
    file.write("\n")
    file.write(featureusability)
    file.write("\n")
    file.write(featurestability)
    file.write("\n")
    file.write(featurecodeart)
    file.write("\n")
    file.write(featuresoftcategory)
    file.write("\n")
    file.write("  </Feature>")
    file.write("\n")

    option = input("Would you like to make another feature Y/N?")
    if option == "y" or option == "Y":
        newfeature()
    else:
        file.write(" </Features>")
        file.write("\n")
        file.write("</Softwaretype>")
        file.write("\n")

    file.close()
start()
