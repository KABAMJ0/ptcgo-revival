from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="01843332-ea9e-5b89-b436-130d733e026d",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meloettaex.Name",
    display_name="Meloetta ex",
    searchable_by=["Meloetta ex", "Basic", "ex", "Meloettaex"],
    subtypes=["Basic", "ex"],
    collector_number=167,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=200,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=648,
    abilities=[
        Ability(
            title="Debut Performance",
            game_text="If you go first, this Pok\u00e9mon can use attacks during your first turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Echoed Voice",
            game_text="During your next turn, this Pok\u00e9mon's Echoed Voice attack does 80 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)