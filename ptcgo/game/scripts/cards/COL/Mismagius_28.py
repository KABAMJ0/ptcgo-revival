from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

from ptcgo.game.data_utils import def_for


async def _poltergeist_look_at_hand(ctx):
    hand = ctx.hand(ctx.opponent_id)
    trainers = sum(1 for card in hand if _trainerish(card))
    if trainers:
        await ctx.deal_damage(30 * trainers)


def _trainerish(card):
    from ptcgo.game.data_utils import def_for
    definition = def_for(getattr(card, "archetype_id", "") or "")
    name = (getattr(definition, "display_name", "") or "").lower()
    return type(definition).__name__ in ("TrainerCardDef", "SupporterCardDef") \
        or "stadium" in name or "supporter" in name


card = PokemonCardDef(
    guid="7cf57621-8b39-5416-b197-caa2e4bc8388",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mismagius.Name",
    display_name="Mismagius",
    searchable_by=["Mismagius", "Stage 1", "Mismagius"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="COL",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name",
    family_id=200,
    abilities=[
        Attack(
            title="Sleeping Spell",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP, flip=True),
        ),
        Attack(
            title="Poltergeist",
            game_text="Look at your opponent's hand. This attack does 30 damage times the number of Trainer, Supporter, and Stadium cards in your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=_poltergeist_look_at_hand,
        ),
    ],
)