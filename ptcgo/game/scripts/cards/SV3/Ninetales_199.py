from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0b3933f1-70d9-5c19-b5c9-a287ab19398f",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name",
    display_name="Ninetales",
    searchable_by=["Ninetales", "Stage 1", "Ninetales"],
    subtypes=["Stage 1"],
    collector_number=199,
    set_code="SV3",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Will-O-Wisp",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
        Attack(
            title="Nine-Tailed Dance",
            game_text="Put 9 damage counters on 1 of your opponent's Pok\u00e9mon. During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.FIRE: 2},
            effect=unimplemented,
        ),
    ],
)