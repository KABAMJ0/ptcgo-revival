from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_until_effect

card = PokemonCardDef(
    guid="3405e964-9005-5d8f-a219-84d09660d31c",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vespiquen.Name",
    display_name="Vespiquen",
    searchable_by=["Vespiquen", "Stage 1", "Vespiquen"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name",
    family_id=415,
    abilities=[
        Attack(
            title="Intelligence Gathering",
            game_text="You may draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=draw_until_effect(6, optional=True),
        ),
        Attack(
            title="Bee Revenge",
            game_text="This attack does 10 more damage for each Pok\u00e9mon in your discard pile.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)