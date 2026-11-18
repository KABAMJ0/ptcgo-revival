from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a9dbb340-d167-53e1-b9eb-d095b6626fa2",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name",
    display_name="Electrike",
    searchable_by=["Electrike", "Basic", "Electrike"],
    subtypes=["Basic"],
    collector_number=196,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=309,
    abilities=[
        Attack(
            title="Rear Kick",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Tiny Bolt",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)