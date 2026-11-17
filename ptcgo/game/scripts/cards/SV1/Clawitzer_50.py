from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c09d145f-5155-596a-af87-a99f3a7d6088",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clawitzer.Name",
    display_name="Clawitzer",
    searchable_by=["Clawitzer", "Stage 1", "Clawitzer"],
    subtypes=["Stage 1"],
    collector_number=50,
    set_code="SV1",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clauncher.Name",
    family_id=692,
    abilities=[
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Aqua Cannon",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=unimplemented,
        ),
    ],
)