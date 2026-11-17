from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a870bf8e-8d4f-5683-85c2-5f4bc4c4c915",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regirockex.Name",
    display_name="Regirock ex",
    searchable_by=["Regirock ex", "Basic", "ex", "Regirockex"],
    subtypes=["Basic", "ex"],
    collector_number=214,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=377,
    abilities=[
        Attack(
            title="Regi Charge",
            game_text="Attach up to 2 Basic Fighting Energy cards from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Giant Rock",
            game_text="If your opponent's Active Pok\u00e9mon is a Stage 2 Pok\u00e9mon, this attack does 140 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=140,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)