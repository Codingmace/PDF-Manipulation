fin = []
names = ['(214) 425-6508.pdf', '(214) 478-0361.pdf', '(817) 458-2755.pdf', '+1 208-810-6259.pdf', '+1 214-223-4296.pdf', '+1 214-425-6508.pdf', '+1 214-509-0828.pdf', '+1 214-697-1135.pdf', '+1 22000.pdf', '+1 227898.pdf', '+1 23333.pdf', '+1 32874.pdf', '+1 33588.pdf', '+1 347-464-0361.pdf', '+1 413-504-3664.pdf', '+1 469-408-5901.pdf', '+1 469-525-5714.pdf', '+1 469-850-2576.pdf', '+1 4891.pdf', '+1 50472.pdf', '+1 509-233-4676.pdf', '+1 510-210-9152.pdf', '+1 612-294-9793.pdf', '+1 66937.pdf', '+1 720-599-0068.pdf', '+1 727272.pdf', '+1 729725.pdf', '+1 7535.pdf', '+1 806-438-4320.pdf', '+1 818-962-4611.pdf', '+1 844-849-7137.pdf', '+1 859-795-2904.pdf', '+1 972-984-9540.pdf', '4.pdf', '41-010-0044.pdf', 'Aaron Putnam.pdf', 'Aaron.pdf', 'Akshay K.pdf', 'Alan Shepard.pdf', 'Alex Crawford.pdf', 'Alex Duffy.pdf', 'Alex Leal.pdf', 'Alex.pdf', 'Andrew Whitecotton.pdf', 'Arturo Sarachi.pdf', 'Arturo.pdf', 'Aryan Barghi.pdf', 'Aryan.pdf', 'Austin Sandifer.pdf', 'Austin Wakefield.pdf', 'Austin.pdf', 'Avery Gleason.pdf', 'Bill Mertz.pdf', 'Blake.pdf', 'Brice Chen.pdf', 'Bryan Briones & Clayton.pdf', 'Bryan Pham.pdf', 'Caleb Portwood.pdf', 'Calvin.pdf', 'Cameron Berry.pdf', 'Cameron Jackson.pdf', 'Camryn Casslyberry.pdf', 'Carlos Naverette, Mom, Monica, David Ward, Hannah Ward & Dad.pdf', 'Carlos Naverette.pdf', 'Carmen Fish.pdf', 'Carolina & +1 638-702-1800.pdf', 'Carolina & David.pdf', 'Carolina & Hannah.pdf', 'Carolina Ward & Dad.pdf', 'Carolina Ward & David Ward.pdf', 'Carolina Ward, David Ward & Hannah Ward.pdf', 'Carolina Ward.pdf', 'Carolina, David & Hannah.pdf', 'Catalina Barragan.pdf', 'Catherine Ward.pdf', 'Catherine, Dad, Mom & Hannah Ward.pdf', 'Catherine, Hannah Ward & Carolina Ward.pdf', 'Catherine.pdf', 'Cayla Rodriguez.pdf', 'Cayla.pdf', 'Chris Yeck.pdf', 'Christian Rameriaz.pdf', 'Christian Velez.pdf', 'Claude Woods.pdf', 'Clayton.pdf', 'Cody Chachal.pdf', 'Cody Chang & Kyle Fromm.pdf', 'Cody Chang, Kyle Fromm & Ryan Talbot.pdf', 'Cody Chang.pdf', 'Collin Cooksey.pdf', 'Cordel Chang.pdf', 'Dad & Carolina.pdf', 'Dad & Hannah.pdf', 'Dad, Carlos Naverette & David Ward.pdf', 'Dad, Carlos Naverette, Carolina Ward, David Ward & Hannah Ward.pdf', 'Dad, Carlos Naverette, Mom, David Ward & Hannah Ward.pdf', 'Dad, Carlos Naverette, Monica, David Ward, Hannah Ward & Mom.pdf', 'Dad, Carolina & David.pdf', 'Dad, Carolina & Hannah.pdf', 'Dad, Carolina Ward & Hannah Ward.pdf', 'Dad, Carolina Ward, David Ward & Hannah Ward.pdf', 'Dad, Carolina Ward, Monica & Hannah Ward.pdf', 'Dad, Carolina, David & Hannah.pdf', 'Dad, Carolina, David, Hannah & Catherine.pdf', 'Dad, Carolina, David, Hannah, Monica & Carlos.pdf', 'Dad, Carolina, Hannah & Carlos.pdf', 'Dad, David & Hannah.pdf', 'Dad, David Ward, Hannah Ward & Mom.pdf', 'Dad, David Ward, Mom & Hannah Ward.pdf', 'Dad, Hannah Ward, Mom, Carlos Naverette, Monica, Catherine & David Ward.pdf', 'Dad, Mom & Hannah Ward.pdf', 'Dad, Mom, David & Hannah.pdf', 'Dad.pdf', 'Dave & Sharon Watson.pdf', 'David & Hannah.pdf', 'David Ward & Dad.pdf', 'David Ward & Mom.pdf', 'David Ward.pdf', 'Dayton Duffy.pdf', 'Dillan Terry.pdf', 'Drew Ravitz.pdf', 'Drew.pdf', 'Emily Latta.pdf', 'Eric Cho.pdf', 'Erica Logan, Cameron Jackson, Noah Trumbone, J.c Ellis, Meap & Ryan Talbot.pdf', 'Erica Logan.pdf', 'Erik Garcia.pdf', 'Ethan Jackson.pdf', 'Gabe The Babe.pdf', 'Hannah & Dad.pdf', 'Hannah & Mom.pdf', 'Hannah School Email.pdf', 'Hannah Ward & Carolina Ward.pdf', 'Hannah Ward & Dad.pdf', 'Hannah Ward & David Ward.pdf', 'Hannah Ward & Erica Logan.pdf', 'Hannah Ward & Monica.pdf', 'Hannah Ward, Cameron Jackson, Catalina Baragan, Meap & Noah Trumbone.pdf', 'Hannah Ward, Noah Trumbone & Cameron Jackson.pdf', 'Hannah Ward.pdf', 'Heritage Band.pdf', 'Het.pdf', 'Hollyn Thill.pdf', 'Husna Chudhary Email.pdf', 'Husna Chudhary.pdf', 'JC.pdf', 'Jack Smith.pdf', 'Jack.pdf', 'Jacob Choi.pdf', 'Jacob McGee.pdf', 'Jacob Montgomery.pdf', 'Jacob School Email.pdf', 'Jaleen Miller.pdf', 'Jalen M., Squeko, Collin Cooksey, Nick Talbot, Ryan Talbot, Kyle, Lorenzo, Nick Gallacher, Avery Gleason & Caleb Portwood.pdf', 'Jalen M..pdf', 'Jalen Morgan.pdf', 'Jessica Cabrasawan.pdf', 'Joey, Ryan Talbot, Lorenzo, Nick Gallacher, Trevor Pyka, Shallice Marcelle, Avery Gleason, Maddie Chetty, Collin Cooksey & Kayla.pdf', 'Joey, Ryan Talbot, Lorenzo, Nick Gallacher, Trevor Pyka, Shallice Marcelle, Avery Gleason, Maddie Chetty, Marco Garcia & Collin Cooksey.pdf', 'Joey.pdf', 'Jon.pdf', 'Josh Elliot.pdf', 'Josh Shmitt.pdf', 'Josh.pdf', 'Joshua.pdf', 'Kate.pdf', 'Kayla Dubak.pdf', 'Kayla.pdf', 'Kaylie.pdf', 'Kelby Jackson.pdf', 'Kevin Kao.pdf', 'Kyle Fromm & Ryan Talbot.pdf', 'Kyle Fromm.pdf', 'Kyle, Ryan & Cody.pdf', 'Lamb Dang.pdf', 'Landon Wheeler.pdf', 'Lorenzo, Kayla, Maddie Chetty, Nick Gallacher, Marco Garcia, Avery Gleason, T.J, Kaylie, Shallice Marcelle & Joey.pdf', 'Lorenzo, Maddie Chetty, Nick Gallacher, Marco Garcia, Avery Gleason, T.J, Kaylie, Joey, Shallice Marcelle & Collin Cooksey.pdf', 'Lorenzo, Nick Gallacher, Jalen M., Squeko, Collin Cooksey, Nick Talbot, Ryan Talbot, Kyle, Thomas Garcia & Avery Gleason.pdf', 'Lori Miller.pdf', 'Maaz Sarwar.pdf', 'Maddie Chetty.pdf', 'Maddie Wallace .pdf', 'Maeve Carmody.pdf', 'Mallory.pdf', 'Marco Garcia.pdf', 'Mark.pdf', 'Matthew Wethington (Meap).pdf', 'Matthew Wethington.pdf', 'Meap.pdf', 'Megan Bacha.pdf', 'Micheal Summeral.pdf', 'Miles.pdf', 'Mom & Carlos Naverette.pdf', 'Mom & Dad.pdf', 'Mom & Hannah Ward.pdf', 'Mom, Dad & David Ward.pdf', 'Mom, Dad, Hannah Ward, David Ward & Catherine.pdf', 'Mom, David Ward & Hannah Ward.pdf', 'Mom.pdf', 'Monica, Hannah Ward, David Ward, Carolina Ward, Dad & Carlos Naverette.pdf', 'Monica.pdf', 'Mykal Summerall.pdf', 'Nick Gallacher & Ryan Talbot.pdf', 'Nick Gallacher, Shallice Marcelle, Trevor Pyka, Lorenzo, Maddie Chetty, Collin Cooksey, Joey, Ryan Talbot, Avery Gleason & (214) 478-0361.pdf', 'Nick Gallacher.pdf', 'Nick Reisinger.pdf', 'Nick Talbot & Thomas Garcia.pdf', 'Nick Talbot.pdf', 'Noah Meskimen.pdf', 'Noah Trumbone, Cameron Jackson & Trenton Price.pdf', 'Noah Trumbone.pdf', 'Nobody & +1 214-824-8096.pdf', 'Nobody Ward & Nobody Ward.pdf', 'Nobody Ward & jacob.ward.869_k12.friscoisd.org.pdf', 'Nobody Ward.pdf', 'Obe.pdf', 'Omar Nazario.pdf', 'Rafael Esspino.pdf', 'Ray.pdf', 'Romi.pdf', 'Ryan & Cody.pdf', 'Ryan Shiplee, Vincent , Maggie, Maddie Wallace , Carmen & Alex.pdf', 'Ryan Talbot & Cody Chang.pdf', 'Ryan Talbot, Lorenzo, Nick Gallacher, Trevor Pyka, Shallice Marcelle, Avery Gleason, Maddie Chetty, Marco Garcia, T.J & Joey.pdf', 'Ryan Talbot.pdf', 'Sai Sunkara.pdf', 'Sam Misuraca.pdf', 'School Mail.pdf', 'Scott.pdf', 'Seth Galtier.pdf', 'Shallice Marcelle, (214) 478-0361, Lorenzo, Trevor Pyka, T.J, Joey, Marco Garcia, Kayla, Kaylie & Nick Gallacher.pdf', 'Shallice Marcelle.pdf', 'Shepard.pdf', 'Shivam.pdf', 'Sushi Fried Rice.pdf', 'T.J.pdf', 'Thomas Finley.pdf', 'Thomas Garcia & Ryan Talbot.pdf', 'Thomas Garcia.pdf', 'Trent.pdf', 'Trenton Price.pdf', 'Trevor Pyka.pdf', 'Tyler Badby.pdf', 'Tyler Dubak.pdf', 'Tyson.pdf', 'Valerie Luckett .pdf', 'Valerie Luckett.pdf', 'Victoria Cardona.pdf', 'Vincent Alcott.pdf', 'Vincent.pdf', 'Vyas.pdf', 'Zane Smith.pdf', 'denise_supermciro.com, flight_bethichdochoi.com, brandy_head-lampv23.com & Nick Reisinger.pdf', 'jacob.ward.869@k12.friscoisd.pdf', 'jward21@cougarmail.collin.pdf', 'michael_thewardsweb.com & Carolina Ward.pdf', 'michael_thewardsweb.com, Carolina Ward & Hannah Ward.pdf', 'nobodyward_gmail.com.pdf', 'wardsomebody@gmail.pdf']

import PyPDF2
import os.path

# Changed to adjust to new files names
# Can add if need to if file not there dont use the name
# Also instead of using java could use fully python

def PDFmerge(pdfs, output): 
    # creating pdf file merger object
    pdfMerger = PyPDF2.PdfFileMerger()
    # appending pdfs one by one
    for pdf in pdfs:
        with open(pdf, 'rb') as f:
            pdfMerger.append(f)

    # writing combined pdf to output pdf file
    with open(output, 'wb') as f:
        pdfMerger.write(f)
        pdfMerger.close
        
    fin.append(pdfMerger.id_count)
    
    
def main():
    pdfs =[]
    for n in names: 
        for x in range(1,8):
            temp = 'iPhone Text Backup ' + str(x) + '\\' + n
            if os.path.isfile(temp):
                pdfs.append(temp)
           # pdfs.append(('iPhone Text Backup (' + str(x) + ')\\"+ n))
        # print(pdfs[:])
        print(n)
        output = 'iPhone Backup Combines\\' + n
        PDFmerge(pdfs, output)
        pdfs = []
        
    fa = 0
    for x in fin:
        fa = fa + x
    print("fin " + str(fa))

if __name__ == "__main__":
    # calling the main function
    main()
