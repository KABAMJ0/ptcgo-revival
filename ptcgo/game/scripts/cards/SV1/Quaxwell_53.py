from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="92cbc515-2a94-52a0-b95c-43cba1935a99",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quaxwell.Name",
    display_name="Quaxwell",
    searchable_by=["Quaxwell", "Stage 1", "Quaxwell"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quaxly.Name",
    family_id=912,
    abilities=[
        Attack(
            title="Rain Splash",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Spiral Kick",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)