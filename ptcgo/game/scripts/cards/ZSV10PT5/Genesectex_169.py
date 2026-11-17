from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0bbbfa26-56f5-5c39-a39b-7b872e664712",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Genesectex.Name",
    display_name="Genesect ex",
    searchable_by=["Genesect ex", "Basic", "ex", "Genesectex"],
    subtypes=["Basic", "ex"],
    collector_number=169,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=649,
    abilities=[
        Ability(
            title="Metallic Signal",
            game_text="Once during your turn, you may search your deck for up to 2 Evolution Metal Pok\u00e9mon, reveal them, and put them into your hand. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Protect Charge",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=unimplemented,
        ),
    ],
)