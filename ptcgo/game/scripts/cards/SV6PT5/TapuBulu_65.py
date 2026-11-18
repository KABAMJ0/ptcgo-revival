from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f3775656-febd-5ac3-b9e2-2281e55b2deb",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuBulu.Name",
    display_name="Tapu Bulu",
    searchable_by=["Tapu Bulu", "Basic", "TapuBulu"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="SV6PT5",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    abilities=[
        Attack(
            title="Wood Hammer",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=220,
            effect=unimplemented,
        ),
    ],
)