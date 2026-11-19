from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.card_effects.passives_common import unafflicted
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

async def _poison_moth_wind(ctx):
    heads = await ctx.flip_coins(1, "Poison Moth Wind")
    if heads and heads[0]:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
    else:
        await ctx.apply_special_condition(ctx.attacker, SpecialConditions.POISONED)

card = PokemonCardDef(
    guid="d88df1d0-422e-5334-8be3-1fd3b601f5e8",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venomoth.Name",
    display_name="Venomoth",
    searchable_by=["Venomoth", "Stage 1", "Venomoth"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="HGSS4",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name",
    family_id=48,
    abilities=[
        Ability(
            title="Poison Moth Wind",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Poisoned. If tails, your Active Pok\u00e9mon is now Poisoned. This power can't be used if Venomoth is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=unafflicted,
            effect=_poison_moth_wind,
        ),
        Attack(
            title="Stun Spore",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
