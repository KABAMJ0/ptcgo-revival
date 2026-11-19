from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import lock_self_attack
from ptcgo.game.data_utils import Triggers
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.passives_common import condition_immunity_passive
from ptcgo.game.models.board import BoardState

def _water_energy_immune(target, carrier):
    if target.owning_player_id != carrier.owning_player_id:
        return False
    return any(energy_provides_type(e, PokemonTypes.WATER.value)
               for e in BoardState.attached_energies(target))


async def frozen_charm_cure(ctx):
    """Cures Paralysis the moment one of your Pokemon picks up Water Energy;
    the passive keeps it immune from then on."""
    receiver = ctx.energy_receiver
    if receiver is None or receiver.owning_player_id != ctx.player_id:
        return
    if not energy_provides_type(ctx.attached_energy, PokemonTypes.WATER.value):
        return
    await ctx.cure_condition(receiver, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="3db6faa8-68fa-5d77-a1c4-ebbc893a390f",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AurorusEX.Name",
    display_name="Aurorus-EX",
    searchable_by=["Aurorus-EX", "Basic", "EX", "AurorusEX"],
    subtypes=["Basic", "EX"],
    collector_number=102,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=699,
    abilities=[
        Ability(
            title="Frozen Charm",
            game_text="Each of your Pok\u00e9mon that has any Water Energy attached to it can't be Paralyzed. (If any of those Pok\u00e9mon are Paralyzed, remove that Special Condition.)",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=frozen_charm_cure,
            passive=condition_immunity_passive(SpecialConditions.PARALYZED, protects=_water_energy_immune),
        ),
        Attack(
            title="Crystal Breath",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=lock_self_attack(),
        ),
    ],
)