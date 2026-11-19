from ptcgo.game.card_effects.attacks_common import count_energy
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import basic_energy_of
from ptcgo.game.card_effects.support_common import attach_from_hand, hand_attach_condition

async def _teal_dance(ctx):
    """Attach a Basic Grass Energy from hand to this Pokemon, then draw a card."""
    await attach_from_hand(
        basic_energy_of("grass"), count=1, target="self", minimum=1,
        prompt="Choose a Basic Grass Energy to attach",
    )(ctx)
    await ctx.draw_cards(1)

card = PokemonCardDef(
    guid="9f6d5415-277e-5f25-8172-c5ca45fc2905",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TealMaskOgerponex.Name",
    display_name="Teal Mask Ogerpon ex",
    searchable_by=["Teal Mask Ogerpon ex", "Basic", "Tera", "ex", "TealMaskOgerponex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=190,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=210,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    abilities=[
        Ability(
            title="Teal Dance",
            game_text="Once during your turn, you may attach a Basic Grass Energy card from your hand to this Pok\u00e9mon. If you attached Energy to a Pok\u00e9mon in this way, draw a card.",
            activation=Activations.ONCE_PER_TURN,
            condition=hand_attach_condition(basic_energy_of("grass"), target="self"),
            effect=_teal_dance,
        ),
        Attack(
            title="Myriad Leaf Shower",
            game_text="This attack does 30 more damage for each Energy attached to both Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 3},
            damage=30,
            damage_operator="+",
            effect=damage_per(lambda c: count_energy("self")(c) + count_energy("defender")(c), 30, base=30),
        ),
    ],
)