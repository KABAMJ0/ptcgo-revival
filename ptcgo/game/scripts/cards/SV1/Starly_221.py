from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0679eb24-d9d0-55ab-9e4a-f6c0c4bd2c7f",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starly.Name",
    display_name="Starly",
    searchable_by=["Starly", "Basic", "Starly"],
    subtypes=["Basic"],
    collector_number=221,
    set_code="SV1",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=396,
    abilities=[
        Attack(
            title="Flap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)