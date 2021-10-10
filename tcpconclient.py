from socket import *
import pickle
import threading
import sys

serverName = 'localhost'
serverPort = 9890

def threaded_clients(clientSocket):
    clientSocket.connect((serverName,serverPort))
    print("Connected to server. Use commands 'set' and 'get' to retrieve or store key value pairs. Use Ctrl D in new line to exit command line and 'quit' to close the connection")
    datakey=['Misfits: A Personal Manifesto, Michaela Coel','Inseparable, Simone de Beauvoir','Matrix, Lauren Groff','Poet Warrior, Joy Harjo','On Freedom: Four Songs of Care and Constraint, Maggie Nelson','Beautiful World, Where Are You, Sally Rooney','The Magician, Colm Tóibín','Unbound: My Story of Liberation and the Birth of the Me Too Movement, Tarana Burke','Harlem Shuffle, Colson Whitehead','The Book of Form and Emptiness, Ruth Ozeki','Cloud Cuckoo Land, Anthony Doerr']
    datavalue=['Michaela Coel, creator and star of I May Destroy You and Chewing Gum, makes her literary debut with a slim manifesto written with the same perfect balance of sentiment, insight and wit that made viewers fall in love with her on the screen. Built on a speech Coel delivered at the 2018 Edinburgh International Television Festival, Misfits describes her experience of racism, prejudice and trauma, and her empowering transformation from a person trying to fit in to a person determined to make new space for herself. It’s an impassioned and rousing defense of staying true to yourself and supporting others to do the same.','Thirty-five years after Simone de Beauvoir’s death, her never-before-published novel Inseparable is finally being released to the world. The iconic French philosopher (and author of the landmark feminist text The Second Sex) describes a profound and passionate friendship between Sylvie and Andrée, two tenacious young women who meet as children and strengthen their bond as they grow into adulthood in post–World War I France. It’s a vibrant exploration of female will and friendship in a world that is still, too often, intent on constraining both.','At the center of Lauren Groff’s new novel, her first since her 2015 hit Fates and Furies, is teenager Marie de France. It’s the 12th century and Marie’s just been sent to an abbey in England after being ousted from the French royal court. The fierce protagonist of Matrix is entering a bleak scene: disease is everywhere at the abbey, and the nuns barely have enough to eat. Marie is tasked with making life better for these women—a challenge that proves both thrilling and heartbreaking. Groff, a two-time National Book Award finalist, crafts an electric work of historical fiction charting Marie’s plight.','Three-time U.S. Poet Laureate Joy Harjo—the first Native American to hold the title—delivers a follow-up to her 2012 memoir Crazy Brave with Poet Warrior, a lyrical study of her relationship to poetry and music. Alternating between poetry and prose, Harjo meditates on the stories and songs she grew up with, her artistic and ancestral influences and how poetry informs and reflects her connection to her community and home. The result is a memoir that is soulful and celebratory.','The latest book from poet and writer Maggie Nelson is a meditative and potent examination of freedom. Looking at freedom through the realms of art, sex, drugs and climate, the author of The Argonauts explores the contradictions, complexities and rhetoric that surround the term. Combining thoughtful cultural criticism with anecdotes from her personal life, Nelson delivers an intriguing work of nonfiction that seeks to challenge readers’ definition of freedom and rethink how the concept operates in our lives.','Sally Rooney exploded onto the literary scene in 2017 with her debut novel Conversations with Friends. Next came her similarly beloved follow-up Normal People, now an acclaimed Hulu series. Rooney’s latest, one of the most anticipated books of the year, is again concerned with Irish millennials navigating the turbulence of falling in and out of love and questioning the seemingly broken world that surrounds them. Tracing the lives of best friends Alice and Eileen, and the emails they write to stay connected to each other, Rooney unravels a sharp narrative about intimacy, religion and romance.','Colm Tóibín, the award-winning author of Brooklyn and The Master, returns with another sweeping historical novel, this time a fictionalized account of the life of Thomas Mann, the Nobel prize-winning author of Death in Venice. Extensively researched and lyrically wrought, The Magician follows Mann from his childhood in early 20th-century Germany—as a young boy grappling with desires he can’t reveal to his conservative family—through his marriage, the trip that inspires his groundbreaking novel, his discomfort with his new role as a public intellectual during World War II and his escape to the U.S. It’s a complex but empathetic portrayal of a writer in a lifelong battle against his innermost desires, his family and the tumultuous times they endure.','In her debut memoir, Tarana Burke mines her past, from her coming-of-age as a Black girl in the Bronx to her rise in activism as the founder of the MeToo movement. In candid terms, Burke lays bare her relationship with trauma, exploring how her sexual assault impacted her sense of self, and how she went on to use that experience to empower others and create meaningful change. Bold and inspiring, Unbound is a searing look at leadership, activism and empathy.','Two-time Pulitzer Prize winner Colson Whitehead is known for narratives that vary greatly in subject matter. His body of work contains multitudes, from his debut about the aftermath of an elevator crash to a zombie apocalypse story to piercing retellings of violent periods in U.S. history. Whitehead’s latest showcases yet more of his range as a storyteller, as Harlem Shuffle follows a 1960s furniture salesman leading a double life of crime. What ensues is part heist novel and part family drama, all set against the backdrop of Harlem, which the author captures in rich, visceral prose.','Ruth Ozeki, the award-winning author of A Tale for the Time Being, weaves a heartfelt, magical tale in her latest, which centers on 13-year-old Benny and his mother Annabelle as they figure out how to live after the unexpected death of their father and husband. Deep in grief, Benny discovers he can suddenly hear the voices of the objects around him—and there are a lot of objects surrounding him, due to his mother’s hoarding. He develops a symbiotic relationship with the Book, the omniscient voice relating the story we’re reading. Ozeki, a practicing Buddhist priest, infuses her story with Zen philosophy, using themes of mindfulness and our connection to the living world to highlight pressing modern concerns like climate change, capitalism and the function of art. Inventive, vivid and propelled by a sense of wonder, The Book of Form and Emptiness will delight younger and older readers alike.','Sweeping and atmospheric, Cloud Cuckoo Land spans centuries and continents, following five protagonists linked by an ancient Greek manuscript about a shepherd who dreams of escaping into paradise. In 15th-century Constantinople, Anna and Omeir are on opposing sides in a violent siege when Anna first discovers the lost manuscript; in 2020 Idaho, 86-year-old vet Zeno clashes with teenage eco-terrorist Seymour against the backdrop of a suburban production of the Greek story as a play; and in the 22nd century, 14-year-old Constance is aboard a spaceship on its way to colonize a distant planet, secretly preserving the story, told to her by her father, on scraps of paper. These characters—like those in Doerr’s Pulitzer Prize–winning novel All the Light We Cannot See—hold their ideals and convictions close, and through their resilience Doerr explores the universal power of hope in catastrophic times.']
    if(cmd=='get')
        while True:
            for i in range(len(datakey)):
               keyval=[]
               keyval.append('get '+ datakey[i])
               data = pickle.dumps(keyval)
               clientSocket.sendall(data)
               key=datakey[i]
               value = clientSocket.recv(1024)
               if(value.decode("utf-8")=="NOT STORED"):
                   print('VALUE ' + key + '\n' + 'NOT STORED')
               elif(value.decode("utf-8")=="STORED"):
                   print('VALUE ' + key + '\n' + 'STORED')
               else:
                   print('VALUE ' + key + ' '+ str(len(value)))
                   print(value.decode("utf-8"))
        print("Connection closed")
        clientSocket.close()
     elif(cmd=='set'):
        for i in range(len(datakey)):
           keyval=[]
           keyval.append('set '+ datakey[i] + len(datavalue[i]))
           data = pickle.dumps(keyval)
           clientSocket.sendall(data)
           key=datakey[i]
           value = clientSocket.recv(1024)
           if(value.decode("utf-8")=="NOT STORED"):
               print('VALUE ' + key + '\n' + 'NOT STORED')
           elif(value.decode("utf-8")=="STORED"):
               print('VALUE ' + key + '\n' + 'STORED')
           else:
               print('VALUE ' + key + ' '+ str(len(value)))
               print(value.decode("utf-8"))
        print("Connection closed")
        clientSocket.close()

cmd=sys.argv[1]
clientSocket = socket(AF_INET, SOCK_STREAM)
t = threading.Thread(target=threaded_clients, args=(clientSocket,))
t.start()
