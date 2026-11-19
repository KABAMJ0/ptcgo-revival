from ptcgo.game.card_effects.attacks_common import flip_damage, flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c8b62a40-676c-5cc2-8acd-0d641e5c1c4e",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name",
    display_name="Weedle",
    searchable_by=["Weedle", "Basic", "Weedle"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="PL2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=13,
    abilities=[
        Attack(
            title="Rescue String",
            game_text="Search your discard pile for up to 5 Pok\u00e9mon, show them to your opponent, and shuffle them into your deck.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Needling Sting",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 10 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_gate(then=lambda ctx: ctx.deal_damage(20)),
        ),
    ],
)