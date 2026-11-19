from ptcgo.game.card_effects.passives_common import ability_lock_passive
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

async def _gastro_acid(ctx):
    """Printed 20; the Defending Pokemon has no Abilities until the end of my
    next turn, which is a lock scoped through the opponent's turn."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    ctx.add_passive_through_opponents_turn(
        defender, ability_lock_passive(lambda p, c: p is defender))


card = PokemonCardDef(
    guid="239d53c9-a709-5809-9a73-475bffb5a909",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arbok.Name",
    display_name="Arbok",
    searchable_by=["Arbok", "Stage 1", "Arbok"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="XY1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ekans.Name",
    family_id=23,
    abilities=[
        Attack(
            title="Gastro Acid",
            game_text="The Defending Pok\u00e9mon has no Abilities until the end of your next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=_gastro_acid,
        ),
        Attack(
            title="Poison Jab",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)