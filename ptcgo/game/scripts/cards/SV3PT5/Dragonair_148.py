from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5b53dc41-fe61-5e5f-a2f7-da943b2b0558",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    display_name="Dragonair",
    searchable_by=["Dragonair", "Stage 1", "Dragonair"],
    subtypes=["Stage 1"],
    collector_number=148,
    set_code="SV3PT5",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    family_id=147,
    abilities=[
        Attack(
            title="Beat",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Aqua Slash",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=90,
            effect=unimplemented,
        ),
    ],
)