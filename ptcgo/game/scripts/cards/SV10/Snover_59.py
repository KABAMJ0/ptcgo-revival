from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="62482042-431f-536c-9771-744f0b1bfc85",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name",
    display_name="Snover",
    searchable_by=["Snover", "Basic", "Snover"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=459,
    abilities=[
        Attack(
            title="Light Punch",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Icicle",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)