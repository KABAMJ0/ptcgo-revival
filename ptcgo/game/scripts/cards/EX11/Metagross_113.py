from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack, flip_gate
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


def _is_metal_energy(card) -> bool:
    return energy_provides_type(card, PokemonTypes.METAL.value)


async def _critical_collection(ctx):
    """Count the Prizes the opponent has taken, then attach up to that many
    Metal Energy from the discard pile to Metagross Star."""
    taken = ctx.prizes_taken(ctx.opponent_id)
    if taken <= 0:
        await ctx.deal_damage()
        return
    await attach_from_discard(_is_metal_energy, count=taken, target="self",
                              minimum=0)(ctx)


card = PokemonCardDef(
    guid="f5699a92-fe4d-54c9-a1d4-dd7cf8f7b3e6",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metagross.Name",
    display_name="Metagross ★",
    searchable_by=["Metagross \u2605", "Basic", "Star", "Metagross"],
    subtypes=["Basic", "Star"],
    collector_number=113,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=376,
    abilities=[
        Attack(
            title="Critical Collection",
            game_text="Count the number of Prize cards your opponent has taken. Search your discard pile for up to that many Metal Energy cards and attach them to Metagross Star.",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            effect=_critical_collection,
        ),
        Attack(
            title="Hyper Beam",
            game_text="Flip a coin. If heads, discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=composed(lambda ctx: ctx.deal_damage(), flip_gate(then=discard_opponent_energy_attack(1, damage=0))),
        ),
    ],
)