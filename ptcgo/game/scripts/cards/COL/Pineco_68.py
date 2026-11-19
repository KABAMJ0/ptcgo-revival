from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_or_nothing

from ptcgo.game.card_effects.passives_common import apply_own_next_turn_boost
from ptcgo.game.data_utils import Attack, def_for


async def focus_energy(ctx):
    """During your next turn Surprise Attack's base damage is 80: the boost is
    the difference from what this card prints on that attack."""
    definition = def_for(ctx.source.archetype_id)
    printed = next((attack.damage for attack in getattr(definition, "abilities", []) or []
                    if isinstance(attack, Attack) and attack.title == "Surprise Attack"), 0)
    await apply_own_next_turn_boost(ctx, 80 - printed, attack_title="Surprise Attack")




card = PokemonCardDef(
    guid="88865fb5-608d-5906-8242-2bda1c592e24",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name",
    display_name="Pineco",
    searchable_by=["Pineco", "Basic", "Pineco"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="COL",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=204,
    abilities=[
        Attack(
            title="Focus Energy",
            game_text="During your next turn, Pineco's Surprise Attack attack's base damage is 80.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=focus_energy,
        ),
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=flip_or_nothing(),
        ),
    ],
)