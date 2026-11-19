from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.card_effects.passives_common import unafflicted
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import is_trainer_card
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _has_rainbow(ctx) -> bool:
    from ptcgo.game.data_utils import def_for
    for energy in ctx.attached_energies(ctx.attacker):
        definition = def_for(getattr(energy, "archetype_id", "") or "")
        if definition is not None and "Rainbow" in (definition.display_name or ""):
            return True
    return False


async def _suspicious_beam(ctx):
    if _has_rainbow(ctx):
        await ctx.deal_damage()
        return
    await ctx.deal_damage(20, target=ctx.attacker, apply_modifiers=False)
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.CONFUSED)

card = PokemonCardDef(
    guid="c6ffe0ba-46a0-5441-b823-66fed6a73ca5",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PorygonZ.Name",
    display_name="Porygon-Z",
    searchable_by=["Porygon-Z", "Stage 2", "PorygonZ"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="HGSS4",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name",
    family_id=137,
    abilities=[
        Ability(
            title="Dimension Transfer",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, search your discard pile for a Trainer card, show it to your opponent, and put it on top of your deck. This power can't be used if Porygon-Z is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=unafflicted,
            effect=flip_gate(then=recover_from_discard(is_trainer_card, count=1, to="deck_top", reveal=True)),
        ),
        Attack(
            title="Suspicious Beam \u03b2",
            game_text="If Porygon-Z has no Rainbow Energy attached to it, Porygon-Z does 20 damage to itself and Porygon-Z is now Confused.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=unimplemented,
        ),
    ],
)
