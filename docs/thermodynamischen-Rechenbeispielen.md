# Rechenbeispiele zu Thermodynamischen Prozessen

- [Rechenbeispiele zu Thermodynamischen Prozessen](#rechenbeispiele-zu-thermodynamischen-prozessen)
  - [Konsistente Notation und Einheiten](#konsistente-notation-und-einheiten)
  - [Rechenbeispiele zu Thermodynamischen Kreisprozessen](#rechenbeispiele-zu-thermodynamischen-kreisprozessen)
    - [Beispiel 1: Carnot-Prozess](#beispiel-1-carnot-prozess)
    - [Beispiel 2: Otto-Prozess](#beispiel-2-otto-prozess)
    - [Beispiel 3: Diesel-Prozess](#beispiel-3-diesel-prozess)
  - [Rechenbeispiele zu Thermodynamischen Größen](#rechenbeispiele-zu-thermodynamischen-größen)
    - [Wärme ($Q$)](#wärme-q)
      - [Beispiel 1: Erwärmung eines Stoffes](#beispiel-1-erwärmung-eines-stoffes)
      - [Beispiel 2: Schmelzen von Eis](#beispiel-2-schmelzen-von-eis)
      - [Beispiel 3: Wärmeleitung durch ein Material](#beispiel-3-wärmeleitung-durch-ein-material)
    - [Arbeit ($W$)](#arbeit-w)
      - [Beispiel 1: Isotherme Expansion eines idealen Gases](#beispiel-1-isotherme-expansion-eines-idealen-gases)
      - [Beispiel 2: Heben eines Gewichts](#beispiel-2-heben-eines-gewichts)
      - [Beispiel 3: Kompression eines Gases](#beispiel-3-kompression-eines-gases)
    - [Wirkungsgrad ($\\eta$)](#wirkungsgrad-eta)
      - [Beispiel 1: Wärmekraftmaschine](#beispiel-1-wärmekraftmaschine)
      - [Beispiel 2: Carnot-Wirkungsgrad](#beispiel-2-carnot-wirkungsgrad)
      - [Beispiel 3: Elektromotor](#beispiel-3-elektromotor)
    - [Energie ($E$)](#energie-e)
      - [Beispiel 1: Kinetische Energie](#beispiel-1-kinetische-energie)
      - [Beispiel 2: Potenzielle Energie](#beispiel-2-potenzielle-energie)
      - [Beispiel 3: Änderung der inneren Energie](#beispiel-3-änderung-der-inneren-energie)
    - [Entropie ($S$)](#entropie-s)
      - [Beispiel 1: Isotherme Expansion eines idealen Gases](#beispiel-1-isotherme-expansion-eines-idealen-gases-1)
      - [Beispiel 2: Entropieänderung bei Wärmezufuhr](#beispiel-2-entropieänderung-bei-wärmezufuhr)
      - [Beispiel 3: Wärmeübertragung zwischen zwei Reservoirs](#beispiel-3-wärmeübertragung-zwischen-zwei-reservoirs)



Diese Zusammenstellung enthält verschiedene Rechenbeispiele zu thermodynamischen Prozessen und Konzepten. Die Beispiele sind so gestaltet, dass sie das Verständnis der Thermodynamik fördern und einen Bezug zur Praxis herstellen.

## Konsistente Notation und Einheiten

**Einheitliche Symbole:**

- $P$: Druck (in Pascal, Pa)
- $V$: Volumen (in Kubikmetern, m³)
- $T$: Temperatur (in Kelvin, K)
- $Q$: Wärme (in Joule, J)
- $W$: Arbeit (in Joule, J)
- $n$: Stoffmenge (in Mol, mol)
- $R$: Universelle Gaskonstante ($8{,}314\,\frac{\text{J}}{\text{mol·K}}$)
- $\eta$: Wirkungsgrad (dimensionslos oder in Prozent)
- $\gamma$: Isentropenexponent ($\gamma = \frac{c_p}{c_v}$)
- $c_p, c_v$: Wärmekapazitäten bei konstantem Druck bzw. Volumen

**Einheitenkonsistenz:** Alle Berechnungen verwenden SI-Einheiten, um Einheitlichkeit zu gewährleisten und Fehler zu vermeiden.

---

## Rechenbeispiele zu Thermodynamischen Kreisprozessen

### Beispiel 1: Carnot-Prozess

**Hintergrund:**

Der Carnot-Prozess ist ein idealisierter thermodynamischer Kreisprozess, der die maximale Effizienz einer Wärmekraftmaschine zwischen zwei Wärmereservoirs definiert. Er dient als Referenz, um die Leistungsfähigkeit realer Maschinen zu beurteilen.

**Gegeben:**

- Temperatur der Wärmequelle (heiße Quelle): $T_H = 500\,\text{K}$
- Temperatur der Wärmesenke (kalte Senke): $T_C = 300\,\text{K}$
- Zugeführte Wärme von der Wärmequelle: $Q_H = 1\,000\,\text{J}$

**Gesucht:**

1. Wirkungsgrad $\eta$ des Carnot-Prozesses
2. Vom System verrichtete Arbeit $W$
3. An die Wärmesenke abgegebene Wärme $Q_C$
4. Entropieänderungen $\Delta S_H$, $\Delta S_C$ und $\Delta S_{\text{gesamt}}$

**Berechnungen:**

1. **Wirkungsgrad des Carnot-Prozesses:**

   Der Wirkungsgrad einer idealen Carnot-Maschine ist gegeben durch:

   $$
   \eta = 1 - \frac{T_C}{T_H}
   $$

   Einsetzen der Werte:

   $$
   \eta = 1 - \frac{300\,\text{K}}{500\,\text{K}} = 1 - 0{,}6 = 0{,}4 \quad \text{oder} \quad 40\,\%
   $$

2. **Vom System verrichtete Arbeit $W$:**

   $$
   W = \eta \times Q_H = 0{,}4 \times 1\,000\,\text{J} = 400\,\text{J}
   $$

3. **An die Wärmesenke abgegebene Wärme $Q_C$:**

   $$
   Q_C = Q_H - W = 1\,000\,\text{J} - 400\,\text{J} = 600\,\text{J}
   $$

4. **Entropieänderungen:**

   - **Entropieänderung der Wärmequelle ($\Delta S_H$):**

     $$
     \Delta S_H = -\frac{Q_H}{T_H} = -\frac{1\,000\,\text{J}}{500\,\text{K}} = -2\,\text{J/K}
     $$

     *(Die Entropie der Wärmequelle nimmt ab, da Wärme abgegeben wird.)*

   - **Entropieänderung der Wärmesenke ($\Delta S_C$):**

     $$
     \Delta S_C = \frac{Q_C}{T_C} = \frac{600\,\text{J}}{300\,\text{K}} = 2\,\text{J/K}
     $$

     *(Die Entropie der Wärmesenke nimmt zu, da Wärme aufgenommen wird.)*

   - **Gesamte Entropieänderung ($\Delta S_{\text{gesamt}}$):**

     $$
     \Delta S_{\text{gesamt}} = \Delta S_H + \Delta S_C = -2\,\text{J/K} + 2\,\text{J/K} = 0\,\text{J/K}
     $$

     *Anmerkung: Bei einem ideal reversiblen Prozess bleibt die Gesamtentropie konstant.*

**Praktische Anwendung:**

Der Carnot-Prozess ist in der Praxis nicht realisierbar, da alle realen Prozesse irreversibel sind und Verluste aufweisen. Dennoch liefert er die theoretische Obergrenze für den Wirkungsgrad von Wärmekraftmaschinen.

---

### Beispiel 2: Otto-Prozess

**Hintergrund:**

Der Otto-Prozess beschreibt idealisiert den Betrieb eines Benzinmotors. Er besteht aus vier Zustandsänderungen: zwei isentrope (adiabatische) und zwei isochore Prozesse.

**Gegeben:**

- Kompressionsverhältnis: $r = \frac{V_1}{V_2} = 8$
- Isentropenexponent: $\gamma = 1{,}4$
- Zugeführte Wärmemenge: $Q_{\text{zu}} = 1\,800\,\text{J}$

**Gesucht:**

1. Theoretischer Wirkungsgrad $\eta$ des Otto-Prozesses
2. Vom System verrichtete Arbeit $W$
3. Abgeführte Wärme $Q_{\text{ab}}$

**Berechnungen:**

1. **Theoretischer Wirkungsgrad des Otto-Prozesses:**

   Der Wirkungsgrad ist definiert als:

   $$
   \eta = 1 - \frac{1}{r^{\gamma - 1}}
   $$

   Berechnung des Exponenten:

   $$
   \gamma - 1 = 1{,}4 - 1 = 0{,}4
   $$

   Berechnung von $r^{\gamma - 1}$:

   $$
   r^{0{,}4} = 8^{0{,}4}
   $$

   Berechnung von $8^{0{,}4}$:

   $$
   8^{0{,}4} = e^{0{,}4 \times \ln 8} = e^{0{,}4 \times 2{,}0794} = e^{0{,}8318} \approx 2{,}297
   $$

   Somit:

   $$
   \eta = 1 - \frac{1}{2{,}297} \approx 1 - 0{,}435 = 0{,}565 \quad \text{oder} \quad 56{,}5\,\%
   $$

2. **Vom System verrichtete Arbeit $W$:**

   $$
   W = \eta \times Q_{\text{zu}} = 0{,}565 \times 1\,800\,\text{J} = 1\,017\,\text{J}
   $$

3. **Abgeführte Wärme $Q_{\text{ab}}$:**

   $$
   Q_{\text{ab}} = Q_{\text{zu}} - W = 1\,800\,\text{J} - 1\,017\,\text{J} = 783\,\text{J}
   $$

**Praktische Anwendung:**

In realen Otto-Motoren ist der Wirkungsgrad aufgrund von Verlusten (z. B. Wärmeverluste, Reibung) geringer. Durch technologische Verbesserungen wie Direkteinspritzung und variable Ventilsteuerung wird versucht, den Wirkungsgrad zu erhöhen.

---

### Beispiel 3: Diesel-Prozess

**Hintergrund:**

Der Diesel-Prozess modelliert den Betrieb eines Dieselmotors, bei dem die Wärmezufuhr bei konstantem Druck (isobar) erfolgt.

**Gegeben:**

- Kompressionsverhältnis: $r = \frac{V_1}{V_2} = 20$
- Isentropenexponent: $\gamma = 1{,}4$
- Volumenzunahme während der Wärmezufuhr: $\rho = \frac{V_3}{V_2} = 1{,}2$
- Zugeführte Wärmemenge: $Q_{\text{zu}} = 2\,000\,\text{J}$

**Gesucht:**

1. Theoretischer Wirkungsgrad $\eta$ des Diesel-Prozesses
2. Vom System verrichtete Arbeit $W$
3. Abgeführte Wärme $Q_{\text{ab}}$

**Berechnungen:**

1. **Theoretischer Wirkungsgrad des Diesel-Prozesses:**

   $$
   \eta = 1 - \frac{1}{r^{\gamma - 1}} \cdot \frac{\rho^\gamma - 1}{\gamma (\rho - 1)}
   $$

   **Berechnung von $r^{\gamma - 1}$:**

   $$
   \gamma - 1 = 0{,}4
   $$

   $$
   r^{0{,}4} = 20^{0{,}4}
   $$

   Berechnung von $20^{0{,}4}$:

   $$
   20^{0{,}4} = e^{0{,}4 \times \ln 20} = e^{0{,}4 \times 2{,}9957} = e^{1{,}1983} \approx 3{,}314
   $$

   Somit:

   $$
   \frac{1}{r^{\gamma - 1}} = \frac{1}{3{,}314} \approx 0{,}3015
   $$

   **Berechnung von $\rho^\gamma$:**

   $$
   \rho^\gamma = 1{,}2^{1{,}4} = e^{1{,}4 \times \ln 1{,}2}
   $$

   Berechnung von $\ln 1{,}2$:

   $$
   \ln 1{,}2 \approx 0{,}182
   $$

   Also:

   $$
   \rho^\gamma = e^{1{,}4 \times 0{,}182} = e^{0{,}2548} \approx 1{,}29
   $$

   **Berechnung des Terms $\frac{\rho^\gamma - 1}{\gamma (\rho - 1)}$:**

   $$
   \gamma (\rho - 1) = 1{,}4 \times (1{,}2 - 1) = 1{,}4 \times 0{,}2 = 0{,}28
   $$

   $$
   \frac{\rho^\gamma - 1}{\gamma (\rho - 1)} = \frac{1{,}29 - 1}{0{,}28} = \frac{0{,}29}{0{,}28} \approx 1{,}036
   $$

   **Berechnung des Wirkungsgrads $\eta$:**

   $$
   \eta = 1 - 0{,}3015 \times 1{,}036 = 1 - 0{,}3125 = 0{,}6875 \quad \text{oder} \quad 68{,}75\,\%
   $$

2. **Vom System verrichtete Arbeit $W$:**

   $$
   W = \eta \times Q_{\text{zu}} = 0{,}6875 \times 2\,000\,\text{J} = 1\,375\,\text{J}
   $$

3. **Abgeführte Wärme $Q_{\text{ab}}$:**

   $$
   Q_{\text{ab}} = Q_{\text{zu}} - W = 2\,000\,\text{J} - 1\,375\,\text{J} = 625\,\text{J}
   $$

**Praktische Anwendung:**

Dieselmotoren haben aufgrund ihres höheren Kompressionsverhältnisses einen höheren Wirkungsgrad als Benzinmotoren. In der Realität beeinflussen jedoch Faktoren wie Wärmeverluste und unvollständige Verbrennung den tatsächlichen Wirkungsgrad.

---

## Rechenbeispiele zu Thermodynamischen Größen

### Wärme ($Q$)

#### Beispiel 1: Erwärmung eines Stoffes

**Hintergrund:**

Die Berechnung der Wärmemenge, die benötigt wird, um einen Stoff zu erwärmen, ist ein grundlegendes thermodynamisches Problem.

**Gegeben:**

- Masse des Wassers: $m = 2\,\text{kg}$
- Spezifische Wärmekapazität von Wasser: $c = 4\,180\,\frac{\text{J}}{\text{kg·K}}$
- Temperaturänderung: $\Delta T = 50\,^\circ\text{C} - 20\,^\circ\text{C} = 30\,\text{K}$

**Gesucht:**

- Übertragene Wärmemenge $Q$

**Berechnung:**

Die benötigte Wärmemenge berechnet sich mit:

$$
Q = m \times c \times \Delta T
$$

Einsetzen der Werte:

$$
Q = 2\,\text{kg} \times 4\,180\,\frac{\text{J}}{\text{kg·K}} \times 30\,\text{K} = 250\,800\,\text{J}
$$

**Praktische Anwendung:**

Diese Berechnung ist relevant für Heizungssysteme, Kochprozesse und industrielle Anwendungen, bei denen Flüssigkeiten erhitzt werden.

---

#### Beispiel 2: Schmelzen von Eis

**Hintergrund:**

Beim Phasenübergang von fest zu flüssig (Schmelzen) wird die spezifische Schmelzwärme benötigt.

**Gegeben:**

- Masse des Eises: $m = 0{,}5\,\text{kg}$
- Schmelzwärme von Eis: $L_f = 334\,000\,\frac{\text{J}}{\text{kg}}$

**Gesucht:**

- Benötigte Wärmemenge $Q$ zum Schmelzen

**Berechnung:**

$$
Q = m \times L_f = 0{,}5\,\text{kg} \times 334\,000\,\frac{\text{J}}{\text{kg}} = 167\,000\,\text{J}
$$

**Praktische Anwendung:**

Diese Berechnung ist wichtig in der Kältetechnik und beim Verständnis von Schmelzprozessen in der Natur.

---

#### Beispiel 3: Wärmeleitung durch ein Material

**Hintergrund:**

Die Wärmeleitung beschreibt den Energiefluss durch ein Material aufgrund eines Temperaturgradienten.

**Gegeben:**

- Wärmeleitfähigkeit: $k = 0{,}5\,\frac{\text{W}}{\text{m·K}}$
- Querschnittsfläche: $A = 1\,\text{m}^2$
- Dicke des Materials: $d = 0{,}1\,\text{m}$
- Temperaturdifferenz: $\Delta T = 20\,\text{K}$

**Gesucht:**

- Wärmeflussrate $\dot{Q}$

**Berechnung:**

Mit Fourier's Gesetz der Wärmeleitung:

$$
\dot{Q} = \frac{k \times A \times \Delta T}{d}
$$

Einsetzen der Werte:

$$
\dot{Q} = \frac{0{,}5\,\frac{\text{W}}{\text{m·K}} \times 1\,\text{m}^2 \times 20\,\text{K}}{0{,}1\,\text{m}} = 100\,\text{W}
$$

**Praktische Anwendung:**

Diese Berechnung ist relevant für die Dimensionierung von Dämmmaterialien in Gebäuden und technischen Anlagen.

---

### Arbeit ($W$)

#### Beispiel 1: Isotherme Expansion eines idealen Gases

**Hintergrund:**

Bei isothermer Expansion bleibt die Temperatur konstant, und die verrichtete Arbeit hängt vom Volumenverhältnis ab.

**Gegeben:**

- Stoffmenge: $n = 1\,\text{mol}$
- Temperatur: $T = 300\,\text{K}$
- Anfangsvolumen: $V_1 = 1\,\text{L} = 1 \times 10^{-3}\,\text{m}^3$
- Endvolumen: $V_2 = 2\,\text{L} = 2 \times 10^{-3}\,\text{m}^3$

**Gesucht:**

- Verrichtete Arbeit $W$

**Berechnung:**

Die Arbeit bei isothermer Expansion ist:

$$
W = n \times R \times T \times \ln\left( \frac{V_2}{V_1} \right)
$$

Einsetzen der Werte:

$$
W = 1\,\text{mol} \times 8{,}314\,\frac{\text{J}}{\text{mol·K}} \times 300\,\text{K} \times \ln\left( \frac{2 \times 10^{-3}\,\text{m}^3}{1 \times 10^{-3}\,\text{m}^3} \right)
$$

Berechnung:

$$
W = 8{,}314\,\frac{\text{J}}{\text{mol·K}} \times 300\,\text{K} \times \ln(2) = 2\,494\,\text{J}
$$

*(Hinweis: $\ln(2) \approx 0{,}6931$)*

**Praktische Anwendung:**

Diese Berechnung ist relevant für thermische Maschinen wie Wärmekraftmaschinen und bei der Analyse von Gasprozessen.

---

#### Beispiel 2: Heben eines Gewichts

**Hintergrund:**

Die Arbeit, die verrichtet wird, um ein Objekt gegen die Schwerkraft anzuheben, ist ein grundlegendes mechanisches Problem.

**Gegeben:**

- Masse: $m = 50\,\text{kg}$
- Höhe: $h = 10\,\text{m}$
- Erdbeschleunigung: $g = 9{,}81\,\frac{\text{m}}{\text{s}^2}$

**Gesucht:**

- Verrichtete Arbeit $W$

**Berechnung:**

$$
W = m \times g \times h = 50\,\text{kg} \times 9{,}81\,\frac{\text{m}}{\text{s}^2} \times 10\,\text{m} = 4\,905\,\text{J}
$$

**Praktische Anwendung:**

Dies ist relevant für die Berechnung von Energiebedarf in Hebezeugen, Kränen und Fahrstühlen.

---

#### Beispiel 3: Kompression eines Gases

**Hintergrund:**

Bei der isothermen Kompression eines idealen Gases wird Arbeit am System verrichtet.

**Gegeben:**

- Anfangsvolumen: $V_1 = 2\,\text{m}^3$
- Endvolumen: $V_2 = 1\,\text{m}^3$
- Anfangsdruck: $P_1 = 100\,\text{kPa}$
- Isothermer Prozess ($P V = \text{konstant}$)

**Gesucht:**

- Notwendige Arbeit $W$ zur Kompression

**Berechnung:**

Da $P V = \text{konstant}$, gilt:

$$
W = n \times R \times T \times \ln\left( \frac{V_2}{V_1} \right)
$$

Da $P_1 V_1 = P_2 V_2$ und die Temperatur konstant ist, können wir $W$ auch schreiben als:

$$
W = P_1 V_1 \ln\left( \frac{V_2}{V_1} \right)
$$

Einsetzen der Werte:

$$
W = 100\,\text{kPa} \times 2\,\text{m}^3 \times \ln\left( \frac{1\,\text{m}^3}{2\,\text{m}^3} \right)
$$

$$
W = 200\,\text{kPa·m}^3 \times (-0{,}6931) = -138{,}62\,\text{kPa·m}^3
$$

Umrechnung in Joule:

$$
1\,\text{kPa} \times 1\,\text{m}^3 = 1\,\text{kJ}
$$

Also:

$$
W = -138{,}62\,\text{kJ}
$$

*(Negative Arbeit zeigt an, dass Arbeit am System verrichtet wird.)*

**Praktische Anwendung:**

Diese Berechnung ist wichtig in der Kompressorentechnik und bei der Analyse von Gaskreisläufen.

---

### Wirkungsgrad ($\eta$)

#### Beispiel 1: Wärmekraftmaschine

**Hintergrund:**

Der Wirkungsgrad einer Wärmekraftmaschine gibt an, welcher Anteil der zugeführten Wärme in mechanische Arbeit umgewandelt wird.

**Gegeben:**

- Zugeführte Wärme: $Q_H = 1\,000\,\text{J}$
- Abgeführte Wärme: $Q_C = 400\,\text{J}$

**Gesucht:**

- Wirkungsgrad $\eta$

**Berechnung:**

Die verrichtete Arbeit ist:

$$
W = Q_H - Q_C = 1\,000\,\text{J} - 400\,\text{J} = 600\,\text{J}
$$

Der Wirkungsgrad ist:

$$
\eta = \frac{W}{Q_H} = \frac{600\,\text{J}}{1\,000\,\text{J}} = 0{,}6 \quad \text{oder} \quad 60\,\%
$$

**Praktische Anwendung:**

Diese Berechnung ist zentral für die Bewertung der Effizienz von Motoren und Kraftwerken.

---

#### Beispiel 2: Carnot-Wirkungsgrad

**Hintergrund:**

Der Carnot-Wirkungsgrad stellt die theoretische Obergrenze für den Wirkungsgrad einer Wärmekraftmaschine dar.

**Gegeben:**

- Temperatur der Wärmequelle: $T_H = 500\,\text{K}$
- Temperatur der Wärmesenke: $T_C = 300\,\text{K}$

**Gesucht:**

- Maximaler Wirkungsgrad $\eta_{\text{Carnot}}$

**Berechnung:**

$$
\eta_{\text{Carnot}} = 1 - \frac{T_C}{T_H} = 1 - \frac{300\,\text{K}}{500\,\text{K}} = 0{,}4 \quad \text{oder} \quad 40\,\%
$$

**Praktische Anwendung:**

Der Carnot-Wirkungsgrad hilft Ingenieuren, die Effizienz realer Maschinen zu bewerten und Verbesserungspotenziale zu identifizieren.

---

#### Beispiel 3: Elektromotor

**Hintergrund:**

Der Wirkungsgrad eines Elektromotors gibt an, wie effizient elektrische Energie in mechanische Energie umgewandelt wird.

**Gegeben:**

- Eingangsleistung: $P_{\text{ein}} = 1\,500\,\text{W}$
- Ausgangsleistung: $P_{\text{aus}} = 1\,350\,\text{W}$

**Gesucht:**

- Wirkungsgrad $\eta$

**Berechnung:**

$$
\eta = \frac{P_{\text{aus}}}{P_{\text{ein}}} = \frac{1\,350\,\text{W}}{1\,500\,\text{W}} = 0{,}9 \quad \text{oder} \quad 90\,\%
$$

**Praktische Anwendung:**

Diese Berechnung ist wichtig für die Auswahl energieeffizienter Motoren in industriellen Anwendungen.

---

### Energie ($E$)

#### Beispiel 1: Kinetische Energie

**Hintergrund:**

Die kinetische Energie eines bewegten Objekts ist die Energie, die es aufgrund seiner Bewegung besitzt.

**Gegeben:**

- Masse: $m = 1\,000\,\text{kg}$
- Geschwindigkeit: $v = 20\,\text{m/s}$

**Gesucht:**

- Kinetische Energie $E_{\text{kin}}$

**Berechnung:**

$$
E_{\text{kin}} = \frac{1}{2} m v^2 = \frac{1}{2} \times 1\,000\,\text{kg} \times (20\,\text{m/s})^2 = 200\,000\,\text{J}
$$

**Praktische Anwendung:**

Diese Berechnung ist relevant für die Fahrzeugdynamik und Sicherheitsberechnungen in der Automobiltechnik.

---

#### Beispiel 2: Potenzielle Energie

**Hintergrund:**

Die potenzielle Energie ist die Energie, die ein Objekt aufgrund seiner Position in einem Gravitationsfeld besitzt.

**Gegeben:**

- Masse: $m = 50\,\text{kg}$
- Höhe: $h = 5\,\text{m}$
- Erdbeschleunigung: $g = 9{,}81\,\frac{\text{m}}{\text{s}^2}$

**Gesucht:**

- Potenzielle Energie $E_{\text{pot}}$

**Berechnung:**

$$
E_{\text{pot}} = m \times g \times h = 50\,\text{kg} \times 9{,}81\,\frac{\text{m}}{\text{s}^2} \times 5\,\text{m} = 2\,452{,}5\,\text{J}
$$

**Praktische Anwendung:**

Wichtig für die Berechnung von Höhenenergie in der Bau- und Umwelttechnik.

---

#### Beispiel 3: Änderung der inneren Energie

**Hintergrund:**

Die innere Energie eines Systems ändert sich bei Temperaturänderungen und Phasenübergängen.

**Gegeben:**

- Stoffmenge: $n = 2\,\text{mol}$
- Molare Wärmekapazität bei konstantem Volumen: $C_v = 12{,}5\,\frac{\text{J}}{\text{mol·K}}$
- Temperaturänderung: $\Delta T = 50\,\text{K}$

**Gesucht:**

- Änderung der inneren Energie $\Delta U$

**Berechnung:**

$$
\Delta U = n \times C_v \times \Delta T = 2\,\text{mol} \times 12{,}5\,\frac{\text{J}}{\text{mol·K}} \times 50\,\text{K} = 1\,250\,\text{J}
$$

**Praktische Anwendung:**

Relevant für die Thermodynamik von Gasen und energetische Betrachtungen in chemischen Reaktionen.

---

### Entropie ($S$)

#### Beispiel 1: Isotherme Expansion eines idealen Gases

**Hintergrund:**

Die Entropieänderung bei isothermer Expansion eines Gases ist ein Maß für die Zunahme der Unordnung.

**Gegeben:**

- Stoffmenge: $n = 1\,\text{mol}$
- Anfangsvolumen: $V_1 = 1\,\text{L} = 1 \times 10^{-3}\,\text{m}^3$
- Endvolumen: $V_2 = 2\,\text{L} = 2 \times 10^{-3}\,\text{m}^3$
- Temperatur: $T = \text{konstant}$

**Gesucht:**

- Entropieänderung $\Delta S$

**Berechnung:**

$$
\Delta S = n \times R \times \ln\left( \frac{V_2}{V_1} \right)
$$

Einsetzen der Werte:

$$
\Delta S = 1\,\text{mol} \times 8{,}314\,\frac{\text{J}}{\text{mol·K}} \times \ln\left( \frac{2 \times 10^{-3}\,\text{m}^3}{1 \times 10^{-3}\,\text{m}^3} \right)
$$

Berechnung:

$$
\Delta S = 8{,}314\,\frac{\text{J}}{\text{K}} \times \ln(2) \approx 8{,}314\,\frac{\text{J}}{\text{K}} \times 0{,}6931 \approx 5{,}76\,\text{J/K}
$$

**Praktische Anwendung:**

Diese Berechnung ist wichtig in der statistischen Mechanik und bei der Analyse thermodynamischer Prozesse.

---

#### Beispiel 2: Entropieänderung bei Wärmezufuhr

**Hintergrund:**

Die Entropieänderung bei der Zufuhr von Wärme bei konstanter Temperatur ist ein grundlegendes Konzept des zweiten Hauptsatzes.

**Gegeben:**

- Zugeführte Wärme: $Q = 1\,000\,\text{J}$
- Temperatur: $T = 400\,\text{K}$

**Gesucht:**

- Entropieänderung $\Delta S$

**Berechnung:**

$$
\Delta S = \frac{Q}{T} = \frac{1\,000\,\text{J}}{400\,\text{K}} = 2{,}5\,\text{J/K}
$$

**Praktische Anwendung:**

Wichtig für die Bewertung der Effizienz thermodynamischer Systeme und Prozesse.

---

#### Beispiel 3: Wärmeübertragung zwischen zwei Reservoirs

**Hintergrund:**

Die Gesamtentropieänderung bei Wärmeübertragung zwischen zwei Reservoirs zeigt die Irreversibilität realer Prozesse.

**Gegeben:**

- Übertragene Wärme: $Q = 600\,\text{J}$
- Temperatur des heißen Reservoirs: $T_H = 500\,\text{K}$
- Temperatur des kalten Reservoirs: $T_C = 300\,\text{K}$

**Gesucht:**

- Gesamtentropieänderung $\Delta S_{\text{gesamt}}$

**Berechnung:**

1. **Entropieänderung des heißen Reservoirs:**

   $$
   \Delta S_H = -\frac{Q}{T_H} = -\frac{600\,\text{J}}{500\,\text{K}} = -1{,}2\,\text{J/K}
   $$

2. **Entropieänderung des kalten Reservoirs:**

   $$
   \Delta S_C = \frac{Q}{T_C} = \frac{600\,\text{J}}{300\,\text{K}} = 2\,\text{J/K}
   $$

3. **Gesamtentropieänderung:**

   $$
   \Delta S_{\text{gesamt}} = \Delta S_H + \Delta S_C = -1{,}2\,\text{J/K} + 2\,\text{J/K} = 0{,}8\,\text{J/K}
   $$

**Interpretation:**

Die positive Gesamtentropieänderung zeigt die Irreversibilität des Prozesses an und steht im Einklang mit dem zweiten Hauptsatz der Thermodynamik.
