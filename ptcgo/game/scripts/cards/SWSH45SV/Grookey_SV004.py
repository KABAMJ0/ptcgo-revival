from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="86ce3778-48a9-5968-9f3e-6f0c4637e477",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grookey.Name",
    display_name="Grookey",
    searchable_by=["Grookey", "Basic", "Grookey"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=810,
    abilities=[
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 10 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)