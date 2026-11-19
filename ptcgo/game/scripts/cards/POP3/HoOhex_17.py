from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.passives_common import on_ko_from_attack
from ptcgo.game.card_effects.support_common import distribute_energy
from ptcgo.game.data_utils import Triggers


async def golden_wing(ctx):
    """Knocked Out by an attack: up to 2 Energy move to your Pokemon in any way
    you like."""
    energies = list(ctx.attached_energies(ctx.source))[:2]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 2, minimum=0, prompt="Choose up to 2 Energy to move")
    if picks:
        await distribute_energy(ctx, list(picks), ctx.my_pokemon_in_play())

card = PokemonCardDef(
    guid="859d24e5-fd07-5e1e-9e6b-5fff8463f0c7",
    key="POP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOhex.Name",
    display_name="Ho-Oh ex",
    searchable_by=["Ho-Oh ex", "Basic", "ex", "HoOhex"],
    subtypes=["Basic", "ex"],
    collector_number=17,
    set_code="POP3",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=250,
    abilities=[
        Ability(
            title="Golden Wing",
            game_text="If Ho-Oh ex would be Knocked Out by damage from an opponent's attack, you may move up to 2 Energy attached to Ho-Oh ex to your Pok\u00e9mon in any way you like.",
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=on_ko_from_attack(golden_wing),
        ),
        Attack(
            title="Rainbow Burn",
            game_text="Does 10 damage plus 20 more damage for each type of basic Energy card attached to Ho-Oh ex.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)