from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.card_effects.passives_common import team_damage_boost_passive
from ptcgo.game.card_effects.support_common import switch_self_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

async def _fluffy_tag(ctx):
    """Switch this Pokemon with a Benched one; that one's attacks do 40 more
    during my next turn."""
    switched = await switch_self_attack()(ctx)
    if switched is None:
        return
    ctx.add_passive_through_own_next_turn(
        switched,
        team_damage_boost_passive(40, attacker_pred=lambda p: p is switched))


card = PokemonCardDef(
    guid="d406af99-4832-5040-8262-b6ee1344db1f",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whimsicott.Name",
    display_name="Whimsicott",
    searchable_by=["Whimsicott", "Stage 1", "Whimsicott"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="BW7",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name",
    family_id=546,
    abilities=[
        Attack(
            title="Fluffy Tag",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. During your next turn, the attacks of that Pok\u00e9mon do 40 more damage to the Active Pok\u00e9mon (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_fluffy_tag,
        ),
        Attack(
            title="Stun Spore",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)