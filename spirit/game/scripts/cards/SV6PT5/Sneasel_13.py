from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3a1dc8c2-b4e3-581f-a5b4-80f6b0e30d55",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    display_name="Sneasel",
    searchable_by=["Sneasel", "Basic", "Sneasel"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="SV6PT5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=215,
    abilities=[
        Attack(
            title="Cut",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Beset",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)