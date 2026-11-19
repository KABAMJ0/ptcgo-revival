from ptcgo.game.card_effects.passives_common import (
    apply_own_next_turn_boost, boost_own_next_turn)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _focus_energy(ctx):
    """Focus Energy: next turn's Peck base damage is 30 rather than printed."""
    peck = next(a for a in card.abilities if getattr(a, "title", "") == "Peck")
    await apply_own_next_turn_boost(ctx, 30 - (getattr(peck, "damage", 0) or 0),
                                    attack_title="Peck")

card = PokemonCardDef(
    guid="d29f8585-c8e4-5803-87ef-5aedf211dd3c",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Taillow.Name",
    display_name="Taillow",
    searchable_by=["Taillow", "Basic", "Taillow"],
    subtypes=["Basic"],
    collector_number=124,
    set_code="DP6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=276,
    abilities=[
        Attack(
            title="Focus Energy",
            game_text="During your next turn, Taillow's Peck attack's base damage is 30.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_focus_energy,
        ),
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)