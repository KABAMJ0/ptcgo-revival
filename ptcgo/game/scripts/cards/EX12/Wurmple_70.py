from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import gust_attack
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.data_utils import Triggers

async def _poison_payback(ctx):
    """Damaged by an opposing attack (even if Knocked Out): the Attacking
    Pokemon is now Poisoned."""
    if ctx.damaged_by is not None:
        await ctx.apply_special_condition(ctx.damaged_by,
                                          SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="c87b51bf-698b-56b8-a06d-d607a32493f9",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wurmple.Name",
    display_name="Wurmple",
    searchable_by=["Wurmple", "Basic", "Wurmple"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="EX12",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=265,
    abilities=[
        Ability(
            title="Poison Payback",
            game_text="If Wurmple is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if Wurmple is Knocked Out), the Attacking Pok\u00e9mon is now Poisoned.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=_poison_payback,
        ),
        Attack(
            title="String Pull",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with 1 of the Defending Pok\u00e9mon. Your opponent chooses the Defending Pok\u00e9mon to switch.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=gust_attack(opponent_chooses=True),
        ),
    ],
)