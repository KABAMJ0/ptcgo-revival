from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.data_utils import Activations


async def long_distance_hypnosis(ctx):
    """Flip a coin: heads puts the Defending Pokemon to Sleep, tails your own
    Active."""
    heads = await ctx.flip_coins(1, "Long-Distance Hypnosis")
    target = ctx.opponent_active() if (heads and heads[0]) else ctx.my_active()
    await ctx.apply_special_condition(target, SpecialConditions.ASLEEP)

card = PokemonCardDef(
    guid="dc05ed6a-a4f2-5e85-b559-76cd93ca106a",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    display_name="Drowzee",
    searchable_by=["Drowzee", "Basic", "Drowzee"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="BASE5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=96,
    abilities=[
        Ability(
            title="Long-Distance Hypnosis",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep; if tails, your Active Pok\u00e9mon is now Asleep. This power can't be used if Drowzee is Asleep, Confused, or Paralyzed.",
            activation=Activations.ONCE_PER_TURN,
            effect=long_distance_hypnosis,
        ),
        Attack(
            title="Nightmare",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)