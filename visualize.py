import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def pie_chart(labels, sizes):
    # Imposta lo stile dark
    plt.style.use("dark_background")
    
    # Colore principale in rosso con opacità ridotta
    main_color = '#e3423c'
    secondary_color = '#7a1f1f'  # Rosso scurito
    
    # Creazione della figura con sfondo scuro
    fig, ax = plt.subplots(figsize=(8, 6), facecolor='#272a2f')  
    
    # Creazione della palette con opacità ridotta
    palette = [main_color, secondary_color] + sns.color_palette("Reds", n_colors=len(labels)-2)
    
    wedges, texts, autotexts = ax.pie(
        sizes, 
        labels=labels, 
        colors=palette,  
        autopct='%1.1f%%',   
        startangle=90,       
        wedgeprops={'linewidth': 1.5},  # Rimosso bordo rosso
        textprops={'fontsize': 10, 'color': 'white', 'fontweight': 'bold'},  
        pctdistance=0.8    # Distanza percentuale dal centro
    )
    
    # Cerchio centrale per effetto donut
    centre_circle = plt.Circle((0,0), 0.65, color='#272a2f', fc='#272a2f', linewidth=0)
    fig.gca().add_artist(centre_circle)
    
    # Rimuove assi
    plt.axis('equal')
    
    # Titolo coerente con il bargram
    ax.set_title("Rapporto promossi bocciati", color='white', fontsize=14, pad=15)
    
    plt.tight_layout()
    plt.show()

def grades_histogram(df):
    # Riempie i valori NaN con "Rimandato"
    grades = df["Esito"]
    grades = grades.fillna("Rimandato")

    # Creiamo una nuova colonna dove i valori numerici restano numerici, e "Rimandato" diventa un numero fittizio (16)
    grades_numeric = grades.apply(lambda x: x if x == "Rimandato" else pd.to_numeric(x, errors='coerce'))

    # Convertiamo "Rimandato" in un numero fittizio, ad esempio 16
    grades_numeric = grades_numeric.replace("Rimandato", 17)

    # Imposta lo stile del grafico su uno sfondo scuro
    plt.style.use("dark_background")
    plt.figure(figsize=(10, 6), facecolor='#272a2f')

    # Crea il grafico per i dati (numerici + "Rimandato" come 16)
    sns.histplot(grades_numeric, kde=False, discrete=True, color="#e3423c", bins=range(16, 32), shrink=0.8, edgecolor='none', linewidth=1.5, alpha=1.0)

    # Aggiungi la categoria "Rimandato" come una stringa
    tick_labels = ['Rimandato'] + list(map(str, range(18, 31)))

    # Cambia i tick dell'asse X per includere correttamente "Rimandato"
    plt.xticks(range(17, 31), tick_labels, fontsize=10, color='white')

    # Rimuoviamo le etichette degli assi
    plt.xlabel('')
    plt.ylabel('')

    # Rimuoviamo la legenda
    plt.legend().set_visible(False)

    # Impostazioni di stile per il grafico
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)

    plt.gca().patch.set_facecolor('#272a2f')

    # Migliora la visualizzazione delle etichette
    plt.grid(axis='y', linestyle='--', alpha=0.5)

    plt.tight_layout()  # Riduce il sovrapporsi delle etichette
    plt.show()

def scores_bargram(scores):
    categories = list(scores.keys())
    points = [x[0] for x in scores.values()]
    max_points = [x[1] for x in scores.values()]

    # Imposta lo stile dark
    plt.style.use("dark_background")
    
    # Creazione della figura
    fig, ax = plt.subplots(figsize=(8, 6), facecolor='#272a2f')

    # Larghezza delle barre più piccole
    bar_width = 0.4  

    # Barre trasparenti per i valori massimi
    bars_max = ax.bar(categories, max_points, color='#e3423c', alpha=0.3, width=bar_width, label="Punteggio max")
    
    # Barre principali senza trasparenza e con zorder più alto
    bars_points = ax.bar(categories, points, color='#e3423c', width=bar_width, label="Punteggio medio", alpha=1.0, zorder=3)

    # Aggiunta etichette per i valori delle barre
    for bar in bars_points:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 0.2, 
                f'{height:.1f}', ha='center', va='bottom', 
                color='white', fontsize=9, fontweight='bold', zorder=4)

    for bar in bars_max:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 0.2, 
                f'{height:.1f}', ha='center', va='bottom', 
                color='white', fontsize=9, fontweight='bold', alpha=0.8, zorder=4)

    # Etichette e titolo
    ax.set_ylabel("Punteggio medio vs Punteggio max", color='white', fontsize=12)
    ax.set_title("Punteggi esercizi", color='white', fontsize=14, pad=15)

    # Miglioramento asse Y
    plt.xticks(fontsize=11, color='white')
    plt.yticks(fontsize=11, color='white')
    plt.ylim(0, max(max(max_points), max(points)) * 1.3)  # +30% spazio

    # Rimuove le spallette
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    # Imposta colore di sfondo e griglia
    ax.set_facecolor('#272a2f')
    ax.grid(axis='y', linestyle='--', alpha=0.5, color='white', zorder=1)

    # Legenda migliorata
    leg = ax.legend(facecolor='#272a2f', edgecolor='none', fontsize=9)
    for text in leg.get_texts():
        text.set_color('white')

    plt.tight_layout()
    plt.show()
