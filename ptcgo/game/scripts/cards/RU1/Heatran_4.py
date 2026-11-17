from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8e9bac40-0b98-5809-884e-20ece684645a",
    key="RU1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heatran.Name",
    display_name="Heatran",
    searchable_by=["Heatran", "Basic", "Heatran"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="RU1",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    family_id=485,
    abilities=[
        Attack(
            title="Heat Boiler",
            game_text="If the Defending Pok\u00e9mon is a Water Pok\u00e9mon, this attack does 60 damage plus 40 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)