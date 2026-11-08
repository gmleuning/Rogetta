# Section pass

Provisional frame for the entry pass (Project Description §7, stage 1, step 2). It is a starting assumption, not placement. No entry is listed under any node here.

## Classes II–III

Scope: Roget entries 180–449 (281 entries) in 36 units. A unit is one distinct section + group in `roget_entries.csv`. Class II has 14 units (180–315) and Class III has 22 (316–449), including the groupless Matter in General (316–320). Word lists were read in `rogets1911.txt`.

How to read each unit:

- **Frame:** the deepest node where most of the unit's entries should land (`node_id` from `hegel_nodes.csv`). Where no single node covers most of them, the frame is the common parent and the spread is given.
- **Confidence:** high, medium or low (§4.5), for the frame.
- **Leavers:** entries expected to land outside the frame's subtree, with the likely destination and the reason in terms of their words. Each carries its own confidence in brackets where it differs from the frame.
- **Inside the frame:** deeper nodes that are already obvious, with no change of branch.
- **Watch:** entries that could go either way and are expected to stay. Secondary candidates (§4.6) are named for later cross-references only.

---

### Class II. Space

**1. Space in General › Abstract Space (180–182, 180a)**
- Frame: `H0218` Space (Nature › Mechanics › Mathematical Mechanics). Confidence: high.
- Inside the frame: 180a Inextension → `H0219` Point (*point, dot, atom*).
- Leavers: 182 Place → `H0227` Place, a sibling under Place and Motion (*place, lieu, spot, niche, nook, station, locality*: the words name a place, not extension).

**2. Space in General › Relative Space (183–185)**
- Frame: `H0227` Place (Nature › Mechanics › Place and Motion). Confidence: medium.
- Leavers: 185 Displacement → `H0228` Motion (*displace, dislodge, transposition, removal*: change of place).
- Watch: 183 Situation (*status, footing, standpoint, posture, pose*) carries social and bodily senses, but the dominant sense is position.

**3. Space in General › Existence in Space (186–191)**
- Frame: `H0227` Place. Confidence: low. This is the most heterogeneous unit in Class II.
- Stay: 186 Presence, 187 Absence (privative of Presence), 190 Contents, 191 Receptacle.
- Leavers:
  - 188 Inhabitant → `H0672` Family (low). The words are *householder, lodger, tenant, settler, colonist*; inhabitants go with the dwelling they serve (§4.2). The citizen, native and population words point to `H0703` The State as a secondary candidate.
  - 189 Abode → `H0672` Family (low–medium). The words are *home, hearth, household, paternal domicile, native land*; animal dens and nests are a minority. Secondary: `H0833` The House as Fundamental Type.
- Watch: 187 *void, vacuum* (secondary `H0034` The One and the Void); 191 *vessel, chest, box, pocket, stomach* (secondary `H0098` Form and Content).

**4. Dimensions › General Dimensions (192–199)**
- Frame: `H0218` Space. Confidence: medium.
- Leavers: 192 Size and 193 Littleness → `H0045` Quantum (low). The headword is magnitude, but the words are ordinary physical size (*bulk, volume, capacity, tonnage; dwarf, pygmy*), so tie-breaker 4 may keep them in Space. Flag for Grant.
- Watch: 194 Expansion and 195 Contraction stay (*dilation, rarefaction, turgescence; atrophy, systole*); secondary `H0050` Alteration of Quantum. 196 Distance, 197 Nearness, 198 Interval and 199 Contiguity stay (secondary `H0259` Adhesion for 199).

**5. Dimensions › Linear Dimensions (200–219, 216a)**
- Frame: `H0220` Line. Confidence: medium.
- Leavers: 204 Layer → `H0221` Surface, a sibling (*lamina, plate, sheet, slab, tier*: extent in two dimensions).
- Watch: 211 Base and 215 Support are mostly physical supports (*prop, pillar, beam, girder, lintel*), with secondary `H0094` Ground. 218 Inversion has secondary `H0092` Opposition. 213 Horizontality carries posture words (*recumbency, supination*).

**6. Dimensions › Centrical Dimensions › General (220–233)**
- Frame: `H0218` Space. Confidence: medium.
- Inside the frame: 220 Exteriority → `H0221` Surface; 230 Outline, 231 Edge, 233 Limit → `H0220` Line.
- Leavers: 225 Clothing and 226 Divestment → `H0690` The Kind of Need and Satisfaction (*dress, raiment, garment, apparel, tailoring*; 226 is the privative: *nudity, undress*). Secondary: `H0867` Draping or Clothing. The molting and exfoliation words in 226 are a minority.
- Watch (all stay):
  - 223 Covering (*roof, awning, blanket, hide, rind*), secondary `H0690`, `H0328`.
  - 220 and 221 Exteriority and Interiority, secondary `H0125` Relation of Outer and Inner.
  - 222 Centrality, secondary `H0187` The Centre.
  - 232 Inclosure (*fence, pen, wall, moat, prison*), secondary `H0617` Property.
  - 233 Limit, secondary `H0018` Determination, Constitution, and Limit.

**7. Dimensions › Centrical Dimensions › Special (234–239)**
- Frame: `H0218` Space. Confidence: medium.
- Orphans (expected, §4.4): 238 Dextrality and 239 Sinistrality. They are placed at the nearest ancestor, `H0218` Space (alternative `H0227` Place), and flagged.
- Leavers: none.
- Watch: 237 Contraposition (*polarity, opposite poles, North and South*) has secondary `H0092` Opposition and `H0269` Magnetism. 236 Laterality carries compass points.

**8. Form › General Form (240–243)**
- Frame: `H0267` Shape (Nature › Physics › Total Individuality). Confidence: high.
- Inside the frame: 241 Amorphism → `H0268` Shapelessness.
- Leavers: 242 Symmetry → `H0751` Regularity and Symmetry (Absolute Spirit › Art › Natural Beauty). The headword names the node, and the words are *symmetry, shapeliness, proportion, eurythmy, uniformity, beauty* (medium). Secondary: `H0267`.
- Watch: 243 Distortion (*malformation, monstrosity, ugliness*) stays in Shape. Secondary: `H0751`, `H0363` Nosology.

**9. Form › Special Form (244–249)**
- Frame: `H0267` Shape. Confidence: high. Contingent shapes go to their kind (§4.2): angle, curve, straightness, circle, convolution, sphere and cylinder.
- Leavers: none.

**10. Form › Superficial Form (250–263, 252a)**
- Frame: `H0267` Shape. Confidence: high. §4.2 names Notch, Fold, Furrow and Stopper as Shape.
- Leavers: none.
- Notes: 262 Perforator follows 260 Opening (instruments go with what they serve), and 261 Closure is its privative. Convexity, Flatness, Concavity, Smoothness and Roughness have secondary `H0221` Surface.

**11. Motion › Motion in General (264–273)**
- Frame: `H0228` Motion. Confidence: medium.
- Leavers: none expected.
- Watch: 268 Traveler, 269 Mariner, 271 Carrier, 272 Vehicle and 273 Ship are agents and instruments, so they go with the activity they serve (§4.2). The weaker alternative is `H0691` The Kind of Work, for *porter, stevedore, coolie, merchantman*. 265 Quiescence is the privative of Motion.

**12. Motion › Degrees of Motion (274–275)**
- Frame: `H0228` Motion (velocity as the relation of space and time). Confidence: high.
- Leavers: none. 275 Slowness has *delay, retardation* words, with secondary `H0222` Time.

**13. Motion › Motion Conjoined with Force (276–277)**
- Frame: `H0232` Impact (Nature › Mechanics › Finite Mechanics). Confidence: medium.
- Leavers: none. 276 Impulse (*momentum, thrust, percussion, collision*) fits well. 277 Recoil has secondary `H0140` Action and Reaction and `H0263` Elasticity.

**14. Motion › Motion with Reference to Direction (278–315)**
- Frame: `H0228` Motion. Confidence: medium. Thirty-eight entries, mostly directional locomotion.
- Leavers:
  - 298 Food → `H0347` Digestive Process (high; the §5 worked example).
  - 299 Excretion → `H0350` Excretion (high; the headword names the node).
  - 306 Descent → `H0233` Fall (medium; *fall, plunge, plummet, drop, collapse*).
  - 288 Attraction → `H0269` Magnetism (low; *lodestone, magnet, electrical attraction, poles*). Secondary: `H0036`, `H0285`, `H0235`.
  - 289 Repulsion → `H0036` Repulsion and Attraction, in the Logic (low). Only a few of its words are physical; the rest are *chase, dispel, give the cold shoulder*. Grant to decide whether 288 and 289 should share a node. Rule 9 means their pairing is not a reason.
  - 304 Shortcoming → `H0016` Finitude, in the Logic (low). The words are *failure, incompleteness, insufficiency, default*, with no literal motion.
- Watch (stay):
  - 296 Reception and 297 Ejection are half bodily (*ingestion, vomiting, venesection*); secondary `H0347`, `H0350`.
  - 295 Egress (*perspiration, exudation*).
  - 303 Transcursion (*transgression, trespass, infringement*); secondary `H0641` Wrong.
  - 312 Rotation; secondary `H0234`.
  - 314 Oscillation; secondary `H0233`, `H0264`.
  - 315 Agitation (*epilepsy, chorea*); secondary `H0363`.

---

### Class III. Matter

**15. Matter in General (316–320; no group)**
- Frame: `H0216` Mechanics. Confidence: medium. The spread inside the frame:
  - 316 Materiality → `H0229` Matter.
  - 318 World → `H0234` Absolute Mechanics (Astronomy) (*heavens, stars, sun, planets, comet, constellation, astronomy*).
  - 319 Gravity → `H0235` Universal Gravitation.
  - 320 Levity → `H0231` Inert Matter (low).
- Leavers: 317 Immateriality → `H0437` The I, in Anthropology (low, flagged privative). The privative rule points to `H0229`, but the words are *spirituality, personality, ego, spirit, astral body*. Grant to confirm.
- Watch: 316 has secondary `H0097` Form and Matter and `H0113` Constitution of the Thing out of Matters. 320 has secondary `H0247` Air.

**16. Inorganic Matter › Solid Matter (321–332)**
- Frame: `H0258` Cohesion (Nature › Physics › Particular Individuality). Confidence: medium.
- Inside the frame:
  - 325 Elasticity and 326 Inelasticity → `H0263` Elasticity.
  - 323 Hardness, 324 Softness and 328 Brittleness → `H0260` Coherence.
  - 327 Tenacity (*glue, cement, viscidity*) → `H0259` Adhesion.
  - 330 Pulverulence stays.
- Leavers: 321 Density and 322 Rarity → `H0257` Specific Gravity, a sibling (*density, solidity, specific gravity, hydrometer; rarefaction, tenuity*). Medium.
- Watch: 329 Texture is half anatomy (*organography, osteology, histology, tissue*) and half textiles; secondary `H0328`. 331 Friction and 332 Lubrication have no obvious Hegel node; secondary `H0232`, `H0259`, `H0265`.

**17. Inorganic Matter › Fluid Matter › Fluids in General (333–336)**
- Frame: `H0256` Physics of Particular Individuality [Tetrad]. Confidence: medium. The spread:
  - 333 Fluidity → `H0258` Cohesion.
  - 335 Liquefaction and 336 Vaporization → `H0265` Heat (*melting, fusion, thaw; evaporation, sublimation*).
- Leavers: 334 Gaseity → `H0247` Air, in Universal Individuality (*gas, air, vapor, ether, steam; pneumatics, aerostatics*). Medium.
- Watch: 335 *solution, solvent* has secondary `H0287` Mixture. 336 *still, retort, distillation* has secondary `H0293` Separation.

**18. Inorganic Matter › Fluid Matter › Specific Fluids (337–346)**
- Frame: `H0295` Terrestrial Organism (Nature › Organics). Confidence: medium. Six of the ten entries are geography:
  - 341 Ocean and 343 Gulf, Lake → `H0309` Sea.
  - 342 Land, 344 Plain, 345 Marsh and 346 Island → `H0310` Land. 345 has alternative `H0306` Alluvial Terrain.
- Leavers (still in Nature, but out of Organics, into Physics › Elements `H0246`):
  - 337 Water → `H0250` Water.
  - 338 Air → `H0247` Air. The weather, climate and barometer words give it secondary `H0308` Atmosphere.
  - 339 Moisture and 340 Dryness → `H0250` Water (low; *humidity, dew* give secondary `H0252`).

**19. Inorganic Matter › Fluid Matter › Fluids in Motion (347–351)**
- Frame: `H0252` Meteorological Process (Nature › Physics). Confidence: low. 349 Wind and 348 River (*rain, rainfall, shower, hurricane* alongside rivers and springs) fit here. 347 Stream is almost empty and follows them.
- Leavers: 350 Conduit → `H0250` Water (*channel, canal, aqueduct, sewer, sluice*); 351 Airpipe → `H0247` Air. Both stay in Physics.
- Watch: 348 could go to `H0310` Land if the rivers outweigh the rain. 351 is half respiratory anatomy (*trachea, larynx, windpipe*); secondary `H0346` Breathing, Cutaneous Process, and Thirst. 350 has secondary `H0701` Public Authority (Police), for public works.

**20. Inorganic Matter › Imperfect Fluids (352–356a)**
- Frame: `H0258` Cohesion. Confidence: low. 352 Semiliquidity → `H0259` Adhesion (*viscidity, stickiness*); 354 Pulpiness and 355 Unctuousness follow it.
- Leavers: 353 Bubble, Cloud → `H0252` Meteorological Process (*cloud, fog, mist, nimbus, cumulus, cirrus* beside *bubble, foam, froth*). Low–medium.
- Watch: 356 Oil and 356a Resin are substances (*oil, fat, wax, petroleum; resin, amber, bitumen*); secondary `H0290` Fire-Process and `H0286` Chemical Process.

**21. Organic Matter › Vitality › Vitality in General (357–363)**
- Frame: `H0294` Organics. Confidence: medium.
- Inside the frame:
  - 357 Organization and 359 Life → `H0294` itself (secondary `H0199` Life, in the Logic).
  - 358 Inorganization → `H0298` Geognosy (*mineral world, mineralogy, geology, geognosy*).
  - 360 Death → `H0365` Death of the Individual (Death has its own node).
  - 362 Corpse → `H0365` (low; it may follow 363 to `H0522`).
- Leavers:
  - 361 Killing → `H0644` Coercion and Crime, in Objective Spirit (*homicide, murder, assassination, massacre, execution*). Medium.
  - 363 Interment → `H0522` The Right of the Individual (Burial of the Dead), in the 1807 Phenomenology (*funeral, obsequies, tomb, cemetery*). Medium; the node names the concept exactly (§4.2). Flag phenomenology-1807.

**22. Organic Matter › Vitality › Special Vitality (364–374a)**
- Frame: `H0294` Organics. Confidence: medium. Six of the twelve entries stay:
  - 364 Animality → `H0327` Animal Nature.
  - 365 Vegetability, 367 Vegetable and 369 Botany → `H0311` Plant Nature.
  - 366 Animal and 368 Zoology → `H0353` Genus and Species (Zoology).
- Leavers:
  - 370 Husbandry (low) and 371 Agriculture (medium) → `H0693` The Substantial (Agricultural) Estate in Objective Spirit (*farming, tillage, gardening, farmer; herdsman, drover*).
  - 373 Man, 374 Woman and 374a Sexuality → `H0383` Sex-Relationship of the Soul, in Anthropology (*man, male, manhood, husband; female, womanhood; sex, mating*). Medium. Secondary: `H0361`, `H0676`.
  - 372 Mankind → `H0368` Soul (Anthropology), at the parent (low). It straddles `H0372` Racial and National Variety (*human race, nation, tribe*) and individual persons.

**23. Organic Matter › Sensation › Sensation in General (375–378)**
- Frame: `H0385` Sensation (Spirit › Subjective Spirit › Anthropology). Confidence: medium. Roget's Matter becomes Spirit here (§4.2 and §8).
- Leavers: none expected.
- Watch: 375 Physical Sensibility may go to `H0390` Sentience. 376 Insensibility is the privative of 375 (secondary `H0428` Hardening against Sensation, and `H0384` Waking and Sleeping for *sleep, coma*). 377 Physical Pleasure and 378 Physical Pain have secondary `H0605` Practical Feeling; a move to Psychology is the risk, and it is low.

**24. Organic Matter › Sensation › Special Sensation › Touch (379–381)**
- Frame: `H0389` Touch (Feeling). Confidence: high. Roget's Matter becomes Spirit here.
- Leavers: none. 380 *itching, tickle, formication* and 381 Numbness (the privative: *anaesthesia, pins and needles*) both stay.

**25. Organic Matter › Sensation › Special Sensation › Heat (382–389, 388a)**
- Frame: `H0265` Heat (Nature › Physics › Particular Individuality). Confidence: high. Heat as a physical phenomenon is Physics (§4.2).
- Leavers: none. 386 Furnace, 387 Refrigerator, 388 Fuel, 388a Insulation and 389 Thermometer are instruments and products that go with Heat (§4.2 names Thermometer). 383 Cold is the privative; its *ice, snow, hail, frost* words give secondary `H0252`. 384 Calefaction (*combustion, ignition*) has secondary `H0290` Fire-Process.

**26. Organic Matter › Sensation › Special Sensation › Taste (390–397, 392a, 392b)**
- Frame: `H0284` Taste (Specific Water), in Nature › Physics. Confidence: medium. The flavours are qualities of bodies: sweetness, sourness, bitterness, saltiness, pungency.
- Leavers: none expected.
- Watch: 390 Taste straddles `H0284` and `H0388` Smell and Taste in Anthropology. The words *flavor, savor, relish, sapidity, twang* outweigh *palate, tongue, gustation*, so it stays (low). 393 Condiment and 394 Savoriness are products and *good taste*; 391 Insipidity is the privative.

**27. Organic Matter › Sensation › Special Sensation › Odor (398–401a)**
- Frame: `H0283` Smell (Specific Air), in Nature › Physics. Confidence: medium.
- Leavers: none.
- Watch: 398 Odor (*olfaction, sense of smell*) has secondary `H0388`. 401a Acridity (*astringency, bite; tear gas, acrid fumes*) may go to `H0284`. 399 Inodorousness is the privative.

**28. Organic Matter › Sensation › Special Sensation › Sound › Sound in General (402–405)**
- Frame: `H0264` Sound. Confidence: high. 403 Silence is the privative, and 404 Loudness and 405 Faintness are degrees.
- Leavers: none. 402's *voice, accent, phonetics* words give secondary `H0595` Language.

**29. Organic Matter › Sensation › Special Sensation › Sound › Specific Sounds (406–412, 408a)**
- Frame: `H0264` Sound. Confidence: high. Specific sounds go to their kind (§4.2): Snap, Roll, Sibilation, Resonance, Stridor.
- Leavers: none.
- Watch: 411 Cry (*shout, scream, yell, howl*) has secondary `H0435` Gesture; 412 Ululation (animal cries) has secondary `H0327` Animal Nature. 408a Nonresonance is the privative.

**30. Organic Matter › Sensation › Special Sensation › Sound › Musical Sounds (413–417)**
- Frame: `H0902` Music (Spirit › Absolute Spirit › Art › Romantic Arts). Confidence: high. This whole unit leaves Roget's Matter for Art.
- Inside the frame:
  - 413 Melody. Concord → `H0907` Particular Characteristics of Music. The words (*rhythm, pitch, scale, key, chords, syncopation*) straddle `H0908`, `H0909` and `H0910`, so it goes at their parent.
  - 414 Discord → `H0909` Musical Harmony (*dissonance, want of harmony*).
  - 415 Music → `H0902` (§5 worked example).
  - 416 Musician and 417 Musical Instruments → `H0914` The Execution of Musical Works of Art (performers and instruments go with performance).
- Leavers: none.

**31. Organic Matter › Sensation › Special Sensation › Sound › Perception of Sound (418–419)**
- Frame: `H0387` Sight and Hearing (Anthropology › Sensation). Confidence: high. §4.2 names Hearing and Deafness.
- Leavers: none.

**32. Organic Matter › Sensation › Special Sensation › Light › Light in General (420–427, 426a)**
- Frame: `H0241` Light (Nature › Physics › Free Physical Bodies). Confidence: medium. Light as a physical phenomenon is Physics (§4.2).
- Inside the frame: 420 Light, 421 Darkness (privative), 423 Luminary and 424 Shade (*awning, parasol, screen, curtain*: instruments that serve shading).
- Leavers: 425 Transparency, 426 Opacity, 426a Turbidity and 427 Semitransparency → `H0273` Transparency, under Relation to Light (the headword names the node). Medium–high.
- Watch: 422 Dimness (*dusk, twilight, crepuscule, break of day*) has secondary `H0253` Universal Solar Relation.

**33. Organic Matter › Sensation › Special Sensation › Light › Specific Light (428–433)**
- Frame: `H0275` Color. Confidence: high. 429 Achromatism is the privative, and 430–433 are particular colours (§4.2).
- Leavers: none. 428 Color (*spectrum, chromatic dispersion*) has secondary `H0276` Prismatic Color; the pigment words in 430–433 give secondary `H0281` Chemical Color.

**34. Organic Matter › Sensation › Special Sensation › Light › Specific Light › Primitive Colors (434)**
- Frame: `H0275` Color. Confidence: high. One entry, 434 Redness (*scarlet, crimson, ruby, flesh color*).
- Leavers: none.

**35. Organic Matter › Sensation › Special Sensation › Light › Specific Light › Complementary Colors (435–440)**
- Frame: `H0275` Color. Confidence: high.
- Leavers: none. 440 Variegation (*iridescence, rainbow, spectrum, iris*) has secondary `H0276` Prismatic Color.

**36. Organic Matter › Sensation › Special Sensation › Light › Perceptions of Light (441–449)**
- Frame: `H0387` Sight and Hearing (Anthropology › Sensation). Confidence: medium. Seeing and its failures are Spirit (§4.2). Roget's Matter becomes Spirit here.
- Inside the frame: 441 Vision, 442 Blindness, 443 Dimsightedness; 444 Spectator (*beholder, observer, onlooker, witness*); 445 Optical Instruments (*lens, microscope, spectacles*; they go with Vision, secondary `H0274` Refraction); 446 Visibility and 447 Invisibility (*perceptibility, conspicuousness, distinctness; concealment*).
- Leavers: 449 Disappearance → `H0009` Moments of Becoming: Coming-to-Be and Ceasing-to-Be, in the Logic (low; *vanish, evanescence, melt away, evaporate*). Secondary: `H0118` Dissolution of Appearance.
- Watch: 448 Appearance matches `H0107` Appearance by headword, but the words are views (*scene, prospect, vista, landscape, tableau*) and §8 warns against matching on shared names. It stays. Secondary: `H0107`, `H0115`. Do not confuse `H0277` Vision, Hegel's physical optics, with seeing (§4.2).

---

### Summary for Classes II–III

- **Branch spread:** about 240 of 281 entries should stay in Nature, and about 41 should leave it (36 for Spirit, 5 for the Logic).

  | | Stay in Nature | To Spirit | To Logic |
  |---|---|---|---|
  | Class II (139) | 130 | 5 | 4 |
  | Class III (142) | 110 | 31 | 1 |

- **Units whose frame is outside Nature:** 23 Sensation in General, 24 Touch, 30 Musical Sounds, 31 Perception of Sound and 36 Perceptions of Light. Together these are 23 entries (375–381, 413–419, 441–449).
- **Units that split across branches or subtrees:** 18 (Physics Elements against Terrestrial Organism), 21 and 22 (Organics against Objective Spirit and Anthropology), and 32 (Light against Transparency).
- **Orphans:** 238 Dextrality and 239 Sinistrality (unit 7).
- **Confidence by unit:** high 14, medium 19, low 3 (units 3, 19 and 20).
- **For Grant's review at the entry pass (low-confidence leavers):** 188, 189 (Family); 192, 193 (Quantum); 288, 289 (Magnetism against Repulsion and Attraction); 304 (Finitude); 317 (The I); 370, 372 (Agricultural Estate, Soul); 449 (Ceasing-to-Be).
- **Possible tree issue, unverified and not changed:** `H0332` Osseous System is listed as a child of `H0331` Nervous System.
