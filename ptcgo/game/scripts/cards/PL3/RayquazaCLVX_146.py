from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0d087bb0-ce2a-55c2-a914-e697306b357a",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaCLVX.Name",
    display_name="Rayquaza C LV.X",
    searchable_by=["Rayquaza C LV.X", "Level-Up", "SP", "RayquazaCLVX"],
    subtypes=["Level-Up", "SP"],
    collector_number=146,
    set_code="PL3",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaC.Name",
    family_id=384,
    abilities=[
        Ability(
            title="Dragon Spirit",
            game_text="If Rayquaza C is your Active Pok\u00e9mon and is damaged but not Knocked Out by an opponent's attack, you may search your discard pile for an Energy card and attach it to Rayquaza C.",
            effect=unimplemented,
        ),
        Attack(
            title="Final Blowup",
            game_text="Discard all Energy attached to Rayquaza C. Ignore this effect if you have no cards in your hand.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=unimplemented,
        ),
    ],
)